# acht bitte acht 135
# live

#### A1

Master().reset()

Clock.bpm = 135;
a0 >> loop("cosmic16", dur=16, sample=2, hpf=(300, PRand([400, 300])), room2=1, revsus=18, shift=var([(0.5, 1), 1], [4, 4]), beat_dur=1).unison(2)
a1 >> play("c", dur=4, hpf=8000, leg=4, echotime=4, echo=0.5, echomix=0.25, pan=PWhite(-1, 1))
a2 >> loop("sub4", dur=4, sample=9, amp=PWhite(0.5, 0) + 0.5, shift=(0, 1.01), hpf=0, shape=var([0, 0.1], [3, 1]))
a3 >> play("o ", amp=2, dur=4, sample=2, room2=1, lpf=400, hpf=400, echotime=4, echo=0.25, echomix=0.2)
a4 >> loop("perc8", dur=8, sample=4, amp=1 - a1.amp, hpf=4000, pan=PWhite(-1, 1))
a5 >> loop("berlin4", dur=8, sample=5, hpf=PRand(100, 1000), amp=PWhite(0, 1), room2=1, revsus=4, leg=0)
a6 >> loop("berlin4", dur=8, sample=4, hpf=PRand(100, 1000), amp=PWhite(0, 1), room2=[1, 0], revsus=4)
a7 >> loop("berlin4", dur=8, sample=5, hpf=PRand(100, 1000), amp=PWhite(0, 1), room2=1, revsus=4)
a8 >> loop("futur8", dur=16, sample=3, amp=P[1, 1, 1, 0] / 1.5)
a9 >> loop("berlin4", dur=8, sample=2, echo=var([0, 0.5], [3, 1]), amp=P[0, 0, 0, 1] / 1.5)
#######################################################
b1 >> loop("cosmic16", dur=16, echotime=8, echo=4, sample=3, hpf=40, amp=0.5).unison(4)
b2 >> loop("sweep16", dur=32, echotime=8, echo=4, spf=200, spfend=8000, spfslide=8, sample=0, hpf=40, amp=0.2).unison(4)
b3 >> loop("cosmic16", dur=16, sample=3, amp=0.5, echotime=4, echo=2, shift=PStep(4, 1, 0.5), hpf=400).unison(4)
a2.stop()
b4 >> loop("hiphop8", dur=16, sample=4)
b5 >> loop("atmo8", dur=8, sample=1, amp=[0, 0, 0.7, 0.5] * 2) #
b6 >> play("Pp", dur=PDur(3, 8), sample=2, hpf=PWhite(2000, 4000))
b7 >> loop("atmo32", dur=32, sample=2).unison(2)
b8 >> loop("atmo32", dur=32, sample=1, delay=8, hpf=4000).unison(2)
b9 >> loop("nszap8", sample=1, dur=16)
b0 >> loop("nsbreak16", sample=2, dur=16) #
#########################################################
a_all.sample=3
b_all.sample=1
c1 >> loop("core16", dur=16, sample=1, cut=1, lpf=0)
c2 >> loop("xvermin16", dur=16, sample=2).unison(2)
c3 >> loop("xbassphase16", dur=16, sample=2).unison(2)
#########################################################
d1 >> loop("nspad16", dur=16, sample=1, amp=0.5)
a_all.stop()
b_all.stop()
c_all.lpf=400
##### ###################################################
d2 >> loop("electrodrum32", dur=32, sample=0, lpf=0)
d3 >> loop("break32", dur=32, sample=2, lpf=0)
d4 >> loop("break32", dur=1/4, cut=0.1, sample=PRand(8), pan=PWhite(0.1, 0.5), lpf=0)
d5 >> play("w", dur=4, echo=2, sample=6, amp=1)
#########################################################
e0 >> loop("drum4", dur=4, sample=1, amp=[1, 0])
e1 >> loop("drum4", dur=4, sample=0, amp=[0, 1])
c_all.lpf=0;
Master().hpf=([4000, 2000], 0)
Master().lpf=0

