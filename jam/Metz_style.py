Clock.bpm = 70;

c0 >> play("v", dur=1/4, lpf=PGauss(2000, 500), hpf=100, hpr=var([0.5, 0.2], 4),mverb=0.5, mverbdamp=0.4, mverbfreeze=0, mverbdiff=0.8, bpf=(1000, 500), bpr=0.8, mpf=1200,dist2=0.5, dist2mix=linvar([0.2, 1], [4, 2, 8]), dist2shape=12)
c1 >> latoo(dur=1, bits=32, amp=2, fmod=128, crush=128, cut=1/4, mverb=PWhite(0, 0.5), mverbdamp=0.8, mverbfreeze=0, mverbdiff=0.8, hpf=50, bpf=(1000, 500), bpr=0.8, mpf=1200, lpf=(200, 600),dist2=1, dist2mix=1, dist2shape=2).unison(2)

c2 >> pink(dur=1/2, cut=1/4, hpf=1200, hpr=PWhite(0.1,1), leg=8, a=PWhite(0, 0.2), pan=PWhite(-1, 1), amp=PWhite(0, 0.5))
c3 >> play("<q><k>", sample=(3,P[0:5]), delay=(0,(0,[0,0.25])), dur=c0.dur, crush=[0,0,0,PRand(8)], bits=4, lpf=0, hpf=2000)
c4 >> play("v", shift=4, amp=PRand([0, 0.2]), a=1, cut=1, r=0.9, echo=0.25, echomix=0.5, mpf=PWhite(1200, 4800), mpr=0.99, hpr=PWhite(0.05, 0.1),hpf=linvar([1000, 4000], 64))


c4 >> bass(amp=[var([1, 2], [4, 2]), 0, 1, 0, 1, 1, 0, 0], sus=[2, 0, 0, 0, 1/2, 1/2, 0, 0], dur=1/4, leg=var([4, 6, 8, 10], [4]), dist2=0.2).unison(2).sometimes("stutter", dist2=2, mverb=0.5)

c5 >> bass(amp=[1, 0, 1, 0, 1, 1, 0, 0], sus=[2, 0, 0, 0, 1/2, 1/2, 0, 0], dur=1/4, leg=var([4, 6, 8, 10], [4]), dist2=0.4).unison(8)

c0.stop()

c3.shift=0
c2.stop()

c3.mverb=1
c3.dist2=0.2

c5.scale=Scale.minor
c5.dur=1/8

c5.leg=4
c5>>dbass()

c4.dur=4

c4.stop()
c3.stop()
c5.dur=2

~c6 >> play("X...Oo..", dur=1/4, sample=4, lpf=1200, hpf=50)

~c6 >> nylon([2, 4, 4, _, P+[Pvar([1, 2, 1, 2, 4]) , 4, 4, P*[0, 0, 12]]], mverb=0.5, rate=0.5, dur=Pvar([1/2, 1/4, 1/4, 4], 8), oct=PStep(3, var([4, 2], 16), 5), cutoff=0, mpf=0, res=1,scale=Scale.minor, dist2=1).unison(6) + var([0, 0, 7, 3], [4, 4, 2, 2]) + var([0, 12, 3], [16, 8, 8])

c8 >> varsaw(c6.degree, scale=Scale.minor, sus=4, lpf=linvar([3000, 6700], 128), lpr=PWhite(0.2,0.9), blur=2, amp=0.4, dur=var([5,1,1], [6,1,1]), oct=PStep(3,3,4), fx2=1, fx2hpf=300, fx2lpf=7800).unison(3) + var([0, 4, 8], [6, 1, 1])

c6 >> play("X...Oo..", dur=1/4, sample=4, lpf=1200, hpf=50)


c6 >> nylon([2, 4, 4, _, P+[Pvar([1, 2, 1, 2, 4]) , 4, 4, P*[0, 0, 12]]], mverb=0.5, rate=0.5, dur=Pvar([1/2, 1/4, 1/4, 4], 8), oct=PStep(3, var([4, 2], 16), 5), cutoff=0, mpf=0, res=1,scale=Scale.minor, dist2=1).unison(6) + var([0, 0, 7, 3], [4, 4, 2, 2]) + var([0, 12, 3], [16, 8, 8])


