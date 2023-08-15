#coding: utf8
#!/usr/bin/env python3
##############################################################################################
#####              CRASH GENERATOR        #############
#########################################
from random import randint, random, sample, choices, seed
from time import gmtime, strftime
import threading
# import configparser
import os

class genSeed():
	''' return a seed for random based on actual time for multiplayer sync '''
	def __init__(self):
		self.seedR = int(''.join(map(str, map(ord, strftime("%a, %d %b %Y %H:%M", gmtime())))))
		self.seedOrigin = self.seedR		
	def txt(self, seedTxt):
		self.seedR = int(sum([ord(c) for c in str(seedTxt)]))
	def add(self):
		self.seedR += 1
	def set(self):
		seed(int(self.seedR))
	def get(self):
		return self.seedOrigin

try:
	genSeed = genSeed()
	genSeed.set()
except Exception as e:
	print("Failed to init random seed", e)

try:
	from .Crashserver.crash_generator.weapons import *
	from .Crashserver.crash_generator.composition import *
	from crash_config import *
	# from .Settings import FOXDOT_ROOT
	from .Crashserver.crash_generator.server_conf import *
except Exception as e:
	print("Error in generating weapons code", e)

serverActive = False

if crashOsEnable:
	# Osc/udp sender
	try:
		if crashSendMode == "udp":
			crashFoxDot_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		if crashSendMode == "osc":
			crashFoxDot_socket = OSCClient()
			crashFoxDot_socket.connect((crashOSIp, crashOSPort))

		#osc receive state
		class OSCReceiver():
			''' OSC Receiver for evaluate command from CrashOS'''
			def __init__(self, crashOSIp):
				self.oscserver = ThreadingOSCServer(("0.0.0.0",2887))
				self.oscserver.addDefaultHandlers()
				self.oscserver.addMsgHandler("/cmd/serverState", self.receiveState)
				self.oscserver.addMsgHandler("/cmd/Video", self.receiveVideo)
				self.videoGrp = 99
				self.videoIndex = 99
				self.videoTotal = 99
				self.videoIntegrity = 99
				self.thread = Thread(target = self.oscserver.serve_forever)
				self.thread.daemon = True
				self.thread.start()

			def receiveState(self, address, tags, contents, source):
				state = int(contents[0])
				if state == 0:
					soff()
				elif state == 1:
					activateServer()
					#son(1,3,9)
				else:
					print("error receiving osc from CrashOs")

			def receiveVideo(self, address, tags, contents, source):
				self.videoGrp = int(contents[0])
				self.videoIndex = int(contents[1]) + 1
				self.videoTotal = int(contents[2])
				self.videoIntegrity = int(contents[3])

		oscReceiver = OSCReceiver(crashOSIp)

	except Exception as err:
		print(f"config UDP or OSC problem : {err}")

class runServer():
	''' Run the server with runserver.start() and generate randomly players'''
	def __init__(self, time=timeChange):
		self.loop = True
		self.time = time
	def toggle(self):
		if self.loop:
			self.stop()
		else:
			self.run()
			self.start()
	def run(self):
		self.loop = True
		sendOut("Server Activated")
	def stop(self):
		self.loop = False
		sendOut("Stop Server")

	def start(self, seedTxt=False):
		try:
			if seedTxt != False:
				genSeed.txt(seedTxt)
			else:
				genSeed.add()
				genSeed.set()
		except Exception as e:
			print("start genseed ", e)
		if self.loop:
			try:
				if serverActive:
					server_order()
				duration = self.time*randint(multDurationMin,multDurationMax)
				Clock.future(duration, lambda: self.start())
			except Exception as e:
				print("start server : ", e)

server = runServer()
playerCount = {}

def server_order():
	''' Server routine, choose [add/stop player, change param, add fx, add function,...'''
	try:
		numPlayer = len(Clock.playing)
		if numPlayer < 3:
			order = [add_player]
		elif numPlayer > maxPlayer:
			order = [stop_player]
		else:
			order = choices([add_player,
							stop_player,
							add_fx,
							change_degree,
							add_player_param,
							add_player_attribute,
							add_event,
							change_synth_attr],
							[probAddPlayer,probStopPlayer,probAddFx,probChangeDegree,probAddPlayerParam,probAddPlayerAttribute,probAddEvent,probChangeSynthAttr]) # probability
		order[0]()  # evaluate order
		addPlayerTurn()  # add 1 turn to each playing players
	except Exception as err:
		print("server_order problem : ", err)

