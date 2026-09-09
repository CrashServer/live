# intro2026 60
# live2026_aube

#@intro(16)
Clock.bpm = 60
Scale.default = "minor"
Root.default = "G#"
hp >> karp([0,3,5,7,5,3, 6,1,3,6,3,1, 5,0,3,5,3,0, 4,6,1,4,1,6], oct=6, dur=0.5, sus=PRand([0.4,0.6,0.8],6), amp=0.28, cheapverb=0.5, cvdecay=2, pan=sinvar([-0.4,0.4],6)).unison(3)

#@build(32)
ch >> choir([0,5,3,4], oct=4, dur=4, sus=sinvar([4,6],16), amp=sinvar([0,0.22],32), room=0.99, mix=0.95, lpf=linvar([500,2000],64)).unison(3)
tm >> gong([0,rest(0),rest(0),rest(0),5,rest(0),rest(0),rest(0),3,rest(0),rest(0),rest(0),4,rest(0),rest(0),rest(0)], oct=4, dur=1, sus=sinvar([0.5,1.2],16), amp=sinvar([0.2,0.55],16), room=0.6, mix=0.5)

#@peak(16)
cx >> cs80([(0,3,5),(6,1,3),(5,0,3),(4,6,1)], oct=2, dur=4, sus=5, amp=sinvar([0.12,0.32],32), cutoff=sinvar([1000,3500],24), vibspeed=3.5, vibdepth=0.012, room=0.9, mix=0.8)
vc >> viola([0,-2,3,2,0,5,3,4], oct=5, dur=var([2,1,1,1,2,1,1,2],[2,1,1,1,2,1,1,2]), sus=var([1.8,0.8,0.8,0.8,1.8,0.8,0.8,1.8],[2,1,1,1,2,1,1,2]), amp=sinvar([0.15,0.35],24), room=0.9, mix=0.8, vibrato=sinvar([0,0.25],16))
br >> brass2([0,3,5,7,5,3,7,5, 0,3,5,7,9,7,5,3], oct=5, dur=var([1,0.5,0.5,1,0.5,0.5,1,2],[1,1,1,1,1,1,1,1]), sus=var([0.85,0.4,0.4,0.85,0.4,0.4,0.85,1.8],[1,1,1,1,1,1,1,1]), amp=sinvar([0.3,0.6],16), bright=0.75, growl=sinvar([0.1,0.45],16), vibrate=4.5, vibdepth=0.018, room=0.6, mix=0.5)

#@break(8)
hp.stop()
~oj >> brass2([0,6,5,6], oct=4, dur=1, sus=0.88, amp=1, room=0.0, mix=0.0, pan=-1, fbdelay=0.5, velhard=0.5, a=0.5, velocity=32, cut=1/2)

#@drop(4)
sw >> swell([(0,3,5),(6,1,3),(5,0,3),(4,6,1)], oct=5, dur=4, sus=5, amp=sinvar([0.1,0.4],32), rate=0.3, wide=0.6)

#@outro(4)
pt >> pianovel([0,3,5,7,5,3,7,5], oct=(3, 5), cut=1/2, delay=(0, 0.5), dur=var([1,1,1,0.5,1,1,2,2],[1,1,1,1,1,1,1,2]), sus=var([0.8,0.8,0.8,0.4,0.8,0.8,1.5,1.5],[1,1,1,1,1,1,1,2]), amp=1, velhard=0.2, velocity=32, pan=sinvar([-0.2,0.2],16))

#@part7(4)
pt >> pianovel([0,3,5,7,5,3,7,5], oct=(3, 5), cut=1/2, delay=(0, 0.5), dur=var([1,1,1,0.5,1,1,2,2],[1,1,1,1,1,1,1,2]), sus=var([0.8,0.8,0.8,0.4,0.8,0.8,1.5,1.5],[1,1,1,1,1,1,1,2]), amp=1, velhard=0.2, velocity=32, pan=sinvar([-0.2,0.2],16))

#@part8(16)
br >> brass2([0,3,5,7,5,3,7,5, 0,3,5,7,9,7,5,3], oct=4, dur=var([1,0.5,0.5,1,0.5,0.5,1,2],[1,1,1,1,1,1,1,1]), sus=var([0.85,0.4,0.4,0.85,0.4,0.4,0.85,1.8],[1,1,1,1,1,1,1,1]), amp=sinvar([0.3,0.6],16), bright=0.75, growl=sinvar([0.1,0.45],16), vibrate=4.5, vibdepth=0.018, room=0.6, mix=0.5)
ch.stop()
tm.stop()

