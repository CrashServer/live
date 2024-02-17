try:
	import pickle
	import os
	import sys
	from time import *
	import re
	from random import choice
	from threading import Thread
	from pathlib import Path
	import socket
except Exception as e:
	print(e)

#### ASCII
asciiEnable = False
clipcopyEnable = False
try:
	from pyfiglet import figlet_format, FigletFont # ASCII GENERATOR
	cool_ascii = [1,6,8,11,13,15,17,18,19,21,22,24,26,30,31,32,33,34,35,37,38,43,44,45,46,47,48,50,59,62,64,65,68,69,77,79,81,82,83,84,85,88,89,96,98,103,104,105,107,111,113,114,117,119,123,124,131,135,143,150,151,152,159,187,190,193,19,201,203,217,225,227,230,240,243,244,245,251,273,275,280,308,325,329,347,363,385,410]
	fig_font = FigletFont()
	fig_fonts_list = fig_font.getFonts()
	fig_skip = ['fbr12___', 'mshebrew210', 'term', 'runic', 'pyramid', 'eftifont', 'DANC4', 'dietcola']
	fig_skip += ['emboss', 'emboss2', 'future', 'letter', 'pagga', 'smblock', 'smbraille', 'wideterm']
	fig_skip += ['dosrebel', 'konto', 'kontoslant']
	font_list = [x for x in fig_fonts_list if x not in fig_skip]
	asciiEnable = True
except:
	asciiEnable = False
	print("Please install pyfiglet")

#### copy to clipboard
try:
	import pyperclip as clip
	clipcopyEnable = True
except:
	clipcopyEnable = False
	print("Please install pyperclip")

#########################
### SERVER CONFIG     ###
#########################

class StorageAttack:
	''' get attack from files and put in a dict, print / clipboardcopy'''
	def __init__(self):
		self.codepath = os.path.join(Path('.').absolute().parent, 'codeBank')
		self.attackDict = {}
		self.compileAttack()
	def compileAttack(self):
		for filename in os.listdir(self.codepath):
			if filename.endswith(('.py')):
				with open(os.path.join(self.codepath, filename)) as f:
					content = f.readlines()
					attackName = content[0].replace("#", "").replace("\n", "").strip()
					self.attackDict[attackName] = ''.join(content[1:])
	def getAttack(self, attackName, printOut=0):
		exten = ''.join(choice(string.ascii_lowercase) for x in range(3))
		prompt = f"##### attack@{attackName}.{exten}:~$ #####"
		if isinstance(attackName, int):
			attackName = list(self.attackDict.keys())[attackName]
			print(attackName)
		if printOut != 0:
			print(prompt)
			print(self.attackDict[attackName])
		if clipcopyEnable:
			clip.copy(prompt + '\n' + self.attackDict[attackName])
	def lost(self):
		attackKeys = list(sorted(self.attackDict.keys()))
		print(attackKeys)
		if crashPanelSending:
			crashpanel.sendOnce(str(attackKeys))

storageAttack = StorageAttack()

### sample description ###
sample_description_path = os.path.join(crash_path, "description.cs")
if os.path.isfile(sample_description_path):
	with open(sample_description_path, "rb") as file:
		sample_description = pickle.load(file)

def ascii_gen(text="", font=""):
	''' Generate ASCII art from text '''
	if clipcopyEnable and asciiEnable:
		if font == "":
			font = randint(0,len(cool_ascii))
		if type(font) != str:
			font = fig_fonts_list[cool_ascii[int(font)]]
		if text != None:
			clip.copy(figlet_format(text, font=font))
	else:
		print("No pyperclip or ascii pyfiglet")

##########################################
###     CRASH SERVER LIVE FUNCTIONS    ###
##########################################

def voiceserver(voice_txt=""):
    masterAll("lpf", 80)
    Voice(voice_txt, rate=1, amp=1, pitch=1 + randint(-10,50), lang="fr", voice=0)
    Clock.future(calc_dur_voice(voice_txt), lambda: masterAll("reset"))

