// @ts-ignore
// import { CONFIG} from '../../config.js';
import CodeMirror from "codemirror";
import { CodemirrorBinding } from "y-codemirror";
import { EventEmitter } from "./eventBus.js";
import { setupConfigPanel } from "./configPanel.js";
import { AudioAnalyzer } from "./audioAnalyzer.js";
import * as Y from "yjs";
import { WebsocketProvider } from "y-websocket";
import { Awareness } from "y-protocols/awareness";

import "codemirror/addon/dialog/dialog.js";
import "./foxdot_mode.js";
import "codemirror/keymap/sublime";
import "codemirror/addon/edit/matchbrackets";
import "codemirror/addon/edit/closebrackets";
import "codemirror/addon/comment/comment";
import "codemirror/addon/hint/show-hint";
import "codemirror/addon/selection/active-line.js";
import "codemirror/addon/scroll/annotatescrollbar.js";
import "codemirror/addon/search/searchcursor.js";
import "codemirror/addon/search/search.js";
import "codemirror/addon/search/jump-to-line.js";
import "codemirror/addon/search/matchesonscrollbar.js";

import { logsUtils } from "./logs.js";
import { functionUtils } from "./functionUtils.js";
import { recUtils } from "./recUtils.js";
// import { markerUtils } from './markerUtils.js';
// import { chatUtils } from './chatUtils.js';
import { foxdotAutocomplete } from "./foxdotAutocomplete.js";
import {
  showDefinition,
  removeAllTooltips,
  updateDefinitions,
} from "./foxdotDefinitions.js";

import "codemirror/lib/codemirror.css";
import "codemirror/addon/hint/show-hint.css";
import "codemirror/addon/dialog/dialog.css";
import "../css/style.css";
import "../css/crashpanel.css";
import "../css/configPanel.css";

const LINES_TO_SHOW = 20; // pretext number of lines to show