c5.dur=1/8
c6 >> dbass(oct=5, lpf=linvar([2000, 3200], 64))


#i2 82
l6.amp=lininf(1, 0, 16)
c6.amp=lininf(1, 0, 16)

c6.stop()
c4.stop()
c5.stop()

Clock.bpm = 82
Root.default = "G#"
i1 >> dbass([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], lpr=0.1, oct=PStep(16, 5, (5, 4)), dur=8, amp=PCoin(1, 0, 0.25), crush=PWhite(0.1, 0.2), mix2=0, bits=0, fmod=4,lpf=4000, mid=4, spf=4, spfslide=4, chop=4, chopwave=1, chopmix=0.4, spfend=12200, hpf=0).every(8, "shuffle").unison(4)
i2 >> varicelle([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], lpr=0.1, oct=PStep(16, 5, (5, 4)), dur=8, amp=PCoin(1, 0, 0.25), crush=PWhite(0.1, 0.2), mix2=0, bits=0, fmod=4, lpf=400, mid=4, high=4, spf=4, spfslide=4, chop=4, chopwave=1, chopmix=0.4, mverb=1, revsus=r2.dur, hpr=0.9, hpf=2000, spfend=12200).every(8, "shuffle").unison(2)

c_all.lpf=lininf(1200, 1, 4)
c_all.stop()

i3 >> pianovel([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 5, (3, 4)), dur=[PDur(1,3), 1/4], echo=var([0.5, 0.25, 0]), amp=var([0, PWhite(0.7, 0.3)] , [8, 24]), crush=4, bits=8, fmod=4, lpf=0, velharl=PWhite(40, 120)).accompany(i1).follow(i1)

i_all.lpf=var([200, 12000], [PRand([1, 5]), 12])
i_all.rate=var([1, linvar([12, 1])], [28, 4])
i_all.shift=var([0,  linvar([PCoin(12, 1, 0.25), PCoin(1, 12, 0.25), 24])], [48, 4])

i4 >> lbass([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 4, (5, 6)), dur=var([ [10, 1, 1, 1, 1, 1/2, 1/2, 1], [1/2, 1/4, 1/4, 1/2, 1, 1/2, 1, 12]]), echo=[0.5, 0.25], echomix=[0.25, 0.5, 0.25], amp=1,octer=0.1, bpf=1200, octersub=0.1, octersubsub=var([0.1, PRand(1,4)], [15, 1]), fmod=0, lpf=0, slide=0.0, low=0, dist2=1).slider().every(4, "shuffle")

i3.stop()
i5 >> lbass(var([i3.degree, (0, -2)]), dur=1/4, oct=7, amp=var([0, 1], [5, 7]), hpf=[400, 1600], crush=0, chop=4, bits=0, fmod=4, lpf=0).slider()

i_all.rate=var([1, PWalk(8, 4, 1)], PRand(16))
i3.stop()
i4.dur=1/2
i5.lpf=100
i4.dur=4
i7.stop()
i4.oct=3
i4.degree=(0, 12)
i4.dist2=1
i4.a=0

i_all.only()

j_all.only()

j0 >> loop("break16", dur=8, dist2=(1), sample=4, amp=[0, 1, 0.5, 1, 1], shift=[0, 1], hpf=100, hpr=0.9).unison(4)
j1 >> glitchbass([0], oct=PStep(4, 5, [6, 3]), dur=[1, 1/2, 1/2, 1, 1/2, 1/2], vib=0.015, leg=12, cut=1/2, bpf=[400, 1200])
j2 >> play("[xBo[B+]]", dur=j1.dur*PRand([1/2, 1, 2]), sample=5, lpf=4480, hpf=60, lpr=0.2, amp=0.8)
j3 >> play("U ", sample=[3, 4, 5], dur=4, formant=0, shape=0.5, hpf=4000, hpr=0.9)

