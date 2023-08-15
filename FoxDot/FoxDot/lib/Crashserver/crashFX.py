from ..Effects import *

# Legato slide
fx = FxList.new("leg", "leg", {"leg":0, "sus":1 }, order = 0)
fx.add("osc = osc * XLine.ar(Rand(0.5,1.5)*leg,1,0.05*sus)")
fx.save()

fx = FxList.new("glide", "glide", {"glide": 0, "glidedur": 0.05}, order=0)
fx.add("osc = Line.kr(start: (osc * glide).clip(-50,22000), end: osc, dur: glidedur)")
fx.save()

# fx = FxList.new("glide", "glissando", {"glide": 0, "glidedelay": 0.5, "sus": 1}, order=0)
# fx.add("osc = osc * EnvGen.ar(Env([1, 1, (1.059463**glide)], [sus*glidedelay, sus*(1-glidedelay)]))")
# fx.save()


# Lpf slide
fx = FxList.new('spf','SLPF', {'spf': 0, 'spr': 1, 'spfslide':1, 'spfend':15000}, order=2)
fx.add_var("spfenv")
fx.add('spfenv = EnvGen.ar(Env.new([spf, spfend], [spfslide]))')
fx.add('osc = RLPF.ar(osc, spfenv, spr)')
fx.save()

# Test FX
fx = FxList.new('test','test', {'test': 0, 'testa': 0, 'testb': 0, 'testc': 0, 'testd': 0}, order=2)
fx.doc("Test Fx")
fx.add('osc = osc*test')
fx.save()

# MoogLPF
fx = FxList.new('mpf','MoogFF', {'mpf': 0, 'mpr': 0}, order=2)
fx.doc("MoogFF filter")
fx.add('osc = MoogFF.ar(osc, mpf, mpr,0,1)')
fx.save()

# DFM1 LPF
fx = FxList.new('dfm','DFM1', {'dfm': 1000, 'dfmr': 0.1, 'dfmd': 1}, order=2)
fx.doc("DFM1 filter")
fx.add('osc = DFM1.ar(osc, dfm, dfmr, dfmd,0.0)')
fx.save()

# VALadder filter
fx = FxList.new('valad', 'VALadder', {'valad': 500, 'valadr': 0.5, 'valadd': 0.5, 'valadt': 0}, order=2)
fx.doc("VALadder filter")
fx.add('osc = VALadder.ar(osc*0.4, valad, valadr, valadd,valadt)')
fx.save()

# VADiode filter
fx = FxList.new('vadiod', 'VADiodeFilter', {'vadiod': 500, 'vadiodr': 0.5, 'vadiodd': 0.5}, order=2)
fx.doc("VADiode filter")
fx.add('osc = VADiodeFilter.ar(osc, vadiod, vadiodr, vadiodd)')
fx.save()


fx = FxList.new("fm_sin", "FrequencyModulationSine", {"fm_sin":0, "fm_sin_i":1}, order=0)
fx.add("osc = osc + (fm_sin_i * SinOsc.kr(osc * fm_sin))")
fx.save()

fx = FxList.new("fm_saw", "FrequencyModulationSaw", {"fm_saw":0, "fm_saw_i":1}, order=0)
fx.add("osc = osc + (fm_saw_i * Saw.kr(osc * fm_saw))")
fx.save()

fx = FxList.new("fm_pulse", "FrequencyModulationPulse", {"fm_pulse":0, "fm_pulse_i":1}, order=0)
fx.add("osc = osc + (fm_pulse_i * Pulse.kr(osc * fm_pulse))")
fx.save()

if SC3_PLUGINS:
    #Dist mod
    fx = FxList.new('disto', 'disto_mod', {'disto': 0, 'smooth': 0.3, 'distomix': 1}, order=1)
    fx.add("osc = LinXFade2.ar(CrossoverDistortion.ar(osc, amp:0.5*disto, smooth:smooth),  osc, 1-distomix)")
    fx.save()

#New Chop, with wave select :
#chopwave = (0: Pulse, 1: Tri, 2: Saw, 3: Sin, 4: Parabolic )
# and chopi = oscillator phase
fx = FxList.new('chop', 'chop', {'chop': 0, 'sus': 1, 'chopmix': 1, 'chopwave': 0, 'chopi': 0}, order=2)
fx.add("osc = SelectX.ar(chopmix, [osc, osc * SelectX.kr(chopwave, [LFPulse.kr(chop / sus, iphase:chopi, add: 0.01), LFTri.kr(chop / sus, iphase:chopi, add: 0.01), LFSaw.kr(chop / sus, iphase:chopi, add: 0.01), FSinOsc.kr(chop / sus, iphase:chopi, add: 0.01), LFPar.kr(chop / sus, iphase:chopi, add: 0.01)])])")
fx.save()