def connect():
	''' Full reset and set bpm, root, sos & video player '''
	Master().reset()
	Clock.set_time(0)
	storageAttack.lost()
	Clock.bpm = 48
	Scale.default = "minor"
	Root.default = "E"
	i3 >> sos(dur=8, lpf=linvar([60,4800],[16*PWhite(1,4), 16*PWhite(1,5)]), hpf=expvar([0,500],[16*PWhite(1,8), 16*PWhite(1,8)]), amplify=0.5)
	if clipcopyEnable:
		clip.copy("i3 >> sos(dur=8, lpf=linvar([60,4800],[16*PWhite(1,4), 16*PWhite(1,5)]), hpf=expvar([0,500],[16*PWhite(1,8), 16*PWhite(1,8)]), amplify=0.5)")

def attack(attackName, prntOut=0):
	storageAttack.getAttack(attackName, prntOut)

def lost():
	storageAttack.lost()

def print_synth(synth=""):
	''' Show the name and the args of a synth '''
	path = os.path.join(FOXDOT_ROOT, "osc", "scsyndef", "")
	if synth == "":
		dir_list = os.listdir(path)
		synth_list = []
		for p in dir_list:
			files,sep,ext = p.partition('.')
			synth_list.append(files)
		print(sorted(synth_list))
		if crashPanelSending:
			crashpanel.sendOnce(str(sorted(synth_list)))
	else:
		path = os.path.join(FOXDOT_ROOT, "osc", "scsyndef", synth + ".scd")
		with open(str(path), "r") as synth:
			synth = synth.readlines()
		synth_txt = [line.strip() for line in synth if line != "\n"]
		txt = str(''.join(synth_txt))
		synthname = re.findall('SynthDef[.new]*[(\\\]*(.+?),',txt)
		synthargs = re.findall('\{\|(.*)\|', txt)
		print(str(synthname[0]), " : ", str(synthargs[0]))
		if crashPanelSending:
			crashpanel.sendOnce(str(synthname[0]) + " : " + str(synthargs[0]))

def print_fx(fx=""):
	''' Show the name and the args of a fx '''
	if fx == "":
		print(sorted(FxList.keys()))
		if crashPanelSending:
			crashpanel.sendOnce(str(sorted(FxList.keys())))
	else:
		print(FxList[fx])
		if crashPanelSending:
			crashpanel.sendOnce(str(FxList[fx]))

def print_sample(sample=""):
	''' print description of samples or find the corresponding letter '''
	if sample=="":
		print("")
		for k, v in sorted(sample_description.items(), key= lambda x: x[0].casefold()):
			print(k.ljust(2, " ") + ': ' + v.ljust(40), end="")
		print("")
	else:
		if len(sample) == 1:
			if sample.lower() in alpha or sample.upper() in alpha or sample in nonalpha:
				print(f'{sample}: {sample_description[sample]}')
		else:
			for key, value in sample_description.items():
				if sample.lower() in value.lower():
					print(f'{key}: {value}')

def print_loops(loop=""):
	''' print all available loops samples '''
	if isinstance(loop, int):
		randomLoops = sample(loops, loop)
		print(randomLoops)
		if crashPanelSending:
			crashpanel.sendOnce(str(randomLoops))
	elif loop=="":
		print(loops)
		if crashPanelSending:
			crashpanel.sendOnce(str(loops))
	elif (loop in loops):
		listloops = sorted([fn.rsplit(".",1)[0] for fn in os.listdir(os.path.join(FOXDOT_LOOP, loop))])
		print(listloops)
		if crashPanelSending:
			crashpanel.sendOnce(str(listloops))
	else:
		filteredList = [s for s in loops if loop in s]
		print(filteredList)
		if crashPanelSending:
			crashpanel.sendOnce(str(filteredList))

def print_video():
	'''Helper for video player'''
	txt = "v1 >> video(pos1=0.3, pos2=0.5, vid1=3, vid2=4, blend1=0.7, blend2=0.3, scene=4, blendtype=3) \n pos* = scrub video* \n vid* = index of video* \n blend* = opacity of video* \n scene = index of scene \n blendtype = choose blend type between vid1 et vid2"
	print(txt)
	clip.copy("v1 >> video(pos1=0.0, pos2=0.0, vid1=0, vid2=0, blend1=0.5, blend2=0.5, scene=1, blendtype=0)")
	if crashPanelSending:
		crashpanel.sendOnce(str(txt))

