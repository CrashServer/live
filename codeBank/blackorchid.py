# blackorchid
# dark

# ============================================================
# BLACK ORCHID — Dark Industrial → Acid Jungle Mutation
# 140 BPM — Chromatic → D minor
# Sources: industrialdrone, prodrums-as-melody, acid, rave,
#          faim, viola, breakcore, resonbank drums, ews
# ============================================================

Clock.bpm = 140
Scale.default = "chromatic"
Root.default = "D"

#@intro(32)
# -- Industrial drone bed --
d1 >> industrialdrone([0], dur=16, oct=4, sus=16, cutoff=linvar([300, 900], 32), feedback=0.4, noise=0.15, amp=linvar([0, 0.45], 32))
# -- Darkpad creeps in --
p1 >> darkpad([0, 6], dur=8, oct=4, sus=6, atk=3, rel=3, cutoff=linvar([400, 1400], 32), dark=PWhite(0.5, 0.9), detune=0.04, amp=linvar([0, 0.35], 32), mverb=0.3)

#@build(32)
# -- faim bass growl --
c1 >> faim([0, 1, 6], dur=4, oct=3, beef=1.5, amp=0.7, fshift=linvar([-15, 15], 16), fmix=0.3)
# -- Prodrums as pitched percussion, melodic --
b1 >> prodrums([0, 6, 12, 7], voice=4, dur=PDur(3, 8), layer1_amp=0.6, layer2_amp=0.5, layer3_amp=0.3, body_tone=var([3500, 2800, 4200], [6, 1, 1]), harmonic=1.5, fm_amount=1.7, fm_ratio=0.5, waveform=var([1, 6], 12), texture=11, decay=var([0.4, 0.2], 8), attack=0.1, mid_sat=0.8, amp=0.45, oct=6, pan=PSine(8) * 0.3)
# -- ethpad high shimmer --
p2 >> ethpad([0, 1, 7], dur=8, oct=5, attack=3, release=4, amp=linvar([0, 0.4], 16), mverb=0.2)

#@peak(32)
# -- Scale shift to minor for melodic content --
Scale.default = "minor"
# -- Acid emerges --
a1 >> acidline([0, 0, 3, 0, 5, 0, 0, 3], dur=0.25, cutoff=linvar([400, 2400], 8), res=linvar([0.5, 0.85], 4), drive=2.5, accent=P[0, 0, 1, 0]*0.5, tubedrive=0.4, amp=0.5, oct=4)
# -- Drums: kick with resonbank --
k1 >> play("X", dur=0.5, sample=5, amp=P[0.9, 0.4, 0.6, 0.4], resonbank=0.2, rbfreq=[47, 50, 57, 62], rbdecay=0.5, rbspread=1, dynfuzz=0.1, dfgain=1, dftone=2, lpf=300)
h1 >> play("{---=}", rate=PWhite(1, 3), pan=PWhite(-1, 1), hpf=4000, amp=0.3).sometimes("stutter", PRand(15))
s1 >> play("..o.", sample=5, dur=0.5, amp=0.7, hpf=200)
# -- Industrial drone drops to sub --
d1 >> industrialdrone([0], dur=16, oct=3, sus=16, cutoff=linvar([200, 600], 16), feedback=0.6, noise=0.05, amp=0.3)
# -- prodrums get heavier --
b1 >> prodrums([0, 3, 7, 5, PWalk(8, 1, 1)], voice=4, dur=0.25, layer1_amp=1, layer2_amp=1.2, layer3_amp=0.8, body_tone=linvar([500, 1400], 16), harmonic=0.7, fm_amount=3.1, fm_ratio=var([2, 2.5, 3], 4), waveform=6, texture=10, decay=0.3, mid_sat=1.6, amp=0.6, oct=4)

#@drop(32)
# -- Acid goes wild --
a1 >> acidline(var([P[0, 0, 3, 0, 5, 0, 0, 3], P[0, 3, 5, 7, 10, 7, 5, 3]], [16, 16]), dur=var([0.25, 0.125], [24, 8]), cutoff=expvar([300, 4000], 8), res=linvar([0.4, 0.9], 16), drive=linvar([1.5, 4], 32), accent=var([P[0, 0, 1, 0]*0.5, P[1, 0, 0, 1]*0.6], [12, 4]), tubedrive=linvar([0.2, 0.7], 48), amp=0.6)
# -- ews experimental texture underneath --
e1 >> ews(PTrir(0, 8), dur=2, sus=2, squiz=0.8, rel=0.2, oct=PWhite(2, 3), amp=0.5)
# -- cs80 lead cuts through --
j1 >> cs80([0, 0, 0.5, 3], dur=0.5, oct=(3, PStep(4, 3, 4)), amp=var([0.3, 0.5], [16, 16]), cutoff=linvar([400, 5000], 8), shape=0.1, shimmer=linvar([0, 0.5], 32), shimsize=0.8, shimmix=0.4)
# -- Drums intensify --
k1 >> play("X", dur=0.5, sample=5, amp=P[1, 0.5, 0.7, 0.5], resonbank=0.3, rbfreq=[47, 50, 50, 57, 50, 62, 69], rbdecay=[0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.2], rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.15, dfgain=1.5, dftone=3, lpf=400)
h2 >> play("-", sample=5, dur=0.25, amp=P[0.4, 0.15, 0.3, 0.15], hpf=4000)
d2 >> play("..C.", sample=2, dur=0.5, amp=0.5)
# -- faim gets aggressive --
c1 >> faim(([0, 1, 7], 0), dur=0.5, oct=4, beef=2, amp=0.8, chorus2=1, chorus2rate=0.7, hpf=100, dist2=0.3).often("stutter", oct=P*[4, 4, 5, 6])

