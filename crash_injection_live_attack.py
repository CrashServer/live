#### crash injection live attack ####


@player_method
	def brk(self, multi=1):
		""" turn loop into break beat (only with splitter player """
		if self.synthdef == "splitter":
			self.dur = P*[1/4,1/2,1]*multi
			self.pos = PWhite(0,1).rnd(1/8)
			self.rate = PwRand([1,0.5,-1,-0.5],[60,10,10,10])
			self.often("stutter", PRand(1,8))
			self.beat_stretch=0
		else:
			print("only with splitter")


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

sample_description_path = os.path.join(crash_path, "description.cs")
if os.path.isfile(sample_description_path):
	with open(sample_description_path, "rb") as file:
		sample_description = pickle.load(file)


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