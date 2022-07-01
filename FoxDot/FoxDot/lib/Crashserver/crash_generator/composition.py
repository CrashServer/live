#coding: utf8
#!/usr/bin/env python3
####### COMPOSITION #######
if __name__ != "__main__":
    from ...Chords import *

### Dictionnaire de valeur min/max d'effets A COMPLETER/TESTER/APPROUVER ###
preso = [0.1,1] # resonant, _delay, mix, ...
pdeg = [-7,7] # degree, shift
pint = [0,10] # int (max < 100)
pfreq = [100,17000] # freq filter ,lpf, hpf, bpf

fxdict = {
'vib' : {'vib': pint, 'vibdepth': preso},
'slide' : {'slide': pdeg, 'slidedelay': preso},
'slidefrom' : {'slidefrom': pdeg, 'slidedelay': preso},
'glide' : {'glide': pdeg, 'glidedelay': preso},
'bend' : {'bend': pdeg, 'benddelay': preso},
'coarse' : {'coarse': preso},
'pshift' : {'pshift': pdeg},
'hpf' : {'hpf': pfreq, 'hpr': preso},
'lpf' : {'lpf': pfreq, 'lpr': preso},
'swell' : {'swell': preso, 'hpr': preso},
'bpf' : {'bpf': [400,12000], 'bpr': preso, 'bpnoise': [0,0.1]},
'crush' : {'bits': [2,16], 'crush': pint},
'dist' : {'dist': preso},
'chop' : {'chop': pint, 'chopmix': preso, 'chopwave': [0,6], 'chopi': preso},
'tremolo' : {'tremolo': pint, 'tremolomix': preso},
'echo' : {'echo': preso, 'echomix': preso, 'echotime': preso},
'spin' : {'spin': preso},
'cut' : {'cut': preso},
'room' : {'room': preso, 'mix': preso},
'formant' : {'formant': [0,4], 'formantmix': preso},
'shape' : {'shape': preso, 'shapemix': preso},
'drive' : {'drive': preso, 'drivemix': preso},
'leg' : {'leg': [0.0,2.0]},
'spf' : {'spf': pfreq, 'spr': preso, 'spfslide': [0.0,10.0], 'spfend': pfreq},
'mpf' : {'mpf': pfreq, 'mpr': preso},
'disto' : {'disto': [0,0.5], 'smooth': preso, 'distomix': preso},
'flanger' : {'flanger': [0,99], 'fdecay': preso, 'flangermix': preso},
'tanh' : {'tanh': preso},
'chorus' : {'chorus': [0,3.0], 'chorusrate': preso},
'octafuz' : {'octafuz': preso, 'octamix': preso},
'krush' : {'krush': [0.0,4.0], 'kutoff': pfreq},
'drop' : {'drop': [0,99], 'dropof': [0,99]},
'squiz' : {'squiz': pint},
'triode' : {'triode': pint},
'octer' : {'octer': preso, 'octersub': [0,10], 'octersubsub': [0,10]},
'sample_atk' : {'sample_atk': preso, 'sample_sus': preso},
'position' : {'position': preso},
'ring' : {'ring': preso, 'ringl': [0,15000], 'ringh': [0,15000]},
'shift' : {'shift': [0.0,5.0], 'shiftsize': [0.0,0.5]},
'fold' : {'fold': [0.0,0.5], 'symetry': preso, 'smooth': preso},
'phaser' : {'phaser': preso, 'phaserdepth': preso},
'ringz' : {'ringz': preso, 'ringzfreq': [50,1000]},
'mverb': {'mverb': preso, 'mverbmix': preso, 'mverbdamp': preso, 'mverbdiff': [0.5,0.99]},
'clouds': {'clouds': preso, 'cpos': [0.0,1.0], 'csize': [0.0,1.0], 'cdens': [0.0,1.0], 'ctex': [0.0,1.0], 'cpitch': [-48,48], 'cgain': [1,4], 'cfb': [0.0,0.5], 'cmode': [0,3]},
'dist2': {'dist2': [0.2,1], 'dist2mix': preso, 'dist2shape': [0.03,0.5]},

}