d6 >> loop("ravebass4", dur=8, sample=4)
d7 >> loop("ravebass8", dur=8, sample=5, shape=0.0, amp=0.5, hpf=4000)

d8 >> loop("ravebass8", dur=16, sample=0, shift=PRand(1, 2), room2=0, shape=0, revsus=0, amp=0.5).unison(2)
d9 >> loop("ravebass4", dur=4, sample=0, room2=0.5, shape=0, revsus=4).unison(2)

e5 >> loop("ravebass4", dur=4, sample=0, room2=0.5, shape=0, revsus=8).unison(0).only()
e2 >> play("X:", sample=(5, 4), lpf=(1200, 4000)).sometimes("stutter")
e3 >> loop("nsbass16", dur=16, sample=1, hpf=400)
e4 >> loop("psych32", dur=32, sample=3, lpf=4000)

Master().hpf=lininf(400, 4000, 256)
a1.stop()

c_all.stop()
Master().hpf=0
r_all.stop()
e_all.stop()

m1 >> play("K ", hpf=0)
m2 >> play("--")
m3 >> loop("fill16", dur=16, sample=4, hpf=400, amp=[1, 1, 1, 0])
m4 >> loop("nshits16", dur=16, sample=0, hpf=600, amp=[0, 0, 0, 1])
m5 >> loop("nshits16", dur=16, sample=3, hpf=600, amp=[0, 0, 0, 0, 0, 0, 0, 1])

x1 >> play("x ", dur=8, lpf=400, room2=1, damp2=0, revus=8, shape=0.1, echo=0.05, echotime=8)
x2 >> play("a ", sample=4, shift=(0, 0.5), feed=0.2, tremolo=4, dur=8, delay=4, lpf=1200, room2=1, damp2=0, revus=8, shape=0.1, amp=0.2, spf=400, spfslide=4, spfend=3200, echo=(0.025,0.25), echotime=8)
x3 >> play("p.", dur=1/2, lpf=1400, room2=0.2, damp2=1, sample=0, revus=8, shape=0.1, echo=[0.05, 0.25], echotime=x3.dur).sometimes("stutter", 2, rate=2, amp=1.5, dur=1/4)
x4 >> play("p.", dur=1/4, lpf=linvar([800, 1400], 32), sample=0, room2=0.1, damp2=0, revus=2, shape=0, amp=[0.5, 0.7], echo=[0.05, 0.25], echotime=x3.dur).often("stutter", 2, rate=2, amp=1.5, dur=1/2)
Master().lpf=400
r_all.stop()
e_all.stop()
Master().lpf=0
e1.stop()
e3.stop()
a5.stop()

e3 >> loop("fill16", dur=16, sample=4 , lpf=0)
es >> loop("xtbass16", dur=16, sample=0, amp=1)
n1 >> loop("noizebeat8", dur=16, sample=4, amp=[1, 0])
n2 >> loop("noizebeat8", dur=16, sample=3, amp=[0, 1])

x_all.stop()
a4 >> play("<[--]><..U(..[UU])><..o.><.:>", amp=1, sample=4, room2=1, mix2=0.3, revsus=0.5, revatk=-0.3).sometimes("stutter", 4)
k4 >> play("..C.", amp=1)
q5 >> play("V ", sample=2, amp=1)

q1 >> play("x", sample=2, dur=PRand([1/4, 1/2]), krush=8, bits=(2, 0), crush=(8, 1), lpf=PRand([1200, PWhite(400, 12000)]), hpf=var([1000, 200, 4000], [2, 14, 2]), amp=0.5, pan=(PWhite(-1, 1), linvar([-1, 1]))).sometimes("stutter").stop()

m2.stop()
g2 >> play(PRand("Xx.xx.xx.xx.xx.x"), amp=0.3, sample=PRand(20), dur=1/4, lpf=0, leg=var([15, 55],[8, 72]), krush=P*[0,4]).sometimes("stutter").slider().stop()
e2.stop()
r_all.stop()
e4.stop()
e3.sample=4
c3.stop()
b2.stop()
n0.stop()
n1.stop()