def PMorse(text, point=1/4, tiret=3/4):
	""" Convert a string to the value of point & tiret """
	MORSE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}
	morse = []
	for l in text.split(" "):
		for w in l:
			for i in MORSE_DICT[w.upper()]:
				if i == ".":
					morse.append(point)
				elif i == "-":
					morse.append(tiret)
			morse.append(rest(5*point))
	morse[-1] += rest(2*point)
	return morse

def unsolo():
	for p in Clock.playing:
		p.solo(0)

# virus_method = ["Injecting... ", "Loading... ", "Init: ", "Dumping: ", "Hacking: ", "Run.."]
# virus_name = ["MyDoom", "Brain", "Zeus", "Sality", "Virut", "Ramnit", "Blaster", "Conficker",\
# "Worm", "TDSS TDL 4"]
# virus_access = ["Kernel", "MBR", "Kernel", "bsdriver.sys", "Hardware", "Security", ]
# virus_protocole = ["Spambot", "PWS", "Stealer", "Proxy", "BackDoor", "KeyLogger", "InfoStealer", "Cryto",\
# "Autoruns", "Rootkit", "Trojan", "Rogue", "Scareware", "Script", "D.O.S." ]
# virus_status = [" | [###.......] % Completed | ###",  "- Lost: 78% - ###", " @@88@@", " /Please Wait...", " |***--------| ", " , ping=3ms", "!WARNING BUFFER(#4F,5E) - VIOLATION ACCESS"]

# def define_virus():
# 	### Generate a random virus text
# 	virus = "###" + choice(virus_method) + choice(virus_name) + "." + choice(virus_access) + "." + choice(virus_protocole) + choice(virus_status)
# 	return virus

@player_method
def gtr(self, strings=1):
	''' set player to match guitar string'''
	self.root = Pattern(strings).submap({0:-10, 1:-8, 2:-3, 3:2, 4:7, 5:11, 6:16})
	self.scale = Scale.chromatic
	return self

@player_method
def chroma(self):
	''' Set player to chromatic scale '''
	self.scale = Scale.chromatic

@player_method
def porta(self, portDelay=0.5):
	if portDelay != 0:
		actualDegree = self.attr["degree"][self.event_n]
		nextDegree = self.attr["degree"][self.event_n+1]
		self.slide = (nextDegree - actualDegree)/12
		self.slidedelay = portDelay
	else:
		self.slide = 0

@player_method
def morph(self, other, prob=50):
	''' morph randomly some attrinute between 2 players, prob = amount of probability (100: full target player)'''
	for k in self.attr.keys():
		try:
			if k in other.attr.keys():
				try:  ### pattern comparaison is buggy, need this hack
					if other[k] != P[0]:
						test = True
					else:
						test = False
				except:
					test = True
				if test:
					sattr = self.__getitem__(k)
					oattr = other.__getitem__(k)
					item = [p if randint(0,100)>prob else oattr[i] for i,p in enumerate(sattr)]
					setattr(self, k, item)
		except Exception as e:
			print(e)
	return self

@player_method
def trim(self, length):
	'''Trim to length evey pattern of player'''
	if length !=0:
		if length >= 1:
			for attr in self.attr:
				try:
					self.attr[attr] = self.attr[attr].trim(length)
				except AttributeError:
					pass
		else:
			for attr in self.attr:
				try:
					self.attr[attr] = self.attr[attr].trim(1)
				except AttributeError:
					pass
			self.attr["dur"] = self.attr["dur"] * length
		return self
	# else:
	# 	self.dur = 0.5 if self.synthdef == SamplePlayer else 1

def genArp(nbrseq=4, lengthseq=8):
	''' Generate arpeggiato based on markov Chords progression '''
	seq = PMarkov()[:nbrseq]
	arp = PRand(P[0:18] | P[20:24] | P[30] | P[40:45] | P[50:55])[:nbrseq]
	genseq = [PArp(seq[i], arp[i]) for i in range(nbrseq)]
	return Pvar(genseq, lengthseq)