j4 >> lbass(([0, 0, 1, 2, 0, [-1, 3, 7], [2, 3, 7]], 0), sus=(P*[1/2, 1/4, 1], 0.5), scale=Scale.chromatic, dur=var([1/4, 1/2, 1/2, 1/4, 1, 1/2, 1/2, 1]), oct=PStep(11, [5, 5, 6], [4, [6.01, 4.95]]),rate=P*[2, 1, 0.5, 4], formant=var([0, 0.2, 0.1, 2, 0.1, 0.1, 0.1, 4], [7, 3, 4, 2]), dist2=1, mverb=0.1,amp=var([1, 0.5, 1], [3, 4, 1])).unison(2)

j4.dur=1/4
j4.oct=4
j4.lpf=200

j5 >> loop("break8", sample=2, dur=8, lofi=1, fold=1)
j6 >> loop("frica8", dur=8, dist2=1, sample=9, amp=[0, 1, 0.5, 1, 1], shift=[0, 1], hpf=100, hpr=0.1).unison(2)
j7 >> play("[xBo[B+]]", dur=k1.dur*12, sample=3, lpf=4480, lpr=0.2, amp=1)
j4.amp=var([0, 1])

j8 >> play("U ", sample=[3, 4, 5], dur=4, formant=0, shape=0.5)
j5.stop()
j9 >> loop("dub16",dur=16, sample=2, fold=1, amp=[0.5, 0, 0, 0])

j4.lpf=1200
j4.lpr=0.99
j4.dur=1/2

j4.sus=2
j4.chop=[4, 128]
j4.bpf=400
j4 >> bass()
j_all.only()
j4.dur=1/2

e2 >> loop("hiphop8", dur=8, sample=1, dist2=2)
d3 >> faim([18,18,-60,18,18,-60,19,21,13,11], dur=[1, 2/3, 0.0, 1/3, 2/3, 0.0, 1/3, 1.0, 4.0, 0],amp=[1, 1, 0, 1, 1, 0, 1, 1, 1, 1], dist2=0.4)


Clock.bpm = 150;

drop(4, 2, 1)

j_all.hpf=4000
d3.lpf=400

m0 >> bell([-18,-60,-18,-60,-18,-60,-18,-60,([-18, -1], -1)], damp2=0.1, echo=1, a=PWhite(0, 1), sus=PWhite(0, 1), mverb=0.5, lpf=4000, lpr=0.01,dur=P[0.5,4.0].stutter([8, 1]),amp=var([ [1, 0, 1, 0, 1, 0, 1, 0, 1], PRand([0, 0.2])], [4, 12]), vol=0.5).unison(4) + var([0, 2])
m1 >> bell([-1,-18,-60,-18,-60,-18,-60,-18,-60],dur=P[4.0, 0.5].stutter([1, 8]),amp=[1, 1, 0, 1, 0, 1, 0, 1, 0], p1=PWhite(0, 1))
m_all.hpf=2000
d3.mverb=1
d3.oct=4

m1 >> play("..+.", sample=4,a=0.25, amp=4,  rate=0.5, shift2=1, echo=0.25, dur=8, mverb=0.8)
m2 >> play("..2.", sample=PRand(32), delay=2,a=0.25, amp=4,  rate=0.5, shift2=1, echo=0.25, dur=8, mverb=0.8)
m1 >> play("- ", sample=4, lpf=0, fdist=1, fdistfreq=linvar([4000, 12000]), leg=PWhite(20, 400), echo=0.25, echomix=PWhite(0, 1))
m2 >> play("+ ", sample=var([4, 0,], [3, 1]), hpf=(1200, var([0, 1200, 1400, 0, 6400])), mverb=P[PWhite(0, 1)], mverbdiff=var([0, 0.2, 0.5, 0.8]), leg=var([4, 2, 0, 12]), mverbfreeze=[1, 0, 0, 0, 1, 0], mverbdamp=var([0.2, 0.5, 0.8, 1]), echo=var([0.5, 0.25]), cut=0, lpf=linvar([200, 3200], 8), dist2=var([2, 4, 1], 8), low=PxRand([0, 2, 4, 8, 12]), high=var([0, 2, 4, 8, 8]), shift=var([0, 0.2], [28, 4]), mid=PWalk(12, 1, 1), vol=0.3)

m_all.only()

m0.stop()
m1.stop()

