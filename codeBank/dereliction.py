# dereliction
a = var(PWhite(2, 4), 4)
b = var(PWhite(2, 4), 4)
c = linvar([a, b], 2)
d = var([a, c, b], [8, 2, 6])
Clock.bpm=90+d*2
Scale.default="minor"
Root.default = d

a1 >> sinepad((PSine(4)|PSine(16)|PSine(32),4), formant=PRand(4), flanger=PWhite(0,0.4), fdecay=PWhite(0,4), drive=0.1, fold=0.2, oct=(3,4,5), dur=8, room=1, mix=0.7, amp=1, chop=1.6, chopwave=PRand(8)).unison(5,0.25)
w2 >> sawbass(PWhite(0,0.3), dur=PDur(var([5,7],[6,2]),8,var(PRand(8),36)), cutoff=PRand(190,1580), oct=(4,5,[6,7]), amp=1)
w3 >> play("k ", sample=0, dur=4, echo=0.5, amp=1, hpf=120).every(4,"stutter").sometimes("amen")
d4 >> play("r r r [rr] r ", amp=[1, 0.8, 1, 0.4] * P[0.5], dur=1/4, rate=PRand(2,7), pan=[-1,0.5,0,-0.5,1], sample=3)
d6 >> play("..u.", lpf=4000, crush=5, room=[0.5,1,0.8], mix=[0,0.2,0.4], sample=0, delay=PWhite(-0.1,0.1)).often("stutter", Cycle([2,4,3,6,5,2]), amp=PWhite(0.5,1.3), rate=PWhite(1,2))
d5 >> play("..g..", sample=16, rate=(1,0.33), dur=1, hpf=1500, hpr=0.1 + PWhite(-0.01, 0.01))
k1 >> play("<X.><..o.><..U(.(...{O.[.O][Oo]}))><..x>", amp=1, sample=0).sometimes("stutter")
h1 >> play("<{[---][--{.-}][-{.-}-][{.-}--]}><(.:)><..+>", hpf=180, lpf=0, amp=1, sample=(3,11,1), pan=PWhite(-1,1), lofi=0).human(40,5)
d3 >> play("..(.z).", shape=0.7, cut=1/2, rate=(1.3,.7), pshift=(linvar([0,12],265),0,-12), delay=0.7, lofi=PWhite(0.3,0.9))
a2 >> bell(a1.degree, formant=(0,PRand(6)), formantmix=0.8, oct=(3,4,5), dur=8, room=1, mix=0.7, amp=1, chop=8, chopwave=PRand(8)).spread() + (0,var([-2,-4,-3,-1],8))
y1 >> pasha(a1.degree, delay=var([0, 0.25],[3, 1]), oct=(4,5), dur=PDur(var([2,3,4,5],[5,1,1,1]),8), amp=1, sus=y1.dur*PWhite(0.5,1.2), echo=var([0.5,[0.125,0.25,0.75]],[6,2])).unison(0).sometimes("unison", cycle=3).slider()
p1 >> play("s ", sample=3, dur=1/8, hpf=expvar([5400, 5600], 32), amp=PWhite(0.8, 1), pan=PWhite(-1,1))
w2.cutoff=P[190,linvar([1580,11800],[64,0], start=now)]
