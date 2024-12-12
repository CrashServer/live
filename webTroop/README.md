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

## Utilisation

### Lancer le serveur

```bash
node server.js
```

### lancer le server de signaling
    
    ```bash
    dans \webTroop
    PORT=4444 node ./node_modules/y-webrtc/bin/server.js
    ```

### lancer le client

```bash
npm run dev
```
### Se connecter

Ouvrir un navigateur et se connecter à l'adresse `http://localhost:3000`