fx = FxList.new('tremolo', 'tremolo', {'tremolo': 0, 'beat_dur': 1, 'tremolomix': 1}, order=2)
fx.add("osc = SelectX.ar(tremolomix, [osc, osc * SinOsc.ar( tremolo / beat_dur, mul:0.5, add:0.5)])")
fx.save()

fx = FxList.new('echo', 'combDelay', {'echo': 0, 'echomix' : 0.5, 'beat_dur': 1, 'echotime': 1}, order=2)
fx.add('osc = SelectX.ar(echomix, [osc, osc + CombL.ar(osc, delaytime: echo * beat_dur, maxdelaytime: 2 * beat_dur, decaytime: echotime * beat_dur)])')
fx.save()

fx = FxList.new('pong', 'pingpong', {'pong': 0, 'beat_dur': 1, 'pongtime': 1}, order=2)
fx.add_var("left")
fx.add_var("right")
fx.add("left = CombN.ar(osc, delaytime: pong * beat_dur, maxdelaytime: 2 * beat_dur, decaytime: pongtime * beat_dur)")
fx.add("left = left*2.distort.tanh")
fx.add("left = LPF.ar(left,12000)")
fx.add("left = HPF.ar(left,300)")
fx.add("right = CombN.ar(osc, delaytime: pong * beat_dur + pong * beat_dur*0.5, maxdelaytime: 2 * beat_dur, decaytime: pongtime * beat_dur)")
fx.add("right = right*2.distort.tanh")
fx.add("right = LPF.ar(right,12000)")
fx.add("right = HPF.ar(right,300)")
fx.add("osc= osc + [left, right]")
fx.save()


fx = FxList.new('flanger', 'flanger', {'flanger': 0, 'fdecay': 0, 'flangermix':0.5}, order=2)
fx.add("osc = SelectX.ar(flangermix, [osc, CombC.ar(osc, 0.01, SinOsc.ar(flanger, 0, (0.01 * 0.5) - 0.001, (0.01 * 0.5) + 0.001), fdecay, 1)])")
fx.save()

fx = FxList.new("formant", "formantFilter", {"formant": 0, 'formantmix': 0.5}, order=2)
fx.add("formant = (formant % 8) + 1")
fx.add("osc = SelectX.ar(formantmix, [osc, Formlet.ar(osc, formant * 200, ((formant % 5 + 1)) / 1000, (formant * 1.5) / 600).tanh])")
fx.save()

fx = FxList.new("shape", "wavesShapeDistortion", {"shape":0, "shapemix":0.5}, order=2)
fx.add("osc = SelectX.ar(shapemix, [osc, (osc * (shape * 50)).fold2(1).distort / 5])")
fx.save()

fx = FxList.new("drive", "overdriveDistortion", {"drive":0, "drivemix":0.5}, order=2)
fx.add("osc = SelectX.ar(drivemix, [osc, (osc * (drive * 50)).clip(0,0.2).fold2(2)])")
fx.save()

fx = FxList.new("tanh", "tanhDisto", {"tanh":0, "tanhmix":0.5}, order=2)
fx.add("osc = SelectX.ar(tanhmix, [osc, osc + (osc*tanh).tanh.sqrt()])")
fx.save()

fx = FxList.new("dist2", "dist2", {"dist2":0, "dist2mix": 1, "dist2shape": 0.1}, order=2)
fx.add_var("tmp")
fx.add("tmp = Fold.ar(osc, -1*dist2shape,dist2shape)")
fx.add("tmp = (tmp * 16.dbamp * dist2).tanh")
fx.add("tmp = BHiShelf.ar(tmp, 9000, 0.8, -12)")
fx.add("tmp = LPF.ar(tmp, 9000)")
fx.add("osc = SelectX.ar(dist2mix, [osc, tmp])")
fx.save()


