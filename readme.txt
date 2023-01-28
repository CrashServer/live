Configuration :

Dans Troop/src/crashconfig.py :

crashTroopHost & crashTroopPort  : ip & port du serveur Troop
crashTroopName : nom dans troop
crashOSIp & crashOSPort : adresse de la machine hebergeant CrashOS 

Dans foxdot/lib/Crashserver/crash_generator/server_conf.py

changer path Ultimate samples crash
changer oscIp&port : adresse machine crashOS


///////

UDP message send (string) to port 20000, start with  :
	- '#' for 'Crash' player name code
	- '!' for 'Server' payer name code
	- '@' for server generated code
	- '_' for state, _0 for activate the server.  


OSC & UDP PORT in use:
2000 : crashPanel
2887 : Foxdot osc receiver from crashOS
20000 : crashOS