es.lpf=6979

p1 >> pianovel(shape=2).unison(4).stop()

a5 >> loop("grat8", dur=16, sample=1, amp=0.8)
q1 >> loop("grat8", dur=16, sample=1, shift=(1, 3), amp=0.2).unison(4)

q4.cut=1/4

q1 >> play("V ", sample=4, lpf=1200)
q4 >> dbass(dur=1/4, shape=0).unison(4)
a4.stop()

e9 >> play("[--]", sample=4)
a5.lpf=400

l9 >> loop("noizebeat8", dur=8, sample=4, amp=[1, 1, 0, 1])
l8 >> loop("noizebeat8", dur=8, sample=6, amp=[0, 0, 1, 0])

a4 >> play("X ", shape=0.0)
l7 >> loop("noizebeat8", dur=8, sample=5, amp=[0, 0, 0, 1])
l0 >> play("..C.", sample=4, amp=2, room2=linvar([0, 1], 8), feed=0, revsus=linvar([1, 4], 4),hpf=400)

g1 >> play(PRand("Xx.xx.xx.xx.xx.x"), room2=.3, amp=0.2, mix2=0.43, revatk=0.1, revsus=0.5, sample=[0,7,4], lpf=0, leg=PRand(0,42), krush=P*[0,4]).sometimes("stutter", PRand(8), rate=PRand(8)).slider(on=0)

n_all.lpf=400
a_all.lpf=400

a4.stop()
a5.lpf=400
q1.lpf=400
i1 >> play("<Oo><[Pp.@]>", sample=PRand(8), cut=PRand([1/2, 1/4, 0]), krush=PRand([0, 12]), bits=PRand([2, 12, 0]), crush=(8, 1), amp=1, lpf=PRand([1200, 3200, 15000]), hpf=4000)
e_all.stop()
b_all.stop()
a_all.stop()
n_all.stop()

k4 >> loop("ragecrux16", sample=1, dur=16).stop()
l_all.only()
l0.stop()

l_all.lpf=0

m1 >> loop("xtech8", dur=8, lpf=0)
m2 >> loop("xxpiano16", dur=16, sample=2, lpf=lininf(1, 1200, 64))
m3 >> loop("xhop16", dur=32, sample=0, lpf=0)
m4 >> loop("xvermin16", dur=16)

Master().cut=1

Clock.bpm = var([PRand(128) + 40])

Master().lpf=[400, 4000]

Master().hpf=4000

Master().shift=4
Master().flanger=8
Master().tremolo=12

Master().hpf=0
drop(3, 2, 4)

Clock.bpm = 170

i1.stop()
g1.stop()

n1 >> loop("ragedrum16", dur=16, sample=2)

# [broken in source] k4 >>

Master().hpf=2000
Master().lpf=100
Master().leg=4
Master().cut=1/16

v1 >> varsaw((0, Scale.minor, 5), dur=16, spf=400, spfslide=PRand(16), spfend=2000, flanger=(0.1, 0.5), sus=22, delay=(0, 4, 8, 12), slide=(4, 1), oct=PStep(4, [(3, 4), (4, 5, 3), (4, 5, 2)], [3, 5, 6]), feed=0.4, slidedelay=PRand(16), lpf=(4000, 6000)).unison(4)
v1.shift=var([0.5, 1, (0.5, 1)], [1, 1, 1])

Master().hpf=0