fx = FxList.new("fdist", "fdist", {"fdist":0, "fdistfreq":1600}, order=2)
fx.add("osc = LPF.ar(osc, fdistfreq)")
fx.add("osc = (osc * 1.1 * fdist).tanh")
fx.add("osc = LPF.ar(osc, fdistfreq)")
fx.add("osc = (osc * 1.1 * fdist).tanh")
fx.add("osc = LPF.ar(osc, fdistfreq)")
fx.add("osc = (osc * 1.4 * fdist).tanh")
fx.add("osc = LPF.ar(osc, fdistfreq)")
fx.add("osc = (osc * 2 * fdist).tanh")
fx.add("osc = osc*0.2")
fx.save()

fx = FxList.new("fdistc", "fdistc", {"fdistc":0, "fdistcfreq1":1600,"fdistcfreq2":1600,"fdistcfreq3":1600,"fdistcfreq4":1600, "fdistcm1": 1.1, "fdistcm2": 1.1, "fdistcm3": 1.4, "fdistcm4": 2, "fdistcq1": 1, "fdistcq2": 1, "fdistcq3":1, "fdistcq4":1}, order=2)
fx.add("osc = RLPF.ar(osc, fdistcfreq1, fdistcq1)")
fx.add("osc = (osc * fdistcm1 * fdistc).tanh")
fx.add("osc = RLPF.ar(osc, fdistcfreq2, fdistcq2)")
fx.add("osc = (osc * fdistcm2 * fdistc).tanh")
fx.add("osc = RLPF.ar(osc, fdistcfreq3, fdistcq3)")
fx.add("osc = (osc * fdistcm3 * fdistc).tanh")
fx.add("osc = RLPF.ar(osc, fdistcfreq4, fdistcq4)")
fx.add("osc = (osc * fdistcm4 * fdistc).tanh")
fx.save()

#based on Derek Kwan chorus
fx = FxList.new("chorus", "chorus", {"chorus":0, "chorusrate":0.5}, order=2)
fx.add_var("lfos")
fx.add_var("numDelays = 4")
fx.add_var("chrate")
fx.add_var("maxDelayTime")
fx.add_var("minDelayTime")
fx.add("chrate = Select.kr(chorusrate > 0.5, [LinExp.kr(chorusrate, 0.0, 0.5, 0.025, 0.125),LinExp.kr(chorusrate, 0.5, 1.0, 0.125, 2)])")
fx.add("maxDelayTime = LinLin.kr(chorus, 0.0, 1.0, 0.016, 0.052)")
fx.add("minDelayTime = LinLin.kr(chorus, 0.0, 1.0, 0.012, 0.022)")
fx.add("osc = osc * numDelays.reciprocal")
fx.add("lfos = Array.fill(numDelays, {|i| LFPar.kr(chrate * {rrand(0.95, 1.05)},0.9 * i,(maxDelayTime - minDelayTime) * 0.5,(maxDelayTime + minDelayTime) * 0.5,)})")
fx.add("osc = DelayC.ar(osc, (maxDelayTime * 2), lfos).sum")
fx.add("osc = Mix(osc)")
fx.save()

# dub delay based on «Dub Echo» by Bjorn Westergard [sccode https://sccode.org/1-h]
fx = FxList.new('dubd', 'dubdelay', {'dubd': 0, 'dublen': 0.1, 'dubwidth': 0.12, 'dubfeed': 0.8}, order=2)
fx.add_var("dry")
fx.add("dry = osc")
fx.add("osc = osc + Fb({ |feedback| var left, right; var magic = LeakDC.ar(feedback*dubfeed + osc); magic = HPF.ar(magic, 400); magic = LPF.ar(magic, 5000); magic = magic.tanh; #left, right = magic; magic = [DelayC.ar(left, 1, LFNoise2.ar(12).range(0,dubwidth)), DelayC.ar(right, 1, LFNoise2.ar(12).range(dubwidth,0))].reverse;	},dublen)")
fx.add("osc = SelectX.ar(dubd, [dry, osc])")
fx.save()

fx = FxList.new('octafuz', 'octafuz', {'octafuz': 0, 'octamix': 0.5}, order=2)
fx.add_var("dis")
fx.add_var("osc_base")
fx.add("osc_base = osc")
fx.add("dis = [1,1.01,2,2.02,4.5,6.01,7.501]")
fx.add("dis = dis ++ (dis*6)")
fx.add("osc = ((osc * dis*octafuz).sum.distort)")
fx.add("osc = (osc * 1/6)!2")
fx.add("osc = SelectX.ar(octamix, [osc_base, osc])")
fx.save()

