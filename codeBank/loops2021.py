# loops 2021 120
# loops

server.start("tristan")

Scale.default = Scale.minor;
Master().reset()

lapin2 = SynthDef("lapin2")

Master().reset()
Clock.bpm = 120;

server.start("basslinexxx")
server.serverActive=True

a1 >> loop("leadfunk16", dur=16, sample=0)
aa >> loop("leadfunk16", dur=16, sample=1, amp=[0, 1])
ab >> loop("leadfunk16", dur=16, sample=2, amp=[0, 0, 1])
ac >> loop("leadfunk16", dur=16, sample=3, amp=[1, 0, 1, 0])
a2 >> loop("futur16", dur=16, sample=0)
a4 >> loop("leadfunk16", dur=16, sample=1, amp=[0, 1])

a_all.lpf=400

q1 >> loop("futur16", dur=16, sample=0)
q2 >> loop("hiphop16", dur=16, sample=0)
q3 >> loop("intro16", dur=16, sample=0)
q4 >> loop("rvoice16", dur=16, sample=3)

a_all.rate=-1

a7 >> loop("rythm16", dur=16, bpf=400, amp=2)
a8 >> loop("trance16", dur=32, sample=4, bpf=400, amp=1)

b2 >> loop("bass16", dur=16, sample=3, bpf=0, amp=1)
b3 >> loop("bass8", dur=8, sample=1, bpf=0, amp=1)
a6 >> loop("sweep16", dur=16)

a0 >> loop("drum16", dur=16, sample=1, bpf=0, amp=1, chop=4)
b1 >> loop("drum16", dur=16, sample=2, bpf=0, amp=1)

b3 >> loop("bass8", dur=8, sample=6, bpf=0, amp=1)
Master().bpf=[400, 4000, 200, 8000]

x1 >> loop("frica8", dur=8, sample=0, bpf=0, amp=1)
x2 >> loop("frica8", dur=8, sample=2, bpf=0, amp=1)

x2 >> loop("fx16", dur=16, sample=1, bpf=0, amp=0.5)

x4 >> loop("rawbass", dur=16, sample=1).only()

Master().rate=linvar([1, 16], 8)

Master().lpf=0
y1 >> pbass(5, oct=(3,4), dur=8, echo=0.25, echotime=PRand(7,10), shape=0.5, room=1).unison(3)

q6 >> dab([0, 1, [[3, 4], 2]], dur=[4, 3, 1], spf=(400, 4000), spfend=(4000, 2000), spfslide=(1, 4)).penta().unison(4).stop()

Clock.bpm = 112;

# [lapin2 not registered] l0 >> lapin2([VI, I, III], slide=0.01, spf=200, spfend=4000, spfslide=4,  dur=(P[4, 6], 8), sus=6, oct=(PStep(3, 5, [6, 5]), PStep(3, 4, 5)))
q4 >> pads((0,2,4,6), dur=16, amp=1/2, room=1, shape=0, shape=0.2, vib=12, slide=1, slidedelay=0.5, chop=16, delay=0.5)
q5 >> pulse([0,1,0,[1,2],0,[7, 4],3,4], scale=Scale.dorian, lpf=linvar([500,2000],32), lpr=linvar([0.1,1],12), dur=1/2, amp=2*P[1,1,1,1,0,1,1,1], width=linvar([0.1, 0.9])).spread().penta() + var([0,[1,2,3,-1]],[6,2])
q3 >> subbass(((0,2,4,6) + var([0,3],[24,8])) % 7, dur=8, sus=2, echo=0.75, oct=linvar([5, 6], 4), echotime=8, lpf=3000, lpr=0.2, room=0.25).spread()
q1 >> blip([0,1,[[3,[4, 7]],2]], dur=[4,3,1], shape=PWhite(0.2,0.7), oct=PStep(4, 5, [6, 4]), lpf=2000, room=1/2, echo=0.75, echotime=var([4, 6, 8]), sus=1).penta().spread()

q2 >> klank(oct=5, lpf=200, lpr=0.5)

q5.dur=PDur(5, 8)
q5.oct=[5, 6]

q_all.dur=4
q_all.room2=1;
q_all.lpf=400;

q_all.amp=0.2