m3 >> rsin(P[-60, 14, -60, 9, 14, -60, 14, -60, 14, -60, 9,-60, 4, 9,-60,9,-60,4,9,-60] | P[-60,11,-60,11,-60,11,11,-60,11,-60,6,-60,6,-60,6,6,-60,6,-60] | P[-60,7,-60,2,7,-60,7,-60,2,7,-60,9,-60,4,9,-60,9,-60,4,9,-60] |  P[-60,11,-60,6,11,-60,11,-60,6,11,-60,6,-60,1,6,-60,6,-60,1,6,-60], dur=P[1.0, 1/3, 0.0, 1/3, 1.0, 1/3, 1/3, 1/3, 1/3, 1.0, 1/3, 0.0, 1/3, 1.0, 1/3, 1/3, 0.0, 1/3, 1/3, 0] | P[1, 1/3, 1/3, 1.0, 0.0, 1/3, 1/3, 1/3, 1/3, 1.0,1/3, 1/3, 1.0, 0.0, 1/3, 1/3, 1/3, 1/3, 0]| P[1, 1/3, 0.0, 1/3, 1.0, 1/3, 1/3, 0.0,  1/3, 1/3, 1.0, 1/3, 0.0, 1/3, 1.0, 1/3, 1/3, 0.0, 1/3, 1/3, 0] | P[1, 1/3, 0.0, 1/3, 1.0, 1/3, 1/3, 0.0, 1/3, 1/3, 1.0, 1/3, 0.0, 1/3, 1.0, 1/3, 1/3, 0.0, 1/3, 1/3, 0], amp=P[0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0] | P[0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0] | P[0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0] | P[0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0], lpr=1, vol=0.5, lpf=4000, dist2=[1, 2]).unison(4)

m_all.only()

m_all.stop()

m4 >> bell(linvar([2, [5, 6]], [4, 0]), shape=linvar([0.01, 0.1], [4, 0]), room2=1, damp2=0.5, scale=Scale.chromatic,dur=1/2, sus=var([1, 2], [28, 4]), fmod=var([8, 32], [60, 4]), oct=3).unison(2)
m5 >> bell(linvar([2, [5, 6]], [4, 0]), shape=linvar([0.01, 1], [14, 2]),scale=Scale.chromatic,dur=1/2, sus=var([1/2, 1/4], [28, 4]), fmod=var([8, 64], [60, 4]), oct=3, hpr=0.01, hpf=1000).unison(2)

m6 >> ebass(linvar([2, [5, 6]], [4, 0]), shape=linvar([0.1, 1], [24, 8]),scale=Scale.chromatic,dur=1/4, sus=var([1/2, 1/4], [28, 4]), fmod=var([8, 64], [60, 4]), oct=5).unison(4)
m5 >> ebass(linvar([2, [5, 6]], [4, 0]), shape=linvar([0.01, 1], [14, 2]),scale=Scale.chromatic,dur=1/2, sus=var([1/2, 1/4], [28, 4]), fmod=var([8, 64], [60, 4]), oct=8, hpr=0.01, hpf=1000).unison(2)
m3.stop()

m3.dur=4
m1.stop()
m3.rate=lininf(1, 0.1, 32)
m4.stop()

m4 >> fbass(linvar([2, [5, 6]], [4, 0]), shape=linvar([0.01, 0.1], [4, 0]), room2=1, damp2=0.5, scale=Scale.chromatic,dur=1/2, sus=var([1, 2], [28, 4]), dist2=0.5, fmod=var([8, 32], [60, 4]), oct=6).unison(2)
h2.hpf=4000

h6 >> soprano((h3.degree, 0), dur=PRand(1,8), blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(7,6,5)), drive=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), amplify=1, spin=0, vol=0.5).unison(2)

m3.lpr=lininf(1, 0.1, 64)
m5.lpr=lininf(1, 0.1, 64)

h3.slide=var([0, 1], [28, 4])
h5.slide=var([0, 1], [28, 4])
masterAll("hpf", 400)
m6.oct=4
m6.dist2=0.4
m3.degree=0.5
m5.degree=var([0.5, 2])

m3.oct=(3, 5)
m5.oct=(3, 5)
m6.stop()
m5.dist2=0.5
h2.stop()
m3.dist2=0.25
m5.dist2=0.6
m5.chop=var([0, 1, 1/2], [12, 2, 2])
m5.dur=1/4