fx = FxList.new('tek', 'tek', {'tek': 0, 'tekr':500, 'tekd':8}, order=2)
fx.add_var("osc_low")
fx.add_var("osc_med")
fx.add_var("osc_high")
fx.add_var("osc_base")
fx.add_var("lfo")
fx.add("lfo = SinOsc.ar(0.5, phase: 0, mul: 50, add: 800)")
fx.add("osc = In.ar(bus, 2)")
fx.add("osc_base = osc")
fx.add("osc_low = LPF.ar(osc, lfo) * 1")
fx.add("osc_med = BPF.ar(osc, lfo * 2)")
fx.add("osc_med = osc_med + Ringz.ar(CrossoverDistortion.ar(osc_med, 1, 0.1, 0.4),100, decaytime: 0.15, mul:0.1)")
fx.add("osc_med = LeakDC.ar(osc_med)")
fx.add("osc_high = HPF.ar(osc, 4000 + SinOsc.ar(4, mul: 24))")
fx.add("osc = osc_low + osc_med + osc_high")
fx.add("osc = DFM1.ar(osc, [400, 600], 0.99, tekd, 0) + osc")
fx.add("osc = RHPF.ar(Gammatone.ar(osc, tekr), tekr, mul:2) + osc")
fx.add("osc = SelectX.ar(tek, [osc_base, osc])")
fx.save()


### TIDAL FX ####
fx = FxList.new("krush", "dirt_krush", {"krush":0, "kutoff":15000, "krushmix": 0.5}, order=2)
fx.add_var("signal")
fx.add_var("freq")
fx.add("freq = Select.kr(kutoff > 0, [DC.kr(4000), kutoff])")
fx.add("signal = (osc.squared + (krush * osc)) / (osc.squared + (osc.abs * (krush-1.0)) + 1.0)")
fx.add("signal = RLPF.ar(signal, clip(freq, 20, 10000), 1)")
fx.add("osc = SelectX.ar(krushmix, [osc, signal])")
fx.save()

fx = FxList.new("drop", "waveloss", {"drop":0, "dropof": 100}, order=2)
fx.add("osc = WaveLoss.ar(osc, drop, outof: dropof, mode: 2)")
fx.save()

fx = FxList.new("squiz", "squiz", {"squiz":0}, order=2)
fx.add("osc = Squiz.ar(osc, squiz)")
fx.save()

fx = FxList.new("triode", "triode", {"triode":0}, order=2)
fx.add_var("sc")
fx.add("sc = triode * 10 + 1e-3")
fx.add("osc = (osc * (osc > 0)) + (tanh(osc * sc) / sc * (osc < 0))")
fx.add("osc = LeakDC.ar(osc)*1.2")
fx.save()

#### Need Tweak ##############
fx = FxList.new("octer", "octer", {"octer":0, "octersub": 0, "octersubsub": 0}, order=1)
fx.add_var("oct1")
fx.add_var("oct2")
fx.add_var("oct3")
fx.add_var("sub")
fx.add("oct1 = 2.0 * LeakDC.ar(abs(osc))")
fx.add("sub = LPF.ar(osc, 440)")
fx.add("oct2 = ToggleFF.ar(sub)")
fx.add("oct3 = ToggleFF.ar(oct2)")
fx.add("osc = SelectX.ar(octer, [osc, octer*oct1, DC.ar(0)])")
fx.add("osc = osc + (octersub * oct2 * sub) + (octersubsub * oct3 * sub)")
fx.save()

fx = FxList.new("feed", "feeddelay", {"feed":0.7, "feedfreq": 50}, order=2)
fx.add_var("out")
fx.add("out = osc + Fb({\
		arg feedback;\
		osc = CombN.ar(HPF.ar(feedback*feed, feedfreq) + osc, 0.5, 0.25).tanh;\
	},0.5,0.125)")
fx.save()

# fx = FxList.new("sample_atk", "sample_atk", {"sample_atk":0, "sample_sus":1}, order=2)
# fx.add_var("env")
# fx.add("env = EnvGen.ar(Env.new(levels: [0,1,0], times:[sample_atk, sample_sus], curve: 'lin'))")
# fx.add("osc = osc*env")
# fx.save()

