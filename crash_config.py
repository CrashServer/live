
''' Global config '''
crash_path = "/home/zbdm/crashserver/UltimateSamples/"
ipZbdm = "localhost"
ipSvdk = "192.168.0.40" #"192.168.0.40"

# Who is Troop Server & what is your name
crashTroopHost=ipZbdm # Troop server IP
crashTroopName="Zbdm"    # your name

 # Who host CrashOS
crashOSIp = ipZbdm   # Crash OS IP

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