def add_player(copyText=False, playerType=None):
	''' add a random synth, drum, loop player  '''
	try:
		para_dict = {}
		textGenerated = ""
		if playerType == None:
			playerType = choices(["synth","drum","loop"],[probAddSynth, probAddDrum, probAddLoop])[0]
		#generate parameter
		if playerType == "synth":
			para_dict = generate_random_synth_player()
			if not copyText:
				run_player_synth(copyText, **para_dict)
			else:
				textGenerated = run_player_synth(copyText, **para_dict)
				return textGenerated 
		if playerType == "drum":
			para_dict = choices([generate_drum_style_player(), generate_random_drum_player()],[probAddStyleDrum,probAddRandomDrum])[0]
			if not copyText:
				run_player_drum(copyText, **para_dict)
			else:
				textGenerated = run_player_drum(copyText, **para_dict)
				return textGenerated
		if playerType == "loop":
			para_dict = generate_random_loop_player()
			if not copyText:
				run_player_loop(copyText, **para_dict)
			else:
				textGenerated = run_player_loop(copyText, **para_dict)
				return textGenerated
	except Exception as err:
		print("add_player problem : ", err)


def stop_player():
	''' choose randomly playing players and stop them'''
	try:
		plyList = Clock.playing
		if len(plyList) > 1:
			playerChoice = choices([choices(plyList),sample(plyList,randint(1,len(plyList)-1))],[probStopOnePlayer,probStopMorePlayers])[0]
			playerChoice += [p for p in Clock.playing if p in playerCount.keys() and playerCount[p] > maxPlayerTurn]
			for ply in playerChoice:
				if ply in playerCount.keys() and playerCount[ply] > minPlayerTurn:
					sendOut(f"{ply}.stop()")
					ply.stop()
				else:
					pass
		if len(Clock.playing) == 0:
			add_player()
			addPlayerTurn()
	except Exception as err:
		print("stop_player problem : ", err)

def add_fx():
	''' add fx parameters '''
	try: 
		player = choice(Clock.playing)
		fx = GENERATE_FX(fxdict)
		for name, argm in fx.items():
			sendOut(f'{player}.{name}={argm}')
			player.__setattr__(name, eval(argm))
	except Exception as err:
		print("add_fx problem : ", err)

def run_player_synth(copyText=False, **kwargs):
	''' Play synth player'''
	try:
		player = kwargs.get("player")
		synth = kwargs.get("synth")
		degree = kwargs.get("degree")
		dur = kwargs.get("dur")
		oct = kwargs.get("oct")
		degree = eval(degree)
		params = GENERATE_SYNTH_ARGS(synth)
		paramsText = synthArgsToText(params)
		dur = kwargs.get("dur")
		if max(degree) > 10:
			degree = remap_pattern(degree, 0,7)
		if not copyText:
			~eval(player) >> eval(synth)(eval(str(degree)), dur=eval(dur), oct=eval(oct))
			for argm, value in params.items():
				eval(player).__setattr__(str(argm), eval(str(value)))
			sendOut(f'{player} >> {synth}({degree}, dur={dur}, oct={oct}, {paramsText})')
			addFilter(eval(player))
		else:
			return f'{player} >> {synth}({degree}, dur={dur}, oct={oct}, {paramsText})'
	except Exception as err:
		print("run_player_synth problem : ", err)

def synthArgsToText(params=''):
	''' Add synth parameters '''
	try:
		paratxt = ''
		for argm, value in params.items():
			paratxt += f'{argm} = {value}, '    
		return paratxt
	except Exception as err:
		print("synthArgsToText problem : ", err)

def run_player_drum(copyText=False, **kwargs):
	''' Play drum player'''
	try:
		player = kwargs.get("player")
		synth = kwargs.get("synth")
		degree = kwargs.get("degree")
		dur = kwargs.get("dur")
		sample = kwargs.get("sample")
		rate = kwargs.get("rate")
		if not copyText:
			sendOut(f'{player} >> {synth}("{degree}", dur={dur}, sample={sample}, rate={rate})')
			~eval(player) >> eval(synth)(degree, dur=eval(dur), sample=eval(sample), rate=eval(rate))
			addFilter(eval(player))
		else:
			return f'{player} >> {synth}("{degree}", dur={dur}, sample={sample}, rate={rate})'
	except Exception as err:
		print("run_player_drum problem : ", err)