fx = FxList.new("a", "attack", {"a":0, "sus": 1, "ac": 0}, order=2)
fx.doc("attack envelope")
fx.add_var("env")
fx.add("env = EnvGen.ar(Env.new(levels: [0,1,1], times:[a*sus, sus - a*sus], curve:[ac,0]))")
fx.add("osc = osc*env")
fx.save()

fx = FxList.new("r", "releas", {"r":0, "sus": 1, "rc": 0}, order=2)
fx.doc("release envelope")
fx.add_var("env")
fx.add("env = EnvGen.ar(Env.new(levels: [1,0,0], times:[r*sus, sus - r*sus], curve:[rc,0]))")
fx.add("osc = osc*env")
fx.save()


fx = FxList.new('ehpf','envHPF', {'ehpf': 0, 'ehpr': 0.7, 'ehpa':0.001, 'ehps':0.01, 'ehpc':-3, 'sus':1}, order=2)
fx.doc("ehpf")
fx.add_var("env")
fx.add('env = EnvGen.ar(Env.new([0, 1, 1, 0.1], [ehpa*sus, sus-(ehpa*sus)-(ehps*sus), ehps], ehpc))')
fx.add('osc = RHPF.ar(osc, ehpf, ehpr, mul: env)')
fx.save()

fx = FxList.new('elpf','envLPF', {'elpf': 0, 'elpr': 0.7, 'elpa':0.001, 'elps':0.01, 'elpc':-3, 'sus':1}, order=2)
fx.doc("elpf")
fx.add_var("env")
fx.add('env = EnvGen.ar(Env.new([0.01, 1, 1, 0.01], [elpa*sus, sus-(elpa*sus)-(elps*sus), elps], elpc), doneAction:0)')
fx.add('osc = RLPF.ar(osc, LinLin.ar(env, 0,1,0,elpf)+10, elpr, mul: 1)')
fx.save()

fx = FxList.new("position", "trimPos", {"position": 0, "sus": 1}, order=2)
fx.add("osc = osc * EnvGen.ar(Env(levels: [0,0,1], curve: 'step', times: [sus * position, 0]))")
fx.save()

fx = FxList.new("ring", "ring_modulation", {"ring":0, "ringl":500, "ringh":1500}, order=0)
fx.add_var("mod")
fx.add("mod = ring * SinOsc.ar(Clip.kr(XLine.kr(ringl, ringl + ringh), 20, 20000))")
fx.add("osc = ring1(osc, mod)")
fx.save()

fx = FxList.new("shift", "pitchshifter", {"shift":0, "shiftsize": 0.1}, order=1)
fx.add("osc = PitchShift.ar(osc, shiftsize, shift, 0.02, 0.01)")
fx.save()

fx = FxList.new("comp", "comp", {"comp": 0, "comp_down": 1, "comp_up": 0.8}, order=2)
fx.add("osc = Compander.ar(osc, osc, thresh: comp, slopeAbove: comp_down, slopeBelow: comp_up, clampTime: 0.01, relaxTime: 0.01, mul: 1)")
fx.save()

fx = FxList.new("mu", "mimu", {"mu": 0}, order=2)
fx.add("osc = MiMu.ar(osc, mu)")
fx.save()


fx = FxList.new("sidechain", "sidechain", {"sidechain": 0, "sidechain_atk": 0.05, "sidechain_rel": 0.1, "thresh":0.006}, order=2)
fx.add_var("schain")
fx.add("schain = In.ar(sidechain,1)")
fx.add("osc = Compander.ar(osc, schain, thresh: thresh, slopeAbove: 0.1, slopeBelow: 1, clampTime: sidechain_atk, relaxTime: sidechain_rel, mul: 1)")
fx.save()

