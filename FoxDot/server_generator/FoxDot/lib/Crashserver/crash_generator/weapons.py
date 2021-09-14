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
	player = generate_player_name()
	synth = choice(synthdefNames)
	degree = checkPattern(GENERATE_PATTERN())
	dur = choices([f"PDur({randint(2,8)},8)",checkPattern(GENERATE_PATTERN())],probPatternDur)[0]
	oct = GENERATE_LIST(synthOctMin,synthOctMax)
	return {"player": player, "synth": synth, "degree": degree, "dur": dur, "oct": oct}

def generate_random_drum_player():
	''' Generate a random Play pattern '''
	player = generate_player_name()
	synth = 'play'
	degree = str(GENERATE_CHAR())
	sample = '[{}]'.format(",".join([GENERATE_INTEGER() for i in range(randint(1,len(degree)))]))
	dur = checkPattern(GENERATE_PATTERN())
	rate = str(GENERATE_LIST(drumRateMin,drumRateMax))
	return {"player":player, "synth":synth, "degree":degree, "dur":dur, "sample": sample, "rate": rate}

def generate_random_loop_player():
	''' Generate loop player, random dur '''
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
		
def generate_drum_style_player():
	''' return a drum style pattern, according to the DrumsPattern2 dict, 
		you can change the char with khsor '''
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

def generate_player_name():
	player = "os"
	while player in ["os", "in", "fx", "if", "at", "or", "is", "in", "as", "id", "it"]:
		player = ''.join(choice(string.ascii_lowercase) for x in range(2))
	return player

def change_drum_char(pattern=None):
	'''Replace drum char'''
	for keys,list_sample in sorted_sample.items():
		for letter in list_sample:
			if str(pattern).find(letter) != -1:
				pattern = pattern.replace(letter, choices([choice(list_sample),choice(list(GENERATE_CHAR()))],probChangeDrumChar)[0])
	return pattern

def gen_player_param():
	''' Generate player parameter (unison, jump, stutter)'''
	args = []
	timePlayer = choice([k for k in player_time_para.keys()])
	for i in range(len(player_time_para[timePlayer])):
		args.append(player_time_para[timePlayer][i]())
	return str(timePlayer) + "({})".format(", ".join(args))

def gen_player_attributes(playerType=None):
	''' Generate player attribute: sus, dur, amp, pan,... '''
	attr = 	choices(['amp','amplify','dur','sus','pan'],probPlayerAttributes)[0]		
	if attr in ["amp", "amplify"]:
		value = GENERATE_AMPLIFY()
	elif attr in ["dur"]:
		if playerType != "loop":
			value = 'eval(generate_rytm(16,choice([0.5,1,2,4])))'
		else:
			attr = "blur"
			value = GENERATE_LIST(1,4) 	
	elif attr in ["sus"]:
		if playerType == "loop":
			attr = "blur"
			value = GENERATE_LIST(1,4)
		else:
			value = GENERATE_FLOAT_LIST(0.2,2)
	elif attr in ["pan"]:
		value = GENERATE_PAN()
	else:
		pass
	return (attr, value)

def gen_arp():
	''' Generate PArp '''
	arpindex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,21,22,23,30,40,41,42,43,44,50,51,52,53,54]
	arp_rnd = choice(['I','II','III','IV','V','VI','VII'])
	return f'PArp({arp_rnd},{choice(arpindex)})'

def gen_filter():
	''' generate a lpf or hpf, linvar or int '''
	filType = choices(['lpf', 'hpf'],[probLowPass,probHighPass])[0]
	filfreq = choices([GENERATE_FREQLIST(filterFreqMin,filterFreqMax,5), GENERATE_INTEGER(filterFreqMin,filterFreqMax), "0"],probFilterFreq)[0]
	return (filType,filfreq)