d4 >> donk((0, 3, 4), beef=1, dur=[1/2, 1/4, 1/4, 1/2], hpr=0.1, hpf=d3.degree * 400, sus=1/4, oct=4, amp=[0.5, 1, 1, 1], shape=0.5).unison(0)
d_all.dur=4

q_all.stop()

l2 >> faim(var([Scale.yu, Scale.minor, Scale.yu], P[0.5, 0.25]), dur=PDur([7, 8, 5], 8), oct=3, glpf=linvar([(400, 8000), (8000, 400)], 128), sus=1/4, hpf=[40, 100, 200, 100, 400, 1200], bpf=0, bpm = Clock.bpm, scale=Scale.minor).every(4, "shuffle").sometimes("stutter", oct=(5, 6, 7), sus=8, echo=[0, 0.25, 0, 0.5], amp=linvar([0, 1])).stop()

# [lapin2 not registered] l1 >> lapin2(var([Scale.yu, Scale.minor, Scale.major], P[0.5, 0.25]), dur=PDur([7, 8, 5], 8), oct=var([PStep(5, (5, 4), (6, 3)), 3], [7, 6]), glpf=linvar([(400, 8000), (8000, 400)], 128), sus=1/4, hpf=[40, 100, 200, 100, 400, 1200], bpf=0, bpm = Clock.bpm, scale=Scale.minor).every(4, "shuffle").sometimes("stutter", oct=(5, 6, 7), sus=8, echo=[0, 0.25, 0, 0.5], amp=linvar([0, 1])).stop())

l4 >> faim((3, 4), dur=[1, 3/4, ])

ue.oct=2

lost()
attack("intervention")

k9 >> play("k.", dur=[4,1/4,1/4,1/2,1,1/2,1], sample=(0,5)).sometimes("stutter", 3)
k0 >> play("d+d", sample=[2,1], dur=PDur(5,8,2)*2, room=PWhite(0.5,1), mix=0.4)
y1.stop()

sw.stop()

# [lapin2 not registered] l1 >> lapin2(var([Scale.yu, Scale.minor, Scale.major], P[0.5, 0.25]), dur=PDur([7, 8, 5], 8), dist=0, oct=var([PStep(5, (5, 4), (6, 3)), 3], [7, 6]), glpf=linvar([(400, 8000), (8000, 400)], 128), sus=1/4, hpf=[40, 100, 200, 100, 400, 1200], bpf=0, bpm = Clock.bpm, scale=Scale.minor).every(4, "shuffle").sometimes("stutter", oct=(5, 7), sus=8, echo=[0, 0.25, 0, 0.5], amp=linvar([0, 1]))
l2 >> faim(var([Scale.yu, Scale.minor, Scale.yu], P[0.5, 0.25]), dur=PDur([7, 8, 5], 8), oct=3, glpf=linvar([(400, 8000), (8000, 400)], 128), sus=1/4, hpf=[40, 100, 200, 100, 400, 1200], bpf=0, bpm = Clock.bpm, scale=Scale.minor).every(4, "shuffle").sometimes("stutter", oct=(5, 6, 7), sus=8, echo=[0, 0.25, 0, 0.5], amp=linvar([0, 1]))

l2 >> faim(Scale.minor, dur=var([1/4, 1/2], [3, 1]), oct=PStep(5, ((5, 6), 5), (6, 3)), glpf=8000, sus=0.1, dist=0, scale=Scale.minor, amp=0.1).every(4, "shuffle")

s0 >> loop("jazzkeys8", dur=4, beat_dur=0, cut=PWhite(0, 1), amp=1)

b1 >> loop("bsbass8", dur=8, sample=1)

s1 >> loop("jazzkeys8", dur=8, sample=5, amp=[0, 0, 0, 1])
s2 >> loop("jazzkeys8", dur=8, sample=4, shape=0.5, delay=5, amp=1)

q_all.stop()

q_all.dur=4
q_all.hpf=400
q_all.amp=[0, 1]