#@break(32)
# -- Viola moment: everything strips back --
Clock.bpm = var([140, 135], [16, 16])
d1.stop()
c1.stop()
a1.stop()
k1.stop()
h1.stop()
h2.stop()
s1.stop()
d2.stop()
e1.stop()
j1.stop()
b1.stop()
# -- Viola over darkpad --
v1 >> viola([6, 3, P*[4, 2, 5]], dur=[P*[2, 4, 8], P*[2, 4], P*[8, 12]], beat_dur=1, rate=1, mverb=0.8, blur=2, lpf=PRand(1200, 3000), hpf=300, amp=0.5).unison(2) + (-7, PStep(5, 7, 0))
p1 >> darkpad([0, 1, 6, 7], dur=var([rest(28), 4], [28, 4]), oct=3, amp=0.6, dark=0.7)
p3 >> ethpad([0, 7], dur=8, oct=6, attack=3, release=4, amp=0.35, room=0.9, mix=0.6)
# -- Sparse prodrums, ghostly --
b2 >> prodrums([0, 3, 7, 10, 12, 7], voice=4, dur=PDur(3, 8), layer1_amp=0.4, layer2_amp=0.3, layer3_amp=0.2, body_tone=var([3500, 3000], [6, 2]), harmonic=2.5, fm_amount=1, fm_ratio=4, waveform=var([3, 6], 12), texture=4, decay=0.5, echo=0.5, amp=0.3, oct=(6, 5), pan=PSine(8) * 0.3)

#@peak2(64)
# -- Jungle/rave explosion --
Clock.bpm = 170
Scale.default = "minor"
Root.default = "D"
v1.stop()
p3.stop()
b2.stop()
# -- Breakcore loop --
l1 >> loop("breakcore160_16", dur=8, sample=var(PRand(66), [32, 32]), sbrk=P*[0.5, 1, 1.5], sbrkdur=P*[0.5, 1, 4], sbrkmix=0.5, hpf=200, high=2, drcomp=0.5)
# -- Rave lead --
r1 >> rave(Pvar([var([14, 18], [15, 1]), PSaw(128)*14], [64, 64]), dur=var([0.5, 1], [15, 1]), glide=PWhite(0.0, 2.0), oct=(5, 4, 5), eb=0.25, ebfeed=0.5, ebmix=0.3, ebmode=1, ebwow=0.56, ebflutter=125, ebsat=0.6, hpf=500, high=2, amp=0.7).unison(3)
# -- plaitsX chromatic run —
x1 >> plaitsX([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dur=1/6, oct=5, cutoff=linvar([2000, 8000], 4), amp=var([0, 0.6, 0, 0.8], [16, 8, 8, 32]), leg=0, crush=4)
# -- dbass sub --
b3 >> dbass([0, 0, 0, 3, 0, 0, 5, 0], dur=0.25, oct=5, amp=P[0.8, 0.3, 0.5, 0.6], lpf=1300, envdist=0.8, envdistgain=2, leg=0)
# -- vati counter-melody --
x2 >> vati([11, 10, 9, 8, 7, 4, 3, 0], dur=0.25, oct=6, cutoff=linvar([800, 4000], 8), amp=var([0, 0.8], [24, 8]), leg=0)
# -- Jungle drums --
k2 >> play("X", amp=Pvar([P[1, 0], PTimebin()], [64, 64]), mid=2, sample=4).sometimes("stutter")
h3 >> play("{---=}", rate=PWhite(1, 3), pan=PWhite(-1, 1), amp=0.35).sometimes("stutter", PRand(15))
s2 >> play("..o...o.", dur=0.25, sample=6, high=1, amp=0.8).sometimes("stutter", 4)
# -- darkpad anchor underneath --
p1 >> darkpad([0, 6], dur=8, oct=3, sus=8, dark=0.6, amp=0.3, cheapverb=0.8, cvdecay=8, cvdamp=0.8)

#@outro(32)
# -- Meltdown: everything decays --
Clock.bpm = linvar([170, 140], [32, 0])
r1.stop()
x1.stop()
x2.stop()
l1.stop()
k2.stop()
h3.stop()
s2.stop()
b3.stop()
# -- Brown noise swells --
n1 >> brown(chop=PRand(8), chopwave=PWhite(0, 8), dur=PWhite(0.1, 4), amp=var([0, expvar([0, 2], [6, 0])], [14, 2]), pan=PWhite(-1, 1), spf=40, spfend=PRand(400, 9800), spfslide=2, drive=1, hpf=linvar([3200, 200], [32, 0]))
# -- faim drone returns, low --
c2 >> faim([0, 6, 12, 1, 7], dur=2, oct=3, beef=2, dist2=0.6, amp=linvar([0.8, 0], 32), leg=2, room=0.6, mix=0.4)
# -- pianovel for unexpected beauty --
p4 >> pianovel(var([[0, 3, 7, [10, 12]], [3, 7, 10, [14, 15]], [-2, 2, 5, [10, 12]]], [12, 12, 8]), dur=4, amp=linvar([0.6, 0], 32), oct=(5, 4), sus=3, room=0.4, verb=0.5)
# -- industrialdrone closes the loop --
d1 >> industrialdrone([0], dur=16, oct=4, sus=16, cutoff=linvar([800, 200], 32), feedback=linvar([0.4, 0.1], 32), noise=0.1, amp=linvar([0.4, 0], 32))
p1 >> darkpad([0, 1, 6, 7], dur=var([rest(28), 4], [28, 4]), oct=3, amp=linvar([0.5, 0], 32), dark=0.9)

#@endfade(16)