j1 >> pianovel([III, I, II, IV], dur=PRand([2, 4, 6]), echo=0.25, flanger=0, velhard=var([1, PRand(100)], [32, 4]), delay=(0, 0.25, 0.5, 1, 2), velocity=PWhite(10,50), slide=0, oct=PStep(4, [(3, 4), (5, 6, 7), (4, 7, 2)], [4, 5, 6]), root=var([0,7]), amp=PWhite(0, 1)).unison(0).solo(1)
j0 >> pianovel(P[0:10], dur=PRand([2, 4, 6]), echo=5, velhard=var([1, PRand(100)], [32, 4]), delay=(0, 0.25, 0.5, 1, 2), velocity=PWhite(10,50), slide=0, oct=PStep(4, [(3, 4), (5, 6, 7), (4, 7, 2)], [4, 5, 6]), root=var([0,7]), amp=PWhite(0, 0.5)).unison(0)
v3 >> pianovel([VI, VI, IV, II], dur=var([ PDur(3, 8), 2], [3, 1]) * P[4, 1, 2] * P[1, 2, 4], flanger=0, root=j1.root, velhard=0.1, velocity=PWhite(1, 120), delay=(0, 0.25, 0.5, 1, 2), slide=0, oct=PStep(4, [(3, 4), (4, 5, 3), (4, 5, 2)], [4, 5, 6]), amp=PWhite(0, 0.5)).unison(0)
v2 >> pianovel([0, Scale.minor, Scale.minorPentatonic[:4]] , root=j1.root, hpf=var([400, 1200]), dur=var([ PDur(3, 8), 2], [3, 1] * 2), velocity=PWhite(10, 110), flanger=0, velhard=0.1, delay=(0, 0.25, 0.5, 1, 2), slide=0, oct=PStep(4, [(3, 4), (4, 5, 4), (4, 5, 2)], [3, 5, 6]), amp=var([PWhite(0, 0.3), 0], [5, 3])).unison(0)
v4 >> pianovel(PRand([V, III, VII]), dur=var([ 2, 2, 1, 1, 1/4, 1/4, 1/4, 1/4, 1/4], [3, 1]), rooot=j1.root, velhard=1, delay=(0, 0.25, 0.5, 1, 2), velocity=PWhite(10,50), slide=0, oct=PStep(4, [(3, 4), (5, 6, 7), (4, 7, 2)], [4, 5, 6]), amp=PWhite(0, 1)).unison(0)
v5 >> pianovel(PRand([V, III, VII]), dur=var([ 2, 2, 1, 1, 1/4, 1/4, 1/4, 1/4, 1/4], [3, 1]), rooot=j1.root, velhard=1, delay=(0, 0.25, 0.5, 1, 2), velocity=PWhite(10,50), slide=0, oct=PStep(4, [(3, 4), (5, 6, 7), (4, 7, 2)], [4, 5, 6]), amp=PWhite(0, 1)).unison(0)

v8 >> faim(Scale.minor,amp=0.5, dur=1/4, oct=((6, 7), 4)).stop()

wobble = SynthDef("wobble")

v_all.root=0

a5 >> subbass(dur=4, sus=8, oct=(3, 6), amp=1).stop()

z1 >> wobble([(-2, P[0, -2, 4] * P[6, 1, 1]), -2.01], hpf=0,oct=(PStep(5, 3, 4),5), lpf=[0, linvar([4000, 1000], 32)], dur=var([1/2, [1/4, 1/2]], [7, 1]), sus=a1.dur + PWhite(0.01, 0.05), wflo=Pvar([4, 1], [12, 16]) * P[2, 1/2, 1/4, 4], wfhi=Pvar([0, 1], [3, 4]) * P[1, 1/2, 2], wfmax=PWhite(400, 12000), wet=linvar([0, 2], [12, 4]), iphase=var([0.5, 1, 4], [3, 1]), amp=0.1).unison(2).only() + var([0, 3], [12, 4]) + var([0, 4, 3], [24, 4, 4])

q4 >> varsaw((0,2,4,6), dur=16, amp=1/2, room2=1, shape=0, shape=0.1, vib=12, slide=1, slidedelay=0.5, chop=16, delay=0.5)

