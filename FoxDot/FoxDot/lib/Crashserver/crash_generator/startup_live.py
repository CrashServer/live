try:
	import pickle
	import os
	import sys
	from time import *
	import re
	from random import choice
	from threading import Thread

except Exception as e:
	print(e)

# ASCII 
asciiEnable = False
clipcopyEnable = False    
try:
	import pyperclip as clip # copy to clipboard
	from pyfiglet import figlet_format, FigletFont # ASCII GENERATOR
	cool_ascii = [1,6,8,11,13,15,17,18,19,21,22,24,26,30,31,32,33,34,35,37,38,43,44,45,46,47,48,50,59,62,64,65,68,69,77,79,81,82,83,84,85,88,89,96,98,103,104,105,107,111,113,114,117,119,123,124,131,135,143,150,151,152,159,187,190,193,19,201,203,217,225,227,230,240,243,244,245,251,273,275,280,308,325,329,347,363,385,410]
	fig_font = FigletFont()
	fig_fonts_list = fig_font.getFonts()
	fig_skip = ['fbr12___', 'mshebrew210', 'term', 'runic', 'pyramid', 'eftifont', 'DANC4', 'dietcola']
	fig_skip += ['emboss', 'emboss2', 'future', 'letter', 'pagga',
					  'smblock', 'smbraille', 'wideterm']
	fig_skip += ['dosrebel', 'konto', 'kontoslant']
	font_list = [x for x in fig_fonts_list if x not in fig_skip]
	asciiEnable = True
	clipcopyEnable = True
except:
	asciiEnable = False
	clipcopyEnable = False
	print("Please install pyperclip & pyfiglet")

#########################
### SERVER CONFIG     ###
#########################

### Read the config file data
serverfile = os.path.join(FOXDOT_ROOT, "lib", "Crashserver", "crash_gui", "server_data.cs")
lostfile = os.path.join(FOXDOT_ROOT, "lib", "Crashserver", "crash_gui", "lostfile.cs")

with open(serverfile, "rb") as fichier:
	mon_depickler = pickle.Unpickler(fichier)
	code_server = mon_depickler.load()

with open(lostfile, "rb") as lost:
	lost_depickler = pickle.Unpickler(lost)
	lost_list = lost_depickler.load()

lost_played = lost_list[:]
server_data = code_server["server_data"]
attack_data = code_server["attack_data"]

### Lieu du Server
lieu = str(server_data["lieu"])
### Longueur mesure d'intro
tmps = int(server_data["tmps"])
### Language
lang = str(server_data["lang"])
if sys.platform.startswith("win") and lang.startswith("english"):
	lang = "english"
voice = int(server_data["voice"])
### BPM intro
bpm_intro = int(server_data["bpm_intro"])
### Scale intro
scale_intro = str(server_data["scale_intro"])
### Root intro
root_intro = str(server_data["root_intro"])
horodatage = int(server_data["horo"])

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

def connect():
	''' Full reset and set bpm, root, sos & video player '''
	Master().reset()
	Clock.set_time(0)
	lost(2)
	print(attack_data["connect"][1].strip())
	if "connect" in lost_played:
		lost_played.remove("connect")
	Clock.bpm = bpm_intro
	Scale.default = scale_intro
	Root.default = root_intro
	i3 >> sos(dur=8, lpf=linvar([60,4800],[tmps*1.5, tmps*3], start=now), hpf=expvar([0,500],[tmps*6, tmps*2]), amplify=0.5)
	if clipcopyEnable:
		clip.copy(figlet_format(attack_data["connect"][0].strip(), font=fig_fonts_list[cool_ascii[51]]) + "\n" + attack_data["connect"][2].strip() + "\n")
	else:
		print(attack_data["connect"][2].strip())

def attack(part="", active_voice=0):
	''' Lanch an attack and copy it to the clipboard, attack voice '''
	if type(part) != str:  ### so we can type attack(42) or attack(43)
		part = str(part)
	### next part
	elif part == "":
		part = lost_played[0]
	if part in lost_played:
		lost_played.remove(part)

	blase = attack_data[part][0].strip()
	voice_txt = attack_data[part][1].strip()
	code_txt = attack_data[part][2].strip()

	### Define prompt
	exten = ''.join(choice(string.ascii_lowercase) for x in range(3))
	prompt = "### attack@{}.{}:~$ ".format(part, exten)

	### Init server
	if part == "init":
		if active_voice == 1:
			init_voice(horodatage)
		global time_init
		time_init = time()
		if clipcopyEnable:
			clip.copy(figlet_format(blase) + "\n" + prompt + define_virus()+ "\n" + code_txt)
		else:
			print(code_txt)

	### Select Part and generate Ascii text
	else:
		if clipcopyEnable:
			clip.copy((figlet_format(blase, font=fig_fonts_list[choice(cool_ascii)]) if blase != None else "") + "\n" + prompt + define_virus()+ "\n" + (code_txt if code_txt is not None else ""))
		else:
			print((code_txt if code_txt is not None else ""))

	### Generate Voice
	if voice_txt != None:   ### Voice generator
		if voice_txt != "" and active_voice==1:
			voice_lpf(400)
			Voice(voice_txt, rate=rate_voice, amp=voiceamp, pitch=pitch + randint(-10,50), lang=lang, voice=voice)
			Clock.future(calc_dur_voice(voice_txt), lambda: voice_lpf(0))

