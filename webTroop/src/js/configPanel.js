export function setupConfigPanel(awareness, editor, otherEditor) {
    const configButton = document.getElementById('configButton');
    const configPanel = document.getElementById('configPanel');
    const userNameInput = document.getElementById('userName');
    const userColorInput = document.getElementById('userColor');
    const fontSelect = document.getElementById('fontSelect');
    const fontSizeSlider = document.getElementById('fontSizeSlider');
    const fontSizeValue = document.getElementById('fontSizeValue');
    const fontInterfaceSizeSlider = document.getElementById('fontInterfaceSizeSlider');
    const fontInterfaceSizeValue = document.getElementById('fontInterfaceSizeValue');
    const modal = document.getElementById("shortcutsModal");
    const modalbtn = document.getElementById("openModalBtn");
    const closeModal = document.getElementById("closeModal");
    const buttonValidatePlayerName = document.getElementById('validatePlayerName');
    const themeInterfaceSelector = document.getElementById('themeInterfaceSelector');

    const splitScreenToggle = document.getElementById('splitScreenToggle');    
    const otherEditorWrapper = document.getElementById('other-editor-wrapper');
    const editorResizeHandle = document.getElementById('editor-resize-handle');
    const mainEditorWrapper = document.getElementById('main-editor-wrapper');
    const spectatorModeToggle = document.getElementById('spectatorModeToggle');
    const consoleToggle = document.getElementById('consoleToggle');
    const guttersToggle = document.getElementById('guttersToggle');
    const themeSelect = document.getElementById('themeSelect');


    // Variables pour le mode spectateur
    let spectatorMode = false;
    let currentFocusedPlayer = null;
    let currentUserName = '';

    // Fonction pour obtenir la clé localStorage avec le nom d'utilisateur
    function getStorageKey(key) {
        return currentUserName ? `${currentUserName}-${key}` : key;
    }

    // Fonction pour charger les paramètres d'un utilisateur
    function loadUserSettings(userName) {
        currentUserName = userName;
        
        // Charger la police
        const savedFont = localStorage.getItem(getStorageKey('preferredFont'));
        if (savedFont) {
            fontSelect.value = savedFont;
            editor.getWrapperElement().style.fontFamily = savedFont;
            otherEditor.getWrapperElement().style.fontFamily = savedFont;
        }

        // Charger le thème
        const savedTheme = localStorage.getItem(getStorageKey('preferredTheme'));
        if (savedTheme) {
            editor.setOption('theme', savedTheme);
            otherEditor.setOption('theme', savedTheme);
            themeSelect.value = savedTheme;
        }

        // Charger la taille de police
        const savedSize = localStorage.getItem(getStorageKey('preferredFontSize'));
        if (savedSize) {
            fontSizeSlider.value = savedSize;
            updateFontSize(savedSize);
        }

        // Charger la taille de l'interface
        const savedInterfaceSize = localStorage.getItem(getStorageKey('preferredInterfaceFontSize'));
        if (savedInterfaceSize) {
            fontInterfaceSizeSlider.value = savedInterfaceSize;
            updateInterfaceFontSize(savedInterfaceSize);
        }

        // Charger le split screen
        const savedSplitScreen = localStorage.getItem(getStorageKey('splitScreenEnabled'));
        const splitScreenEnabled = savedSplitScreen !== 'false';
        splitScreenToggle.checked = splitScreenEnabled;
        toggleSplitScreen(splitScreenEnabled);

        // Charger l'état de la console
        const savedConsoleState = localStorage.getItem(getStorageKey('consoleVisible'));
        const consoleVisible = savedConsoleState !== 'false';
        consoleToggle.checked = consoleVisible;
        toggleConsole(consoleVisible);

        // Charger l'état des gutters
        const savedGuttersState = localStorage.getItem(getStorageKey('guttersVisible'));
        const guttersVisible = savedGuttersState !== 'false';
        guttersToggle.checked = guttersVisible;
        toggleGutters(guttersVisible);

        // Charger le thème d'interface
        const savedInterfaceTheme = localStorage.getItem(getStorageKey('selectedInterfaceTheme')) || 'dark';
        document.documentElement.className = `${savedInterfaceTheme}-theme`;
        themeInterfaceSelector.value = savedInterfaceTheme;

        // Charger le mode spectateur
        const savedSpectatorMode = localStorage.getItem(getStorageKey('spectatorMode'));
        const spectatorModeEnabled = savedSpectatorMode === 'true';
        spectatorModeToggle.checked = spectatorModeEnabled;
        toggleSpectatorMode(spectatorModeEnabled);
    }

    // Restaurer les données utilisateur
    const savedUser = localStorage.getItem('webtroop-user');
    if (savedUser) {
        const userInfo = JSON.parse(savedUser);
        userNameInput.value = userInfo.name;
        userColorInput.value = userInfo.color;
        updateUserInfo(); // Met à jour awareness
        loadUserSettings(userInfo.name); // Charger les paramètres de cet utilisateur
    }

    function updateUserInfo(forceSpectator = false) {
        const newUserName = forceSpectator ? 'Spectator' : (userNameInput.value || 'Anonyme');
        const userInfo = {
            name: newUserName,
            color: userColorInput.value
        };
        
        // Sauvegarder dans localStorage (sauf si mode spectateur)
        if (!forceSpectator) {
            localStorage.setItem('webtroop-user', JSON.stringify(userInfo));
            
            // Si le nom d'utilisateur a changé, charger les paramètres de ce nouvel utilisateur
            if (newUserName !== currentUserName) {
                loadUserSettings(newUserName);
            }
        }
        
        // Mettre à jour awareness
        awareness.setLocalStateField('user', userInfo);
    }

    // Event listeners
    userNameInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            updateUserInfo();
            userNameInput.blur();
        }
    });

    buttonValidatePlayerName.addEventListener('click', (e) => {
        e.preventDefault();
        updateUserInfo();
        userNameInput.blur();
    }
    );
    
    userColorInput.addEventListener('input', updateUserInfo);

    // Gestion du changement de police
    fontSelect.addEventListener('change', (e) => {
        const font = e.target.value;
        editor.getWrapperElement().style.fontFamily = font;
        otherEditor.getWrapperElement().style.fontFamily = font;
        document.body.style.fontFamily = font;
        localStorage.setItem(getStorageKey('preferredFont'), font);
    });

    // Restaurer la police sauvegardée
    // Supprimé car maintenant géré dans loadUserSettings

    // Gestion ouverture/fermeture du panneau
    configButton.addEventListener('click', () => {
        configPanel.classList.toggle('open');
    });

    // Fermer le panneau en cliquant en dehors
    document.addEventListener('click', (e) => {
        if (!configPanel.contains(e.target) && 
            !configButton.contains(e.target) && 
            configPanel.classList.contains('open')) {
            configPanel.classList.remove('open');
        }
    });

    // Gestion du thème
    themeSelect.addEventListener('change', (e) => {
        const theme = e.target.value;
        editor.setOption('theme', theme);
        otherEditor.setOption('theme', theme);
        localStorage.setItem(getStorageKey('preferredTheme'), theme);
    });

    // Restaurer le thème
    // Supprimé car maintenant géré dans loadUserSettings

    // Restaurer la taille sauvegardée
    // Supprimé car maintenant géré dans loadUserSettings

    // Mettre à jour lors du changement
    fontSizeSlider.addEventListener('input', (e) => {
        const size = e.target.value;
        updateFontSize(size);
        });

    function updateFontSize(size) {
        // Mettre à jour l'affichage
        fontSizeValue.textContent = size;
        
        // Mettre à jour l'éditeur
        editor.getWrapperElement().style.fontSize = size + 'px';
        otherEditor.getWrapperElement().style.fontSize = size + 'px';
        

        // Forcer le rafraîchissement
        editor.refresh();
        otherEditor.refresh();

        // Sauvegarder la préférence
        localStorage.setItem(getStorageKey('preferredFontSize'), size);
    }

    fontInterfaceSizeSlider.addEventListener('input', (e) => {
        const size = e.target.value;
        updateInterfaceFontSize(size);
        });
    
    function updateInterfaceFontSize(size) {
        // Mettre à jour l'affichage
        fontInterfaceSizeValue.textContent = size;
        
        // Mettre à jour l'interface
        document.documentElement.style.fontSize = size + 'px';
        
        // Sauvegarder la préférence
        localStorage.setItem(getStorageKey('preferredInterfaceFontSize'), size);
    };

    // Ouvrir la modal
    modalbtn.onclick = function() {
        modal.style.display = "block";
    }

    // Fermer la modal
    closeModal.onclick = function() {
        modal.style.display = "none";
    }

    // Fermer la modal en cliquant en dehors de celle-ci
    window.onclick = function(event) {
        if (event.target == modal) {
        modal.style.display = "none";
        }
    }

    // Restore the interface theme
    // Supprimé car maintenant géré dans loadUserSettings
    
    // Gérer le changement de thème
    themeInterfaceSelector.addEventListener('change', (e) => {
        const selectedInterfaceTheme = e.target.value;
        document.documentElement.className = `${selectedInterfaceTheme}-theme`;
        localStorage.setItem(getStorageKey('selectedInterfaceTheme'), selectedInterfaceTheme);
    });


    // Gestion du split screen
    function toggleSplitScreen(enabled) {
        if (enabled) {
            // Activer le split screen
            otherEditorWrapper.style.display = 'flex';
            if (editorResizeHandle) {
                editorResizeHandle.style.display = 'block';
            }
            mainEditorWrapper.style.height = '90%';
            
            // Restaurer les flex values par défaut
            mainEditorWrapper.style.flex = '9';
            otherEditorWrapper.style.flex = '1';
        } else {
            // Désactiver le split screen
            otherEditorWrapper.style.display = 'none';
            if (editorResizeHandle) {
                editorResizeHandle.style.display = 'none';
            }
            mainEditorWrapper.style.height = '100%';
            mainEditorWrapper.style.flex = '1';
        }
        
        // Rafraîchir les éditeurs après changement
        setTimeout(() => {
            editor.refresh();
            if (enabled) {
                otherEditor.refresh();
            }
        }, 10);
        
        // Sauvegarder la préférence
        localStorage.setItem(getStorageKey('splitScreenEnabled'), enabled.toString());
    }

    // Restaurer l'état du split screen
    // Supprimé car maintenant géré dans loadUserSettings

    // Event listener pour le toggle
    splitScreenToggle.addEventListener('change', (e) => {
        const enabled = e.target.checked;
        toggleSplitScreen(enabled);
    });

    
    // Gestion de la console
    function toggleConsole(visible) {
        const consoleElement = document.getElementById('logPanel');
        if (visible) {
            consoleElement.style.display = 'flex';
        } else {
            consoleElement.style.display = 'none';
        }
        // Sauvegarder la préférence
        localStorage.setItem(getStorageKey('consoleVisible'), visible.toString());
    }
    
    // Restaurer l'état de la console
    // Supprimé car maintenant géré dans loadUserSettings

    consoleToggle.addEventListener('change', (e) => {
        const visible = e.target.checked;
        toggleConsole(visible);
    });

    // Gestion des gutters
    function toggleGutters(visible) {
        if (visible) {
            editor.setOption('lineNumbers', true);
            otherEditor.setOption('lineNumbers', true);
        } else {
            editor.setOption('lineNumbers', false);
            otherEditor.setOption('lineNumbers', false);
        }
        // Sauvegarder la préférence
        localStorage.setItem(getStorageKey('guttersVisible'), visible.toString());
    }
    
    // Restaurer l'état des gutters
    // Supprimé car maintenant géré dans loadUserSettings

    guttersToggle.addEventListener('change', (e) => {
        const visible = e.target.checked;
        toggleGutters(visible);
    });

    // Gestion du mode spectateur
    function toggleSpectatorMode(enabled) {
        spectatorMode = enabled;
        
        if (enabled) {
            // Forcer le nom à "Spectator"
            updateUserInfo(true);
            // Désactiver le champ de saisie du nom
            userNameInput.disabled = true;
        } else {
            currentFocusedPlayer = null;
            // Réactiver le champ et restaurer le nom original
            userNameInput.disabled = false;
            updateUserInfo(false);
        }
        
        // Sauvegarder la préférence
        localStorage.setItem(getStorageKey('spectatorMode'), enabled.toString());
    }

    // Écouter les changements d'awareness pour suivre les joueurs en temps réel
    awareness.on('change', () => {
        const states = awareness.getStates();
        const localUserName = awareness.getLocalState()?.user?.name;
        const players = [];
        
        // Collecter tous les joueurs actifs
        states.forEach((state) => {
            if (state.otherInstantCode && state.user?.name && 
                state.user.name !== 'Spectator') {
                // En mode spectateur : collecter tous les joueurs (sauf Spectator)
                // En mode normal : exclure le joueur local
                if (spectatorMode || state.user.name !== localUserName) {
                    players.push({
                        name: state.user.name,
                        line: state.otherInstantCode.line,
                        position: state.otherInstantCode.position,
                        color: state.user.color
                    });
                }
            }
        });
        
        if (spectatorMode) {
            // MODE SPECTATEUR: haut = joueur 1, bas = joueur 2
            if (players.length > 0) {
                const player1 = players[0];
                
                if (currentFocusedPlayer !== player1.name) {
                    currentFocusedPlayer = player1.name;
                }
                
                // Scroller vers le joueur 1 dans l'éditeur principal
                if (player1.line >= 0 && player1.line < editor.lineCount()) {
                    editor.scrollIntoView(
                        {line: player1.line - 1, ch: player1.position}, 
                        50
                    );
                }
            }
            
            // Si split screen activé et qu'il y a un deuxième joueur
            if (players.length > 1 && splitScreenToggle.checked) {
                const player2 = players[1];
                
                // Scroller vers le joueur 2 dans l'éditeur du bas
                if (player2.line >= 0 && player2.line < otherEditor.lineCount()) {
                    otherEditor.scrollIntoView(
                        {line: player2.line - 1, ch: player2.position}, 
                        50
                    );
                }
            }
        } else {
            // MODE NORMAL: haut = joueur local, bas = autre joueur (pas Spectator)
            // L'éditeur du bas suit le premier autre joueur trouvé
            if (players.length > 0 && splitScreenToggle.checked) {
                const otherPlayer = players[0];
                
                // Scroller vers l'autre joueur dans l'éditeur du bas
                if (otherPlayer.line >= 0 && otherPlayer.line < otherEditor.lineCount()) {
                    otherEditor.scrollIntoView(
                        {line: otherPlayer.line - 1, ch: otherPlayer.position}, 
                        50
                    );
                }
            }
        }
    });

    // Restaurer l'état du mode spectateur
    // Supprimé car maintenant géré dans loadUserSettings

    // Event listener pour le toggle spectateur
    spectatorModeToggle.addEventListener('change', (e) => {
        toggleSpectatorMode(e.target.checked);
    });

    return {
        updateUserInfo() {
            const userInfo = {
                name: userNameInput.value || 'Anonyme',
                color: userColorInput.value
            };
            return userInfo;
        }, 
        isSplitScreenEnabled() {
            return splitScreenToggle.checked;
        },
        isSpectatorMode() {
            return spectatorMode;
        },
    };
}