s3 >> loop("jazzkeys8", dur=8, sample=4, amp=1, shift=0)
s4 >> loop("jazzkeys8", dur=8, sample=3, amp=[0, 1])
s5 >> loop("jazzkeys8", dur=8, sample=4, amp=[1, 0])
s6 >> loop("jazzkeys8", dur=8, sample=2, amp=[0, 0, 1])
s7 >> loop("atmo8", dur=8, sample=0, amp=[0, 0, 1, 1])

s3.cut=1/4
s4.cut=1/2
s_all.cut=1/2
b_all.cut=[1/4, 1/2, 1/4]

d4.stop()

##

a8 >> nylon([3, (3, [4, 3])], dur=1/2, oct=(5, (7, linvar([6, 7], 1024))), scale=Scale.chromatic, shape=[0.5, 0.1], lpf=6400, bpf=linvar([200, 2600, 32], [16, 8, 32]), shape=[0, linvar([0, 1], [24, 8])], high=1, mid=linvar([1, 1.1], 32), low=0.1, vol=0.1).unison(8)

g4 >> play(PRand("fff".replace("f", "{o-}")), rate=1, sample=PRand(20), dur=1/4, amp=0.4, lpf=0, leg=200, krush=P*[0,8]).sometimes("stutter").slider()
a4 >> play("<Oo><[Pp.@]>", sample=PRand(8), cut=PRand([1/2, 1/4, 0]), krush=PRand([0, 12]), bits=PRand([2, 12, 0]), crush=(8, 1), amp=1, lpf=PRand([1200, 3200, 15000]), hpf=4000)
a3 >> alva([0, 2, [2, 4]], sus=1/4, amp=PRand([0, 0.5, 1]), dur=[4, 2, 1/4, 3/4, 1], atk=0, oct=(4, 3), crush=(4, 0), bits=4, fmod=32, shape=4).unison(4)

r1 >> organ([3, (3, [4, 3])], scale=Scale.chromatic, dur=1/4, amp=1.4, crush=8, room2=1, mix2=0.2, bits=8, fmod=4, lpf=0).slider()

r1.dur=PDur(5, 8)
g_all.lpf=400
a8.lpf=400

s_all.stop()
g_all.stop()
a8.stop()
a3.stop()

r1.lpf=200

e2 >> play("....-.......1...", dur=0.25, sample=(3, 3), echo=0.5).often("stutter", [3, 12])
e1 >> play("....-.......q...", dur=[0.25, 1/4, 1/4, 1/2, 3], sample=(3, 3), echo=0.5).often("stutter", [3, 12])

# [broken in source] e3 >> play("--&--------------", dur=0.25, sample=(3, 0), cut=1/2, lpf=0, bpr=0.9, bpf=4000, rate=var([ [1/2, 1/4, 1/4, 1/4, 1/2], 1/4]]))

e4 >> play("......====......", dur=0.25, sample=var([2, 4], [7, 1]), hpf=4000)

Clock.bpm = 140

g1 >> play(PRand("Xx.xx.xx.xx.xx.x"), room2=.3, amp=0.2, mix2=0.43, revatk=0.1, revsus=0.5, sample=[0,7,4], lpf=8120, leg=PRand(0,42), krush=P*[0,4]).sometimes("stutter", PRand(8), rate=PRand(8)).slider(on=0)
g2 >> play(PRand("Xx.xx.xx.xx.xx.x"), amp=0.3, sample=PRand(20), dur=1/4, lpf=0, leg=var([15, 55],[8, 72]), krush=P*[0,4]).sometimes("stutter").slider()
g3 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), amp=0.2, cut=PWhite(0.1, 1), sample=PRand(20), dur=1/4, lpf=0, leg=20, krush=P*[0,2]).sometimes("stutter").slider()
a8.lpf=400
a8.hpf=4000
a8.dur=[1/4, 1/2, 1/4]
r1.dur=[1/2, 1/4, 1/4]
r1.shape=1

e_all.stop()
e1 >> play("x.........x.....", dur=0.25, sample=(1,5), amp=1, shape=PCoin(0, 1, 0.1))

r1.lpf=400
r1.stop()

