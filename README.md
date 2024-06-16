# Crash Server Ultimate live Repo

## Working with Python virtual env

For a better foxdot modules management, use a python virtual environment.  
Here are the steps to create and activate it.  

### Create, activate and install modules

```bash
cd /path/to/FoxDot
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

To leave the virtual environment, just type `deactivate` in the terminal.  

### List installed packages
```bash
pip freeze
```

### Update `requirements.txt` file if new modules
```bash
pip freeze > requirements.txt
```

## Crash Config file

Here is the content of the `crash_config.py` file in the root directory if it doesn't exist.  
It's better to rename the `crash_config.py.sample` to `crash_config.py` and start tweaking it.  

### Global config
crash_path = "/DATA/sound/UltimateSamples/"  
ipZbdm = "192.168.0.42"  
ipSvdk = "192.168.0.40"

### Who is Troop Server & what is your name
crashTroopHost=ipZbdm # Troop server IP  
crashTroopName="Zbdm" # your name in troop

### Who host CrashOS
crashOSIp = ipSvdk   # Crash OS IP

### CrashOS & osc out & CrashPanel
crashPanelSending = True  # enable output to CrashPanel  
crashOsEnable = True  # enable history code crashos (!!! True for only 1 of the 2 players)  
crashInstantCode = True # enable instant code display (both player can be True)
crashSendMode = "osc" # enable "osc" or "udp" sending  

### Not so important

#### Troop
crashTroopPort=57890  
crashTroopPassword=""

#### Crash OS
crashOSPort = 20000

### Console output
printOut = True # server msg log console output

### Live config, startup live & arduino button
startupLive = True	# load crashserver live funtion (attack,  lost, ...)

## CrashOs infos

UDP message send (string) to port 20000, start with  :
- '#' for 'Crash' player name code
- '!' for 'Server' payer name code
- '@' for server generated code
- '_' for state, 
- '_0' for activate the server.  


OSC & UDP PORT in use:
- **2000** : crashPanel
- **2887** : Foxdot osc receiver from crashOS
- **20000** : crashOS


