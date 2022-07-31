#coding: utf8
#!/usr/bin/env python3
if __name__ != "__main__":
	try:
		from ...SCLang   import SynthDef, SynthDefs
		from ...Players  import Player
		from ...Patterns import Sequences
		from ...Buffers import alpha, nonalpha
		from ...Patterns.Sequences import *
		from ...Effects.Util import FxList
		from crash_config import crash_path
		from .composition import *
		from .synthArgs import *

		from types import FunctionType
		from random import random, randint, uniform
		from random import choice, sample
		from os import listdir
		from os.path import join, isdir
		from inspect import signature
		from re import findall
	except Exception as e:
		print(e)

	FOXDOT_LOOP  = join(crash_path, "_loop_")
	if not isdir(FOXDOT_LOOP):
		print("Could not find _loop_ in crash_path : ", crash_path)
	
	#PATTERN LIST & Exclude
	patternNames = {name: obj for name, obj in vars(Sequences).items() \
				if (type(obj) == FunctionType and name.startswith("P"))}
	patternExclude = ['PSq', 'PSine', 'PPairs', "Pow", "PEq","PNe","PulsesToDurations", "PatternMethod","PatternFormat",
						"PEuclid2","PZip2","PJoin", "PBeat", "PDelay","PQuicken"]
	try:
		for k in patternExclude: del patternNames[k]
	except:
		pass
	
	#SYNTH LIST & Exclude
	synthdefNames = [i for i in SynthDefs]
	synthExclude = ['video', 'loop', 'stretch', 'gsynth', 'breakcore', 'splitter', 'splaffer', 'play1', 'play2', 'audioin' ]
	penible_synth = ['glitchbass', 'crackle', 'crunch', 'dustV', 'brown', 'fuzz', 'glitcher', 'gray', 'grat', 'hnoise', 
					'latoo', 'pink', 'saw', 'scratch', 'viola', 'bnoise', 'twang', "noise", "rsin", "rave", "virus", "combs", 
					"plaits", "braids", "arpy", "orient", "elmbass", "rhodes", "lfnoise", "bounce"]
	#penible_synth = ['gray']
	synthExclude += penible_synth
	for exclude in synthExclude:
		try:
			synthdefNames.remove(exclude)
		except:
			pass

	#LOOP LIST
	loopNames = sorted([fn for fn in listdir(FOXDOT_LOOP)])
	loopExclude = [".directory", "recin", "xmas", "voicetxt", "os4", "os16", "os32", "atmobis8"]
	for loopxclude in loopExclude:
		try:
			loopNames.remove(loopxclude)
		except:
			pass
	
	fxExclude = ["coarse", "dist", "formant", "shape", "drive", "disto", "tanh", "octafuz", "krush", 
				"drop", "triode", "squiz", "fold", "bpf", "ringz", "shift"]
	for fxclude in fxExclude:
		try:
			del fxdict[fxclude]
		except:
			pass	
# Generic actions	

def GENERATE_PATTERN(_min=1, _max=9):
	pat = choice(list(patternNames.values()))
	n = len(signature(pat).parameters)
	if pat.__name__ not in patternInputs:
		args = [str(GENERATE_INTEGER(_min,_max)) for i in range(n)]
	else:
		args = []
		for i in range(n):
			args.append(str(patternInputs[pat.__name__][i](_min, _max)))        
	return pat.__name__ + "({})".format(", ".join(args))

def GENERATE_LIST(_min=1, _max=9, length=6):
	return '[{}]'.format(", ".join([str(GENERATE_INTEGER(_min, _max)) for n in range(randint(2,length))]))

def GENERATE_FLOAT_LIST(_min=1, _max=9, length=6, digits=2):
	return '[{}]'.format(", ".join([str(GENERATE_RDM(_min, _max, digits)) for n in range(randint(2,length))]))

def GENERATE_TUPLE(_min=1, _max=9, length=4):
	return '({})'.format(", ".join([str(GENERATE_INTEGER(_min, _max)) for n in range(randint(2,length))]))

def GENERATE_INTEGER(_min=1, _max=9):
	return str(randint(_min,_max))

def GENERATE_NUMBER(_min=1, _max=9):
	''' Return a random number or fraction '''
	if random() > 0.5:
		return randint(_min,_max)
	else:
		return eval(str(randint(max(_min, 1),_max)) + "/" + str(randint(max(_min, 1),_max)))

def GENERATE_NOTHING(_min=1, _max=9):
	return " "

def GENERATE_RDM(_min=0, _max=1, digits=2):
	return round(uniform(_min,_max), digits)