z2 >> faim([(-2, P[0, -2, 4] * P[6, 1, 1]), -2.01], oct=(PStep(5, 4, 5),6), lpf=[0, linvar([400, 16000], 32)], dur=var([1/2, 1/4], [7, 1]), sus=a1.dur + PWhite(0.01, 0.2), amp=1, beef=1).unison(2) + var([0, 3], [12, 4]) + var([0, 6, 5], [24, 4, 4])
g9 >> dbass(linvar([12.01, (12, 11.86)], [PRand([1/2, 1/4]), 4]), oct=(3, 4), shape=0, shape=0.1, bpf=(2100, 0),  dur=[1/4, 1/2, 1/4, 1/4], lpf=0).unison(4)
o2 >> alva([0, 2, [2, 4]], sus=1/4, amp=PRand([0, 0.5, 1]), dur=[4, 2, 1/4, 3/4, 1], atk=0, oct=(4, 3), crush=(4, 0), bits=4, fmod=32, shape=4).unison(4)
i3 >> pbass(P[3,7,4 + P*[1, 2]], amp=P*[0, 0.5, 1], beef=2,dur=P[1, 1/2, 1/4], oct=PStep(3, 5, 4))

r_all.stop()
e_all.stop()
Master().lpf=0

a2.stop()

aster().reset()
Scale.default = Scale.majorPentatonic;
a_all.oct=(5, 4)

q4.stop()

p1 >> ebass(0,dur=1/2, amp=PRand([0, 0.5, 1]), oct=(4, 6), bits=2, crush=4).every(1, "shuffle").unison(4)

# III

o1 >> donk((0, 3, [4, 5]) + var([0, 1], [7, 1]), dur=[1/2, 1/4, 1/4, 1/2], hpr=0.1, hpf=d4.degree * P[400, 100], sus=1/4, oct=4, amp=[0.5, 1, 1, 1], shape=0.5).unison(0)
o2 >> loop("cosmic16", dur=16, rate=(1, 0.5), sample=2, hpf=40).unison(2)
o2.hpf=2000
o2.sample=3
Master().hpf=var([0, linvar([400, 8000], [8]), [7, 1]])
Master().hpf=lininf(200,12000,128)
Master().hpf=0
Master().cut=1/4

Master().cut=0
Master().hpf=0
Master().hpf=0

a4 >> play("..//.", dur=4)
m1 >> play("X ")
m2 >> loop("bass8", dur=8, sample=2, amp=1, lpf=0)

Clock.bpm = lininf(135, 140, 1024)

e_all.stop()

n1 >> loop("basslow8", dur=8, sample=2)

Master().hpf=0

p2 >> faim(var([1,0,-2,-4],4), beef=2, sus=abs(p2.degree), dur=1/2, amp=[1,1,0,1]).sometimes("amp.trim", 3)
n2 >> play("<&&><->", lpf=(200, 8000), sample=PWalk(0, 1, 12))

n3 >> play(PRand("Xx.xx.xx.xx.xx.x"), room2=.3, amp=0.2, mix2=0.43, revatk=0.1, revsus=0.5, sample=[0,7,4], lpf=8120, leg=PRand(0,42), krush=P*[0,4]).sometimes("stutter", PRand(8), rate=PRand(8)).slider(on=0)
n4 >> play(PRand("Xx.xx.xx.xx.xx.x"), amp=0.3, sample=PRand(20), dur=1/4, lpf=0, leg=var([15, 55],[8, 72]), krush=P*[0,4]).sometimes("stutter").slider()
p1 >> faim(([3,4,5,4],7,[9,9,9,10]), dur=4, spin=8, tremolo=4, room=1, amp=2).unison(4)
n5 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), amp=0.2, cut=PWhite(0.1, 1), sample=PRand(20), dur=1/4, lpf=0, leg=20, krush=P*[0,2]).sometimes("stutter").slider()
n5 >> play("x.........x.....", dur=0.25, sample=(1,5), amp=1, shape=PCoin(0, 1, 0.1))
e7 >> varsaw([I, VI],dur=[2, 4, 6], oct=(5, PStep(4, 5, 6)), sus=[4, 6], rate=0.5, lpf=4000, hpf=2000).unison(4)
x9 >> zap([-5, 5, 0], dur=PDur([3,5, 1], 8), oct=PStep(5, 4, 5), delay=2, echo=0.25, shift=0, slide=2).unison(2)
q2 >> klank(oct=5, lpf=200, lpr=0.5)
q3 >> subbass(p1.degree, dur=8, sus=2, echo=0.75, oct=linvar([5, 6], 4), echotime=8, lpf=3000, lpr=0.2, room=0.25).spread()
q5 >> pulse([0,1,0,[1,2],0,4,5,4], lpf=linvar([500,2000],32), lpr=linvar([0.1,1],12), dur=1/2, amp=2*P[1,1,1,1,0,1,1,1]).spread().penta() + var([0,[1,2,3,-1]],[6,2])