#@part9(16)
Clock.bpm = 60
Scale.default = "minor"
Root.default = "C#"

#@part10(16)
Clock.bpm = 60
Scale.default = "minor"
Root.default = "G#"

#@part11(8)
cx.degree=0
cx.dur=1/2
vc.oct=3
cx.only()
cx >> cs80([(0,3,5),(6,1,3),(5,0,3),(4,6,1)], oct=2, dur=1/2, sus=1, amp=sinvar([0.12,0.32],32), cutoff=sinvar([1000,3500],24), vibspeed=3.5,  vibdepth=0.012, room=0.9, mix=0.8, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1)

#@part12(16)
cx >> cs80([(0,3,5),(6,1,3),(5,0,3),(4,6,1)], oct=3, dur=1/2, sus=1, amp=sinvar([0.12,0.32],32), cutoff=sinvar([1000,3500],24), vibspeed=3.5,  vibdepth=0.012, room=0.9, mix=0.8, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1)

#@part13(16)
attack("Connection 48")
a = 32
b = expinf(0, 0.5, a * 2)
i3 >> sos(dur=PRand(16), vib=PRand(10600), lpf=linvar([60,4800],[PRand(8,24), PRand(32,48)]), hpf=expvar([0,500],[PRand(64,96), PRand(8,32)]),fx1=b, fx2=b, output=4, shift=lininf(1, 2, a)).unison(3,0.75,99)

#@part14(8)
cx.chop=4

#@part15(16)
cx.amp=0.2
cx.amp=0.1

#@part16(8)
g1 >> play("g...", sample=0, vol=0.8, lpf=PWhite(200,8000), room=0.2, mix=PWhite(0.2,0.9), shape=(0,0.2), dur=2, output=6)
g2 >> play("g...", delay=4, echo=0.25, amp=0.2, sample=0, lpf=PWhite(200,8000), room2=1, mix2=PWhite(0.2,0.9), shape=(0,0.2), dur=2, output=6)
z4 >> play("E ", dur=16, sample=PRand(200), amp=2, output=22)
x2 >> play("x.-x..", echo=0.5, dur=1/2, shape=.4, rate=1, octafuz=linvar([0.3,1]), formant=var([1, 0,5]), fdist=1, output=10).every(3, "stutter")
g1 >> play("g...", sample=0, vol=0.8, lpf=PWhite(200,8000), room=0.2, mix=PWhite(0.2,0.9), shape=(0,0.2), dur=2, output=6)

#@part17(16)
g1 >> play("g...", sample=0, vol=0.8, lpf=PWhite(200,8000), room=0.2, mix=PWhite(0.2,0.9), shape=(0,0.2), dur=2, output=6)
~g1 >> play("g...", sample=0, vol=0.8, lpf=PWhite(200,8000), room=0.2, mix=PWhite(0.2,0.9), shape=(0,0.2), dur=2, output=6)
e1 >> play("g...", sample=0, vol=0.8, lpf=PWhite(200,8000), room=0.2, mix=PWhite(0.2,0.9), shape=(0,0.2), dur=2, output=6)
e2 >> play("g...", delay=4, echo=0.25, amp=0.2, sample=0, lpf=PWhite(200,8000), room2=1, mix2=PWhite(0.2,0.9), shape=(0,0.2), dur=2, output=6)
e4 >> play("E ", dur=16, sample=PRand(200), amp=2, output=22)
e2 >> play("x.-x..", echo=0.5, dur=1/2, shape=.4, rate=1, octafuz=linvar([0.3,1]), formant=var([1, 0,5]), fdist=1, output=10).every(3, "stutter")

#@part18(8)
i5 >> bbass(0, oct=(lininf(2, 3, a), lininf(2, 4, a)), output=18, dur=1/4, shape=0, shapemix=0.2, med=0, sus=1, blur=1, amp=1, fx1=b, fx2=b, vol=0.4).unison(3)

#@part19(16)
cx.stop()

#@part20(4)
Clock.bpm = 70;

#@part21(16)
i3.stop()
e1.stop()
e2.stop()

#@part22(4)
e4.stop()

