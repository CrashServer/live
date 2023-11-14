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

//////
Here is the content of the crash_config.py file in the root directory if it doesn't exist.


''' Global config '''
crash_path = "/DATA/sound/UltimateSamples/"
ipZbdm = "192.168.0.42"
ipSvdk = "192.168.0.40" #"192.168.0.40"

# Who is Troop Server & what is your name
crashTroopHost=ipZbdm # Troop server IP
crashTroopName="Zbdm"    # your name

 # Who host CrashOS
crashOSIp = ipSvdk   # Crash OS IP

''' CrashOS & osc out & CrashPanel '''
crashPanelSending = True  # enable output to CrashPanel

crashOsEnable = True  # enable history code crashos (!!! True for only 1 of the 2 players)
crashInstantCode = True # enable instant code display (both player can be True)

crashSendMode = "osc" # enable "osc" or "udp" sending

#### Not so important #################

# Troop
crashTroopPort=57890
crashTroopPassword=""

# Crash OS
crashOSPort = 20000

''' Console output '''
printOut = True # server msg log console output

''' Live config, startup live & arduino button '''
startupLive = True	# load crashserver live funtion (attack,  lost, ...)