a2 >> play("x", sample=4, dur=PRand([1/4, 1/2]), krush=8, bits=(2, 0), crush=(8, 1), lpf=PRand([1200, PWhite(400, 12000)]), hpf=var([1000, 200, 4000], [2, 14, 2]), amp=0.3, pan=(PWhite(-1, 1), linvar([-1, 1]))).sometimes("stutter", rate=2, echo=0.25).stop()
a9 >> dbass(linvar([12.01, (12, 11.86)], [PRand([1/2, 1/4]), 4]), oct=(3, 4), shape=1, shape=0.1, bpf=(2100, 0),  dur=[1/4, 1/2, 1/4, 1/4]).unison(4)

a8.stop()
im >> loop("bsbass4", dur=4, sample=2, lpf=4000)
es.stop()
uz >> play("<c......cc.c....c><................><....R...R.R.R.RR><................>", dur=0.5, sample=18, rate=[1.59, -0.88, 2.95, 3.05, 3.1, 3.2], feed=0.125)
uz.shape=[0.64, 0.66, 0.37, 0.13, 0.93, 0.82]
uz.shapemix=[0.14, 0.44, 0.83]
uz.stop()
a9.stop()

a9.dur=[1/4, 1/2, 1/4]
a9.amp=[0, 1]

k4 >> play("..=.",dur=4, amp=2, delay=(0, [1.5, 0]))
k5 >> play("X:", lpf=0)

Master().rate=(1, 2)

Master().reset()

d1 >> faim([0, 0, 3, 0], dur=2, amp=[1, 0, 1, 1])

d2 >> faim([0, 0, [3, 4], 0], dur=1/2, amp=[0.5, 1, 1, 1]).unison(4)
d3 >> faim([3, [0, [7, [0, (12, 7)]]], [3, 4], 0], beef=1, dur=[1/2, 1], sus=[1/4, 1/2, 2, 4], oct=PStep([3, 5], 4, [5,6]), amp=[0.5, 1, 1, 1]).unison(4)

d_all.stop()

r1.dur=1/2
r1.oct=(3, 4, 5)
a3.stop()
g4.stop()
a4.stop()
d4.stop()

b1 >> loop("bsbass4", dur=4, sample=2)

Master().bpf=linvar([400, (4000, 2000)], [28, 4])

a5 >> varsaw([0],dur=1/4, amp=PRand([0, 0.5, 0.25]), oct=(4, 5), bits=2, crush=4).every(1, "shuffle").unison(4).stop()

a8 >> nylon([3, (3, [4, 3])], dur=1/2, oct=(5, (7, 6)), scale=Scale.chromatic, shape=[0.5, 0.1], lpf=6400, bpf=linvar([200, 12600, 32], [16, 8, 32]), shape=PTri(0, 1), high=2, mid=4, low=0.1, vol=0.8).unison(8).stop()

a_all.stop()

a8.hpf=400
a8.lpf=400

a5 >> subbass(dur=1/4, oct=(4, 5), amp=1).stop()

Master().reset()

server.start("tooo")

bi >> loop("choir16", dur=32, sample=1)

Master().bpf=0

a_all.stop()
r_all.stop()

es >> loop("tbass4", dur=8, sample=9)
es.lpf=6979

ep >> ssaw(P[1, 0], dur=PDur(8,8), oct=[5, 3, 3, 3, 5]).stop()
ep.lpf=linvar([[6630, 3999, 5063, 1284],[4513, 3189]],[8, 14, 24])

s_all.stop()

tt >> play("<Q......Q...Q....><....u.......u...>", dur=0.25, sample=21, rate=[1.24, 2.12, -0.42, 5.72]).stop()

g1 >> play(PRand("Xx.xx.xx.xx.xx.x"), room2=.3, amp=0.2, mix2=0.43, revatk=0.1, revsus=0.5, sample=[0,7,4], lpf=8120, leg=PRand(0,42), krush=P*[0,4]).sometimes("stutter", PRand(8), rate=PRand(8)).slider(on=0)
g2 >> play(PRand("Xx.xx.xx.xx.xx.x"), amp=0.3, sample=PRand(20), dur=1/4, lpf=0, leg=var([15, 55],[8, 72]), krush=P*[0,4]).sometimes("stutter").slider()

SERVER: aq >> glitcher(P[9, 8, 7], dur=PDur(7,8), oct=[2, 3, 5, 5])
# [broken in source] SERVER: <aq - glitcher>.lpf=linvar([[6748, 6675],[621, 4744, 6199]],[1, 21, 32])