Root.default='C'
Scale.default="minor"
Clock.bpm = lininf(68, 170, 128)

l_all.stop()
k_all.stop()

b1 >> faim(var([0, -2, 0.5], 8), formant=var([0, 0.1], [24, 8]), formantmix=PWhite(0, 0.3), oct=(6, 5, [4, 3]) + var([0, 1], [14, 2]) + PwRand([0, 1, 1.25], [30, 1, 1]), rate=linvar([1.2, 0.3], [32]), fmod=linvar([0, 1], [128]), scale=Scale.chromatic, drive=var([0, (0.1, 0)], [12, 4]), dur=1/2, amp=0.3, mverb=0, mverbdamp=[0.2, 1], mverbdiff=[1, 0.4], hpf=linvar([100, 400], 8)).slider().unison(4).every(8, "stutter", slide=2, lpf=linvar([4000, 8000], 16))

b2 >> faim(var([0, -2, 0.5], 8), oct=(4, 5, 6) + var([0, 1], [14, 2]), width=PWhite(0.1, 0.9), rate=linvar([1.2, PWhite(0.3, 8)], [64]), shift=var([0, 1, 1.2], [13, 2, 1]), fmod=linvar([0, PRand(4, 8)], [128]), scale=Scale.chromatic, delay=(0, 0.25, [0.5, 0, 4]), dur=P*[1/2, 1, 1, 1/4, 1/4, 2], amp=1, hpf=100).slider().unison(2).every(8, "stutter", slide=[2, -2], degree=(-12, 12), echo=(0, 0.125), echotime=1, lpf=linvar([1000, 4000], 16))

x_all.only()

b1.rate=lininf(1, 0.1, 32)
b1.mverb=0
b3 >> soprano((b1.degree, 0), dur=PRand(1,8), blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(7,6,5)), drive=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), room=0.5, mix=0.5, amplify=0.5, spin=0).unison(2)
b1.lpr=lininf(1, 0.1, 64)
b1.slide=var([0, 1], [28, 4])
b1.degree=0.5
b7.oct=(3, 5)
b1.dist2=0.5

b_all.only()

b1.oct=4
b1.dist2=lininf(1, 2, 8)

b1.chop=var([0, 1, 1/2], [12, 2, 2])
b2.dur=1/4

b1.dur=lininf(1/2, 1/4, 16)
b1.lpf=linvar([3200, 1600], 128)
b1.amp=0.9

b8 >> dbass(var([0, -2, 0.5], 8), oct=(6, 5) + var([0, 1], [14, 2]), rate=linvar([1.2, 0.3], [64]), scale=Scale.chromatic, dur=1/2, amp=4, hpf=100).slider().unison(2).solo(0)

x1 >> play(PRand("Xx.xx.xx.xx.xx.x"), room2=.3, amp=0.2, mix2=0.43, revatk=0.1, revsus=0.5, sample=[0,7,4], lpf=8120, leg=PRand(0,42), krush=P*[0,4]).sometimes("stutter", PRand(8), rate=PRand(8)).slider(on=0)
x2 >> play(PRand("Xx.xx.xx.xx.xx.x"), amp=0.3, sample=PRand(20), dur=1/4, lpf=0, leg=var([15, 55],[8, 72]), krush=P*[0,4]).sometimes("stutter").slider()
x3 >> play('V ', amp=2, sample=3)