valueDict = {}

def masterAll(args = 0, value=1, *argsall):
	global valueDict
	if args == "reset" or args == 0:
		for k,v in valueDict.items():
			for l, w in v.items():
				try:
					k.__setattr__(l, w)
				except:
					pass
		valueDict = {}
	elif isinstance(args, str):
		for p in Clock.playing:
			if p in valueDict:
				if args in valueDict[p]:
					pass
				else:
					try:
						valueDict[p][args] = p.__getitem__(args)
					except:
						valueDict[p][args] = 0
			else:
				valueDict[p] = {}
				try:
					valueDict[p][args] = p.__getitem__(args)
				except:
					valueDict[p][args] = 0
			p.__setattr__(args, value)
	else:
		pass

### CrashPanel

try:
	if crashPanelSending:
		class PlatduJour():
			def __init__(self):
				self.choicePlat = [self.pat_du_jour, self.synth_du_jour, self.loop_du_jour, self.nombre_du_jour,
									self.fx_du_jour, self.para_du_jour, self.pattern_du_jour, self.gen_dict_words,
									self.scale_du_jour, self.fonction_du_jour]

			def pat_du_jour(self):
				return ("Pattern", [name for name, obj in vars(Sequences).items() if (type(obj) == FunctionType and name.startswith("P"))])

			def synth_du_jour(self):
				return ("Synth",[i for i in SynthDefs])

			def loop_du_jour(self):
				return ("Loop", loopNames)

			def nombre_du_jour(self):
				return ("Nombre", [GENERATE_AMPLIFY(), GENERATE_LIST(), GENERATE_FLOAT_LIST(), GENERATE_TUPLE(),
						GENERATE_NUMBER(), GENERATE_RDM(), GENERATE_VARLIST(), GENERATE_FREQLIST()])

			def fx_du_jour(self):
				randfx = GENERATE_FX()
				txt = []
				for k,v in randfx.items():
					txt.append(f"{k}={v}")
				return ("FX", [txt])

			def para_du_jour(self):
				para = GENERATE_PARA()
				return ("Parametre", [f"{para}"])

			def pattern_du_jour(self):
				pat = GENERATE_PATTERN()
				return ("Pattern", [f"{pat}\n\n{eval(pat)}"])

			def gen_dict_words(self):
				try:
					aa33listimpp = '''
					datetime sys pprint os time
					codecs random glob warnings
					token pipes re'''.split()
					pass
					vg33modules   = map(__import__, aa33listimpp)
					sg33doctext   = " ".join([vxx.__doc__ for vxx in vg33modules])
					pass
					rgx33word4min = r'[a-zA-Z0-9]{4,}'  ## regex to find words of 4chars or more
					aa33listword  = [str(vxx).lower() for vxx in re.findall(rgx33word4min,sg33doctext) ]
					aa33listword  = set(aa33listword)
					aa33listword  = sorted(aa33listword)
					pass
					return ("Mot", aa33listword)
				except:
					return ("Mot", ["composite", "occidental", "demembrer", "chimique", "fissure", "serpent", "perturbation",
							"berserker", "plaid", "donut", "jaillissement", "citron vert", "rouille", "barbouillage", "hiver",
							"assurance", "nerveux", "aversion", "mixeur", "innocent", "canard", "objet", "rage", "anonyme", "perturber", "meurtre", "sagesse",
							"encore", "secteur", "horrible", "puissant"])

			def scale_du_jour(self):
				return ("Scale", Scale.names())

			def fonction_du_jour(self):
				fct = ["PMorse(text, point=1/4, tiret=3/4)", ".gtr(string=1)", "random_bpm_var()", ".unison(unison=2, detune=0.125, analog=0)",
						 ".human(velocity=20, humanize=5, swing=0)", ".fill(mute_player=0, on=1)", "brk(multi=1, code='')",
						 ".renv(nbr=1)", "PBin(number)", "PTime()", "PTimebin()", "lininf(start=0, finish=1, time=32)", "expinf(start=0, finish=1, time=32)",
						 "PDrum(style=None, pat='', listen=False, khsor='', duree=1/2, spl = 0, charPlayer='d')", "darker()", "lighter()", "PChords(chords)",
						 "PGauss(mean, deviation)", "PLog(mean, deviation)", "PTrir(low,high,mode)", "PCoin(low, high, proba)", "PChar(case=2, alpha=2)",
						 "PMarkov(init_value='')", "switch(other, key, bypass=1)", "clone(player)", "add(value)", "mul(value)", "drop(playTime=6, dropTime=2, nbloop=1)",
						 "drop_bpm(duree=32, nbr=0, end=4)", "melody()", "PArp(seq, index=0)", "SDur(target)"]
				return ("Fonction", fct)

			def choix(self):
				choix = choice(self.choicePlat)
				mot, chx = choix()
				return (mot, choice(chx))


		class CrashPanel():
			def __init__(self, ipZbdm="localhost", ipSvdk = None, port=2000):
				self.ipZbdm = ipZbdm
				self.ipSvdk = ipSvdk
				self.port = port

				self.bpmTime = 0.2  # time cycle send bpm
				self.beatTime = 0.1 # time cycle send beat
				self.plyTime = 1.0 # time cycle send player
				self.pdjTime = 60 #time cycle send PlatduJour
				self.chronoTime = 1.0 # time cycle send chrono
				self.videoTime = 1.0 # time cycle send video index

				self.playerCounter = {}

				if self.ipZbdm:
					self.clientZbdm = OSCClient()
					self.clientZbdm.connect((self.ipZbdm, 2000))
				if self.ipSvdk:
					self.clientSvdk = OSCClient()
					self.clientSvdk.connect((self.ipSvdk, 2000))

				self.pdj = PlatduJour()
				self.timeInit = time()

				self.threadBpm = Thread(target = self.sendBpm)
				self.threadBpm.daemon = True
				self.threadScale = Thread(target = self.sendScale)
				self.threadScale.daemon = True
				self.threadRoot = Thread(target = self.sendRoot)
				self.threadRoot.daemon = True
				self.threadBeat = Thread(target = self.sendBeat)
				self.threadBpm.daemon = True
				self.threadPlayer = Thread(target = self.sendPlayer)
				self.threadPlayer.daemon = True
				self.threadPdj = Thread(target = self.sendPdj)
				self.threadPdj.daemon = True
				self.threadChrono = Thread(target = self.sendChrono)
				self.threadChrono.daemon = True
				self.threadVideoIndex = Thread(target = self.sendVideoIndex)
				self.threadVideoIndex.daemon = True


			def sendOscMsg(self, msg):
				if self.ipZbdm:
					try:
						self.clientZbdm.send(msg)
					except:
						pass
				if self.ipSvdk:
					try:
						self.clientSvdk.send(msg)
					except:
						pass

			def sendBpm(self):
				''' send Clock.bpm to OSC server '''
				try:
					while self.isrunning:
						msg = OSCMessage("/panel/bpm", [int(Clock.get_bpm())])
						self.sendOscMsg(msg)
						sleep(self.bpmTime)
				except:
					pass

			def sendScale(self):
				''' send Scale to OSC server '''
				try:
					while self.isrunning:
						msg = OSCMessage("/panel/scale", [str(Scale.default.name)])
						self.sendOscMsg(msg)
						sleep(self.bpmTime*10)
				except:
					pass

			def sendRoot(self):
				''' send Root to OSC server '''
				try:
					while self.isrunning:
						msg = OSCMessage("/panel/root", [str(Root.default)])
						self.sendOscMsg(msg)
						sleep(self.bpmTime*10)
				except:
					pass

			def sendBeat(self):
				''' send Clock.beat to OSC server '''
				try:
					while self.isrunning:
						msg = OSCMessage("/panel/beat", [Clock.beat])
						self.sendOscMsg(msg)
						sleep(self.beatTime)
				except:
					pass

			def sendPlayer(self):
				''' send active player to OSC server '''
				try:
					while self.isrunning:
						self.addPlayerTurn()
						playerListCount = [f'{k} {divmod(v,60)[0]:02d}:{divmod(v,60)[1]:02d}' for k,v in self.playerCounter.items()]
						msg = OSCMessage("/panel/player", [playerListCount])
						self.sendOscMsg(msg)
						sleep(self.plyTime)
				except:
					pass

			def sendPdj(self):
				''' send platdujour to OSC server '''
				try:
					while self.isrunning:
						intitule, plat = self.pdj.choix()
						msg = OSCMessage("/panel/pdj", [intitule, plat])
						self.sendOscMsg(msg)
						sleep(self.pdjTime)
				except:
					pass

			def sendChrono(self):
				''' send ChronoTime to OSC server '''
				try:
					while self.isrunning:
						elapsedTime = time() - self.timeInit
						msg = OSCMessage("/panel/chrono", [elapsedTime])
						self.sendOscMsg(msg)
						sleep(self.chronoTime)
				except:
					pass

			def addPlayerTurn(self):
				''' add one to player dictionnary turn '''
				try:
					playerList = Clock.playing
					for p in playerList:
						if p in self.playerCounter.keys():
							self.playerCounter[p] += 1
						else:
							self.playerCounter[p] = 1
					# Clean non playing player
					delplayer = [k for k in self.playerCounter.keys() if k not in playerList]
					for d in delplayer:
						self.playerCounter.pop(d, None)
				except Exception as err:
					print("addPlayerTurn problem : ", err)

			def sendVideoIndex(self):
				try:
					while self.isrunning:
						msg = OSCMessage("/panel/video", [oscReceiver.videoGrp, oscReceiver.videoIndex, oscReceiver.videoTotal, oscReceiver.videoIntegrity])
						self.sendOscMsg(msg)
						sleep(self.videoTime)
				except:
					pass

			def sendOnce(self, txt):
				''' send on txt msg to OSC '''
				msg = OSCMessage("/panel/help", [txt])
				self.sendOscMsg(msg)

			def stop(self):
				self.isrunning = False

			def start(self):
				self.isrunning = True
				self.threadBpm.start()
				self.threadScale.start()
				self.threadRoot.start()
				self.threadBeat.start()
				self.threadPlayer.start()
				self.threadPdj.start()
				self.threadChrono.start()
				self.threadVideoIndex.start()

		def panelreset():
			crashpanel = CrashPanel(ipZbdm, ipSvdk, 2000)
			crashpanel.start()

		def chrono():
			crashpanel.timeInit = time()

		crashpanel = CrashPanel(ipZbdm, ipSvdk, 2000)
		crashpanel.start()
