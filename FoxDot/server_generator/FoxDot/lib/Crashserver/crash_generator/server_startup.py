#coding: utf8
#!/usr/bin/env python3
##############################################################################################
#####              CRASH GENERATOR        #############
#########################################
from random import randint, random, sample, choices, seed
from time import gmtime, strftime
import threading

class genSeed():
	''' return a seed for random based on actual time for multiplayer sync '''
	def __init__(self):
		self.seedR = int(''.join(map(str, map(ord, strftime("%a, %d %b %Y %H:%M", gmtime())))))
	def txt(self, seedTxt):
		self.seedR = int(sum([ord(c) for c in str(seedTxt)]))
	def add(self):
		self.seedR += 1
	def set(self):
		seed(int(self.seedR))

try:
	genSeed = genSeed()
	genSeed.set()
except Exception as e:
	print("Failed to init random seed", e)

try:
	from .Crashserver.crash_generator.weapons import *
	from .Crashserver.crash_generator.composition import *
	from .Crashserver.crash_generator.server_conf import *
except Exception as e:
	print("Error in generating weapons code", e)

serverActive = False
# osc receive state
if oscOut:
	# Osc sender
	try:
		crashFoxDot_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	
	except:
		print("config UDP problem")

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
			print(e)
		if self.loop:
			try:
				if serverActive:
					server_order()
				duration = self.time*randint(multDurationMin,multDurationMax)
				Clock.future(duration, lambda: self.start())
			except Exception as e:
				print(e)

server = runServer()
playerCount = {}

def server_order():
	''' Server routine, choose [add/stop player, change param, add fx, add function,...'''
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
						add_event],
						[probAddPlayer,probStopPlayer,probAddFx,probChangeDegree,probAddPlayerParam,probAddPlayerAttribute,probAddEvent]) # probability
	order[0]()  # evaluate order
	addPlayerTurn()  # add 1 turn to each playing players

def add_player(copyText=False, playerType=None):
	''' add a random synth, drum, loop player  '''
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

def stop_player():
	''' choose randomly playing players and stop them'''
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

def add_fx():
	''' add fx parameters '''
	player = choice(Clock.playing)
	fx = GENERATE_FX(fxdict)
	for name, argm in fx.items():
		sendOut(f'{player}.{name}={argm}')
		player.__setattr__(name, eval(argm))

def run_player_synth(copyText=False, **kwargs):
	''' Play synth player'''
	player = kwargs.get("player")
	synth = kwargs.get("synth")
	degree = kwargs.get("degree")
	dur = kwargs.get("dur")
	oct = kwargs.get("oct")
	degree = eval(degree)
	if max(degree) > 10:
		degree = remap_pattern(degree, 0,7)
	try:
		if not copyText:
			sendOut(f'{player} >> {synth}({degree}, dur={dur}, oct={oct})')
			~eval(player) >> eval(synth)(eval(str(degree)), dur=eval(dur), oct=eval(oct))
			addFilter(eval(player))
		else:
			return f'{player} >> {synth}({degree}, dur={dur}, oct={oct})'
	except Exception as e:
		print(e)

def run_player_drum(copyText=False, **kwargs):
	''' Play drum player'''
	player = kwargs.get("player")
	synth = kwargs.get("synth")
	degree = kwargs.get("degree")
	dur = kwargs.get("dur")
	sample = kwargs.get("sample")
	rate = kwargs.get("rate")
	try:
		if not copyText:
			sendOut(f'{player} >> {synth}("{degree}", dur={dur}, sample={sample}, rate={rate})')
			~eval(player) >> eval(synth)(degree, dur=eval(dur), sample=eval(sample), rate=eval(rate))
			addFilter(eval(player))
		else:
			return f'{player} >> {synth}("{degree}", dur={dur}, sample={sample}, rate={rate})'
	except Exception as e:
		print(e)

def run_player_loop(copyText=False, **kwargs):
	''' Play loop player'''
	player = kwargs.get("player")
	synth = kwargs.get("synth")
	degree = kwargs.get("degree")
	dur = kwargs.get("dur")
	sample = kwargs.get("sample")
	try:
		if not copyText:
			sendOut(f'{player} >> {synth}("{degree}", dur={dur}, sample={sample})')
			~eval(player) >> eval(synth)(degree, dur=eval(dur), sample=eval(sample))
			addFilter(eval(player))
		else:
			return f'{player} >> {synth}("{degree}", dur={dur}, sample={sample})'
	except Exception as e:
		print(e)

def addPlayerTurn():
	''' add one to player dictionnary turn '''
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

def add_player_param():
	''' add player parameters (like .spread, .offbeat, .jump, ...) '''
	player = choice(Clock.playing)
	param = gen_player_param()
	sendOut(f'{player}.{param}')
	eval(f'{player.name}.{param}')

def add_player_attribute():
	''' add or change player attribute (sus, pan, ) '''
	player = choice(Clock.playing)
	attr = gen_player_attributes(player_type(player))
	sendOut(f'{player}.{attr[0]}={attr[1]}')
	player.__setattr__(attr[0], eval(str(attr[1])))

def change_degree(player=None):
	''' According to player type change degree(synth), char(drum), sample(loop)'''
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

def add_event():
	rnd_event = choices([change_scale, change_root, humanizer, change_bpm, masterFilter, dropevent, addKick, addFxOut],
						[probChangeScale, probChangeRoot, probChangeHumanizer, probChangeBpm, probAddLpf, probAddDrop, probAddKick,probAddFxOut])[0]
	rnd_event()