fx = FxList.new("lofi", "lofi", {"lofi": 0, "lofiwow": 0.5, "lofiamp":0.5}, order=2)
fx.add_var("minWowRate")
fx.add_var("wowRate")
fx.add_var("maxDepth")
fx.add_var("maxLfoDepth")
fx.add_var("depth")
fx.add_var("depthLfoAmount")
fx.add_var("wowMul")
fx.add_var("maxDelay")
fx.add_var("ratio")
fx.add_var("threshold")
fx.add_var("gain")
fx.add("osc = HPF.ar(osc, 25)")
fx.add("ratio = LinExp.kr(lofiamp, 0, 1, 0.15, 0.01)")
fx.add("threshold = LinLin.kr(lofiamp, 0, 1, 0.8, 0.33)")
fx.add("gain = 1/(((1.0-threshold) * ratio) + threshold)")
fx.add("osc = Limiter.ar(Compander.ar(osc, osc, threshold, 1.0, ratio, 0.1, 1, gain), dur: 0.0008)")
fx.add("minWowRate = 0.5")
fx.add("wowRate = LinExp.kr(lofiwow, 0, 1, minWowRate, 4)")
fx.add("maxDepth = 35")
fx.add("maxLfoDepth = 5")
fx.add("depth = LinExp.kr(lofiwow, 0, 1, 1, maxDepth - maxLfoDepth)")
fx.add("depthLfoAmount = LinLin.kr(lofiwow, 0, 1, 1, maxLfoDepth).floor")
fx.add("depth = LFPar.kr(depthLfoAmount * 0.1, mul: depthLfoAmount, add: depth)")
fx.add("wowMul = ((2 ** (depth * 1200.reciprocal)) - 1)/(4 * wowRate)")
fx.add("maxDelay = (((2 ** (maxDepth * 1200.reciprocal)) - 1)/(4 * minWowRate)) * 2.5")
fx.add("osc = DelayC.ar(osc, maxDelay, SinOsc.ar(wowRate, 2, wowMul, wowMul + ControlRate.ir.reciprocal))")
fx.add("osc = ((osc * LinExp.kr(lofiamp, 0, 1, 1, 2.5))).tanh")
fx.add("osc = LPF.ar(osc, LinExp.kr(lofi, 0, 1, 2500, 10000))")
fx.add("osc = HPF.ar(osc, LinExp.kr(lofi, 0, 1, 40, 1690))")
fx.add("osc = MoogFF.ar(osc, LinExp.kr(lofi, 0, 1, 1000, 10000), 0)")
fx.save()

### need the miSCellaneous Quark, install in SC
fx = FxList.new("fold", "wavefold", {"fold": 0, "symetry": 1, "smooth": 0.5}, order=2)
fx.add_var("gain")
fx.add_var("compensationGain")
fx.add_var("envFollower")
fx.add_var("ampgain")
fx.add("compensationGain = max(LinLin.kr(fold, 0, 1, 1, 20) * 0.75, 1).reciprocal")
fx.add("envFollower = EnvFollow.ar((osc * 2).softclip, 0.9999)")
fx.add("ampgain = (compensationGain * (1 - 0.4)) + (envFollower * 0.4)")
fx.add("osc = SmoothFoldS.ar((osc + LinLin.kr(symetry, 0, 1, 1, 0)) * LinLin.kr(fold, 0, 1, 1, 20), smoothAmount: smooth)")
fx.add("osc = LeakDC.ar(osc*ampgain)")
fx.save()

fx = FxList.new('low','L_Equalizer', { 'low': 1, 'lowfreq': 80}, order=2)
fx.doc("Low shelf Equalizer")
fx.add('osc = BLowShelf.ar(osc, freq: lowfreq, db: abs(low).ampdb)')
fx.save()

fx = FxList.new('mid','M_Equalizer', {'mid': 1, 'midfreq': 1000, 'midq': 1}, order=2)
fx.doc("Middle boost Equalizer")
fx.add('osc = BPeakEQ.ar(osc, freq: midfreq, rq: midq.reciprocal, db: abs(mid).ampdb)')
fx.save()

fx = FxList.new('high','H_Equalizer', {'high': 1, 'highfreq': 8000}, order=2)
fx.doc("High shelf Equalizer")
fx.add('osc = BHiShelf.ar(osc, freq: highfreq, db: abs(high).ampdb)')
fx.save()

fx = FxList.new('djf','djFilter', {'djf': 0, 'djfq': 0.3}, order=2)
fx.doc("DJ Filter")
fx.add_var('lpfCutoffFreq')
fx.add_var('hpfCutoffFreq')
fx.add('lpfCutoffFreq = djf.linexp(0, 0.5, 50, 15000)')
fx.add('hpfCutoffFreq = djf.linexp(0.5, 1, 50, 15000)')
fx.add('osc = RHPF.ar(RLPF.ar(osc,lpfCutoffFreq, djfq),hpfCutoffFreq, djfq)')
fx.save()