except Exception as e:
	print(e)

### French cut
try:
	if os.name != "nt":
		é = linvar([0,1],[16,0])
		é4 = linvar([0,1], [4,0])
		é8 = linvar([0,1],[8,0])
		é32 = linvar([0,1],[32,0])
		è = linvar([1,0],[16,0])
		è4 = linvar([1,0],[4,0])
		è8 = linvar([1,0],[8,0])
		è32 = linvar([1,0],[32,0])
		ê = linvar([0,1],[16,16])
		ê4 = linvar([0,1],[4,4])
		ê8 = linvar([0,1],[8,8])
		ê32 = linvar([0,1],[32,32])
		ù = PDur(var([4,PRand(8)],[6,2]), 8)
		ù3 = PDur(var([3,PRand(8)],[6,2]), 8)
		ù5 = PDur(var([5,PRand(8)],[6,2]), 8)
		à = PRand(10)
		ç = PWhite(-1,1)
		ç0 = PWhite(0,1)
	# ô = PGauss(0, 1)

	### scene OF
	scene0 = 0
	scene1 = 0
	scene2 = 0
	scene3 = 0
	scene4 = 0
	scene5 = 0
	scene6 = 0
	scene7 = 0
	scene8 = 0
	scene9 = 0
	scene10 = 0
	scene11 = 0
	scene12 = 0
	scene13 = 0
	scene14 = 0
	scene99 = 0

	# define chords and circle of fifth
	circ5 = (P[0:12]*7)%12
	circ5m = circ5.rotate(3)
	Maj = P(0,4,7)
	Min = P(0,3,7)
	Sus2 = P(0,2,7)
	Sus4 = P(0,5,7)
	Dim = P(0,3,6)
	Maj7 = P(0,4,7,11)
	Aug = P(0,4,8)
	Six = P(0,4,7,9)