sorted_sample = {
'kick_sample': ["k","K","v","V","W","x","X"],
'hh_sample': ["-","d"],
'snare_sample': ["o","O","u","U","c","C","d","p","P","^","@"],
'oh_sample': ["=",":"],
'ride_sample': ["~","7","h","s","S"],
'rim_sample': ["R","r","p","P","+","d"],
'perc_sample': ["+","h","^","d","{m,M,t,T}"]}


krhytm = {
    0.25: [0.25,0.25,0.25,0.5],
    0.5:  [0.25,0.5,0.125,1,0.125],
    0.125: [0.375,0.125],
    0.375: [0.375,0.375,1],
    1: [1,0.75,0.25,0.5,1],
    0.75: [0.25,1,0.125,0.125]
    }

# 0 = rest(0.5)
rythmMarkov = {
    0.5: [[0.5,1,1.5,0], [0.2,0.3,0.2,0.3]],
    1:   [[0.5,1,1.5], [0.5,0.3,0.2]],
    1.5: [[0.5,1,0], [0.3,0.5,0.2]],
    0: [[0.5,0], [0.7,0.3]]
    }

chords = {
    I: [[I, II, III, IV, V, VI], [2,2,2,39,20,35]],
    II: [[I, II, III, IV, V, VI], [3,2,1,4,86,4]],
    III: [[I, II, III, IV, V, VI], [0,5,0,85,2,8]],
    IV: [[I, II, III, IV, V, VI], [20,1,1,1,76,1]],
    V: [[I, II, III, IV, V, VI], [70,1,2,13,1,14]],
    VI: [[I, II, III, IV, V, VI], [5,5,1,49,39,1]],
    }

synthType = {
    "pads" : ["ambi", "angst", "charm", "creep", "glass", "organ", "ripple", "sinepad", "soprano", "space", "swell", "total", "varsaw"],
    "lead" : ["arpy", "blip", "dirt", "karp", "lapin", "nylon", "pasha", "piano", "pluck", "prof", "prophet", "pulse", "quin", "razz", "saw", "scatter", "sine", "sitar", "spark", "star", "supersaw", "tb303", "tritri", "varicelle", "zap"],
    "fx" : ["noise", "lazer", "scratch", "snick"],
    "bass" : ["bass", "bbass", "dab", "dafbass", "dbass", "dirt", "faim", "glitchbass", "jbass", "pbass", "sawbass"],
    }

melody_dict = {
        0: [[0,1,2,3,4,5,6,7,8,9,10,11], [27,0,22,0,19,1,0,12,0,6,1,13]],
        1: [[0,1,2,3,4,5,6,7,8,9,10,11], [9,0,77,0,14,0,0,0,0,0,0,0]],
        2: [[0,1,2,3,4,5,6,7,8,9,10,11], [32,0,22,0,26,6,0,8,0,2,0,3]],
        3: [[0,1,2,3,4,5,6,7,8,9,10,11], [10,0,38,16,0,29,0,7,0,0,0,0]],
        4: [[0,1,2,3,4,5,6,7,8,9,10,11], [11,0,30,0,22,16,0,19,0,2,0,0]],
        5: [[0,1,2,3,4,5,6,7,8,9,10,11], [0,0,13,0,43,17,0,18,0,6,0,1]],
        6: [[0,1,2,3,4,5,6,7,8,9,10,11], [1,0,4,0,7,1,12,67,0,8,0,0]],
        7: [[0,1,2,3,4,5,6,7,8,9,10,11], [16,0,3,0,17,22,1,30,0,10,0,1]],
        8: [[0,1,2,3,4,5,6,7,8,9,10,11], [0,0,0,0,0,27,0,55,0,18,0,0]],
        9: [[0,1,2,3,4,5,6,7,8,9,10,11], [4,0,2,0,1,5,0,60,0,19,1,8]],
        10: [[0,1,2,3,4,5,6,7,8,9,10,11], [17,0,2,1,12,2,0,22,1,18,24,2]],
        11: [[0,1,2,3,4,5,6,7,8,9,10,11], [45,0,12,0,0,1,0,7,0,26,0,9]]
        }

freqs = {
    "lpf": [40,5000],
    "hpf": [40,5000],
    "bpf": [40,5000]}
