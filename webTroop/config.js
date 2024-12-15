const SERVER_IP = '192.168.1.7';

export const CONFIG = {
    SERVER_IP, // adresse IP du serveur

    FOXDOT_SERVER: `ws://${SERVER_IP}:1234`, // adresse du serveur local qui communique avec FoxDot
    CRASHOS_SERVER: `ws://${SERVER_IP}:20000`, // adresse du serveur qui transmet les données à CrashPanel et Cables.gl
    SIGNALING_SERVER: `ws://${SERVER_IP}:4444`, // adresse du serveur de signalisation pour WebRTC
    FOXDOT_PATH: '/home/zbdm/CrashServer/live/FoxDot', // chemin vers le dossier FoxDot
}   