#coding: utf8
#!/usr/bin/env python3
#####  SERVER STARTUP ###########
if __name__ != "__main__":
	try:
		import os
		import sys
		import pickle
		import time
		from random import randint, sample
		
		from .Settings import FOXDOT_ROOT, SAMPLES_BANK
		from .Buffers import alpha, nonalpha

		from pathlib import Path
		sys.path.append(str(Path('.').absolute().parent))

		try:
			from crash_config import *
		except Exception as e:
			print(e)

		# from .Crashserver.crash_generator.server_conf import *
		from .Extensions.PArp import PArp
	except Exception as e:
		print("error in import modules", e)

	''' LOAD CUSTOM SYNTHDEFS '''
	try:
		from .Crashserver.crashSynthDefs import * ### Crash Custom SynthDefs
		from .Crashserver.crashFX import * ### Crash Custom Fx
	except:
		print("Error importing SynthDefs, FX or Loop player : ", sys.exc_info()[0])

	#########################
	### SERVER CONFIG     ###
	#########################

	### Voice parameters ####
	rate_voice = 100
	pitch = 0
	voiceamp = 0.5

	### Useful path and list
	gamme = ["locrianMajor", "locrian", "phrygian", "minor", "dorian", "mixolydian", "major", "lydian", "lydianAug"]

	### EXTENSIONS #######
	### TXT 2 Speech ####
	try:
		if sys.platform == "Windows":
			from .Crashserver.speech.voice import *   ### Text2Speech Windows
		elif sys.platform.startswith("linux"):
			from .Crashserver.speech.voice_linux_mbrola import *   ### Text2Speech linux
		else:
			print("Txt2Speech don't work for ", sys.platform)
	except:
		print("Error importing Speech Extension")

	### Foxdot tools
	try:
		from .Crashserver.sdur import *
		from .Chords import *
	except:
		print("Error importing Extensions : ", sys.exc_info())

	### Sample custom directory
	try:
		FOXDOT_SND   = crash_path
		FOXDOT_LOOP  = os.path.join(crash_path, "_loop_")
		BANK_LEN = [item for item in os.listdir(FOXDOT_SND) if not (item.startswith("."))]
		FoxDotCode.use_sample_directory(FOXDOT_SND)
		loops = []
		for bankNbr in BANK_LEN:
			Samples.addPath(os.path.join(FOXDOT_SND, str(bankNbr), "_loop_"))
			loops += sorted([fn.rsplit(".",1)[0] for fn in os.listdir(os.path.join(FOXDOT_SND, str(bankNbr), '_loop_'))])
		loops.remove('')
		loops.remove('__init__')
	except:
		print("Error importing Custom Sound", sys.exc_info()[0])

	### Load weapons - Code generator
	try:
		from .Code.main_lib import _StartupFile
		FOXDOT_STARTUP = _StartupFile(os.path.join(FOXDOT_ROOT, "lib", "Crashserver", "crash_generator", "server_startup.py"))
		execute.load_startup_file()
		if startupLive:
			FOXDOT_STARTUP = _StartupFile(os.path.join(FOXDOT_ROOT, "lib", "Crashserver", "crash_generator", "startup_live.py"))
			execute.load_startup_file()
	except Exception as e:
		print("fail : ", e)

	####################
	###    VOICE     ###
	####################
	def init_voice(horodatage=False):
		''' Voice initalisation, windows / linux '''
		if sys.platform.startswith("win"):
			voix = Voice(lang=lang, rate=0.45, amp=1.0)
			voix.initi(lieu)
		elif sys.platform.startswith("linux"):
			serv = init_server(lang, lieu, horodatage)
			txt_init = serv.initi()
			Voice(txt_init, rate=rate_voice, amp=voiceamp, pitch=pitch, lang=lang, voice=voice)
		else:
			print("Sorry, we crash only from windows or linux")

	def voice_lpf(freq=400):
		''' Low pass everything during speech voice '''
		Master().lpf=freq

	def calc_dur_voice(phrase=""):
		''' return the voice duration in beats '''
		phrase = len(phrase.split())
		try:
			if phrase or phrase > 0:
				return (Clock.seconds_to_beats(phrase * 0.6))
			else:
				return 8
		except:
			return 8

	def clear_voice_dir():
		''' delete all voice sample in _loop_/voicetxt dir '''
		voicetxt_path = os.path.join(crash_path, str(SAMPLES_BANK), "_loop_", "voicetxt")
		voices_files = os.listdir(voicetxt_path)
		for f in voices_files:
			os.remove(os.path.join(voicetxt_path, f))


	### RANDOM function ###

	def random_bpm_var():
		'''Change the clock randomly with random var'''
		bpm_rand = [PRand(38,220)[0] for n in range(PRand(2,9)[0])]
		var_rand = [PRand(1,16)[0] for n in range(PRand(2,9)[0])]
		Clock.bpm = var(bpm_rand,var_rand)
		print("Clock.bpm = var({},{})".format(bpm_rand, var_rand))

	def random_bpm():
		''' Change Clock to a random number'''
		Clock.bpm = PRand(38,220)[0]
		print("Clock.bpm = ", Clock.bpm)

	def setseed(seed=None):
		RandomGenerator.set_override_seed(seed)


	###############################################################################################
	###########################
	###   PLAYERS METHODS   ###
	###########################
	try:
		@player_method
		def unison(self, unison=2, detune=0.125, analog=0):
			""" Like spread(), but can specify number of voices(unison)
			Sets pan to (-1,-0.5,..,0.5,1) and pshift to (-0.125,-0.0625,...,0.0625,0.125)
			If unison is odd, an unchanged voice is added in the center
			Eg : p1.unison(4, 0.5) => pshift=(-0.5,-0.25,0.25,0.5), pan=(-1.0,-0.5,0.5,1.0)
				p1.unison(5, 0.8) => pshift=(-0.8,-0.4,0,0.4,0.8), pan=(-1.0,-0.5,0,0.5,1.0)
				p1.unison(5,(0.3,2)) => pshift=(-2.0,-0.3,0,0.3,2.0), pan=(-1,-0.5,0,0.5,1)
			"""
			if unison > 1:
				pan=[]
				pshift=[]
				uni = int(unison if unison%2==0 else unison-1)
				for i in range(1,int(uni/2)+1):
					pan.append(2*i/uni)
					pan.insert(0, -2*i/uni)
				for i in range(1, int(uni/2)+1):
					if type(detune)==tuple:
						pshift.append(detune[i-1]+PWhite(0,detune[i-1]*(analog/100)))
						pshift.insert(0,detune[i-1]*-1+PWhite(0,-1*detune[i-1]*(analog/100)))
					else:
						pshift.append(detune*(i/(uni/2))+PWhite(0,detune*(analog/100)))
						pshift.insert(0,detune*-(i/(uni/2))+PWhite(0,-1*detune*(analog/100)))
				if unison%2!=0 and unison > 1:
					pan.insert(int(len(pan)/2), 0)
					pshift.insert(int(len(pan)/2), 0)
				self.pan = tuple(pan)
				self.pshift = tuple(pshift)
			else:
				self.pan=0
				self.pshift=0
			return self

		@player_method
		def human(self, velocity=20, humanize=5, swing=0):
			""" Humanize the velocity, delay and add swing in % (less to more)"""
			try:
				if humanize == 0:
					humanize = 1
				if velocity!=0:
					self.delay=[0,PWhite((-1*int(humanize)/100)*self.dur, (int(humanize)/100)*self.dur) + (self.dur*int(swing)/100)]
					self.amplify=[1,PWhite((100-velocity)/100,1)]
				else:
					self.delay=0
					self.amplify=1
				return self
			except Exception as e:
				return self

		@player_method
		def fill(self, mute_player=0, on=1):
			""" add fill to a drum player
			you can mute other players with .fill(Group(p1,d2,d3))
			0 = off
			1 = dur + amplify
			2 = dur  //  amplify =1
			3 = amplify // dur=1/2
			"""
			if on==1:
				self.dur = PwRand([1/4,1/2,3/4],[45,45,10])
				self.amplify = var([0,1],[[PRand([3,7,15]),PRand([6,2,14])],[1,2]])*[1,PWhite(0.2,1)]
				if mute_player != 0:
					mute_player.amplify = self.amplify.map({0:1, 1:0})
			elif on==2:
				self.dur = PRand([1/4,1/2,3/4])
				self.amplify=1
			elif on==3:
				self.amplify = var([0,1],[[3,6,7,2,15,2,3,14],[1,2]])*PWhite(0,1)
				self.dur = 1/2
			else:
				self.dur = 1/2
				self.amplify = 1

		@player_method
		def brk(self, multi=1, code=""):
			""" turn loop into break beat (only with splitter player """
			if self.synthdef == "loop":
				if multi != 0:
					eval(f"z{self.name[1:]} >> splitter('{self.filename}', dur=P*[1/4,1/2,1]*{multi}, sample=self.sample, pos=PWhite(0,1.25).rnd(1/8), rate=PwRand([1,0.5,-1,-0.5],[60,10,10,10]), beat_stretch=0, {code}).often('stutter', PRand(1,8))")
				else:
					eval(f"z{self.name[1:]}.stop()")
			else:
				print("only with loop")

		@player_method
		class PChain2(RandomGenerator):
			""" PChain Mod Markov Chain generator pattern with probability."""
			def __init__(self, mapping, **kwargs):
				assert isinstance(mapping, dict)

				RandomGenerator.__init__(self, **kwargs)

				self.args = (mapping,)

				self.last_value = 0
				self.mapping = {}
				i = 0
				for key, value in mapping.items():
					self.mapping[key] = [asStream(value[0]), asStream(value[1])]
					if i == 0:
						self.last_value = key
						i += 1
				self.init_random(**kwargs)

			def func(self, *args, **kwargs):
				# key = list(self.mapping[self.last_value][0])
				# prob = list(self.mapping[self.last_value][1])
				# self.last_value = self.choices(key, prob)[0]
				index = self.last_value
				if index in self.mapping:
					self.last_value = self.choices(self.mapping[index][0], self.mapping[index][1])[0]
				return self.last_value
	except Exception as e:
		print(f'Player method problem : {e}')

	###############################
	###     PATTERN METHODS     ###
	###############################

	try: 
		@PatternMethod
		def renv(self, nbr=1):
			""" Pattern Chord Inversion """
			sorted_chord = sorted(self)
			if nbr > 0:
				for i in range(nbr):
					sorted_chord[-1] -= 7
					sorted_chord = sorted(sorted_chord)
			return PGroup(sorted_chord)
	except Exception as e:
		print(f'Pattern method problem : {e}')

	###########################
	###   Useful FUNCTIONS  ###
	###########################

	try:
		@loop_pattern_func
		def PBin(number=0):
			""" Returns a random binary pattern or convert number to bin pattern """
			if number==0:
				number = PRand(10,1000000)[0]
			return [int(i) for i in str(bin(number)[2:])]

		@loop_pattern_func
		def PSaw(n=16, inverse = 0):
			""" Returns values of one cycle of Saw wave split into 'n' parts """
			i = 1 / (n-1)
			if not inverse:
				return Pattern([i * j for j in range(0,int(n))])
			else:
				return Pattern([i * j for j in range(0,int(n))]).reverse()

		@loop_pattern_func
		def PTime():
			"""Generate a pattern from the local machine time"""
			return [int(t) for t in str(Clock.get_time_at_beat(int(Clock.now()))) if t != '.']

		@loop_pattern_func
		def PTimebin():
			"""Generate a pattern of actual time converted to binary"""
			return PBin(int(Clock.get_time_at_beat(int(Clock.now()))))

		@loop_pattern_func
		def PFrac(a=0.63,b=0.0, size=16, mapl=0, maph=1):
			''' return a Pattern with fractional step, 
				not sure what it is but sounds cool try with:  
					a = 0.63, b = 0.00
					a = 0.66, b = 0.08
					a = 0.42, b = 0.10
					a = 0.60, b = 0.68
					a = 0.62, b = 0.67
				'''
			return Pattern([(a*i + b )%1 for i in range(size)]).lmap(mapl, maph)

		@loop_pattern_func
		def PFr(mapl=0, maph=1, seedFr=1664, size=16):
			''' Simpliest version of PFrac '''
			a=PWhite(0,0.99, seed=seedFr)[0]
			b=PWhite(0,0.99, seed=seedFr)[0]
			return Pattern([(a*i + b )%1 for i in range(size)]).lmap(mapl, maph)

		def lininf(start=0, finish=1, time=32):
			''' linvar from start to finish but stay at finish after time '''
			return linvar([start,finish],[time,inf], start=now)

		def expinf(start=0, finish=1, time=32):
			''' expvar from start to finish but stay at finish after time '''
			return expvar([start,finish],[time,inf], start=now)

		def linbpm(endBpm=170, durBpm=128):
			''' use with Clock.bpm = linbpm(220, 12) to change bpm from current bpm to target in x beats'''
			Clock.bpm = linvar([int(Clock.bpm),endBpm],[durBpm,inf], start=now)

		def linmod(start, end, duration, default=0):
			''' linvar from start to end during duration at next mod(duration) and switch back to default'''
			return linvar([start, end, default], [duration, 0, inf], start=Clock.mod(duration))

		def PDrum(style=None, pat='', listen=False, khsor='', duree=1/2, spl = 0, charPlayer="d") :
			''' Generate a drum pattern style '''
			ppat = ""
			dplayers = {"d1":d1,"d2":d2,"d3":d3,"d4":d4,"d5":d5,"d6":d6,"d7":d7,"d8":d8,"d9":d9,"d0":d0}
			stopList = [p for p in dplayers.keys()]
			sample = "x-u=~r+"
			if style == None:
				print(DrumsPattern2.keys())
			else:
				patlist = [key for key in DrumsPattern2[style].keys()]
				if pat == "":
					print(DrumsPattern2[style].keys())
				elif type(pat) == int:
					if pat > len(DrumsPattern2[style])-1:
						pat = 0
						print("no more patterns...")
					player_idx = 0
					ppat = ""
					for i in DrumsPattern2[style][patlist[pat]]:
						ply, pat, rst = i.split('"')
						if khsor != '':
							for idx, char in enumerate(sample):
								try:
									pat = pat.replace(char, khsor[idx])
								except:
									pass
						player_idx += 1
						ppat += f'{charPlayer}{player_idx} >> play("{pat}", dur={duree}, sample={spl})'
						ppat += "\n"
						stopList.remove(f'd{player_idx}')
						if listen:
							dplayers[f"d{player_idx}"] >> play(pat, dur=duree, sus=duree, sample=spl)
					clip.copy(ppat)
					if listen:
						for p in stopList:
							dplayers[p].stop()
					else:
						print(ppat)
				else:
					for i in DrumsPattern2[style][pat]:
						ppat += i
						ppat += "\n"
					clip.copy(ppat)

		def darker():
			''' Change Scale to a darkest one '''
			if Scale.default.name not in gamme:
				Scale.default = "major"
			if Scale.default.name == gamme[0]:
				print("Darkest scale reach !")
			else:
				actual = Scale.default.name
				Scale.default = gamme[gamme.index(actual) - 1]

		def lighter():
			''' Change Scale to a lightest one '''
			if Scale.default.name not in gamme:
				Scale.default = "major"
			if Scale.default.name == gamme[-1]:
				print("Lightest scale reach !")
			else:
				actual = Scale.default.name
				Scale.default = gamme[gamme.index(actual) + 1]

		class PChords(RandomGenerator):
			''' Chords generator '''
			def __init__(self, chord=None, **kwargs):
				RandomGenerator.__init__(self, **kwargs)
				self.list_chords = {"I": I, "II": II, "III": III, "IV": IV, "V": V, "VI": VI, "VII":VII}
				self.last_value = None
				self.chord = None
				self.list_of_choice = []
				self.init_random(**kwargs)
			def func(self, index, list_of_choice=[]):
				self.list_of_choice = []
				if self.chord == None:
					self.chord = tuple(self.list_chords[self.choice(list(self.list_chords))])
				for keys, values in self.list_chords.items():
					for note in values:
						if note in list(self.chord):
							if values not in self.list_of_choice:
								self.list_of_choice.append(values)
				self.list_of_choice.remove(self.chord)
				self.last_value = self.choice(self.list_of_choice)
				self.chord = self.last_value
				return self.last_value

		class PGauss(RandomGenerator):
			''' Returns random floating point values using Gaussian distribution '''
			def __init__(self, mean=0, deviation=1, **kwargs):
				RandomGenerator.__init__(self, **kwargs)
				self.args = (mean, deviation)
				self.mean = mean
				self.deviation = deviation
				self.init_random(**kwargs)
			def func(self, index):
				if isinstance(self.mean, float):
					return self.gauss(self.mean, self.deviation)
				elif isinstance(self.mean, int):
					return int(round(self.gauss(self.mean, self.deviation)))

		class PLog(RandomGenerator):
			''' Returns random floating point values using logarithmic distribution '''
			def __init__(self, mean=0, deviation=1, **kwargs):
				RandomGenerator.__init__(self, **kwargs)
				self.args = (mean, deviation)
				self.mean = mean
				self.deviation = deviation
				self.init_random(**kwargs)
			def func(self, index):
				if isinstance(self.mean, float):
					return self.lognormvariate(self.mean, self.deviation)
				elif isinstance(self.mean, int):
					return int(round(self.lognormvariate(self.mean, self.deviation)))

		class PTrir(RandomGenerator):
			''' Returns random floating or int point values using triangular distribution '''
			def __init__(self, low=0, high=8, mode=None, **kwargs):
				RandomGenerator.__init__(self, **kwargs)
				self.args = (low, high)
				self.low = low
				self.high = high
				if mode is None:
					self.mode = (self.high-self.low) / 2
				else:
					self.mode = mode
				self.init_random(**kwargs)
			def func(self, index):
				if isinstance(self.low, float) or isinstance(self.high, float):
					return self.triangular(self.low, self.high, self.mode)
				else:
					return int(round(self.triangular(self.low, self.high, self.mode)))

		class PCoin(RandomGenerator):
			''' Choose between 2 values with probability, eg : PCoin(0.25,2,0.2)'''
			def __init__(self, low=0, high=1, proba=0.5, **kwargs):
				RandomGenerator.__init__(self, **kwargs)
				self.low = low
				self.high = high
				self.proba = proba
				if self.proba > 1:
					self.proba /= 100
				self.init_random(**kwargs)
			def func(self, index):
				return self.choices([self.low, self.high], [1-self.proba, self.proba])[0]

		class PChar(RandomGenerator):
			''' Generate characters randomly, PChar(case, alpha)
				case = 0 , only lowercase
				case = 1 , only uppercase
				case = 2 , lower case and uppercase
				alpha = 0, only alpha
				alpha = 1, only nonalpha
				alpha = 2, alpha + nonalpha'''
			def __init__(self, case=2, alpha=2, **kwargs):
				RandomGenerator.__init__(self, **kwargs)
				self.case = case
				self.alpha = alpha
				self.init_random(**kwargs)
			def func(self, index):
				if self.alpha == 0:
					charList = alpha
				if self.alpha == 1:
					charList = ''.join([x for x in nonalpha.keys()])
				else:
					charList = ''.join([x for x in nonalpha.keys()]) + alpha
				if self.case == 0:
					char = self.choice(charList)
				elif self.case == 1:
					char = self.choice(charList).upper()
				else:
					char = self.choice([self.choice(charList), self.choice(charList).upper()])
				return char

		from .Crashserver.chords_dict import *

		@player_method
		class PMarkov(RandomGenerator):
			""" An example of a Markov Chain generator pattern. The mapping argument
				should be a dictionary of keys whose values are a list/pattern of possible
				destinations.  Mod to add probability"""
			def __init__(self, init_value="", **kwargs):
				RandomGenerator.__init__(self, **kwargs)
				self.init_value = init_value
				self.active_value = 0
				self.first_value = 0
				self.second_value = 0
				self.third_value = 0
				self.mapping = {}
				self.turn = 0
				self.init_random(**kwargs)
			def stream_value(self, active_dict):
				""" Return mapping dict with a list of keys and probability"""
				for key, value in active_dict.items():
					self.mapping[key] = [asStream(value[0]), asStream(value[1])]
					#self.last_value = key
			def key_prob(self, active_dict):
				"""return the key and prob of previous value from active dictionnary"""
				self.stream_value(active_dict)
				key = list(self.mapping[self.active_value][0])
				prob = list(self.mapping[self.active_value][1])
				return key, prob
			def value_choice(self, active_dict):
				""" Return a key from probabilty of active dictionnary """
				key, prob = self.key_prob(active_dict)
				return self.choices(key, prob)[0]
			def func(self, index):
				if self.turn == 0:
					if self.init_value == "":
						self.init_value = self.choice(list(cho1.keys()))
					self.active_value = self.init_value
					self.turn += 1
					return self.active_value
				else:
					if self.turn == 1:
						self.first_value = self.value_choice(cho1)
						self.active_value = self.first_value

					elif self.turn == 2:
						self.second_value = self.value_choice(cho2[self.init_value])
						self.active_value= self.second_value

					elif self.turn == 3:
						try:
							self.third_value = self.value_choice(cho3[self.init_value][self.first_value])
							self.active_value = self.third_value
						except:
							list_cho = list(cho1.keys())
							list_cho.remove(self.init_value)
							self.third_value = self.choice(list_cho)
							self.active_value = self.third_value

					self.turn += 1
					if self.turn > 3:
						self.turn = 0
					return self.active_value

		class PZero(GeneratorPattern):
			''' Generate a Pattern with '1' and size-1 '0' 
				eg: PZero(5) -> P[1,0,0,0,0] 
				the '1' position can be offset 
				'''
			def __init__(self, size=2, offset=0):
				GeneratorPattern.__init__(self)
				self.size = size
				self.offset = offset
			def func(self, index):
				if ((index-self.offset)%int(self.size) == 0):
					return 1
				else:
					return 0			

		class PBool(GeneratorPattern):
			''' Binary operation between 2 Pattern, you can select the operator:
				0 -> and
				1 -> or
				2 -> xor   '''
			def __init__(self, pat1=P[0], pat2=P[0], operator=0):
				GeneratorPattern.__init__(self)
				self.pat1 = pat1
				self.pat2 = pat2
				self.operator = operator
			def func(self, index):
				if self.operator == 0:
					return self.pat1[index] and self.pat2[index]
				elif self.operator == 1:
					return self.pat1[index] or self.pat2[index]
				elif self.operator == 2:
					return self.pat1[index] ^ self.pat2[index]

		@player_method
		def switch(self, other, key, bypass=1):
			""" Switch the attr of a player
				eg: b1 >> dbass(P[0:4], amp=1)
					b2 >> blip(-2, amp=1).switch(b1, "degree")"""
			if bypass != 0:
				self_temp = self.attr[key]
				other_temp = other.attr[key]
				other.attr[key] = self_temp
				self.attr[key] = other_temp
				return self

		@player_method
		def clone(self, player):
			""" Clone a player, eg: a2 >> saw().clone(a1)"""
			self.attr = copy(player.attr)
			return self

		@PatternMethod
		def add(self, value):
			''' pattern method add, eg:  s1.sometimes("degree.add",2) '''
			return self + value

		@PatternMethod
		def mul(self, value):
			''' pattern method mul, eg: d1.often("rate.mul", -1) '''
			return self * value

		def drop(playTime=14, dropTime=2, nbloop=1):
			""" Drop the amplify to 0 for random players.
				ex : drop(6,2,4) => amplify=0 for random playing players at the 2 last beats of 8, 4 times
			"""
			if nbloop > 0:
				totalTime = playTime + dropTime
				clkPly = Clock.playing
				if len(clkPly)>1:
					for p in clkPly:
						p.amplify=1
					if nbloop == 1:
						rndPlayerIndex = sample(range(0,len(clkPly)), len(clkPly))
						print("Final Drop !!!")
					else:
						rndPlayerIndex = sample(range(0,len(clkPly)), randint(1,len(clkPly)-1))
						print(f"Drop loop left : {nbloop}")
					if rndPlayerIndex:
						for i in rndPlayerIndex:
							clkPly[i].amplify = var([1,0],[playTime, dropTime])
				nbloop -= 1
				Clock.future(totalTime, drop, args=(playTime, dropTime, nbloop))
			else:
				for p in Clock.playing:
					p.amplify = 1
				return

		def drop_bpm(duree=32, nbr=0, end=4):
			""" Create a drop bpm effect (var bpm),
				duree = durée totale de la partie,
				nbr = nombre de division du drop,
				end = duree du drop en partant de la fin
				pour retablir le tempo simplement drop(92)
				"""
			if nbr == 0:
				Clock.bpm = duree
			else:
				init_bpm = Clock.bpm
				actual_bpm = Clock.bpm
				divi = 1
				bpm_list = []
				duree_list = []
				for i in range(nbr):
					actual_bpm /= divi
					if actual_bpm < 10:
						actual_bpm = 10
					bpm_list.append(int(actual_bpm))
					if i == 0:
						duree_list.append(duree-end)
					else:
						duree_list.append(end/(2**i))
					divi = 2
				duree_list[-1] = end-sum(duree_list[1:-1])
				Clock.bpm = var([bpm_list], [duree_list], start=Clock.mod(8))
				print('var({}, {})'.format([bpm_list], [duree_list]))

		# def melody(scale_melody=Scale.default.name, melody_dict=melody_dict):
		# 	''' Generate melody with a Markov chain dict of melody '''
		# 	scale_melody_dict = {key: melody_dict[key] for key in melody_dict.keys() if key in Scale[scale_melody]}
		# 	for keys, values in scale_melody_dict.items():
		# 		note, prob = values
		# 		fnote, fprob = zip(*((key, pro) for key, pro in zip(note, prob) if key in Scale[scale_melody]))
		# 		scale_melody_dict[keys] = [list(fnote), list(fprob)]
		# 		return PChain2(scale_melody_dict)

		def melody():
			''' Generate a melody based on Markov chain dict of melody '''
			return PChain2(melody_dict)

		def chaos(chaosInt=1):
			''' Generate some random players '''
			chaosText = ""
			for i in range(chaosInt):
				chaosText += add_player(True)
				chaosText += "\n"
			clip.copy(chaosText)

		def PRy(total=16, div=4, restProb=0):
			''' Generate a ryhtm pattern '''
			pat = PSum(div, total)
			patTotal = []
			for i in range(0, len(pat)):
				patTotal.append(PSum(PRand(1, div)[i], pat[i]))
			patTotal = PJoin(patTotal)
			#patTotal = PShuf(patTotal)
			if restProb !=0:
				for i in range(1,len(patTotal)):
					if PRand(0,100)[0] < restProb*100:
						patTotal[i] = rest(patTotal[i])
			return patTotal

		@player_method
		def once(self):
			''' play a player once and stop it '''
			self.dur=1/32
			self.amplify=var([1,0],[1/32,inf], start=now)
			self.after(32, "stop")

		@player_method
		def start(self, startBeat=8):
			""" Start a player at a specific beat"""
			if (startBeat==0):
				beatStart = now
			else:
				beatStart = Clock.mod(startBeat)
			self.amplify=linvar([0,1],[0,inf], start=beatStart)

		@PatternMethod
		def norm(self, mult=1):
			""" Returns the pattern with all values between 0 and 1*mult """
			pos = self - min(self)
			return (pos / max(pos))*mult

		@PatternMethod
		def clamp(self, mini, maxi):
			""" Returns the pattern with all values clamped to min – max """
			return self.transform(lambda n: max( min(maxi, n), mini))

		@PatternMethod
		def lmap(self, oMin, oMax):
			""" Retruns the pattern mapped to min and max values """
			return ((self - min(self)) / (max(self)-min(self)) * (oMax - oMin) + oMin)

	except Exception as e:
		print(f"useful function problem : {e}")