fx = FxList.new('phaser', 'phaser', {'phaser': 0, 'phaserdepth': 0.5}, order=2)
fx.add_var("delayedSignal")
fx.add("delayedSignal = osc")
fx.add("for(1, 4, {|i| delayedSignal = AllpassL.ar(delayedSignal, 0.01 * 4.reciprocal, LFPar.kr(LinExp.kr(phaser, 0, 1, 0.275, 16), i + 0.5.rand, LinExp.kr(phaserdepth*4.reciprocal, 0, 1, 0.0005, 0.01 * 0.5), LinExp.kr(phaserdepth*4.reciprocal, 0, 1, 0.0005, 0.01 * 0.5)), 0)})")
fx.add("osc = osc + delayedSignal")
fx.save()

fx = FxList.new('ringz','Ringmod', {'ringzfreq': 50, 'ringz': 0.1}, order=2)
fx.doc("Ringmodulation")
fx.add('osc = Ringz.ar(osc, freq: ringzfreq, decaytime: ringz, mul: 0.05)')
fx.save()

fx = FxList.new('resonz','resonz', {'rfreq': 50, 'resonz': 0.1}, order=2)
fx.doc("Resonz")
fx.add('osc = Resonz.ar(osc, freq: rfreq, bwr: resonz)')
fx.save()

fx = FxList.new('room2', 'reverb_stereo', {'room2': 0, 'mix2': 0.2, 'damp2':0.8, 'revatk':0, 'revsus':1}, order=2)
fx.add_var("dry")
fx.add("dry = osc")
fx.add("osc = HPF.ar(osc, 100)")
fx.add("osc = LPF.ar(osc, 10000)")
fx.add("osc = FreeVerb2.ar(osc[0], osc[1], 1, room2, damp2)")
fx.add("osc = osc * EnvGen.ar(Env([0,1,0], [revatk,revsus], curve: 'welch'))")
fx.add("osc = SelectX.ar(mix2, [dry, osc])")
fx.save()

fx = FxList.new('mverb', 'miVerb', {'mverb': 0, 'mverbmix': 0.5, 'mverbdamp':0.8, 'mverbdiff':0.625, 'mverbfreeze': 0}, order=2)
fx.add("osc = MiVerb.ar(osc, time: mverb.clip(0.0,1.0), drywet: mverbmix, damp: mverbdamp, hp: 0.1, freeze: mverbfreeze, diff: mverbdiff, mul:1.5)")
fx.save()

fx = FxList.new('stut', 'stutterfx', {'t_reset': 0, 'stut': 1, 'stutrate':1, 'stutlen':0.02}, order=2)
fx.add_var("dry")
fx.add_var("reset")
fx.add_var("wet")
fx.add("~stutter = { |snd, reset, stutlen, maxdelay = 1| var phase, fragment, del; phase = Sweep.ar(reset); fragment = { |ph| (ph - Delay1.ar(ph)) < 0 + Impulse.ar(0) }.value(phase / stutlen % 1); del = Latch.ar(phase, fragment) + ((stutlen - Sweep.ar(fragment)) * (stutrate - 1)); DelayC.ar(snd, maxdelay, del); }")
fx.add("dry = osc")
fx.add("reset = Onsets.kr(FFT(LocalBuf(1024), osc), t_reset)")
fx.add("wet = ~stutter.(osc, reset, stutlen)")
fx.add("osc = SelectX.ar(stut, [dry, wet], wrap:1)")
fx.save()

fx = FxList.new('sbrk', 'stutbreak', {'sbrk': 0.5, 't_reset': 0, 'sbrkdur': 4, 'sus': 1}, order=2)
fx.add_var("dry")
fx.add_var("reset")
fx.add_var("wet")
fx.add_var("stuti")
fx.add_var("stutlen")
fx.add_var("stutrate")
fx.add("stutrate=Rand(0.01, 1.0)")
fx.add("stutlen=Rand(0.01,0.08)")
fx.add("~stutter = { |snd, reset, stutlen, maxdelay = 1| var phase, fragment, del; phase = Sweep.ar(reset); fragment = { |ph| (ph - Delay1.ar(ph)) < 0 + Impulse.ar(0) }.value(phase / stutlen % 1); del = Latch.ar(phase, fragment) + ((stutlen - Sweep.ar(fragment)) * (stutrate - 1)); DelayC.ar(snd, maxdelay, del); }")
fx.add("dry = osc")
fx.add("stuti = IRand(1,sus*sbrkdur).round(2)")
fx.add("reset = Onsets.kr(FFT(LocalBuf(1024), osc), t_reset)")
fx.add("wet = ~stutter.(osc, reset, stutlen)")
fx.add("wet = wet * LFPulse.kr(stuti/sus, 0.5, mul:1.0)")
fx.add("dry = dry * LFPulse.kr(stuti/sus, mul:1.5)")
fx.add("osc = SelectX.ar(sbrk, [dry, wet], wrap:1)")
fx.save()