def sendOut(msg=""):
	''' send all generated text to output : console, osc '''
	if oscOut:
		sendOsc(msg)
	if printOut:
		if startupLive:
			msg = 'SERVER: ' + msg
		print(msg)

def sendOsc(msg=""):
	''' Send osc text to osc ip '''
	try:
		byte_message = bytes("@" + msg, "utf-8")
		crashFoxDot_socket.sendto(byte_message, (oscIp, oscPort))
	except:
		pass

# def video(msg=""):
# 	''' Send osc message for video '''
# 	try:
# 		oscMsg = OSCMessage("/video")
# 		oscMsg.append(msg)
# 		myclient.send(oscMsg)
# 	except:
# 		pass

def state(msg=1):
	''' Send osc message for server status '''
	global serverActive
	if msg == 0:
		serverActive = True
	else:
		serverActive = False
	try:
		byte_message = bytes("_" + str(msg), "utf-8")
		crashFoxDot_socket.sendto(byte_message, (oscIp, oscPort))
	except:
		pass

def player_type(player):
	''' return player type '''
	if player.synthdef in ["loop"]:
		return "loop"
	elif player.synthdef in ["play", "play2"]:
		return "drum"
	else:
		return "synth"

def change_bpm():
	''' Change randomly and lineary the bpm'''
	bpmNow = int(Clock.bpm)
	bpmTarget = randint(changeBpmMin,changeBpmMax)
	randTime = randint(changeBpmTimeMin,changeBpmTimeMax)
	sendOut(f'Clock.bpm = lininf({bpmNow}, {bpmTarget},{randTime})')
	Clock.bpm = lininf(bpmNow, bpmTarget,randTime)

def change_scale():
	''' set a random scale '''
	scale_name = "freq"
	while scale_name == "freq":
		scale_name = choice(Scale.names())
	Scale.__setattr__("default", Scale.get_scale(scale_name))
	sendOut(f'Scale.default={scale_name}')

def change_root():
	''' up or down root '''
	updown = 0
	while updown == 0:
		updown = randint(changeRootMin,changeRootMax)
	if int(Root.default) > 5:
		updown = -1
	elif int(Root.default) < -4:
		updown = 1
	sendOut(f'Root.default+={updown}')
	Root.default=Root.default + updown

def humanizer(player=None):
	''' humanize a drum pattern '''
	if player == None:
		player = choice(Clock.playing)
	hum = [int(GENERATE_INTEGER(humanAmpMin,humanAmpMax)), int(GENERATE_INTEGER(humanDelayMin,humanDelayMax)), int(GENERATE_INTEGER(humanSwingMin,humanSwingMax))]
	sendOut(f'{player}.humanize({hum[0]}, {hum[1]}, {hum[2]})')
	player.human(hum[0], hum[1], hum[2])

def masterFilter():
	''' Add random Master().lpf, Master().bpf, Master().hpf '''
	timef = 4*round(randint(3,32)/4)
	filtr = choice(["lpf", "hpf", "bpf"])
	set_master_filter(filtr, freqs[filtr], timef)
	sendOut(f'Master().{filtr}=linvar({freqs[filtr]},[{timef-1},1])')
	Clock.future(timef, lambda: set_master_filter(filtr, 0, 0))

def set_master_filter(filtr, freqf, timef):
	''' set the master filter, use with clock.future '''
	if timef == 0:
		Master().__setattr__(filtr, 0)
	else:
		Master().__setattr__(filtr, linvar(freqf, [timef-1, 1], start=now))

def dropevent():
	''' Add random drop() '''
	time = randint(dropTimeMin,dropTimeMax)
	drop(time, dropTimeMax-time,dropLoop)

def addFilter(player=None):
	''' add lpf or hpf to player '''
	if player == None:
		player = choice(Clock.playing)
	filType, filFreq = gen_filter()
	#if filFreq != '0':
		#sendOut(f'{player}.{filType}={filFreq}')
	player.__setattr__(filType, eval(filFreq))

def addKick():
	''' Add 4 to the floor Kick player '''
	player = generate_player_name()
	kick = choice(sorted_sample["kick_sample"])	+ "."
	sple = randint(0,99)
	lpf = randint(40,7000)
	sendOut(f'{eval(player)} >> play({kick}, dur=1/2, sample={sple}, lpf={lpf})')
	~eval(player) >> play(kick, dur=1/2, sample=sple, lpf=lpf, amp=randint(1,3)).sometimes("stutter")
	addPlayerTurn()

def generate_rytm(length=16, mult=1):
	rytm = PChain2(rythmMarkov)[:length]*mult
	for i,n in enumerate(rytm):
		if n == 0:
			rytm[i] = f'rest({0.5*mult})'
	return str(rytm).replace("'","")

def addFxOut():
	''' add fxOut to player '''
	player = choice(Clock.playing)
	fxout = choice(["fx1", "fx2"])
	sendOut(f'{player}.{fxout}=1')
	player.__setattr__(fxout, 1)

def killserver():
	''' stop all server's players, preserve numeric end players (d1, s3, e8)'''
	stopPlayer = [p for p in Clock.playing if p.name[-1:] in string.ascii_lowercase]
	for ply in stopPlayer:
		sendOut(f"{ply}.stop()")
		ply.stop()

server.start()