def GENERATE_WHITE(_min=0, _max=1):
	return round(uniform(0,1),2)

def GENERATE_FREQLIST(_min=0, _max=22000, length=6):
	return 'linvar([{},{}],{})'.format(GENERATE_LIST(_min,_max, randint(2,length)),GENERATE_LIST(_min,_max, randint(2,length)),GENERATE_LIST(1,32,randint(2,length)))

def GENERATE_VARLIST(_min=0, _max=1, length=6):
	''' Generate a linvar float list '''
	return 'linvar([{},{}],{})'.format(GENERATE_FLOAT_LIST(_min,_max, randint(2,length)),GENERATE_FLOAT_LIST(_min,_max, randint(2,length)),GENERATE_FLOAT_LIST(1,32,randint(2,length)))

def GENERATE_FX(fxdict=fxdict):
	### Generate a fx LIST
	try:
		fx_rnd = fxdict[choice([e for e in fxdict.keys()])]
		fx_arg = {}
		for argmt in fx_rnd.keys():
			fx_min = fx_rnd[argmt][0]
			fx_max = fx_rnd[argmt][1]
			if type(fx_min) == float or type(fx_max) == float: # float fx
				fx_arg[argmt] = GENERATE_FLOAT_LIST(fx_min,fx_max,8)
			elif type(fx_max) == int and fx_max > 100:  # freq fx
				fx_arg[argmt] = GENERATE_FREQLIST(fx_min, fx_max)
			else: # int fx
				fx_arg[argmt] = GENERATE_LIST(fx_min, fx_max,8)
		return fx_arg
	except Exception as e:
		print("generate FX : " + e)


def GENERATE_SYNTH_ARGS(synthName, synthArgsDict=synthArgs):
	### Generate synth arguments
	try:
		synth_arg = {}
		if synthName in synthArgsDict.keys():
			synthParam = synthArgsDict[synthName]
			if len(synthParam) > 0:
				randArgs = sample(list(synthParam), randint(1,len(synthParam)))
				for argmt in randArgs:
					if argmt not in ["atk", "decay", "rel"]:
						para_min = synthParam[argmt][0]
						para_max = synthParam[argmt][1]	
						if random() < 0.2:
							synth_arg[argmt] = GENERATE_VARLIST(para_min, para_max, 8)
						else:
							if type(para_min) == float or type(para_max) == float:
								synth_arg[argmt] = GENERATE_FLOAT_LIST(para_min,para_max,8)
							elif type(para_max) == int and para_min > 100:  # freq args
								synth_arg[argmt] = GENERATE_FREQLIST(para_min, para_max)
							else: # int args
								synth_arg[argmt] = GENERATE_LIST(para_min, para_max,8)
			return synth_arg
		else:
			print(synthName, "not found in dictionnay")
			return {"vol": '1'}
	except Exception as e:
		print("generate synth arg : " + e)


def GENERATE_CHAR():
	### Generate a character LIST 
	try:
		rnd_char_list = []
		#clr_list = ["1","2","3","4","?","!", "\\"] 
		clr_list = []
		clr_nonalpha = [x for x in nonalpha.keys()]
		for i in clr_list:
			clr_nonalpha.remove(i)
		for i in range(randint(3,10)):
			if random() > 0.4:
				if random() > 0.7:
					rnd_char_list.append(choice(list(clr_nonalpha)))
				else:
					rnd_char_list.append(choice(list(alpha.upper())+list(alpha))) 
			else:
				rnd_char_list.append(".")               
		return "".join(rnd_char_list)    
	except Exception as e:
		print("generate char : " + e)


def GENERATE_PARA():
	''' generate parameters .stutter, .shuffle, .unison'''
	try:
		args = []
		player_merge = {**player_para, **player_para2}
		paraPlayer = choice([p for p in player_merge.keys()]) 
		for i in range(len(player_merge[paraPlayer])):
			args.append(player_merge[paraPlayer][i]())
		return f'"{paraPlayer}"' + '{}'.format(",".join(args))
	except Exception as e:
		print("generate para : " + e)

def GENERATE_PARA2():
	''' generate parameters not working with "after" like .amen, .bubble'''
	try:
		args = []
		paraPlayer = choice([p for p in player_para.keys()])
		for i in range(len(player_para[paraPlayer])):
			args.append(player_para[paraPlayer][i]())
		return f'"{paraPlayer}"' + '{}'.format(",".join(args))
	except Exception as e:
		print("generate para2 : " + e)