n4.stop()

j4 >> play("x", sample=8, dur=PRand([1/4, 1/2]), krush=8, bits=(2, 0), crush=(8, 1), lpf=PRand([1200, PWhite(400, 12000)]), hpf=var([1000, 200, 4000], [2, 14, 2]), amp=0.3, pan=(PWhite(-1, 1), linvar([-1, 1]))).stop()

x4 >> play("W ", sample=2, lpf=0)

drop(1, 1, 1)

Master().lpf=PRand(8000)

Master().cut=1/2

t1 >> fbass(PCoin(8,1) + PSine(64), dur=PDur(5,8), oct=(5,6)).unison(3)

q5.stop()

s1.stop()
c_all.stop()

q1 >> blip([0,1,[[3,4],2]], dur=[4,3,1,2,3,4], shape=PWhite(0.2,0.7), oct=(PStep(6, 7, 5), PStep(4, 4, 6)), lpf=2000, room=1/2, echo=0.75, echotime=var([4, 6, 8]), sus=1).penta().spread().stop()

q5.stop()

l2 >> faim(var([Scale.minorPentatonic, Scale.minor, Scale.major], P[0.5, 0.25]), dur=PDur([7, 8, 5], 8), oct=PStep(3, (4, 5), (5, 4)), glpf=linvar([(400, 8000), (8000, 400)], 128), sus=var([1/2, 1], [3, 1]), hpf=[40, 100, 200, 100, 400, 1200], bpf=0, beef=2, bpm = Clock.bpm, scale=Scale.minor).every(4, "shuffle").sometimes("stutter", oct=(5, 6, 7), sus=8, echo=[0, 0.25, 0, 0.5], amp=linvar([0, 1])).human(0, 0, 0).stop()

# [lapin2 not registered] l0 >> lapin2([VI, I, III], slide=0.01, spf=(PRand([200, 1200]), 0), spfend=1000, spfslide=PRand(32), shape=0,  dur=(P[4, 1, 6], 8), sus=[6, 8, 2], oct=(PStep(3, 5, [6, 5, (5, 6), (6, 7)]), PStep(3, 4, 5)))

l2 >> faim(var([Scale.yu, Scale.minor, Scale.yu], P[0.5, 0.25]), dur=PDur([7, 8, 5], 8), oct=4, glpf=linvar([(400, 8000), (8000, 400)], 128), sus=1/4, hpf=[40, 100, 200, 100, 400, 1200], bpf=0, bpm = Clock.bpm, scale=Scale.minor).every(4, "shuffle").sometimes("stutter", oct=(5, 6, 7), sus=8, echo=[0, 0.25, 0, 0.5], amp=linvar([0, 1])).stop()

l2.stop()

l2 >> faim(Scale.minor, dur=var([1/4, 1/2], [3, 1]), oct=PStep(5, ((5, 6), 5), (6, 3)), glpf=8000, sus=0.1, dist=0, scale=Scale.minor, amp=0.1).every(4, "shuffle").stop()

s0 >> loop("jazzkeys8", dur=4, beat_dur=0, cut=PWhite(0, 1), amp=1).stop()

b1 >> loop("bsbass8", dur=8, sample=1).stop()

dj >> feel(P[0.03125, 0.03125, 0.03125, 0.03125, 0.03125, 0.03125, 0.03125, 0.03125, 0.03125], dur=PDur(5,8), oct=[5, 3, 2, 4]).stop()
dj.lpf=linvar([[629, 3373, 5169, 509],[1288, 706]],[15, 16])

