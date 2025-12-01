# webTroop - Un portage de Troop en full web

## Préréquis
- nodejs
- FoxDot
- SuperCollider

## Installation

```bash
git clone
cd webTroop
npm install
```

## Configuration
Copier le fichier `crash_config_sample.json` en `crash_config.json` et modifier les paramètres en fonction de votre configuration
Les ports n'ont pas besoin d'être modifiés si vous n'avez pas de conflit.


## Utilisation

### Lancer le serveur

```bash
node server.js
```

````markdown
# webTroop - Un portage de Troop en full web

## Préréquis
- nodejs
- FoxDot
- SuperCollider

## Installation

```bash
git clone
cd webTroop
npm install
```

## Configuration
Copier le fichier `crash_config_sample.json` en `crash_config.json` et modifier les paramètres en fonction de votre configuration
Les ports n'ont pas besoin d'être modifiés si vous n'avez pas de conflit.


## Utilisation

### Lancer le serveur

```bash
node server.js
```

### lancer le server de synchro websocket pour pair-programming
    
    ```bash
    dans \webTroop
    HOST=0.0.0.0 PORT=4444 YPERSISTENCE=./dbDir node ./node_modules/y-websocket/bin/server.cjs
    ```

### lancer le client

```bash
npm run dev
```
### Se connecter

Ouvrir un navigateur et se connecter à l'adresse `http://localhost:3000`

---

## Arduino (optionnel)

- Activation dans `crash_config.json` via `"ARDUINO": true`.
- Détection automatique du port série (ttyACM*/ttyUSB*). Baud 115200.
- Envois depuis FoxDot/serveur vers Arduino selon l'auteur du message:
  - `zbdm` → `z`
  - `svdk` → `v`
  - `SERVER` → `s`
- CPU depuis CrashPanel: le client envoie `{ type: "cpu_data", cpu: <0-100> }` au serveur WebSocket (port 1234). Le serveur mappe en lettres `a`..`f` avec un cooldown de 1s et uniquement en cas de changement de niveau.
- Bouton Arduino: si le sketch envoie 10× `s` consécutifs → `activateServer()` est envoyé à FoxDot; 10× `c` → `soff()`. Anti-rebond interne de 2s pour éviter les doubles déclenchements.

## Définitions dynamiques (Alt‑I)

- À la réception de l'autocomplete FoxDot, les définitions de synths et d'effets sont enrichies dynamiquement:
  - Synths: seules les entrées dont le label se termine par `_` (avec paramètres) sont prises; la signature est extraite pour affichage.
  - FX: même logique; les paramètres sont ajoutés à la table des définitions.
- Utilisez `Alt‑I` sur un nom de synth/FX/fonction pour afficher la signature utile.

````

### lancer le client

```bash
npm run dev
```
### Se connecter

Ouvrir un navigateur et se connecter à l'adresse `http://localhost:3000`