def lost(total=0):
	''' Print the part for live show'''
	global lost_played
	global lost_list
	if total==0:
		print(lost_played)
		if crashPanelSending:
			crashpanel.sendOnce(str(lost_played))
	elif total==1:
		print(lost_list)
		if crashPanelSending:
			crashpanel.sendOnce(str(lost_list))
	elif total==2:
		print("Reinit lost")
		lost_played=lost_list[:]
		print(lost_played)

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
	path = os.path.join(FOXDOT_ROOT,"osc", "sceffects", "")
	if fx == "":
		dir_list = os.listdir(path)
		fx_list = []
		for p in dir_list:
			files,sep,ext = p.partition('.')
			fx_list.append(files)
		print(sorted(fx_list))
		if crashPanelSending:
			crashpanel.sendOnce(str(sorted(fx_list)))
	else:
		path = os.path.join(FOXDOT_ROOT, "osc", "sceffects", fx + ".scd")
		with open(str(path), "r") as fx:
			fx = fx.readlines()
		fx_txt = [line.strip() for line in fx if line != "\n"]
		print(fx_txt[1])
		if crashPanelSending:
			crashpanel.sendOnce(str(fx_txt[1]))

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
	if loop=="":
		print(loops)
		if crashPanelSending:
			crashpanel.sendOnce(str(loops))
	else:
		listloops = sorted([fn.rsplit(".",1)[0] for fn in os.listdir(os.path.join(FOXDOT_LOOP, loop))])
		print(listloops)
		if crashPanelSending:
			crashpanel.sendOnce(str(listloops))

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

virus_method = ["Injecting... ", "Loading... ", "Init: ", "Dumping: ", "Hacking: ", "Run.."]
virus_name = ["MyDoom", "Brain", "Zeus", "Sality", "Virut", "Ramnit", "Blaster", "Conficker",\
"Worm", "TDSS TDL 4"]
virus_access = ["Kernel", "MBR", "Kernel", "bsdriver.sys", "Hardware", "Security", ]
virus_protocole = ["Spambot", "PWS", "Stealer", "Proxy", "BackDoor", "KeyLogger", "InfoStealer", "Cryto",\
"Autoruns", "Rootkit", "Trojan", "Rogue", "Scareware", "Script", "D.O.S." ]
virus_status = [" | [###.......] % Completed | ###",  "- Lost: 78% - ###", " @@88@@", " /Please Wait...", " |***--------| ", " , ping=3ms", "!WARNING BUFFER(#4F,5E) - VIOLATION ACCESS"]


def define_virus():
	### Generate a random virus text
	virus = "###" + choice(virus_method) + choice(virus_name) + "." + choice(virus_access) + "." + choice(virus_protocole) + choice(virus_status)  
	return virus

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

def PRy(duration=16, div=4, restprob=0.3):
	''' Generate a ryhtm pattern '''
	pat = PSum(randint(1,duration), duration)
	pat_total = []
	for i in range(0,len(pat)):
		pat_total.append(PSum(randint(1,div),pat[i]))
	pat_total = PJoin(pat_total)
	if rest !=0:
		for i in range(0,len(pat)):
			if randint(0,100) < restprob*100:
				pat_total[i] = rest(pat_total[i])    
	return pat_total

### CrashPanel 
### Root, scale
### generateur de "Plat du jour"

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
					 ".renv(nbr=1)", "binary(number)", "PTime()", "PTimebin()", "lininf(start=0, finish=1, time=32)", "expinf(start=0, finish=1, time=32)",
					 "PDrum(style=None, pat='', listen=False, khsor='', duree=1/2, spl = 0, charPlayer='d')", "darker()", "lighter()", "PChords(chords)", 
					 "PGauss(mean, deviation)", "PLog(mean, deviation)", "PTrir(low,high,mode)", "PCoin(low, high, proba)", "PChar(case=2, alpha=2)", 
					 "PMarkov(init_value='')", "switch(other, key, bypass=1)", "clone(player)", "add(value)", "mul(value)", "drop(playTime=6, dropTime=2, nbloop=1)",
					 "drop_bpm(duree=32, nbr=0, end=4)", "melody(scale_melody=Scale.default.name, melody_dict=melody_dict)", "PArp(seq, index=0)", "SDur(target)"]
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
			self.plyTime = 0.3 # time cycle send player
			self.pdjTime = 60 #time cycle send PlatduJour
			
			self.clientZbdm = OSCClient()
			self.clientZbdm.connect((self.ipZbdm, 2000))
			if self.ipSvdk:
				self.clientSvdk = OSCClient()
				self.clientSvdk.connect((self.ipSvdk, 2001))
			
			self.pdj = PlatduJour()

			self.threadBpm = Thread(target = self.sendBpm)
			self.threadBpm.daemon = True
			self.threadBeat = Thread(target = self.sendBeat)
			self.threadBpm.daemon = True
			self.threadPlayer = Thread(target = self.sendPlayer)
			self.threadPlayer.daemon = True
			self.threadPdj = Thread(target = self.sendPdj)
			self.threadPdj.daemon = True
			

		def sendOscMsg(self, msg):
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
					msg = OSCMessage("/panel/player", [[str(p) for p in Clock.playing]])
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

		def sendOnce(self, txt):
			''' send on txt msg to OSC '''
			msg = OSCMessage("/panel/help", [txt])
			self.sendOscMsg(msg)
		
		def stop(self):
			self.isrunning = False
		
		def start(self):
			self.isrunning = True
			self.threadBpm.start()
			self.threadBeat.start()
			self.threadPlayer.start()
			self.threadPdj.start()
	
	def panelreset():
		crashpanel = CrashPanel(ipZbdm, ipSvdk, 2000)
		crashpanel.start()

	crashpanel = CrashPanel(ipZbdm, ipSvdk, 2000)
	crashpanel.start()

	