except Exception as e:
	print(e)


# dwarfDict = {
#     "chorus": {
#         "phase": 10,
#         "depth": 11,
#         "delay": 12,
#         "contour": 13,
#         "wet": 14,
#         "freq": 15},
#     "whammy": {
#         "first": 16,
#         "last": 17,
#         "gain": 18,
#         "clean": 19
#         },
#     "drive": {
#         "attack": 20,
#         "bright": 21,
#         "gate": 22,
#         "level": 23
#         },
#     "master": {
#         "bass": 24,
#         "treble": 25,
#         },
#     "shimmer": {
#         "predelay": 27,
#         "early": 28,
#         "shimmer": 29
#         }
#     }
#
# def dwarf(fx="", param="", value="", duree=1):
#     def findName():
#         playerList = [f'm{p}' for p in list(string.ascii_lowercase)]
#         playerFiltred = [ply for ply in playerList if ply not in [p.name for p in Clock.playing]]
#         if len(playerFiltred) >= 1:
#             return playerFiltred[0]
#         else:
#             return None
#     if fx == "":
#         print(dwarfDict.keys())
#     else:
#         if param == "":
#             print(dwarfDict[fx].keys())
#         else:
#             if value != "" and fx in dwarfDict.keys() and param in dwarfDict[fx].keys():
#                 para = dwarfDict[fx][param]
#                 playerName = findName()
#                 if playerName is not None:
#                     clip.copy(f"{playerName} >> MidiOut(channel=8, cc={para}, value={value}, dur={duree}) # {fx}/{param}")
#                     eval(f"{playerName} >> MidiOut(channel=8, cc={para}, value={value}, dur={duree})")
#                 else:
#                     print("No more player left...")
#             else:
#                 print("Wrong name or give me a value")

