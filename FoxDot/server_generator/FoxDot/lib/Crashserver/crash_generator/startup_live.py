try:
	import pickle
	import os
	import sys
	import time
	import re
	from random import choice
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
		clip.copy(figlet_format(attack_data["connect"][0].strip(), font=fig_fonts_list[cool_ascii[51]]) + "\n" + attack_data["connect"][2].strip() + "\n" + video_line)
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
		time_init = time.time()
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
	elif total==1:
		print(lost_list)
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
	else:
		path = os.path.join(FOXDOT_ROOT, "osc", "scsyndef", synth + ".scd")
		with open(str(path), "r") as synth:
			synth = synth.readlines()
		synth_txt = [line.strip() for line in synth if line != "\n"]
		txt = str(''.join(synth_txt))
		synthname = re.findall('SynthDef[.new]*[(\\\]*(.+?),',txt)
		synthargs = re.findall('\{\|(.*)\|', txt)
		print(str(synthname[0]), " : ", str(synthargs[0]))

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
	else:
		path = os.path.join(FOXDOT_ROOT, "osc", "sceffects", fx + ".scd")
		with open(str(path), "r") as fx:
			fx = fx.readlines()
		fx_txt = [line.strip() for line in fx if line != "\n"]
		print(fx_txt[1])

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
	else:
		listloops = sorted([fn.rsplit(".",1)[0] for fn in os.listdir(os.path.join(FOXDOT_LOOP, loop))])
		print(listloops)

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