Master().hpf=0

Master().unison(4)

Master().spf=0
Master().lpf=0

dro

Master().cut=var([0, 1/4], [4, 1])
Master().hpf=linvar([400, 1200], 32)

Master().lpf=0
Master().hpf=0
Master().cut=0
Master().bpf=0

k6 >> pianovel(Scale.minor, dur=1/4, oct=(3,2)).stop()

rh >> play(".ATn..2.", dur=PAlt(PEuclid(8, 1), [6, 2], PRhythm((3, 3, 2))), sample=[5,4,8,6,9,7,6,4], rate=[6, 0, 6, 5, 2])

# [broken in source] e1 >> play("x.........x.....", dur=0.25 sample=(1,5), amp=1, shape=PCoin(0, 1, 0.1))
e2 >> play("....u.......u...", dur=0.25, sample=3)
e3 >> play("----------------", dur=0.25, sample=3)
e4 >> play("......====......", dur=0.25, sample=var([2, 4], [7, 1]), hpf=4000)

a9 >> dbass(linvar([12.01, (12, 11.86)], [PRand([1/2, 1/4]), 4]), oct=(3, 4), shape=1, shape=0.1, bpf=(2100, 0),  dur=[1/4, 1/2, 1/4, 1/4]).unison(4).solo(1)

s_all.lpf=400
wr.stop()
rh.stop()
s1.stop()
s2.stop()
s3.stop()
s4.stop()
s5.stop()

a3 >> alva([0, 2, [2, 4]], sus=1/4, amp=PRand([0, 0.5, 1]), dur=[4, 2, 1/4, 3/4, 1], atk=0, oct=(4, 3), crush=(4, 0), bits=4, fmod=32, shape=4).unison(4)

a9.stop()

s_all.lpf=200

tj >> loop("swing8", dur=16, sample=8)
tj.lpf=linvar([[3616, 7208],[6986, 4798, 6543]],[7, 13])
tq >> loop("swing8", dur=16, sample=4)

a9.lpf=400
a3.lpf=400
a3.stop()
yj.hpf=2409
dt.lpf=linvar([[7915, 7228, 4045, 5051],[7429, 7357, 6833, 4002, 7165]],[18, 12])
tj.lpf=linvar([[3616, 7208],[6986, 4798, 6543]],[7, 13])
rx >> loop("dub16", dur=16, sample=6)
dt.degree = PArp(II,6)
rx.pan=PSine(98)

Master().shape=0.2
Master().bpf=[400, 800, 1200]

bi >> virus(P[5, 1, 0.015625, 3, 0.5, 0.015625, 2, 0.5, 0.015625, 6, 0.5, 0.015625, 9, 0.5, 0.015625, 5, 0.5, 0.015625, 3, 1.5], dur=PDur(7,8), oct=[3, 2]).stop()
uh >> dbass(P[1, 9, 0.25, 9, 6, 0.25, 1, 7, 0.25, 9, 9, 0.25, 1, 6, 0.25, 9, 7, 0.25, 1, 9], dur=PDur(3,8), oct=[5, 3]).stop()
uh.lpf=7961

# [broken in source] uh - dbass>.degree = PArp(VI,44)

eh >> bounce(P[6, 6, 6, 6, 6, 6, 6, 6], dur=PDur(6,8), oct=[5, 2, 4, 4, 5]).stop()
ot >> abass(P[2], dur=PDur(5,8), oct=[3, 3, 2, 2, 4]).stop()
ru >> waves(P[0.5, 0.25, 0.5, 0.25], dur=PStrum(5), oct=[4, 2])

a2 >> sawbass([0, [4, 7], [2, 3]] + var([0, 4], [5, 3]), oct=PStep([12, 20], PStep(3, 5, (4, 5)), (5, 6)), dur=var([1/2, 1/4, 1/4, 1/2, [1/2, 1/4], 1/4, 1/4, 1/4, [1/4, 1/2]], 1/4), fold=0, lpf=4400, amp=[1, 0.5], sus=[1/2, 1/2, 1], scale=Scale.minorPentatonic).stop()