def run_player_loop(copyText=False, **kwargs):
	''' Play loop player'''
	try:
		player = kwargs.get("player")
		synth = kwargs.get("synth")
		degree = kwargs.get("degree")
		dur = kwargs.get("dur")
		sample = kwargs.get("sample")
		if not copyText:
			sendOut(f'{player} >> {synth}("{degree}", dur={dur}, sample={sample})')
			~eval(player) >> eval(synth)(degree, dur=eval(dur), sample=eval(sample))
			addFilter(eval(player))
		else:
			return f'{player} >> {synth}("{degree}", dur={dur}, sample={sample})'
	except Exception as err:
		print("run_player_loop problem : ", err)

def addPlayerTurn():
	''' add one to player dictionnary turn '''
	try:
		playerList = Clock.playing
		for p in playerList:
			if p in playerCount.keys():
				playerCount[p] += 1
			else:
				playerCount[p] = 1
		# Clean non playing player
		delplayer = [k for k in playerCount.keys() if k not in playerList]
		for d in delplayer:
			playerCount.pop(d, None)
	except Exception as err:
		print("addPlayerTurn problem : ", err)

def add_player_param():
	''' add player parameters (like .spread, .offbeat, .jump, ...) '''
	try:
		player = choice(Clock.playing)
		if (player_type(player)!="loop"):
			param = gen_player_param()
			sendOut(f'{player}.{param}')
			eval(f'{player.name}.{param}')
	except Exception as err:
		print("add_player_param problem : ", err)

def add_player_attribute():
	''' add or change player attribute (sus, pan, ) '''
	try:
		player = choice(Clock.playing)
		attr = gen_player_attributes(player_type(player))
		sendOut(f'{player}.{attr[0]}={attr[1]}')
		player.__setattr__(attr[0], eval(str(attr[1])))
	except Exception as err:
		print("add_player_attribute problem : ", err)

def change_degree(player=None):
	''' According to player type change degree(synth), char(drum), sample(loop)'''
	try:
		if not player:
			player = choice(Clock.playing)
		playerType = player_type(player)
		if playerType == "loop":
			param = choices(["degree", "position", "sample"],probLoopChangeDegree)[0]
			if param == "position":
				deg = GENERATE_FLOAT_LIST(0,1)
			else:
				deg = GENERATE_INTEGER(0,99)
			sendOut(f"{player}.{param}={deg}")
			player.__setattr__(param,eval(deg))
		elif playerType == "drum":
			deg = change_drum_char(player.__getitem__("degree"))
			sendOut(f'{player}.degree = {deg}')
			player.__setattr__("degree", eval(str(deg)))
		else:
			deg = choices([gen_arp(), 'melody()', 'PGauss()','PChain2(chords)'],probSynthChangeDegree)[0]
			sendOut(f'{player}.degree = {deg}')
			player.__setattr__("degree", eval(deg))
	except Exception as err:
		print("change_degree problem : ", err)

# def change_adsr(player=None):
#   try:
#       if player == None:
#           player = choice(Clock.playing)
#       playerType = player_type(player)
#       if playerType == "loop" or playerType == "drum":
#           genAtk = GENERATE_FLOAT_LIST(0.0,1.0)
#           genSus = GENERATE_FLOAT_LIST(0.0,1.0)
#           player.__setattr__('sample_atk',eval(genAtk))
#           sendOut(f"{player}.sample_atk={genAtk}")
#           player.__setattr__('sample_sus',eval(genSus))
#           sendOut(f"{player}.sample_sus={genSus}")
#       else:
#           adsr = GENERATE_ADSR(player.synthdef, float(player.sus))
#           for argm, value in adsr.items():
#               player.__setattr__(argm,eval(value))
#               sendOut(f"{player}.{argm}={value}")
#   except Exception as err:
#       print("change_adsr problem : " + err)

def change_synth_attr(player=None):
	''' add or change the synth attr or loop/play adsr '''
	try: 
		if player == None:
				player = choice(Clock.playing)
		playerType = player_type(player)
		if playerType == "synth":
			params = GENERATE_SYNTH_ARGS(player.synthdef)
			for k, v in params.items():
				player.__setattr__(k, eval(v))
				sendOut(f"{player}.{k}={eval(v)}")
		else:
			pass
			# genAtk = GENERATE_FLOAT_LIST(0.0,0.2)
			# genSus = GENERATE_FLOAT_LIST(0.8,1.0)
			# player.__setattr__('sample_atk',eval(genAtk))
			# sendOut(f"{player}.sample_atk={genAtk}")
			# player.__setattr__('sample_sus',eval(genSus))
			# sendOut(f"{player}.sample_sus={genSus}")
	except Exception as err:
		print(f"change_synth_attr problem : {err}")

