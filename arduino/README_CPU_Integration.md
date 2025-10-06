# Intégration CPU CrashPanel → Arduino

## 🔗 Flux de données (Architecture interne)

```
CrashPanel.js → WebSocket (port 1234) → Server.js → Arduino USB
     │                 │                    │             │
   CPU %        {type:'cpu_data'}      Mapping a-f      LED States
```

## 📊 Mapping CPU → Arduino

| CPU Range | Caractère | État LED Arduino |
|-----------|-----------|------------------|
| 0-20%     | `a`       | Niveau 0 (calme) |
| 20-40%    | `b`       | Niveau 1         |
| 40-60%    | `c`       | Niveau 2         |
| 60-80%    | `d`       | Niveau 3         |
| 80-100%   | `e`       | Niveau 4         |
| 100%+     | `f`       | Niveau 5 (max)   |

## ⚙️ Fonctionnalités implémentées

### 🛡️ **Protection anti-spam**
- **Cooldown CPU** : 1 seconde entre les mises à jour
- **Détection de changement** : N'envoie que si le niveau change
- **Flush automatique** : Assure l'envoi immédiat

### 🔄 **Reconnexion automatique**
- Reconnexion au CrashPanel toutes les 5 secondes si déconnecté
- Continue de fonctionner même sans CrashPanel

### 📝 **Logs informatifs**
- Affichage des niveaux CPU envoyés
- Statut de connexion CrashPanel
- Erreurs de communication

## 🧪 Tests disponibles

### 1. Test du flux interne
```bash
# Terminal 1: Démarrer le serveur
node server.js

# Terminal 2: Tester le flux CPU interne
node test_internal_cpu.js

# Observer les logs: CPU simulé → Arduino
```

### 2. Test direct Arduino
```bash
# Test les 6 niveaux CPU directement sur l'Arduino
node test_arduino_cpu.js
```

### 3. Test Arduino simple
```bash
# Test basique de communication
node test_arduino.js /dev/ttyACM1
```

## 🚀 Utilisation en production

1. **Vérifier la configuration**
   ```json
   // crash_config.json
   {
     "HOST_IP": "localhost"  // IP du CrashPanel
   }
   ```

2. **Démarrer le serveur**
   ```bash
   npm run server
   ```

3. **Vérifier les connexions**
   - ✅ Arduino détecté et connecté
   - ✅ Connexion au CrashPanel établie
   - ✅ Messages CPU reçus et transmis

## 🔧 Configuration Arduino

Le code Arduino `living_server_light_V2.ino` gère déjà les caractères `a-f` :
- Change `metaIndex` (0-5) selon le niveau CPU
- Modifie la vitesse et couleur des pulsations LED
- Met à jour l'état du "meta brain" central

## 📈 Monitoring

Le système affiche en temps réel :
```
État CPU 'c' (45%) envoyé à l'Arduino
Connexion au CrashPanel établie pour monitoring CPU
Arduino connecté avec succès!
```

## 🛠 Dépannage

### CrashPanel non connecté au serveur principal
```
WebSocket connection failed
→ Vérifier que le serveur principal fonctionne sur le port 1234
```

### Arduino non détecté
```
Arduino non trouvé automatiquement
→ Vérifier la connexion USB et les permissions
```

### Pas de mise à jour CPU
```
→ Vérifier que le CrashPanel envoie bien les messages 'cpu'
→ Utiliser le simulateur pour tester
```

Le système est maintenant complet : CrashPanel → Server → Arduino ! 🎯