s1 >> loop("jazzkeys8", dur=8, sample=5, amp=[0, 0, 0, 1])
s2 >> loop("jazzkeys8", dur=8, sample=4, shape=0.5, delay=5, amp=1)

ep >> ssaw(P[1, 0], dur=PDur(8,8), oct=[5, 3, 3, 3, 5])
ep.lpf=linvar([[6630, 3999, 5063, 1284],[4513, 3189]],[8, 14, 24])

lapin2=SynthDef("lapin2")

r_all.stop()
n3 >> play("{..o.-.&}", sample=PwRand([4, 1, 2], [8, 1, 1]), room2=1, revsus=1).every(2, "stutter", amp=1, rate=[2, 3, 4]).stop()
n4 >> loop("choir16", dur=16, sample=2).unison(0).stop()
n5 >> loop("sweep16", dur=16, sample=0).unison(0).stop()

b8.sample=2
o_all.stop()
c_all.stop()
s_all.stop()
n_all.stop()
g_all.stop()

n2 >> loop("ravebass4", dur=4, sample=4)

Master().reset()

x_all.stop()

b_all.stop()

d2 >> play("O:", dur=4, delay=2, sample=PRand(8)).stop()
d1 >> loop("dub16", dur=16, amp=2, sample=2).stop()

drop(1, 1, 4)

r3.lpf=400
r3.cut=1/4
r3.stop()
d_all.stop()

Master().hpf=0

m2 >> loop("indus32", dur=64, sample=1)
rh >> play(".ATn..2.", dur=PAlt(PEuclid(8, 1), [6, 2], PRhythm((3, 3, 2))), sample=[5,4,8,6,9,7,6,4], rate=[6, 0, 6, 5, 2])
e1 >> play("x.........x.....", dur=0.25, sample=(1,5), amp=1, shape=PCoin(0, 1, 0.1))
e2 >> play("....u.......u...", dur=0.25, sample=3)
e3 >> play("----------------", dur=0.25, sample=3)
e4 >> play("......====......", dur=0.25, sample=var([2, 4], [7, 1]), hpf=4000)
c5 >> loop("bass8", dur=8, sample=4, amp=1, fdist=1, fdistfreq=1400, shape=(0,PWhite(0, 2))).sometimes("stutter", echo=[2, 2, 2, 1/2,1/2, 1/4, 1/4, 1/2]).stop()
q8 >> nylon([3, (3, [4, 3])], dur=1/2, oct=(5, (7, linvar([6, 7], 1024))), scale=Scale.chromatic, shape=[0.5, 0.1], lpf=6400, bpf=linvar([200, 2600, 32], [16, 8, 32]), shape=[0, linvar([0, 1], [24, 8])], high=1, mid=linvar([1, 1.1], 32), low=0.1, vol=0.1).unison(8)

o9 >> dbass(linvar([12.01, (12, 11.86)], [PRand([1/2, 1/4]), 4]), oct=(3, 4), shape=1, shape=0.1, bpf=(2100, 0),  dur=[1/4, 1/2, 1/4, 1/4]).unison(4).solo(0)

tj >> loop("swing8", dur=16, sample=8)
tj.lpf=linvar([[3616, 7208],[6986, 4798, 6543]],[7, 13])
tq >> loop("swing8", dur=16, sample=4)

a8 >> nylon([3, (3, [4, 3])], dur=1/2, oct=(5, (7, 6)), scale=Scale.chromatic, shape=[0.5, 0.1], lpf=6400, bpf=linvar([200, 12600, 32], [16, 8, 32]), shape=PTri(0, 1), high=2, mid=4, low=0.1, vol=0.8).unison(8)

a5 >> varsaw([0],dur=1/4, amp=PRand([0, 0.5, 0.25]), oct=(4, 5), bits=2, crush=4).every(1, "shuffle").unison(4).stop()