#@part23(16)
c0 >> play("v", dur=1/2, lpf=PGauss(2000, 200), hpf=100, hpr=var([0.5, 0.2], 4),mverb=0.5, mverbdamp=0.1, mverbdiff=0.8, bpf=(3000, 2500), bpr=0.8, dist2=0.5, dist2mix=linvar([0.2, 1], [4, 2, 8]), dist2shape=1).only()
c1 >> latoo(dur=1, amp=1, cut=1/4, mverb=PWhite(0, 0.5), mverbdamp=0.8, mverbfreeze=0, mverbdiff=0.8, hpf=50, bpf=(3000,2500), bpr=0.8, mpf=0, lpf=(1000,1500), dist2=1, dist2mix=1, dist2shape=1).unison(2)
c2 >> pink(dur=1/2, cut=1/4, hpf=1200, hpr=PWhite(0.1,1), leg=8, a=PWhite(0, 0.2), pan=PWhite(-1, 1), amp=PWhite(0, 0.5))
~c3 >> play("<q><k>", sample=(3,P[0:5]), delay=(0,(0,[0,0.25])), dur=c0.dur, crush=[0,0,0,PRand(8)], bits=4, lpf=0, hpf=0)
c4 >> bass(amp=[1, 0, 1, 0, 1, 1, 0, 0], sus=[2, 0, 0, 0, 1/2, 1/2, 0, 0], dur=1/4, leg=4, dist2=0.4).unison(3)
c6 >> play("X...Oo..", dur=1/4, sample=4, lpf=1200, hpf=50)

#@part24(8)
c6 >> play("X...Oo..", dur=1/4, sample=4, lpf=1200, hpf=50)

#@part25(8)
~c6 >> nylon([2, 4, 4, _, P+[Pvar([1, 2, 1, 2, 4]) , 4, 4, P*[0, 0, 12]]], mverb=0.5, rate=0.5, dur=Pvar([1/2, 1/4, 1/4, 4], 8), oct=PStep(3, var([4, 2], 16), 5), cutoff=1000, scale=Scale.minor, dist2=1).unison(3) + var([0, 0, 7, 3], [4, 4, 2, 2]) + var([0, PStep(4, 4, 3), 3], [16, 8, 8])

#@part26(8)
c6 >> play("X...Oo..", dur=1/4, sample=4, lpf=1200, hpf=50)
~c6 >> play("X...Oo..", dur=1/4, sample=4, lpf=1200, hpf=50)
c6 >> play("X...Oo..", dur=1/4, sample=4, lpf=1200, hpf=50)
~c6 >> nylon([2, 4, 4, _, P+[Pvar([1, 2, 1, 2, 4]) , 4, 4, P*[0, 0, 12]]], mverb=0.5, rate=0.5, dur=Pvar([1/2, 1/4, 1/4, 4], 8), oct=PStep(3, var([4, 2], 16), 5), cutoff=1000, scale=Scale.minor, dist2=1).unison(3) + var([0, 0, 7, 3], [4, 4, 2, 2]) + var([0, PStep(4, 4, 3), 3], [16, 8, 8])
~c6 >> nylon([2, 4, 4, _, P+[Pvar([1, 2, 1, 2, 4]) , 4, 4, P*[0, 0, 12]]], mverb=0.5, rate=0.5, dur=Pvar([1/2, 1/4, 1/4, 4], 8), oct=PStep(3, var([4, 2], 16), 5), cutoff=1000, scale=Scale.minor, dist2=1).unison(3) + var([0, 0, 7, 3], [4, 4, 2, 2]) + var([0, PStep(4, 4, 3), 3], [16, 8, 8])

#@part27(16)
c6 >> play("X...Oo..", dur=1/4, sample=4, lpf=1200, hpf=50)
~c6 >> nylon([2, 4, 4, _, P+[Pvar([1, 2, 1, 2, 4]) , 4, 4, P*[0, 0, 12]]], mverb=0.5, rate=0.5, dur=Pvar([1/2, 1/4, 1/4, 4], 8), oct=PStep(3, var([4, 2], 16), 5), cutoff=1000, scale=Scale.minor, dist2=1).unison(3) + var([0, 0, 7, 3], [4, 4, 2, 2]) + var([0, PStep(4, 4, 3), 3], [16, 8, 8])
~c6 >> play("X...Oo..", dur=1/4, sample=4, lpf=1200, hpf=50)

#@part28(16)
~c6 >> nylon([2, 4, 4, _, P+[Pvar([1, 2, 1, 2, 4]) , 4, 4, P*[0, 0, 12]]], mverb=0.5, rate=0.5, dur=Pvar([1/2, 1/4, 1/4, 4], 8), oct=PStep(3, var([4, 2], 16), 5), cutoff=1000, scale=Scale.minor, dist2=1).unison(3) + var([0, 0, 7, 3], [4, 4, 2, 2]) + var([0, PStep(4, 4, 3), 3], [16, 8, 8])