def GENERATE_DUR(dur=None):
	''' Generate a random dur pattern '''
	try:
		if dur == None:
			dur = choice([1,2,4])
		if type(dur) == str:
			dur = f"{dur}.sus" 
		return f'(PChain(krhytm)[:16]*{str(dur)}).limit(sum,16).limit(len,20)'
	except Exception as e:
		print("generate dur : " + e)

def GENERATE_AMPLIFY(_min=0, _max=1):
	''' Generate a random amplify pattern [0,1,0,1,0,1]'''
	try:
		rndList = sorted([randint(1,16) for i in range(2)])
		pat = [GENERATE_LIST(0,1), P10(rndList[1]), PBern(rndList[1]), PEuclid(rndList[0],rndList[1])]
		return f'{str(choice(pat))}'
	except Exception as e:
		print("generate amplify : " + e)

def GENERATE_PAN(_min=-1, _max=1):
	''' Generate a random pan pattern [-1,0.2,-0.3,1] or PSine(64) '''
	pan = choice([f'PSine({randint(2,128)})', f'{GENERATE_FLOAT_LIST(-1,1,12)}', f'PWhite(-1,1)'])
	return pan

def GENERATE_ADSR(synthName='', sustain=1):
	try:
		adsrArg = sample(['atk', 'decay', 'rel'], randint(1,3))
		adsrDict = {}
		for argm in adsrArg:
			if argm in synthArgs[synthName]:
				argMin = synthArgs[synthName][argm][0]
				argMax = (synthArgs[synthName][argm][1])*float(sustain/3)
				adsrDict[argm] = GENERATE_FLOAT_LIST(_min=argMin, _max=argMax, length=6, digits=5)
		return adsrDict
	except Exception as e:
		print("generate adsr : " + e)

# Patterns that take patterns as input

_pat = lambda _min, _max: choice([GENERATE_PATTERN, GENERATE_LIST]).__call__(_min, _max)
_int = GENERATE_INTEGER
_num = GENERATE_NUMBER
_tuple = GENERATE_TUPLE
_list = GENERATE_LIST
_rdm = GENERATE_RDM
_white = GENERATE_WHITE
_null = GENERATE_NOTHING
_para_player = GENERATE_PARA
_para_player2 = GENERATE_PARA2

patternInputs = {
	'PStutter' : [_pat, _int],
	'PShuf'    : [_pat],
	'PAlt'     : [_pat, _pat, _pat],
	'PStep'    : [_int, _num, _num],
	'PSum'     : [_int, _num, _null],
	'PStretch'  : [_pat, _int],
	'PZip'     : [_pat, _pat, _pat],
	'PRhythm'  : [_tuple],
	'PBern'    : [_int, _white],
	'PDur'     : [_int, _int, _int, _null],
	'PRange'	: [_int, _int, _null],
	'PTri'		: [_list, _list, _null]
				 }

# parameters
player_time_para = {
	"often": [_para_player], 
	"sometimes": [_para_player],
	"rarely": [_para_player],
	"every" : [_int, _para_player],
	"after": [_int, _para_player2]}

player_para = {
	"stutter": [_null, _null],
	"jump": [_null, _int],
	"spread": [_null],
	"unison": [_null],
	"slider": [_null],
	"penta": [_null],
	"reverse": [_null],
	"shuffle": [_null], 
	"degrade":[_null], 
	"offbeat":[_null],
	"fill": [_null]
	}

player_para2 = {
	"amen": [_null],
	"bubble": [_null]
}

# Utils

def remap_pattern(pat, oMin, oMax):
	''' remap a pattern, keep original range ''' 
	try:
		pmin = min(pat)
		pmax = max(pat)
		#print(f'remap {pat, pmin, pmax}')
		pat = [remap(p,pmin,pmax,oMin,oMax) for p in pat]
		return f'{pat}'
	except Exception as e:
		print("remap pattern : " + e)

def remap(x, oMin, oMax, nMin, nMax):
	''' remap value '''
	try:
		oldRange = (oMax - oMin)
		if oldRange == 0:
			newValue = nMin
		else:
			newRange = (nMax - nMin)  
			newValue = (((x - oMin) * newRange) / oldRange) + nMin
		if type(nMin) == int:
			return int(newValue)
		else:
			return newValue
	except Exception as e:
		print("remap : " + e)

def checkPattern(pat =""):
	''' limit a pattern len output < 20, avoid P[1,1,1,1,...,1,1,1,1] error ''' 
	if pat != "":
		patlen = len(eval(pat))
		if patlen > 20:
			pat += ".limit(len, 20)" 
	return pat