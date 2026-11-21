# Projet Dôme — FoxDot / SuperCollider sur un dôme Dante 25 HP

Documentation du projet : jouer une performance live coding (FoxDot + webTroop) dans un dôme de 25 haut-parleurs piloté en Dante, depuis notre laptop Linux.

- Branche : `live2026_riga`
- Dossier : `dome/`
- Dernière mise à jour : 13 octobre 2026

---

## 1. Contexte

On nous propose de jouer dans un dôme sonore. Les haut-parleurs (HP) sont alimentés via **Dante** (audio sur réseau IP, protocole propriétaire d'Audinate). Notre système actuel est **stéréo** : tout finit dans `makeSound` → sorties 0/1.

Objectifs :

1. **Spatialiser** FoxDot sur les 25 HP, avec des paramètres jouables en live (`az`, `elev`, `dspread`).
2. **Répéter sans le dôme** : écoute virtuelle sur 2 HP (ou un casque), avec une vue 3D où la caméra = l'auditeur.
3. **Sortir en Dante depuis Linux**, idéalement avec [Inferno](https://github.com/teodly/inferno), une implémentation Dante libre (non officielle).

---

## 2. Le dôme

Source : `dome/dome.txt` (infos transmises par Karmen Camina) et captures « Spat Viewer » (IRCAM Spat → le lieu utilise probablement Max/Spat sur Mac).

Convention : **azimut** 0° = face, + = droite. **Élévation** 0° = hauteur d'oreille, 90° = zénith. Distance en mètres.

| Sortie | Couronne | Positions idéales (az / él) |
|---|---|---|
| 1 | centre haut | 0° / 90° |
| 2–5 | quadri haut | −45, 45, 135, −135 / 60° |
| 6–13 | couronne de 8 (milieu) | −45, 0, 45, 90, 135, 180, −135, −90 / 30° |
| 14–25 | couronne de 12 (bas) | −45, −15, 15, 45, 75, 105, 135, 165, −165, −135, −105, −75 / 0° |

Remarques :

- Le dôme réel est **étiré en rectangle**. Les positions mesurées vont de 3,5 m à 6,8 m de distance, et la couronne du bas est à 7–11° d'élévation. Le lieu conseille de travailler avec les **positions idéales**.
- Pour la musique algorithmique, on peut aussi traiter les sorties comme des **numéros dans des couronnes**.
- **Pas de subwoofer mentionné** : à demander.

Les deux jeux de positions (`ideal`, `real`) sont codés dans `FoxDot/FoxDot/lib/Dome.py` (`LAYOUTS`) et dans `dome/dome_listener.html` (`IDEAL`, `REAL`).

---

## 3. Architecture

```
                 FoxDot (Python)
                      │  chaque note : synth → effets → exit node
                      ▼
 ┌──────────────────── scsynth ─────────────────────────────────────────┐
 │  dôme OFF : makeSound      → sorties 0/1 (stéréo, comme avant)       │
 │  dôme ON  : makeSoundDome  → bus privé 25 canaux (panoramique az/él) │
 │                                   │                                   │
 │            ┌──────────────────────┴──────────────────┐                │
 │            ▼                                         ▼                │
 │   domeMonitor (écoute virtuelle)            domeDirect (concert)      │
 │   25 HP → stéréo selon la position          25 canaux → sorties       │
 │   de l'auditeur → sorties 0/1               matérielles 2..26          │
 └──────────────────────────────────────────────────────────────────────┘
          ▲   │ niveaux + notes (OSC)                    │
          │   ▼                                          ▼
   sclang (OSCdef) ⇄ dome/bridge.mjs ⇄ navigateur     PipeWire → Inferno
   (port 57120)      (UDP 57140, HTTP/WS 8091)         → réseau Dante → 25 HP
                     dome_listener.html (vue 3D,
                     caméra = auditeur)
```

Ordre des nœuds dans scsynth :

```
RootNode
 ├─ domeGroup (en tête)    domeMonitor, domeDirect  ← lisent le bus dôme avec InFeedback
 ├─ groupe 1 (default)     notes FoxDot → makeSoundDome écrit sur le bus dôme
 ├─ global_fx_group        effets globaux FoxDot (sur le bus 0)
 └─ StageLimiter           (en queue)
```

Le groupe dôme est **en tête du RootNode**, donc :

- `Clock.clear()` / `/g_freeAll 1` ne le tue pas ;
- il passe toujours avant les effets globaux et le limiteur ;
- la lecture en `InFeedback` ajoute 1 bloc (64 échantillons, ~1,3 ms) de latence, sans problème d'ordre.

---

## 4. Ce qui est fait

### 4.1 FoxDot

| Fichier | Changement |
|---|---|
| `FoxDot/FoxDot/lib/Dome.py` | **Nouveau.** Classe `Dome` : génère le code SC, le charge dans sclang, gère l'état (layout, monitor, direct). |
| `FoxDot/FoxDot/lib/Players.py` | `az`, `elev`, `dspread` ajoutés à `base_attributes`. |
| `FoxDot/FoxDot/lib/ServerManager.py` | `get_exit_node` : si `dome.active`, utilise `makeSoundDome` + `domebus/az/elev/dspread`. |
| `FoxDot/FoxDot/lib/__init__.py` | Crée l'objet global `dome = Server.dome = Dome(Server)`. |

**Attributs de player :**

| Attribut | Rôle | Défaut |
|---|---|---|
| `az` | azimut en degrés (0 = face, + = droite) | 0 |
| `elev` | élévation en degrés (0 = couronne basse, 90 = zénith) | 0 |
| `dspread` | largeur angulaire de la source en degrés | 0 → 30° |

- Le nom est `dspread` et non `spread`, car `spread` existe déjà dans `play2`, `loop`, `reese`, `dblbass`, `bounce`, etc.
- Ce sont des attributs normaux : patterns, TimeVars (`linvar`, `var`…) et PGroups fonctionnent. Par exemple `az=(0,180)` envoie chaque voix de l'accord dans une direction.

**API :**

```python
dome.start()                      # dôme ON + monitor stéréo sur sorties 0/1
dome.start(layout="real")         # panoramique avec les positions mesurées
dome.layout("ideal")              # change de layout à chaud
dome.monitor(False)               # coupe l'écoute virtuelle (concert)
dome.direct(2)                    # 25 canaux → sorties matérielles 2..26
dome.direct(None)                 # coupe les sorties directes
dome.stop()                       # retour au stéréo normal
dome                              # affiche l'état
```

**Fonctionnement interne :**

- `Dome` écrit un fichier `.scd` temporaire (`/tmp/foxdot_dome.scd`). Il demande ensuite à sclang de l'interpréter via le mécanisme existant `/foxdot` (`Server.loadSynthDef`). Il n'y a donc **aucune modification du démarrage SC**.
- Le bus dôme occupe les **32 bus audio du haut** (≈ 992–1016 avec 1024 bus). Ils sont retirés de l'allocateur tournant de FoxDot (`Server.max_busses`) pour éviter les collisions.

### 4.2 SuperCollider (code généré par `Dome.py`)

**`makeSoundDome`** : remplace `makeSound` pour chaque note.

- Même enveloppe et même `DetectSilence` que `makeSound`.
- Panoramique **par direction** : gain gaussien selon l'angle entre la source et chaque HP, `exp(-angle² / 2σ²)` avec σ = `dspread`, normalisé en puissance (Σg² = 1).
- Le canal **L** est placé à `az − 0.4·dspread` et le **R** à `az + 0.4·dspread`. On garde ainsi la largeur stéréo des synthés, et le `pan` existant décale légèrement la source.
- `SendReply` → `/dome/note [az, elev, spread]` pour la visualisation.

**`domeMonitor`** : simule l'écoute dans la salle, sur 2 HP.

- Pour chaque HP : vecteur auditeur→HP, rotation selon le lacet et le tangage de la tête.
- Gain en distance inverse (référence 3,5 m).
- Directivité : les HP visent le centre, donc −9 dB derrière eux.
- Retard de propagation (dist/343).
- Filtre passe-bas pour les sources derrière (repère avant/arrière), puis `Pan2` à puissance constante.
- Positions des HP modifiables (`\spk`, 75 valeurs). Pose de l'auditeur : `lx ly lz yaw pitch`.
- `SendPeakRMS` des 25 canaux à 20 Hz → `/dome/levels`.

**`domeDirect`** : copie les 25 canaux vers `out .. out+24`.

**OSCdefs dans sclang :**

| Adresse | Sens | Rôle |
|---|---|---|
| `/dome/listener x y z yaw pitch` | bridge → sclang | pose de l'auditeur → `domeMonitor` |
| `/dome/speakers [75]` | bridge → sclang | positions des HP du monitor |
| `/dome/monitor amp` | bridge → sclang | volume du monitor |
| `/dome/levels [25]` | scsynth → sclang → bridge | RMS par HP |
| `/dome/note az elev spread` | scsynth → sclang → bridge | chaque note jouée |

Coordonnées envoyées à SC : convention Spat, **x droite, y face, z haut**. Le `yaw` est un azimut en degrés (+ = droite).

### 4.3 Bridge et visualisation

**`dome/bridge.mjs`** (Node, sans nouvelle dépendance : réutilise `ws` de `webTroop/node_modules`) :

- sert `dome_listener.html` sur **http://localhost:8091** ;
- WebSocket navigateur ⇄ OSC/UDP sclang (envoi vers 57120, réception sur 57140) ;
- variables d'environnement : `DOME_HTTP_PORT`, `DOME_OSC_PORT`, `SCLANG_PORT`, `SCLANG_HOST`.

**`dome/dome_listener.html`** (Three.js + Web Audio) :

- vue 3D des 25 HP (couleur par couronne), mini-carte vue de dessus, positions idéales ou réelles ;
- **la caméra est l'auditeur** : glisser pour regarder, WASD pour se déplacer, Q/E pour descendre/monter, Maj pour aller plus vite ;
- raccourcis de position : Sweet spot, Edge, Outside, Lie down (allongé, regard vers le haut), Above ;
- **Mode « Browser test »** : sons de test synthétisés dans le navigateur.
  - Source mobile : orbite, spirale, sauts, manuel.
  - Test HP : de 1 à 25, ou par couronne.
  - Clic sur un HP pour le « pinger ».
  - Rendu « 2 HP » (equal-power) ou « Casque » (HRTF).
- **Mode « FoxDot live »** :
  - envoie la pose de la caméra à SC (~30 Hz) ;
  - affiche les **vrais niveaux** des 25 HP ;
  - fait clignoter chaque note à sa direction.
  - Le son vient de SuperCollider.

### 4.4 Tests effectués (13/10/2026)

- **Code SC** : compilé sur un scsynth de test (port 57190).
  - Une note à az 90° / él 30° sort au maximum sur le **HP 9** (90°/30°).
  - Les voisins captent un peu : 8, 10, 3, 4, 18 et 19.
- **Chaîne complète** : bridge + client WebSocket simulé + scsynth de test.
  - La pose (1.5, 2, 0.5, yaw 45, pitch 10) arrive bien dans `domeMonitor`.
  - 95 messages de niveaux et 12/12 notes reçus côté navigateur.
- **Python** : `az/elev/dspread` sont acceptés comme attributs. L'exit node bascule bien `makeSound` ↔ `makeSoundDome`.
- **Pas encore testé** : une vraie session FoxDot complète (il faut redémarrer FoxDot), et l'écoute réelle du rendu.

---

## 5. Utilisation (répétition à la maison)

```bash
# 1. lancer FoxDot / webTroop comme d'habitude (redémarrer FoxDot après les changements)
# 2. dans un autre terminal :
node dome/bridge.mjs
# 3. ouvrir http://localhost:8091 → bouton « FoxDot live »
```

```python
dome.start()

p1 >> pluck([0,2,4,7], dur=1/4, az=linvar([-180,180],16), elev=10)    # tourne sur la couronne basse
b1 >> dbass([0,3], dur=2, elev=0, dspread=90)                          # basse large et basse
s1 >> blip(P[0:8], az=[0,90,180,-90], elev=var([0,30,60,90],4))        # monte vers le zénith
d1 >> play("x-o-", dspread=60)

dome.layout("real")
dome.stop()
```

Idées de jeu :

- `elev=var([0,30,60,90],8)` : montée à travers les couronnes (comme la structure en 5–7 parties).
- `az=linvar([-180,180],32)` lent pour les pads, rapide (`4`) pour des effets de rotation.
- `dspread=linvar([20,120],64)` : une source ponctuelle qui devient enveloppante.
- `az=PRand(-180,180)` sur des percussions : éclats dans tout le dôme.
- Basse et kick : `elev=0`, `dspread` large, ou HP dédié / sub (voir TODO).

---

## 6. À implémenter (TODO)

### Priorité haute (avant le concert)

- [ ] **`FoxDot.sc`** (`/home/svdk/live/FoxDot.sc` et `config/FoxDot.sc`) : passer `numOutputBusChannels` de 16 à **32**, pour que `dome.direct(2)` puisse sortir sur 2..26.
- [ ] **Limiteur sur les 25 canaux** : `StageLimiter.activate(2)` ne protège que 0/1. Ajouter un `Limiter.ar` dans `domeDirect`, ou activer le StageLimiter sur plus de canaux. **Indispensable pour protéger les HP du lieu.**
- [ ] **Effets globaux** (`global_fx_group`, bus 0) : ils ne s'appliquent pas au bus dôme. Décider : les ignorer en mode dôme, ou les porter sur le bus dôme.
- [ ] **Sub / LFE** : si le lieu a un sub, ajouter une sortie (somme mono passe-bas du bus dôme) et éventuellement un paramètre `sub=`.
- [ ] **Script `dome/connect.sh`** : `pw-link` des sorties SC 3..27 vers les entrées 1..25 du sink Inferno (noms de ports à vérifier avec `pw-link -o` / `pw-link -i`).
- [ ] **Test en conditions réelles** : session FoxDot complète + bridge, mesure CPU (25 gains par note + 25 retards/filtres dans le monitor).
- [ ] **Re-lancer `dome.start()` après un redémarrage de SC** : les synthés du dôme ne survivent pas à un reboot du serveur. À automatiser éventuellement.

### Priorité moyenne

- [ ] **Adressage direct par numéro / couronne** : `spk=9` (un seul HP), `ring="mid"` (répartition sur une couronne). C'est la proposition du lieu (« traiter les sorties comme des chiffres »).
- [ ] **Enregistrement multicanal** : 25 pistes du bus dôme (archive, réécoute, remix binaural).
- [ ] **Autocomplétion webTroop** pour `az`, `elev`, `dspread`, `dome.*`.
- [ ] **Couleur par player** dans la visualisation : passer un identifiant de player dans `/dome/note`.
- [ ] **Monitor binaural** (casque) côté SC, avec ATK/HOA ou HRTF. Le monitor actuel est stéréo simple : la hauteur et l'avant/arrière y sont peu perceptibles.
- [ ] Alternative **VBAP** (sc3-plugins installés) au panoramique gaussien, à comparer à l'écoute.

### Option B : stems + Spat du lieu

Si le lieu préfère spatialiser lui-même (Max/Spat) :

- [ ] sortir N stems (un par player / groupe) au lieu des 25 HP ;
- [ ] envoyer les positions en OSC vers Spat (`/source/N/aed az el dist` ou le format qu'ils indiquent) avec un helper `spat()`. FoxDot parle déjà OSC.

---

## 7. Dante depuis Linux

Dante Virtual Soundcard (le pilote logiciel officiel) n'existe que pour Windows et macOS. Options :

| Option | Pour | Contre |
|---|---|---|
| **Inferno** (Dante libre, Linux) | 25+ canaux depuis le laptop, pas de matériel | alpha, à tester sérieusement |
| Interface multicanal USB / ADAT / MADI → convertisseur Dante du lieu | fiable | dépend du matériel du lieu |
| Interface Dante USB class-compliant (ex. RME Digiface Dante) | fiable si compatible Linux | à vérifier, coût |
| Stems → machine Spat du lieu + OSC | élégant, moins de canaux | dépend de leur setup |
| AES67 via PipeWire | standard | horloge PTPv2 + config Dante Controller, risqué |
| Stéréo, le lieu répartit | sûr | gâche le dôme |

### 7.1 Inferno : ce qu'il faut savoir

- Implémentation Dante en Rust, en espace utilisateur, par rétro-ingénierie. GPLv3 / AGPLv3.
- Maturité : **« Alpha but used in production »**. Utilisable pour des usages non critiques selon l'auteur.
- Testé avec : AVIO, Yamaha (Rio, MY16, PM3), Allen&Heath SQ/Qu, Soundcraft Vi, Klark Teknik DN32, Dante Via / DVS, Dante Controller.
- Composants :
  - `alsa_pcm_inferno` : carte son ALSA virtuelle, fonctionne avec PipeWire et JACK ;
  - `inferno2pipe` : enregistrement ;
  - `inferno_aoip` : bibliothèque.
- **Horloge** : il faut un démon PTP, le **fork Statime** de l'auteur (branche `inferno-dev`).
  - Le Dante classique utilise **PTPv1**, que seul ce fork gère.
  - Inferno doit **suivre** l'horloge maître du lieu, **jamais** être maître.
- Le périphérique virtuel n'existe que tant qu'une appli l'ouvre. D'où l'intérêt d'un **nœud PipeWire permanent** : un crash ou un reboot de scsynth ne fait pas disparaître Inferno du réseau.
- Le routage se fait **depuis Dante Controller, côté lieu**. Inferno ne gère pas encore la modification de ses réglages depuis Dante Controller.
- Latence par défaut : 10 ms (RX/TX). Dante autorise jusqu'à 40 ms.

**Notre machine** (vérifié) :

- `eno1` supporte le **timestamping matériel PTP** (`/dev/ptp0`, « Precise IEEE 1588 ») ;
- Rust / cargo installés, PipeWire 1.6.4, noyau `PREEMPT_DYNAMIC`.

### 7.2 Installation d'Inferno (à faire)

```bash
# 0. Dossier de travail
mkdir -p ~/src && cd ~/src

# 1. Statime (fork Inferno), démon d'horloge PTP
git clone --recurse-submodules -b inferno-dev https://github.com/teodly/statime
cd statime && cargo build --release
#   éditer inferno-ptpv1.toml : interface = "eno1"
#   timestamping matériel : hardware-clock = "auto" (voir README Inferno)
sudo target/release/statime -c inferno-ptpv1.toml
cd ..

# 2. Inferno
git clone --recursive https://github.com/teodly/inferno
cd inferno/alsa_pcm_inferno
sudo pacman -S --needed alsa-lib
cargo build --release
sudo cp ../target/release/libasound_module_pcm_inferno.so /usr/lib/alsa-lib/
#   (vérifier le chemin : find /usr/lib* -type d -name alsa-lib)
```

**`~/.asoundrc`** (d'après `alsa_pcm_inferno/asoundrc`, valeurs en dur pour éviter les chaînes trop longues dans PipeWire) :

```
pcm.inferno {
    type inferno
    NAME "svdk-foxdot"
    BIND_IP "eno1"
    SAMPLE_RATE "48000"
    TX_CHANNELS "32"
    RX_CHANNELS "2"
    # CLOCK_PATH "/dev/ptp0"     # si timestamping matériel
    # TX_LATENCY_NS "10000000"
    hint { show on description "Inferno Dante" }
}
```

**PipeWire** :

```bash
# autoriser les appels horloge au service PipeWire
mkdir -p ~/.config/systemd/user/pipewire.service.d
cp ~/src/inferno/os_integration/systemd_allow_clock.conf \
   ~/.config/systemd/user/pipewire.service.d/override.conf
systemctl --user daemon-reload && systemctl --user restart pipewire

# fréquence d'échantillonnage = celle du lieu (probablement 48 kHz)
pw-metadata -n settings 0 clock.force-rate 48000

# sink Inferno permanent (adapté de alsa_pcm_inferno/start_pipewire_sink)
pw-cli create-node adapter '{ object.linger=1 factory.name=api.alsa.pcm.sink
  node.name="Inferno sink" media.class=Audio/Sink
  api.alsa.path="inferno" session.suspend-timeout-seconds=0
  node.pause-on-idle=false node.suspend-on-idle=false node.always-process=true
  api.alsa.headroom=128 api.alsa.pcm.card=999 }'
```

`api.alsa.headroom` > 0 est **plus important que la taille de période** pour la stabilité.

**Système, le jour J** :

- couper la synchro NTP, qui entre en conflit avec l'horloge Inferno : `sudo systemctl stop systemd-timesyncd` (ou `chronyd`) ;
- pare-feu : ouvrir UDP **4455, 8700, 4400, 8800, 5353** et l'UDP entrant depuis les émetteurs Dante ;
- `eno1` en filaire sur le switch Dante (réseau **primaire**), avec une IP dans le sous-réseau Dante du lieu ;
- mesurer la stabilité temps réel, 20 min Inferno arrêté, et en déduire `TX_LATENCY_NS` :
  `cyclictest --mlockall --smp --priority=80 --interval=5000 --distance=0`

**SuperCollider → Inferno** :

- scsynth tourne via `pw-jack` ;
- `numOutputBusChannels = 32` ;
- `dome.start(monitor=False, direct=2)` → sorties SC 3..27 → `pw-link` vers les canaux 1..25 du sink Inferno (script `connect.sh` à écrire) ;
- les sorties 0/1 restent libres pour un retour casque.

### 7.3 Tester sans le dôme

1. Emprunter un **Mac ou PC Windows** avec **Dante Controller** (gratuit) et une version d'essai de **Dante Virtual Soundcard** ou **Dante Via**.
2. Relier les deux machines par câble (ou petit switch). Vérifier que « svdk-foxdot » apparaît, que l'horloge se verrouille, et que les 25 canaux passent proprement **pendant au moins 1 h**.
3. Tester le crash et le redémarrage de scsynth pendant le flux : le nœud PipeWire doit maintenir Inferno sur le réseau.

### 7.4 Plan B (toujours prêt et câblé)

- Interface multicanal USB → convertisseur Dante du lieu, ou stems vers leur machine Spat.
- En dernier recours : stéréo `dome.stop()` sur 2 canaux Dante, répartis par le lieu.

---

## 8. Questions pour le lieu / Karmen Camina

1. **Connexion** : peut-on brancher un laptop Linux sur le réseau Dante (avec Inferno) ? Ont-ils une interface Dante USB / ADAT / MADI de secours ? Sinon, faut-il venir avec un Mac / PC (DVS) ?
2. **25 sorties directes ou stems ?** Si stems via leur Spat : combien d'entrées, quel format OSC, quel port, quelle IP ?
3. **Horloge** : Dante classique (PTPv1) ou mode AES67 (PTPv2) ? Qui est maître d'horloge ? **Fréquence d'échantillonnage** (48 kHz ?) ?
4. **Réseau** : sous-réseau / IP à utiliser, réseau primaire + secondaire (redondant) ? IGMP / multicast ?
5. **Routage** : un technicien peut-il router nos canaux dans Dante Controller ? Correspondance canal → HP confirmée (1 = zénith … 25) ?
6. **Subwoofer** : y en a-t-il un, sur quel canal, avec quel crossover ?
7. **Niveaux** : niveau de référence / limiteur côté système ? Gain par HP calibré ?
8. **Temps de test dans le dôme** : combien, et quand (la veille ?) ?
9. **Disposition** : où est placé le public, où est-on placé, y a-t-il un « devant » ? (Ça définit az = 0°.)
10. **Vidéo** : projection dans le dôme possible (OF CrashOS / pretexte) ?

---

## 9. Checklist jour J

- [ ] FoxDot.sc à 32 sorties, limiteur sur les 25 canaux du dôme
- [ ] Statime lancé et horloge verrouillée sur le maître du lieu, NTP coupé
- [ ] Sink PipeWire Inferno créé, « svdk-foxdot » visible dans Dante Controller
- [ ] Routage Inferno 1..25 → HP 1..25 fait par le technicien
- [ ] `dome.start(monitor=False, direct=2)` + `connect.sh`
- [ ] Test HP par HP : mode « Speaker check », ou un player `az`/`elev` par HP
- [ ] Bridge + vue 3D sur un écran (optionnel : montrer les sources au public)
- [ ] Plan B câblé et testé
- [ ] Enregistrement (stéréo du monitor, ou 25 pistes si implémenté)

---

## 10. Fichiers et références

| Chemin | Contenu |
|---|---|
| `dome/dome.txt` | positions des HP fournies par le lieu |
| `dome/dome-réel-KarmenCamina.png`, `dome/dome-idéalisé-KarmenCamina.png` | captures Spat Viewer |
| `dome/dome_listener.html` | vue 3D + auditeur virtuel (test navigateur / FoxDot live) |
| `dome/bridge.mjs` | pont WebSocket ⇄ OSC |
| `FoxDot/FoxDot/lib/Dome.py` | module dôme (code SC généré, API `dome.*`) |
| `FoxDot/FoxDot/lib/ServerManager.py` | `get_exit_node` → `makeSoundDome` |
| `FoxDot/FoxDot/lib/Players.py` | attributs `az`, `elev`, `dspread` |
| `FoxDot.sc`, `config/FoxDot.sc` | options de démarrage SC (nombre de sorties) |

Liens :

- Inferno : https://github.com/teodly/inferno
- Statime (fork Inferno) : https://github.com/teodly/statime (branche `inferno-dev`)
- network-audio-controller (`netaudio`, contrôle Dante en ligne de commande) : https://github.com/chris-ritsen/network-audio-controller
