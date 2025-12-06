# Installation and Setup Guide for CrashServer

## System Requirements
Before installing the software, ensure that your system meets the following requirements:
- only tested on Linux
- Python 3.12 or higher
- Supercollider & SC3 plugins

## Python libraries
The following Python libraries are required:
- `python-websockets`
- `python-rtmidi`
- `python-pyfiglet` (optional for ASCII art)

## Supercollider Setup
- install Quarks: BatLib, FeedBack, FoxDot, miSCellaneous_lib
- install this supercollider plugins (see `config/sc_Extensions`):
    - [mi-UGens](https://github.com/v7b1/mi-UGens)
    - [PortedPlugins](https://github.com/madskjeldgaard/portedplugins)
    - [Open303](https://github.com/schollz/open303)
- replace `.local/share/SuperCollider/downloaded-quarks/FoxDot/FoxDot.sc` with the one provided in `config/FoxDot.sc` for multioutput, midicc and memsize fixs.

## Configuration

Before running CrashServer, you may need to adjust the configuration files located in the `webTroop/crash_config.json`. 

> **Remove comments from the JSON file before using it.**

```json
{
    "HOST_IP": "192.168.1.42", // the IP address of your machine
    "FOXDOT_PATH": "/home/zbdm/CrashServer/live/FoxDot", // path to FoxDot installation
    "sample_path": "/home/zbdm/CrashServer/ UltimateSamples/", // path to your samples
    "FOXDOT_WS_PORT": 20000, // FoxDot websocket port
    "freesoundApiKey": "theAPIkeyFromFreesound", // your Freesound API key
    "SC_CPU_PORT": 2887, // SuperCollider CPU OSC send port
    "showTodo": 0, // set to 1 to show TODO list 
    "ARDUINO": 0 // set to 1 if you want to use Arduino integration
}
```

## Install webTroop
To install the webTroop library, navigate to the `webTroop` directory and run:
```bash
npm install
```

## Running CrashServer
go to the `/webTroop` directory and run:
```bash
HOST=0.0.0.0 PORT=4444 YPERSISTENCE=./dbDir node ./node_modules/y-websocket/bin/server.cjs
```

In another terminal, navigate to the CrashServer directory and run:
```bash
node server.js
```

And then, in another terminal, run:
```bash
npm run dev
```

This will start the CrashServer application, and you can access it via your web browser at `http://<HOST_IP>:3000`.