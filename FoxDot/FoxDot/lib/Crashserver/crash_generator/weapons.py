#coding: utf8
#!/usr/bin/env python3
try:
	from random import choice, randint, sample, choices
	import string
	from re import findall
	from ...SCLang.SynthDef import SynthDefs
	from ...Patterns import Sequences
	from ...TempoClock import *
	from .Grammar import *
	from .server_conf import *
	from ..drumspattern2 import *
except Exception as e:
	print(e)

########
### Generate players 
######

def generate_random_synth_player():
	''' Generate a random synth pattern '''
	try:
		player = generate_player_name()
		synth = choice(synthdefNames)
		degree = gen_synth_degree()
		dur = choices([f"PDur({randint(2,8)},8)",f'SDur({choice([8,16,32])})',checkPattern(GENERATE_PATTERN())],probPatternDur)[0]
		oct = GENERATE_LIST(synthOctMin,synthOctMax)
		return {"player": player, "synth": synth, "degree": degree, "dur": dur, "oct": oct}
	except Exception as e:
		print("random synth error :" + e)

def generate_random_drum_player():
	''' Generate a random Play pattern '''
	try:
		player = generate_player_name()
		synth = 'play'
		degree = str(GENERATE_CHAR())
		sample = '[{}]'.format(",".join([GENERATE_INTEGER() for i in range(randint(1,len(degree)))]))
		dur = checkPattern(GENERATE_PATTERN())
		rate = str(GENERATE_LIST(drumRateMin,drumRateMax))
		return {"player":player, "synth":synth, "degree":degree, "dur":dur, "sample": sample, "rate": rate}
	except Exception as e:
		print("random drum player : " + e)

def generate_random_loop_player():
	''' Generate loop player, random dur '''
	try:
		player = generate_player_name()
		synth = 'loop'
		degree = str(choice(loopNames))
		sample = '{}'.format(",".join([GENERATE_INTEGER()]))
		dur_length = findall(r'\d+', degree)
		if not dur_length:
			dur_length=[4]
		try:
			dur = str(int(dur_length[0])*choices(multDurLoopPLayer, probDurLoopPlayer)[0])
		except:
			dur = "8"
		if int(dur) < 4:
			dur="4"
		return {"player":player, "synth": synth, "degree": degree, "sample": sample, "dur": dur}
	except Exception as e:
		print("random loop player : " + e)
		
def generate_drum_style_player():
	''' return a drum style pattern, according to the DrumsPattern2 dict, 
		you can change the char with khsor '''
	try:
		drumpat = ""
		player = generate_player_name()
		synth = 'play'
		sample = str(randint(0,100))
		rate = str(choices([GENERATE_FLOAT_LIST(drumRateMin,drumRateMax),1],probDrumStyleRate)[0])
		dur = str(choices(DrumStyleDur,probDrumStyleDur)[0])
		style = str(choice(list(DrumsPattern2.keys())))
		pat = str(choice(list(DrumsPattern2[style].keys())))
		for drmpat in DrumsPattern2[style][pat]:
			drumpat += '<'+ drmpat.split('"')[1::2][0] +'>'
		drumpat = change_drum_char(drumpat)
		return {"player":player, "synth": synth, "degree": drumpat, "sample": sample, "dur": dur, "rate": rate}
	except Exception as e:
		print("drum style : " + e)

def generate_player_name():
	try:
		player = "os"
		while player in ["os", "in", "fx", "if", "at", "or", "is", "in", "as", "id", "it", "re", "on"]:
			player = ''.join(choice(string.ascii_lowercase) for x in range(2))
		return player
	except Exception as e:
		print("player name : " + e)

def change_drum_char(pattern=None):
	'''Replace drum char'''
	try:
		for keys,list_sample in sorted_sample.items():
			for letter in list_sample:
				if str(pattern).find(letter) != -1:
					pattern = pattern.replace(letter, choices([choice(list_sample),choice(list(GENERATE_CHAR()))],probChangeDrumChar)[0])
		return pattern
	except Exception as e:
		print("change drum char : " + e)

def gen_player_param():
	''' Generate player parameter (unison, jump, stutter)'''
	try:
		args = []
		timePlayer = choice([k for k in player_time_para.keys()])
		for i in range(len(player_time_para[timePlayer])):
			args.append(player_time_para[timePlayer][i]())
		return str(timePlayer) + "({})".format(", ".join(args))
	except Exception as e:
		print("gen player param : " + e)

def gen_player_attributes(playerType=None):
	''' Generate player attribute: sus, dur, amp, pan,... '''
	try:
		attr = choices(['amp','amplify','dur','sus','pan'],probPlayerAttributes)[0]
		if attr in ["amp", "amplify"]:
			value = GENERATE_AMPLIFY()
		elif attr in ["dur"]:
			if playerType != "loop": 
				value = f'SDur({choice([8,16,32])})'
			else:
				attr = "sbrk"
				value = GENERATE_FLOAT_LIST(0.2,0.8)
		elif attr in ["sus"]:
			if playerType == "loop":
				attr = "sbrk"
				value = GENERATE_FLOAT_LIST(0.2,0.8)
			else:
				value = GENERATE_FLOAT_LIST(0.2,2)
		elif attr in ["pan"]:
			value = GENERATE_PAN()
		else:
			pass
		return (attr, value)
	except Exception as e:
		print("gen player attribut : " + e)


def gen_arp():
	''' Generate PArp '''
	try:
		arpindex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,23,30,40,41,42,43,44,50,51,52,53,54]
		arp_rnd = choice(['I','II','III','IV','V','VI','VII'])
		return f'PArp({arp_rnd},{choice(arpindex)})'
	except Exception as e:
		print("gen arp : " + e)

def gen_filter():
	''' generate a lpf or hpf, linvar or int '''
	try:
		filType = choices(['lpf', 'hpf'],[probLowPass,probHighPass])[0]
		if filType == 'hpf':
			filfreq = choices([GENERATE_FREQLIST(filterFreqMin,int(filterFreqMax/3),5), GENERATE_INTEGER(filterFreqMin,int(filterFreqMax/3)), "0"],probFilterFreq)[0]
		else:	 
			filfreq = choices([GENERATE_FREQLIST(filterFreqMin,filterFreqMax,5), GENERATE_INTEGER(filterFreqMin,filterFreqMax), "0"],probFilterFreq)[0]
		return (filType,filfreq)
	except Exception as e:
		print("gen filter : " + e)

def gen_synth_degree():
	''' generate degree for synth '''
	try:
		melody_length = choice([4,8,16])
		return f'melody()[:{melody_length}]'
	except Exception as e:
		print("gen synth degree : " + e)
