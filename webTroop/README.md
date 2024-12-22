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
modifier le fichier `crash_config_sample.json` en `crash_config.json` et modifier les paramètres en fonction de votre configuration
Les ports n'ont pas besoin d'être modifiés si vous n'avez pas de conflit.


## Utilisation

### Lancer le serveur

```bash
node server.js
```

### lancer le server de signaling
    
    ```bash
    dans \webTroop
    HOST=localhost PORT=4444 YPERSISTENCE=./dbDir node ./node_modules/y-websocket/bin/server.cjs
    ```

### lancer le client

```bash
npm run dev
```
### Se connecter

Ouvrir un navigateur et se connecter à l'adresse `http://localhost:3000`