document.addEventListener("DOMContentLoaded", async () => {
  // Récupération de la configuration
  const configRequest = await fetch("../../crash_config.json");
  if (!configRequest.ok) {
    throw new Error(`HTTP error! status: ${configRequest.status}`);
  }
  const config = await configRequest.json();

  // Connexion aux serveurs
  const wsServer = new WebSocket(`ws://${config.HOST_IP}:1234`);
  let foxdotWs = null;
  let activeSequence = null; // {id, currentIndex} for #@ section sequencing

  // Récupération des éléments du DOM
  const chrono = document.getElementById("chrono");

  // Initialisation de YJS
  const ydoc = new Y.Doc();
  const awareness = new Awareness(ydoc);
  const provider = new WebsocketProvider(
    `ws://${config.HOST_IP}:4444`,
    "webtroop",
    ydoc,
    {
      awareness: awareness,
    },
  );
  const ytext = ydoc.getText("webtroop");
  // const ychat = ydoc.getArray('chat');
  // const ymarkers = ydoc.getArray('markers');

  // Configuration de CodeMirror
  const editor = CodeMirror(document.getElementById("editor"), {
    mode: "python",
    theme: "material-darker",
    lineNumbers: true,
    autofocus: true,
    matchBrackets: true,
    autoCloseBrackets: { pairs: "()[]{}<>''\"\"", override: true },
    lineWrapping: true,
    fixedGutter: false,
    singleCursorHeightPerLine: false,
    styleActiveLine: true,
    gutters: ["CodeMirror-linenumbers"],
    keyMap: "sublime",
  });

  const otherUserDoc = editor.getDoc().linkedDoc({ shareHist: false });
  const otherEditor = CodeMirror(document.getElementById("other-editor"), {
    mode: "python",
    theme: "material-darker",
    lineNumbers: true,
    readOnly: true,
    lineWrapping: true,
    styleActiveLine: true,
  });

  otherEditor.swapDoc(otherUserDoc);

  let otherUserCursorMark = null;
  let otherUserNameWidget = null;

  // Fonction pour mettre à jour l'affichage de l'autre utilisateur
  function updateOtherUserDisplay(userName, userColor, line, position, _code) {
    if (!configPanelControls.isSplitScreenEnabled) {
      return;
    }

    // Ne pas traiter si on est en mode spectateur ou si c'est un spectateur
    if (configPanelControls.isSpectatorMode() || userName === "Spectator") {
      return;
    }

    // Supprimer l'ancien marqueur de curseur
    if (otherUserCursorMark) {
      otherUserCursorMark.clear();
    }
    if (otherUserNameWidget) {
      otherUserNameWidget.remove();
      otherUserNameWidget = null;
    }

    // Ajouter le nouveau marqueur de curseur si valide
    if (line >= 0 && line < otherEditor.lineCount() && position >= 0) {
      const lineLength = otherEditor.getLine(line).length;
      const endPos = Math.min(position + 1, lineLength);

      if (position <= lineLength) {
        otherUserCursorMark = otherEditor.markText(
          { line: line, ch: position },
          { line: line, ch: endPos },
          {
            className: "other-user-cursor",
            css: `border-left: 2px solid ${userColor}`,
            inclusiveLeft: true,
            inclusiveRight: false,
          },
        );

        const nameElement = document.createElement("span");
        nameElement.className = "other-user-name-widget";
        nameElement.textContent = userName;
        nameElement.style.cssText = `
        background-color: ${userColor};
        color: white;
        padding: 2px 6px;
        border-radius: 3px;
        font-size: 11px;
        font-weight: bold;
        white-space: nowrap;
        box-shadow: 0 1px 3px rgba(0,0,0,0.3);
        z-index: 1000;
        position: relative;
        top: -20px;
        left: -10px;
      `;

        // Ajouter le widget au-dessus du curseur
        otherUserNameWidget = otherEditor.addWidget(
          { line: line, ch: position },
          nameElement,
          false, // false = au-dessus de la ligne
        );

        otherUserNameWidget = nameElement;
      }
    }

    // Centrer la vue sur le curseur de l'autre utilisateur
    if (line >= 0 && line < otherEditor.lineCount()) {
      otherEditor.scrollIntoView({ line: line, ch: position }, 0);
    }
  }

  const resizeObserver = new ResizeObserver((entries) => {
    for (let entry of entries) {
      if (entry.target.id === "editor-container") {
        logsUtils.refreshEditors();
      }
    }
  });

  resizeObserver.observe(document.getElementById("editor-container"));

  setTimeout(() => {
    logsUtils.refreshEditors();
  }, 100);

  // undo Manager
  const yUndoManager = new Y.UndoManager(ytext, {
    trackedOrigins: new Set([]),
  });
  // Binding YJS avec CodeMirror
  const binding = new CodemirrorBinding(ytext, editor, provider.awareness, {
    yUndoManager,
  });

  // Configuration du panneau de configuration
  const configPanelControls = setupConfigPanel(awareness, editor, otherEditor);

  // Initialiser l'analyseur audio (sera géré par le configPanel)
  const audioVizContainer = document.getElementById("audio-viz");
  const audioAnalyzer = new AudioAnalyzer(audioVizContainer);

  // Passer l'analyseur audio au panneau de configuration AVANT de charger les settings
  configPanelControls.setAudioAnalyzer(audioAnalyzer);

  // Configuration des logs
  logsUtils.initResize(editor, otherEditor);

  EventEmitter.on("send_foxdot", (command) => {
    wsServer.send(
      JSON.stringify({
        type: "evaluate_code",
        code: command,
      }),
    );
  });

  //Gestion des logs FoxDot pour la console
  wsServer.onmessage = (event) => {
    try {
      const message = JSON.parse(event.data);
      if (message.type === "foxdot_log") {
        logsUtils.appendLog(message.data, message.color);
        if (message.attackRequestName != "") {
          awareness.setLocalStateField("attackRequest", {
            attackRequestName: message.attackRequestName,
          });
        }
      }
      // Handle section sequencing callback from FoxDot
      else if (message.type === "seq_next") {
        if (activeSequence && message.seqId == activeSequence.id) {
          activeSequence.currentIndex++;
          // Re-scan sections fresh from editor (content may have changed)
          const freshSections = functionUtils.findAllSections(editor);
          if (activeSequence.currentIndex < freshSections.length) {
            const nextSection = freshSections[activeSequence.currentIndex];
            evaluateSection(editor, nextSection.line);
          } else {
            activeSequence = null; // no more sections, keep playing
          }
        }
      }
      // Handle compose() auto-play: paste arrived via foxdotWs, now start section
      else if (message.type === "compose_start") {
        setTimeout(() => {
          const sections = functionUtils.findAllSections(editor);
          const target = sections.find(s => s.name === message.section);
          if (target) evaluateSection(editor, target.line);
        }, 300);
      }
      // Handle recording output: insert generated script in editor
      else if (message.type === "rec_script") {
        functionUtils.insertAttackContent(editor, message.content);
      }
    } catch (error) {}
  };

  // Reset du chrono lors du clic sur le chrono
  chrono.addEventListener("click", () => functionUtils.resetChrono(wsServer));

  function evaluateCode(cm, multi) {
    // Detect #@ section tag → enter section sequencing mode
    const cursorLine = cm.getCursor().line;
    const cursorLineText = cm.getLine(cursorLine).trim();
    if (cursorLineText.startsWith('#@')) {
      evaluateSection(cm, cursorLine);
      return;
    }

    const videoCodeResult = functionUtils.isVideoCode(cm);
    if (videoCodeResult) {
      var [videoCode, startLine] = videoCodeResult;
      var endLine = startLine;
      foxdotWs.send(
        JSON.stringify({
          type: "sceneName",
          sceneName: videoCode,
        }),
      );
    }
    const isServerFxCode = functionUtils.isServerFxCode(cm);
    if (isServerFxCode) {
      var [serverFxCode, startLine] = isServerFxCode;
      var endLine = startLine;
      wsServer.send(
        JSON.stringify({
          type: "evaluate_code",
          code: "Server.clearFx()",
        }),
      );
    } else {
      var [blockCode, startLine, endLine] = functionUtils.getCodeAndCheckStop(
        cm,
        multi,
      );

      const userState = awareness.getLocalState();
      const userName = userState.user.name;
      const userColor = userState.user.color;
      // Envoyer le code
      wsServer.send(
        JSON.stringify({
          type: "evaluate_code",
          code: blockCode,
          userColor: userColor,
          userName: userName,
        }),
      );

      foxdotWs.send(
        JSON.stringify({
          type: `${userName}Code`,
          code: blockCode,
        }),
      );
    }

    // Flash effect
    awareness.setLocalStateField("flash", {
      lineStart: startLine,
      lineEnd: endLine,
      timestamp: Date.now(),
    });
  }

  // Section sequencing: evaluate a #@ section and schedule next
  function evaluateSection(cm, sectionLine) {
    const tag = functionUtils.parseSectionTag(cm.getLine(sectionLine));
    if (!tag) return;

    const seqId = Date.now();
    const allSections = functionUtils.findAllSections(cm);
    const currentIdx = allSections.findIndex(s => s.line === sectionLine);

    // Special terminator sections
    if (tag.type === 'end' || tag.type === 'endfade' || tag.type === 'clear') {
      let cmd = '_seq_cancel()\n';
      if (tag.type === 'end') {
        cmd += tag.beats !== null ? `_seq_end(${tag.beats})\n` : `Clock.clear()\n`;
      } else if (tag.type === 'endfade') {
        cmd += `_seq_endfade(${tag.beats !== null ? tag.beats : 8})\n`;
      } else {
        cmd += `Clock.clear()\n`;
      }
      wsServer.send(JSON.stringify({
        type: 'evaluate_code',
        code: cmd
      }));
      activeSequence = null;
      awareness.setLocalStateField('flash', {
        lineStart: sectionLine, lineEnd: sectionLine, timestamp: Date.now()
      });
      return;
    }

    // Loop: jump to target section after optional beat delay
    if (tag.type === 'loop') {
      let loopCode = functionUtils.getSectionCode(cm, sectionLine);
      // Pick target: weighted random from targets, or first section
      let targetIdx = 0;
      if (tag.targets && tag.targets.length > 0) {
        const names = tag.targets.map(t => t.name);
        const weights = tag.targets.map(t => t.weight);
        const totalWeight = weights.reduce((a, b) => a + b, 0);
        let r = Math.random() * totalWeight;
        let picked = names[0];
        for (let i = 0; i < weights.length; i++) {
          r -= weights[i];
          if (r <= 0) { picked = names[i]; break; }
        }
        targetIdx = allSections.findIndex(s => s.name === picked);
        if (targetIdx === -1) targetIdx = 0;
      }
      // Build atomic command: cancel + loop code + schedule
      const loopSeqId = Date.now();
      const delay = tag.beats || 0.125;
      let cmd = '_seq_cancel()\n';
      if (loopCode.trim()) cmd += loopCode + '\n';
      cmd += `_seq_schedule(${delay}, ${loopSeqId})\n`;
      wsServer.send(JSON.stringify({
        type: 'evaluate_code',
        code: cmd
      }));
      activeSequence = { id: loopSeqId, currentIndex: targetIdx - 1 };
      awareness.setLocalStateField('flash', {
        lineStart: sectionLine, lineEnd: sectionLine, timestamp: Date.now()
      });
      return;
    }

    // Collect and process the code block for this section
    let sectionCode = functionUtils.getSectionCode(cm, sectionLine);
    sectionCode = sectionCode.split('\n').map(line => {
      line = functionUtils.convertQuestionMarkToPRand(line);
      line = functionUtils.convertExclamationToVar(line);
      return functionUtils.ifPlayerStop(line);
    }).join('\n');

    const userState = awareness.getLocalState();
    const userName = userState.user.name;
    const userColor = userState.user.color;

    // Build atomic command: cancel + code + schedule
    let cmd = '_seq_cancel()\n' + sectionCode;
    if (tag.beats !== null && currentIdx < allSections.length - 1) {
      cmd += '\n_seq_schedule(' + tag.beats + ', ' + seqId + ')';
    }

    // Send as single message to avoid race conditions
    wsServer.send(JSON.stringify({
      type: 'evaluate_code',
      code: cmd,
      userName, userColor
    }));

    // Send to CrashOS visuals
    foxdotWs.send(JSON.stringify({
      type: `${userName}Code`,
      code: sectionCode
    }));

    // Flash effect on section block
    const endLine = (currentIdx < allSections.length - 1)
      ? allSections[currentIdx + 1].line - 1
      : cm.lineCount() - 1;
    awareness.setLocalStateField('flash', {
      lineStart: sectionLine, lineEnd: endLine, timestamp: Date.now()
    });

    // Store sequence state
    activeSequence = { id: seqId, currentIndex: currentIdx };
  }

  const stopClockAndSequence = () => {
    functionUtils.stopClock(wsServer);
    if (activeSequence) {
      wsServer.send(JSON.stringify({
        type: 'evaluate_code',
        code: '_seq_cancel()\n'
      }));
      activeSequence = null;
    }
  };

  // Gestion de CTRL+ENTER
  editor.setOption("extraKeys", {
    "Ctrl-,": stopClockAndSequence,  // Chromium
    "Ctrl-;": stopClockAndSequence,  // Firefox
    "Ctrl-Space": "autocomplete",
    "Ctrl-S": (cm) => {
      functionUtils.saveEditorContent(cm, wsServer);
    },
    "Alt-X": (cm) => {
      cm.toggleComment();
      evaluateCode(cm, false);
    },
    "Ctrl-Alt-X": (cm) => {
      const { startLine, endLine } = functionUtils.getBlock(
        cm,
        cm.getCursor().line,
      );
      cm.setSelection(
        { line: startLine, ch: 0 },
        { line: endLine, ch: cm.getLine(endLine).length },
      );
      cm.toggleComment();
      evaluateCode(cm, true);
    },
    "Alt-S": (cm) => {
      functionUtils.soloPlayer(cm, wsServer);
    },
    "Ctrl-Alt-S": () => {
      functionUtils.unSoloPlayers(wsServer);
    },
    "Alt-J": (cm) => {
      functionUtils.jumpToOtherPlayer(cm, awareness);
    },
    "Ctrl-Alt-J": (cm) => {
      functionUtils.previousJump(cm);
    },
    "Ctrl-Enter": (cm) => {
      evaluateCode(cm, false);
    },
    "Ctrl-Alt-Enter": (cm) => {
      evaluateCode(cm, true);
    },
    "Alt-I": (cm) => showDefinition(cm),
    "Alt-F": "findPersistent",
    "Ctrl-G": "findNext",
    "Ctrl-Alt-Left": "goLineStart",
    "Ctrl-Alt-Right": "goLineEnd",
    "Shift-Alt-Right": "selectBetweenBrackets",
    "Ctrl-Left": (cm) => {
      functionUtils.goToPreviousComma(cm);
    },
    "Ctrl-Right": (cm) => {
      functionUtils.goToNextComma(cm);
    },
    "Alt-P": () => {
      document.getElementById("piano-roll").classList.toggle("hidden");
    },
    "Alt-T": (cm) => {
      recUtils.autoRecToggle(cm, evaluateCode);
    },
    "Alt-Up": (cm) => {
      functionUtils.incrementValue(cm, 1);
      evaluateCode(cm, false);
      recUtils.autoRecCapture(cm);
    },
    "Alt-Down": (cm) => {
      functionUtils.incrementValue(cm, -1);
      evaluateCode(cm, false);
      recUtils.autoRecCapture(cm);
    },
    "Ctrl-Up": (cm) => {
      functionUtils.incrementValue(cm, 10);
      evaluateCode(cm, false);
      recUtils.autoRecCapture(cm);
    },
    "Ctrl-Down": (cm) => {
      functionUtils.incrementValue(cm, -10);
      evaluateCode(cm, false);
      recUtils.autoRecCapture(cm);
    },
    "Alt-A": (cm) => {
      functionUtils.randomizer(cm);
    },
    "Alt-R": (cm) => {
      functionUtils.resetPlayer(cm, wsServer);
    },
    "Alt-O": (cm) => {
      functionUtils.soloDrop(cm, wsServer);
    },
    Esc: (cm) => {
      if (recUtils._autoRec.armed) {
        recUtils.autoRecCancel(cm, evaluateCode);
      } else {
        removeAllTooltips();
      }
    },
  });

  // Gestion de l'autocomplétion
  editor.setOption("hintOptions", {
    hint: (cm) => {
      return foxdotAutocomplete.hint(cm, CodeMirror);
    },
    completeSingle: true,
    extraKeys: {
      Right: function (cm, handle) {
        // Si on est sur une catégorie, montrer ses éléments
        const activeElement = document.querySelector(".CodeMirror-hint-active");
        if (activeElement) {
          const categoryAttr = activeElement.getAttribute("data-category");
          const categoryTypeAttr =
            activeElement.getAttribute("data-category-type") || "attack";

          if (categoryAttr) {
            const categoryItems = foxdotAutocomplete.showCategoryItems(
              cm,
              categoryAttr,
              categoryTypeAttr,
            );
            if (categoryItems) {
              handle.close();
              setTimeout(() => {
                cm.showHint({
                  hint: () => categoryItems,
                  completeSingle: false,
                  extraKeys: {
                    Left: function (cm, handle) {
                      // Retour aux catégories
                      handle.close();
                      setTimeout(() => {
                        cm.showHint();
                      }, 50);
                    },
                  },
                });
              }, 50);
            }
          }
        }
      },
      Left: function (cm, handle) {
        // Si on est dans les éléments et que le premier élément (bouton retour) est sélectionné
        const selectedItem = handle.data[handle.selectedHint];
        if (
          selectedItem &&
          selectedItem.displayText &&
          selectedItem.displayText.includes("Retour aux catégories")
        ) {
          handle.close();
          setTimeout(() => {
            cm.showHint();
          }, 50);
        }
      },
    },
  });

  // Ajouter l'écouteur d'awareness
  awareness.on("change", () => {
    const states = awareness.getStates();
    states.forEach((state) => {
      // Gestion de l'effet flash
      if (state.flash) {
        const { lineStart, lineEnd, timestamp } = state.flash;
        // Vérifier si le flash est récent (moins de 100ms)
        if (Date.now() - timestamp < 100) {
          // Créer l'effet flash
          for (let i = lineStart; i <= lineEnd; i++) {
            const mark = editor.markText(
              { line: i, ch: 0 },
              { line: i, ch: editor.getLine(i).length },
              { className: "flash-highlight" },
            );
            setTimeout(() => mark.clear(), 200);
          }
        }
      }
      // Gestion de l'affichage du code en temps réel des autres utilisateurs
      if (
        state.otherInstantCode &&
        state.user?.name !== awareness.getLocalState().user?.name &&
        state.user?.name !== "Spectator"
      ) {
        const { user, code, position, line } = state.otherInstantCode;
        const userColor = state.user?.color || "#fff";

        // Mettre à jour l'affichage (line-1 car votre code utilise line+1)
        updateOtherUserDisplay(user, userColor, line - 1, position, code);
      }
    });
  });

  function foxDotWs() {
    foxdotWs = new WebSocket(`ws://${config.HOST_IP}:${config.FOXDOT_WS_PORT}`);
    foxdotWs.onopen = () => {
      foxdotWs.send(JSON.stringify({ type: "get_autocomplete" }));
    };
    foxdotWs.onmessage = (event) => {
      try {
        const message = JSON.parse(event.data);
        if (message.type === "attack") {
          if (
            awareness.getLocalState().attackRequest.attackRequestName ===
            awareness.getLocalState().user.name
          ) {
            functionUtils.insertAttackContent(editor, message.content);
            // Reset to prevent duplicate inserts from multiple WS deliveries
            awareness.setLocalStateField("attackRequest", { attackRequestName: "" });
          }
        } else if (message.type === "autocomplete") {
          const { loops, fxList, synthList, attackList } =
            functionUtils.formatFoxDotAutocomplete(message);

          const toExclude = ["__init__", "1s", ""];
          let filteredLoops = loops.filter(
            (i) => !toExclude.includes(i.displayText),
          );

          foxdotAutocomplete.loopList = filteredLoops;
          foxdotAutocomplete.fxList = fxList;
          foxdotAutocomplete.synths = synthList;
          foxdotAutocomplete.attackList = attackList;
          foxdotAutocomplete.attackCategories =
            foxdotAutocomplete.getAttackCategories();
          foxdotAutocomplete.fxCategories =
            foxdotAutocomplete.getFxCategories();
          foxdotAutocomplete.synthCategories =
            foxdotAutocomplete.getSynthCategories();

          // Construire les définitions dynamiques pour les synths
          // Ne garder que ceux dont displayText se termine par '_' (signature avec paramètres)
          try {
            const dynamicSynthDefs = {};
            (synthList || [])
              .filter((item) => {
                return (
                  item &&
                  typeof item.displayText === "string" &&
                  typeof item.text === "string"
                );
              })
              .forEach((item) => {
                const baseName = item.displayText; // retirer le '_'
                const parenIdx = item.text.indexOf("(");
                const signature =
                  parenIdx >= 0 ? item.text.slice(parenIdx) : "";
                if (baseName && signature) {
                  dynamicSynthDefs[baseName] = signature; // ex: tb303 -> (wave=0, cutoff=800, ...)
                }
              });

            // Construire les définitions dynamiques pour les FX
            const dynamicFxDefs = {};
            (fxList || [])
              .filter((item) => {
                return (
                  item &&
                  typeof item.displayText === "string" &&
                  item.displayText.endsWith("_") &&
                  typeof item.text === "string"
                );
              })
              .forEach((item) => {
                const baseName = item.displayText.slice(0, -1); // retirer le '_'
                // Pour les FX, "text" est souvent une liste de paramètres sans parenthèses
                const signature = item.text.includes("(")
                  ? item.text.slice(item.text.indexOf("("))
                  : item.text;
                if (baseName && signature) {
                  dynamicFxDefs[baseName] = signature; // ex: sidechain -> "sidechain: 0, sidechain_atk: 0.05, ..."
                }
              });

            // Mettre à jour les définitions utilisées par Alt-I (showDefinition)
            updateDefinitions({
              synthDefs: dynamicSynthDefs,
              fxDefs: dynamicFxDefs,
            });
          } catch (e) {
            console.warn(
              "Impossible de mettre à jour les définitions dynamiques (synth/fx):",
              e,
            );
          }

          if (
            filteredLoops.length == 0 ||
            fxList.length == 0 ||
            synthList.length == 0 ||
            attackList.length == 0
          ) {
            console.error(
              `Erreur lors de la récupération de la liste des boucles (${loops.length}), effets (${fxList.length}), synthés (${synthList.length}) ou attaques (${attackList.length})`,
            );
          }
        }
      } catch (error) {
        console.error("Erreur lors de la réception de message FoxDot:", error);
      }
    };
    foxdotWs.onclose = (e) => {
      console.log(
        "Socket is closed. Reconnect will be attempted in 1 second.",
        e.reason,
      );
      setTimeout(function () {
        foxDotWs();
      }, 1000);
    };
    foxdotWs.onerror = (err) => {
      console.error(
        "Socket encountered error: ",
        err.message,
        "Closing socket",
      );
      foxdotWs.close();
    };
  }

  foxDotWs();

  // Fonction pour extraire une fenêtre de lignes autour de la position courante
  // Positionne la ligne active au quart haut pour zbdm, au 3/4 bas pour svdk
  function getLineWindow(cm, linesToShow = 5, userName = 'Anonymous') {
    const cursor = cm.getCursor();
    const totalLines = cm.lineCount();

    // Calculer le positionnement selon le joueur
    // zbdm: ligne active au 1/4 haut (1/4 avant, 3/4 après)
    // svdk: ligne active au 3/4 bas (3/4 avant, 1/4 après)
    let beforeLines, afterLines;
    if (userName === 'zbdm') {
      beforeLines = Math.floor(linesToShow / 4);
      afterLines = linesToShow - beforeLines - 1;
    } else if (userName === 'svdk') {
      beforeLines = Math.floor(linesToShow * 3 / 4);
      afterLines = linesToShow - beforeLines - 1;
    } else {
      // Défaut: centré
      beforeLines = Math.floor(linesToShow / 2);
      afterLines = linesToShow - beforeLines - 1;
    }

    let startLine = Math.max(0, cursor.line - beforeLines);
    let endLine = Math.min(totalLines, cursor.line + afterLines + 1);

    // Ajuster les limites pour garder approximativement la taille de fenêtre
    if (endLine - startLine < linesToShow) {
      if (startLine === 0) {
        endLine = Math.min(totalLines, linesToShow);
      } else if (endLine === totalLines) {
        startLine = Math.max(0, totalLines - linesToShow);
      }
    }

    // Extraire les lignes de la fenêtre
    const lines = [];
    for (let i = startLine; i < endLine; i++) {
      lines.push(cm.getLine(i));
    }

    return {
      windowLines: lines.join('\n'),
      windowStartLine: startLine + 1,      // 1-indexed
      windowEndLine: endLine,              // 1-indexed
      currentLineNumber: cursor.line + 1,  // Position absolue du curseur
      cursorCh: cursor.ch
    };
  }

  // Gestion de l'envoi de code en temps réel
  editor.on("cursorActivity", (cm) => {
    // Récupérer les infos utilisateur depuis awareness
    const userState = awareness.getLocalState();
    const userName = userState?.user?.name || "Anonymous";

    // Récupérer la position du curseur et extraire une fenêtre de lignes
    const cursor = cm.getCursor();
    const currentLine = cm.getLine(cursor.line);
    const windowData = getLineWindow(cm, LINES_TO_SHOW, userName);

    // Préparer le message avec fenêtre de lignes au lieu du code complet
    const message = {
      type: `${userName}InstantCode`,
      position: cursor.ch,
      code: currentLine,
      windowLines: windowData.windowLines,        // Fenêtre de lignes autour du curseur
      windowStartLine: windowData.windowStartLine, // Numéro de la première ligne de la fenêtre
      windowEndLine: windowData.windowEndLine,     // Numéro de la dernière ligne de la fenêtre
      currentLineNumber: cursor.line + 1,
    };

    // envoyer le message dans le live other player display
    try {
      awareness.setLocalStateField("otherInstantCode", {
        user: userName,
        code: currentLine,
        position: cursor.ch,
        line: cursor.line + 1,
        windowLines: windowData.windowLines,
        windowStartLine: windowData.windowStartLine,
        windowEndLine: windowData.windowEndLine,
      });
    } catch (error) {}

    if (foxdotWs.readyState === WebSocket.OPEN) {
      foxdotWs.send(JSON.stringify(message));
    }
  });

  // Gestion de l'activation/désactivation du serveur dans CrashPanel
  crashPanelTitle.addEventListener("click", () => {
    if (foxdotWs.readyState === WebSocket.OPEN) {
      foxdotWs.send(JSON.stringify({ type: "serverToggle" }));
    }

    crashPanelTitle.classList.toggle("loading");
    setTimeout(() => {
      crashPanelTitle.classList.toggle("loading");
    }, 4000);
  });

  // piano insert at cursor
  document.querySelectorAll("#piano-roll .piano-key li").forEach((key) => {
    key.addEventListener("click", (event) => {
      const index = event.currentTarget.dataset.index;
      if (index !== undefined) {
        insertAtCursor(index);
      }
    });
  });

  function insertAtCursor(index) {
    // insert index text at cursor position
    const cursor = editor.getCursor();
    const line = cursor.line;
    const ch = cursor.ch;
    editor.replaceRange(index + ",", { line, ch }, { line, ch });
  }

  // Cleanup lors du fermeture
  window.addEventListener("beforeunload", () => {
    if (audioAnalyzer.isRunning) {
      audioAnalyzer.stop();
    }
  });
});