def add_event():
	try:
		rnd_event = choices([change_scale, change_root, humanizer, change_bpm, masterFilter, dropevent, addKick, addAccompany, addFxOut],
							[probChangeScale, probChangeRoot, probChangeHumanizer, probChangeBpm, probAddLpf, probAddDrop, probAddKick, probAddAccompany, probAddFxOut])[0]
		rnd_event()
	except Exception as err:
		print("add_event problem : ", err)

def sendOut(msg=""):
	''' send all generated text to output : console, osc '''
	try:
		if crashOsEnable:
			if crashSendMode == "udp":
				sendUdp(msg)
			if crashSendMode == "osc":
				sendOsc(msg)
		if printOut:
			if startupLive:
				msg = 'SERVER: ' + msg
			print(msg)
	except Exception as err:
		print("sendOut problem : ", err)

def sendUdp(msg=""):
	''' Send osc text to osc ip '''
	try:
		byte_message = bytes("@" + msg, "utf-8")
		crashFoxDot_socket.sendto(byte_message, (crashOSIp, crashOSPort))
	except:
		pass

def sendOsc(msg=""):
	''' Send osc text to osc ip '''
	try:
		byte_message = OSCMessage("/serverCode", msg)
		crashFoxDot_socket.send(byte_message)
	except:
		pass

def player_type(player):
	''' return player type '''
	try:
		if player.synthdef in ["loop"]:
			return "loop"
		elif player.synthdef in ["play", "play2"]:
			return "drum"
		else:
			return "synth"
	except Exception as err:
		print("player_type problem : ", err)

def change_bpm():
	''' Change randomly and lineary the bpm'''
	try:
		bpmNow = int(Clock.bpm)
		bpmTarget = randint(changeBpmMin,changeBpmMax)
		randTime = randint(changeBpmTimeMin,changeBpmTimeMax)
		sendOut(f'Clock.bpm = lininf({bpmNow}, {bpmTarget},{randTime})')
		Clock.bpm = lininf(bpmNow, bpmTarget,randTime)
	except Exception as err:
		print("change_bpm problem : ", err)

def change_scale():
	''' set a random scale '''
	try:
		scale_name = "freq"
		while scale_name == "freq":
			scale_name = choice(Scale.names())
		Scale.__setattr__("default", Scale.get_scale(scale_name))
		sendOut(f'Scale.default={scale_name}')
	except Exception as err:
		print("change_scale problem : ", err)

def change_root():
	''' up or down root '''
	try:
		updown = 0
		while updown == 0:
			updown = randint(changeRootMin,changeRootMax)
		if int(Root.default) > 5:
			updown = -1
		elif int(Root.default) < -4:
			updown = 1
		sendOut(f'Root.default+={updown}')
		Root.default=Root.default + updown
	except Exception as err:
		print("change_root problem : ", err)

def humanizer(player=None):
	''' humanize a drum pattern '''
	try:
		if player == None:
			player = choice(Clock.playing)
		hum = [int(GENERATE_INTEGER(humanAmpMin,humanAmpMax)), int(GENERATE_INTEGER(humanDelayMin,humanDelayMax)), int(GENERATE_INTEGER(humanSwingMin,humanSwingMax))]
		sendOut(f'{player}.humanize({hum[0]}, {hum[1]}, {hum[2]})')
		player.human(hum[0], hum[1], hum[2])
	except Exception as err:
		print("humanizer problem : ", err)

def masterFilter():
	''' Add random Master().lpf, Master().hpf '''
	try:
		#timef = 4*round(randint(3,32)/4)
		timef = choice([4,8,16,32])
		filtr = choice(["lpf", "hpf"])
		set_master_filter(filtr, freqs[filtr], timef)
		sendOut(f'Master().{filtr}=linvar({freqs[filtr]},[{timef-0.25},0.25])')
		Clock.future(timef, lambda: set_master_filter(filtr, 0, 0))
	except Exception as err:
		Master().__setattr__("lpf", 0)
		Master().__setattr__("hpf", 0)
		print("masterFilter problem : ", err)

def set_master_filter(filtr, freqf, timef):
	''' set the master filter, use with clock.future '''
	try:
		if timef == 0:
			Master().__setattr__(filtr, 0)
		else:
			Master().__setattr__(filtr, linvar(freqf, [timef-0.25, 0.25], start=now))
	except Exception as err:
		print("set_master_filter problem : ", err)

def dropevent():
	''' Add random drop() '''
	try:
		time = randint(dropTimeMin,dropTimeMax)
		drop(time, dropTimeMax-time,dropLoop)
	except Exception as err:
		print("dropevent problem : ", err)