####
#### Rock Pattern Generator

try:
		from .Crashserver.drumRockPattern import * ### Crash Drum rock pattern
		@player_method
		def drummer(self, durloop=16, durPlyr=1/2):
			''' Transform the player into an automatic drummer '''
			if durloop!=0:
				drumCat = PRand(1, len(drumRockPattern))[0]
				drumPat = PRand(1,len(drumRockPattern[drumCat]))[0]
				drumFillCat = PRand(1, len(drumRockFill))[0]
				drumFillPat = PRand(1, len(drumRockFill[drumFillCat]))[0]
				fillDur = durloop/PRand([4,8,16])
				# durPlayer = PwRand([durPlyr,durPlyr*2],[80,20])[:1]
				self.degree=Pvar([drumRockPattern[drumCat][drumPat], drumRockFill[drumFillCat][drumFillPat]], [durloop-fillDur, fillDur])
				self.human(30,PWhite(-5,5))
				self.comp=0.8
				self.dur = durPlyr
				self.every(durloop, "drummer", durloop, durPlyr)
except:
		print("Error importing drumRockPattern", sys.exc_info()[0])

if crashPanelSending:
	class SendOsBpm():
		''' Send current Bpm to crashOS'''
		def __init__(self, ipCrashOS="localhost", port=20000):
			self.ipCrashOS = ipCrashOS
			self.port = port
			self.clientBpm = OSCClient()
			self.clientBpm.connect((self.ipCrashOS, self.port))
			self.threadOsBpm = Thread(target = self.sendOsBpm)
			self.threadOsBpm.daemon = True
		def sendOsBpm(self):
			try:
				while self.isrunning:
					msg = OSCMessage("/OSbpm", [int(Clock.get_bpm())])
					self.clientBpm.send(msg)
					sleep(0.5)
			except:
				pass
		def start(self):
			self.isrunning = True
			self.threadOsBpm.start()
		def stop(self):
			self.isrunning = False

	## start sending Bpm to crashOS
	osBpm = SendOsBpm(crashOSIp, crashOSPort)
	osBpm.start()




# @player_method
# def basser(self, duration=64, markdur=2):
# 	if duration!=0:
# 		durChoice = choice([P[6,1,1], P[1], PDur(var([4,PRand(7)],[6,2]), 8), PDur(var([5,PRand(7)],[6,2]), 8), PDur(var([3,PRand(7)],[6,2]), 8)])
# 		sequence = PMarkov()[:markdur]
# 		print(durChoice)
# 		print(sequence)
# 		var.seq = var(sequence,8)
# 		degreeChoice = choice([var.seq[0], var([var.seq[0], P*[var.seq[1], _, var.seq[2]], P*[var.seq[2], var.seq[2] -7, var.seq[1] - 7]], [6,1,1])])
# 		self.degree = degreeChoice
# 		self.dur = durChoice
# 		self.rarely("stutter", oct=self.oct+1, cut=0.5)
# 		self.every(duration, "basser", duration, markdur)