fx = FxList.new('clouds','clouds', {'clouds': 0, 'cpos':0.5, 'csize':0.25, 'cdens': 0.4, 'ctex': 0.5, 'cpitch': 0, 'cgain':2, 'cfb': 0, 'cmode': 0}, order=2)
fx.doc("Clouds granulator")
fx.add("osc = MiClouds.ar(osc, pit: cpitch, pos: cpos, size:csize, dens: cdens, tex: ctex, drywet: clouds, in_gain: cgain, fb: cfb, mode:cmode)")
#fx.add("ReplaceOut.ar(bus, osc)")
fx.save()

fx = FxList.new('mring','MiRings', {'mring': 0, 'rstruct':0.1, 'rbright': 0.8, 'rdamp': 0.7, 'rpos': 0, 'rmodel': 1, 'rpoly': 4, 'regg': 0, 'sus':0, 'rsus': 2}, order=2)
fx.doc("Mi Rings resonator")
fx.add_var("dry")
fx.add_var("pitch")
fx.add("pitch = In.kr(bus, 1)")
fx.add("dry = osc")
fx.add("osc = MiRings.ar(in: osc,trig:1,pit: pitch.cpsmidi.clip(1,80),struct: rstruct, bright: rbright, damp: rdamp, pos: rpos, model: rmodel, poly: rpoly, intern_exciter: 1, easteregg: regg, mul: 1)")
fx.add("osc = osc * EnvGen.kr(Env([1,1,0], [sus*rsus, 0.01]), doneAction: 2)")
fx.add("osc = SelectX.ar(mring, [dry, osc], wrap:1)")
fx.save()

fx = FxList.new('panR','panR', {'panR': 1}, order=2)
fx.doc("Pan rear")
fx.add("osc = Pan4.ar(osc, 0, panR)")
fx.save()



fx = FxList.new('vol','volume', {'vol': 1}, order=2)
fx.doc("Volume")
fx.add("osc = osc*vol")
fx.save()


# Fx LOOP
fx = FxList.new('fx1','fx1out', {'fx1': 0, 'lpfx1':22000, 'hpfx1':0, 'fx1mix': 1}, order=2)
fx.doc("FX1 Bus")
fx.add_var("fxsig")
fx.add("fxsig = LPF.ar(osc, lpfx1)")
fx.add("fxsig = HPF.ar(fxsig, hpfx1)")
fx.add("Out.ar(4, Mix.ar(fxsig*fx1))")
fx.add("osc = osc * fx1mix")
fx.save()

fx = FxList.new('fx2','fx2out', {'fx2': 0, 'lpfx2':22000, 'hpfx2':0, 'fx2mix': 1}, order=2)
fx.doc("FX2 Bus")
fx.add_var("fxsig")
fx.add("fxsig = LPF.ar(osc, lpfx2)")
fx.add("fxsig = HPF.ar(fxsig, hpfx2)")
fx.add("Out.ar(5, Mix.ar(fxsig*fx2))")
fx.add("osc = osc * fx2mix")
fx.save()

fx = FxList.new('fx','fxout', {'fx': 0, 'lpfx':22000, 'hpfx':0, "fxout": 6, "fxmix": 1}, order=2)
fx.doc("FX Bus")
fx.add_var("fxsig")
fx.add("fxsig = LPF.ar(osc, lpfx)")
fx.add("fxsig = HPF.ar(fxsig, hpfx)")
fx.add("Out.ar([fxout, fxout+1], Mix.ar(fxsig*fx))")
fx.add("osc = osc * fxmix")
fx.save()

fx = FxList.new('output','output', {'output': 0}, order=2)
fx.doc("Output select Bus")
fx.add("Out.ar(output, osc)")
fx.save()

fx = FxList.new('mon','monitoring', {'mon': 0}, order=2)
fx.doc("Monitoring Bus")
fx.add("Out.ar([mon, mon+1], osc)")
fx.add("osc = osc*0")
fx.save()


###########

Effect.server.setFx(FxList)