def addFilter(player=None):
	''' add lpf or hpf to player '''
	try:
		if player == None:
			player = choice(Clock.playing)
		filType, filFreq = gen_filter()
		if filFreq != '0':
			sendOut(f'{player}.{filType}={filFreq}')
		player.__setattr__(filType, eval(filFreq))
	except Exception as err:
		print("addFilter problem : ", err)

def addKick():
	''' Add 4 to the floor Kick player '''
	try:

		player = generate_player_name()
		kick = choice(sorted_sample["kick_sample"]) + "."
		sple = randint(0,99)
		lpf = randint(40,5000)
		if randint(0,100) > probAddDrummer:
			sendOut(f'{eval(player)} >> play({kick}, dur=1/2, sample={sple}, lpf={lpf})')
			~eval(player) >> play(kick, dur=1/2, sample=sple, lpf=lpf, amp=randint(1,3)).sometimes("stutter")
		else:
			lpf = randint(2400,14000)
			sendOut(f'{eval(player)} >> play({kick}, dur=1/2, sample={sple}, lpf={lpf}).drummer()')
			~eval(player) >> play(kick, dur=1/2, sample=sple, lpf=lpf, amp=randint(1,3)).drummer().sometimes("stutter")
		addPlayerTurn()
	except Exception as err:
		print("addKick problem : ", err)

def generate_rytm(length=16, mult=1):
	try:
		rytm = PChain2(rythmMarkov)[:length]*mult
		for i,n in enumerate(rytm):
			if n == 0:
				rytm[i] = f'rest({0.5*mult})'
		return str(rytm).replace("'","")
	except Exception as err:
		print("generate_rytm problem : ", err)

def addAccompany():
	try:
		synthPlayer = [p for p in Clock.playing if p.synthdef not in ["loop", "play1", "play2"]]
		if len(synthPlayer) > 2:
			choosenPlayer = sample(synthPlayer,2)
			choosenPlayer[0].accompany(choosenPlayer[1])    
			sendOut(f'{choosenPlayer[0]}.accompany{choosenPlayer[1]}')
	except:
		print("addAccompany problem : ", err)

def addFxOut():
	''' add fxOut to player '''
	try:
		player = choice(Clock.playing)
		fxout = choice(["fx1", "fx2"])
		sendOut(f'{player}.{fxout}=1')
		player.__setattr__(fxout, 0.3)
	except Exception as err:
		print("addFxOut problem : ", err)

def shutup():
	''' stop all server's players, preserve numeric end players (d1, s3, e8)'''
	print("Shut the fuck up you evil server")
	stopPlayer = [p for p in Clock.playing if p.name[-1:] in string.ascii_lowercase]
	for ply in stopPlayer:
		sendOut(f"{ply}.stop()")
		ply.stop()

def son(s=999, d=999, l=999):
	''' activate the server, probability (Synth, drums, Loops) '''
	print("Server On")
	global serverActive, probAddSynth, probAddDrum, probAddLoop
	if s!=999:	
		probAddSynth = s
		probAddDrum = d
		probAddLoop = l
	server.start()
	serverActive = True

def soff():
	print("Server Off")
	global serverActive
	serverActive = False

def activateServer():
	Clock.bpm=92
	eval('se >> loop("serverVoice", dur=16, beat_stretch=0, looping=0, mverb=0.1, amp=0.5).unison(3).only()')
	Server.freeAllNodes()
	Clock.future(32, lambda: son())

### start the server
server.start()

##### GARBAGE FOR ARCH ######

# def changeConf():
# 	cfg = configparser.RawConfigParser()
# 	cfg.optionxform = str
# 	pth = os.path.join(FOXDOT_ROOT, "lib", "Crashserver","crash_generator","server_conf0.cfg")
# 	cfg.read(pth)
# 	par=dict(cfg.items("Settings"))
# 	for p in par:
# 		par[p]=par[p].split("#",1)[0].strip() # To get rid of inline comments
# 	globals().update(par)  #globally

# def state(msg=1):
# 	''' Send osc message for server status '''
# 	global serverActive
# 	if msg == 0:
# 		serverActive = True
# 	else:
# 		serverActive = False
# 	try:
# 		byte_message = bytes("_" + str(msg), "utf-8")
# 		crashFoxDot_socket.sendto(byte_message, (crashOSIp, crashOSPort))
# 	except:
# 		pass

# def video(msg=""):
#   ''' Send osc message for video '''
#   try:
#       oscMsg = OSCMessage("/video")
#       oscMsg.append(msg)
#       myclient.send(oscMsg)
#   except:
#       pass