from rtmidi.midiconstants import CONTROL_CHANGE

class MidiDwarf:
    def __init__(self, ch=12):
        midiout = rtmidi.MidiOut()
        available_ports = midiout.get_ports()
        midiout.open_port(0)
        print(f"Dwarf connected to {available_ports[0]}")
        self.channel = ch
        self._midi = midiout
        self.length = 16
        self.channelTrack = 1
        self.recordStatus = ""
    def send_channel_message(self, status, data1=None, data2=None, ch=None):
        """Send a MIDI channel mode message."""
        msg = [(status & 0xF0) | ((ch if ch else self.channel) - 1 & 0xF)]
        if data1 is not None:
            msg.append(data1 & 0x7F)
            if data2 is not None:
                msg.append(data2 & 0x7F)
        self._midi.send_message(msg)
    def send_control_change(self, cc=0, value=0, ch=None):
        """Send a 'Control Change' message."""
        self.send_channel_message(CONTROL_CHANGE, cc, value, ch=ch)
    def send_record(self):
        print(f"{self.recordStatus} Recording: {str(self.length)} bars at channel {self.channelTrack}")
        self.send_control_change(1, 0)
        if (self.recordStatus == "Start"):
            self.recordStatus = "Stop"
        else:
            self.recordStatus = "Start"
    def record(self, length=16):
        self.length=length
        self.recordStatus = "Start"
        Clock.schedule(self.send_record, Clock.mod(self.length))
        Clock.schedule(self.send_record, Clock.mod(self.length) + self.length)
    def send_start(self):
        self.send_control_change(2,0)
    def undo(self):
        self.send_control_change(4,0)
    def start(self):
        Clock.schedule(self.send_start, Clock.mod(self.length))
    def stop(self, duration=0):
        if (duration != 0):
            Clock.schedule(self.send_start, Clock.mod(duration))
        else:
            send_start()
        print(f"Stop {self.channelTrack} channel")
    def clear(self):
        self.send_control_change(3,0)
    def track(self, channelTrack=1):
        self.channelTrack = channelTrack
        if(channelTrack>1):
            channelTrack=127
        self.send_control_change(5,channelTrack)

dwarf = MidiDwarf()

