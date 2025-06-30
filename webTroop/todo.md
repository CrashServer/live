# WebTroop 2000

## Todo
- [ ] randomizer
- [ ] keymap vim, emacs, ...
- [X] ajout paramètre pour showTodo ou pas


## Bug
- [X] copy paste
- [X] etat du serveur
- [X] unifier les fichiers de configuration
- [X] fix le ascii_gen 
- [X] fix des ligatures 
- [X] fix plats du jour length
- [X] fix undefined dans les logs
- [X] unifier les variables css pour tous les composants
- [X] stop/start sur comment
- [X] stop/start sur multi block
- [X] fix comment sur une ligne sans player reconnu
- [X] voir config signaling
- [X] anti-jump
- [X] search
- [X] font interface
- [X] undo for user (compliqué)
- [X] fix ping au ligne bon numéro
- [X] visibilité du ping
- [X] chaos bug et attack de temps à autre.
- [X] trim erreurs dans la console  

### Editeur
- [X] alt + + pour augmenter une valeur
- [X] dialog box pour envoie messages video
- [X] autocompletion foxdot
- [X] améliorer coloration syntaxique pour foxdot
- [X] ctrl + . pour arreter Foxdot
- [X] ctrl + alt + C pour envoyer commenter une ligne
- [X] ctrl + shift + D pour dupliquer une ligne
- [X] Amélioration du rendu des joueurs
- [X] Flasher lors de l'évaluation d'une ligne
- [X] ctrl + shift + enter : Evalation d'un block
- [ ] player actif dans le gutter
- [X] flasher chez les 2 joueurs
- [X] coloration des erreurs dans la console
- [X] liste des evaluations dans console
- [ ] ajout de tabs pour plusieurs editeurs
- [ ] flash message pour changement de nom de joueur
- [X] position des joueurs dans le gutter
- [X] affichage de l'instant code entre le log et l'editeur + no de ligne 
- [X] ping sur une ligne pour laisser des marques 
- [X] flash message pour envoie de message
- [X] save code
- [ ] opacité de l'editeur
- [X] affichage des player solo
- [X] sauvegarde attack 

### Autocomplete 
- [X] autocompletion foxdot
- [X] ajout des fonctions
- [X] ajout des players
- [X] ajout des loops (récupéré depuis foxdot)
- [X] autocomplete synth

### logs
- [X] coloration en fonction du joueur et affichage du nom du joueur

### Serveur
- [X] Envoie des messages 
- [X] fix bug deconnection, envoie de message
- [X] utillisation webrtc pour les messages avec Yjs
- [X] persistance des messages (voir indexeddbProvider)
- [X] gestion du out de foxdot
- [X] envoie des message du serveur
- [X] envoie des markers aux joueurs
- [X] enregistrement des sessions de code / modifier pour utilisation dans foxdot server
- [ ] ajout time stamp

### Chat
- [X] Ajouter un chat
- [X] propager le chat aux autres joueurs

### Panneau de configuration
- [X] changement police
- [X] changement couleur
- [X] changement taille
- [X] Nom du joueur
- [X] Sauvegarder l'état de l'interface en localstorage
- [X] liste des shortcuts
- [X] changement du theme de l'interface

### CrashPanel
- [X] intégrer précédentes modifications
- [X] tests envoie de message websockets vers cable
- [X] raz chrono
- [X] stop player en cliquant sur le joueur
- [X] affichage du nom de la loop dans la liste des players actif
- [X] ajout d'un bouton pour activer le server (click title)
- [X] ajout d'un bouton pour changer le theme dark/light
- [ ] ajout des loops au click

### Shortcut
- ctrl + ; pour arreter Foxdot
- ctrl + c pour copier la ligne courante
- ctrl + d pour tout selectionner
- ctrl-shift-d pour dupliquer
- ctrl-shift-up pour monter la ligne