s1 >> dab((0,-2), dur=32,fx1=1, amp=0.9, fx2=1, lpf=PRand(800,8000), fmod=PRand(8).rnd(2), oct=PStep(3,6,5), cut=0).every(4, "rotate").unison(3,0.25,99)
b8 >> fbass(oct=(4,5,6), echo=0, lpf=PRand(800,10800), hpf=40, drive=linvar([0,0.7],[16,0]), dur=PDur(var([8,P*[5,7,6]],[6,2]),8), sus=1/6, vol=1)
v1 >> play("K", amp=[1,0,0,0], dur=1/4, output=8, sample=0, cut=0)
v3 >> play("@", amp=[[0,1,0,0],0,0,0], dur=1/4)
v4 >> play("N", amp=[0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0,  0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0,  0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0,  0,0,0,0, 0,0,0,0, 0,1,0,0, 1,0,0,0], dur=1/4, shape=1, sample=PRand(99)[:12], cut=1, lpf=200, amplify=1)
v5 >> play("[-]", amp=[0,[0,0,0,[0,1]],1,[0,0,0,[0,0,0,1]]], dur=1/4, sample=8, rate=PWhite(-0.5,3), hpf=180, vol=0.8, pan=PWhite(-1,1))
x3 >> play("s", amp=linvar([0.5, 1]), sample=0, dur=1/4, amplify=[0.76, 0.2, 0.4], lpf=PRand(8000,18000), pan=PWhite(-1,1)).human(40,.8)
x4 >> play("c", amp=[[0,1],0,0,0], dur=1/4, shape=PWhite(0.2,2), lpf=P*[200,linvar([40,18200],[32,0])])
x9 >> play("X ", sample=5, lpf=5800, amp=2)

b1.lpf=P*[400, 800, 1000, 500, 4000]

b1.dur=4
b1.sus=4

x4 >> play("X:")

attack("filter")
##### attack@filter.cna:~$ #####
masterAll("lpf", var([0, 4000, 6000, 15000], [24, 4, 2, 2]))
masterAll("hpf", var([0, 20, 30, linvar([3200, 6400], 32)], [24, 4, 2, 2]))
masterAll("cut", var([0, 1, 1/2, linvar([1/4, 1], 32)], [24, 4, 2, 2]))
masterAll("degree", linvar([1, linvar([0, 2],[4, 0])], 8))
masterAll("rate", 2) 
masterAll("dur", P*[1/2, 1, 1, 1/2, 2])
masterAll("reset")

v_all.only()

b_all.dur=8

v6 >> play("I", sample=4, hpf=PRand(2000,8000), rate=PWhite(-1,2), dur=P*[1,1/2], amp=[[0,1],0,0,0], pan=PWhite(-1,1))
v2 >> play("t", amp=[0,0,[0,1],[0,0,0,1]], lpf=P*[200,2000], dur=1/4)
z1 >> play("K", amp=[1,0,0,0], dur=1/4)
z2 >> play("o", amp=[[0,1],0,0,0], lpf=200, dur=1/4)
z3 >> play("-", amp=[0,0,[1,[1,0],1,1],0], dur=1/4, amplify=[0.76, 0.2, 0.4], rate=PWhite(1,4), pan=PWhite(-1,1))
z4 >> play("-ikk", sample=1, amp=[[0,1],0,0,0], dur=1/4, shape=1, lpf=2200, rate=PWhite(1,4), pan=PWhite(-1,1))
z6 >> play("t", hpf=12000, dur=1/4, amp=[1,[0,1],1,[0,1]], sample=2, amplify=PGauss(4, 0.1), echo=0.125, echomix=var([0, 0.125], 4))


Root.default ="C"
Scale.default="minor"
Clock.bpm = linvar([131, 134],[32,0]);


f2 >> pluck(linvar([0, 0.4], [4, 0]),oct=(linvar([6,6.2],[32,0]),5), dur=1/4, sus=linvar([1/8,1/4],[32,0]), vol=0.5).unison(4).human(80,0.5)

x1 >> play("K", amp=[1,0,0,0], dur=1/4)
x2 >> play("--", amp=[0,0,0,[1,1,1,[1,0]]], lpf=200, dur=1/4, pan=linvar([-1, 1], 16))
x5 >> play("o", amp=[[0,1],0,0,0], dur=1/4, sample=2)
x7 >> play("p", hpf=8000, dur=1/4, amp=[0,[0,1],0,[1,0]])
l1 >> play("V ", sample=3, cut=1, output=20)

x3 >> play("x").drummer()
f2.hpf=3000
f2.dur=2


f3 >> varsaw(linvar([1, 2.4], [8, 0]), leg=4,oct=(linvar([6,6.2],[64,0]),5), dur=1/2, sus=linvar([1/8,1/4],[32,0]), lpf=0, vol=0.5).unison(4).human(80,0.5)
Master().cut=0