try:
	class FilterOSCClient(OSCClient):
		def send(self, message, *args):
			if "video" in str(message.message):
				OSCClient.send(self, message, *args)
	def OSCVideo(video_adress):
		my_client = FilterOSCClient()
		my_client.connect((video_adress, 20000))
		Server.forward = my_client
	OSCVideo(crashOSIp)
	print("Video Connected")
except Exception as e:
	print(e)


class voice_count():
	''' random count recursively every 8 bars.
		voicecount.start(lang="fr", voice=2, dur=8, amp=1.0, pitch=0.0)
		voicecount.help() to show all available voices'''
	def __init__(self):
		self.loop = True
	def stop(self):
		if self.loop:
			self.loop = False
		else:
			self.loop = True
	def start(self, lang="fr", voice=2, dur=8, amp=1.0, pitch=0):
		self.lang=lang
		self.voice=voice
		self.dur = dur
		self.amp = amp
		self.pitch = pitch
		Voice(str(randint(0,1000)), voice=self.voice, lang=self.lang, amp=self.amp, pitch=self.pitch)
		if self.loop:
			nextBar(Clock.future(self.dur, lambda: self.start(lang=self.lang, voice=self.voice, dur=self.dur, amp=self.amp, pitch=self.pitch)))
	def help(self):
		print(Voice().get_voices())

voicecount = voice_count()

# def reboot():
#     Clock.clear()
#     import signal
#     carla = subprocess.Popen(["pgrep", "carla"], stdout=subprocess.PIPE, shell=False)
#     for pid in carla.stdout:
#         os.kill(int(pid),signal.SIGTERM)
#     scsynth = subprocess.Popen(["pgrep", "scsynth"], stdout=subprocess.PIPE, shell=False)
#     for pid in scsynth.stdout:
#         os.kill(int(pid),signal.SIGTERM)
#     scide = subprocess.Popen(["pgrep", "scide"], stdout=subprocess.PIPE, shell=False)
#     for pid in scide.stdout:
#         os.kill(int(pid),signal.SIGTERM)
#     sleep(1)
#     os.system('scide %F &')
#     sleep(10)
#     os.system('carla /home/zbdm/crashserver/config/carla_live.carxp &')
#     FoxDot.reload()

### Mixer
# try:
# 	class Mixer():
# 		def __init__(self):
# 			self.client = OSCClient()
# 			self.client.connect((ipZbdm, 7788))
# 			self.strip = ["foxdot", "fx1", "fx2", "voice", "reverb", "master"]
# 			self.audio = ["foxdot", "fx1", "fx2", "voice"]
#
# 		def gain(self, strip, gain):
# 			if strip in self.strip:
# 				msg = OSCMessage(f"/strip/{strip}/Gain/Gain%20(dB)/unscaled", float(gain))
# 				self.client.send(msg)
#
# 		def mute(self, strip):
# 			if strip in self.strip:
# 				msg = OSCMessage(f"/strip/{strip}/Gain/Gain%20(dB)/unscaled", float(-70.0))
# 				self.client.send(msg)
#
# 		def solo(self, strip):
# 			for s in [st for st in self.audio if st != strip]:
# 				msg = OSCMessage(f"/strip/{s}/Gain/Gain%20(dB)/unscaled", float(-70.0))
# 				self.client.send(msg)
#
# 		def unsolo(self):
# 			for s in self.audio:
# 				msg = OSCMessage(f"/strip/{s}/Gain/Gain%20(dB)/unscaled", float(0.0))
# 				self.client.send(msg)
#
# 		def reverb(self, strip, gain):
# 			if strip in self.audio:
# 				msg = OSCMessage(f"/strip/{strip}/Aux%20(A)/Gain%20(dB)/unscaled", float(gain))
# 				self.client.send(msg)
#
# 		def feed(self, strip, gain):
# 			if strip in ["fx1", "fx2"]:
# 				msg = OSCMessage(f"/strip/{strip}/Aux%20/Gain%20(dB)/unscaled", float(gain))
# 				self.client.send(msg)
#
# 	mixer = Mixer()
# except Exception as e:
# 	print(e)
