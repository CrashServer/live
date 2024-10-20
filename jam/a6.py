# jamphex -- only begin is interesting
#aphex between
Master().reset()
Clock.bpm = 170
Root.default = var([3, 8, 4, 11], 4)
Root.default = 6
g1.mix2=0
g1 >> play(PRand("Xx.x{Cxxx}.x{c--}.x-.x[xxx].x"), room2=.3, amp=0.4, mix2=PGauss(0.3, 0.1), revatk=(1-g1.mix2), revsus=(g1.mix2 / 0.5), sample=[0,7,4], lpf=8120, leg=PRand(0,(g1.mix * 10)+1), echo=(0, g1.mix2/4), rate=(1, var([1, linvar([[-1, 4], [4, -1]], 16)])), delay=(0.5, 0),pan=PWhite(-1, 1), echomix=g1.mix2, krush=P*[0,4]).sometimes("stutter", PRand(8), low=[(0, 0.5), 0.0], bpm=var([Clock.bpm, Clock.bpm/0.5], 8), rate=PRand(8)).slider(on=0)
g2 >> play(PRand("{gc.m.5.cc.--.-}"), lpr=g1.mix2, amp=0.4, sample=PRand(20), dur=1/4, lpf=g1.revsus * 1400, leg=var([15, 55],[8, 72]), krush=P*[0,4]).sometimes("stutter").slider()
g2.amp=1
g3 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), amp=0.4, cut=PWhite(0.1, 1), sample=PRand(20), dur=1/4, lpf=0, leg=20, krush=P*[0,2]).sometimes("stutter").slider()
g7 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), rate=PRand(-12, 12), amp=1.4, cut=PWhite(0.5, 1), sample=PRand(20), dur=1/2, lpf=0, leg=10, krush=0).sometimes("stutter").slider()

g_all.rate=124
g_all.rate=1
g_all.rate=1

g4 >> play("h", sample=4, rate=linvar([PRand([1, 2, 4, 8, 16]), 1], PRand([1, 2, 4, 8])), dur=var([PRand([4, 16, 32]), 1/4]), shift=PRand([2, 4, 8]))
g_all.rate=var([1, linvar([12, 1])], [28, 4])

g5 >> play(PRand("fff".replace("f", "{o-}")), rate=1, sample=PRand(20), dur=1/4, amp=0.4, lpf=0, leg=200, krush=P*[0,8]).sometimes("stutter").slider()
g_all.dubd=var([0.2, 0.1, 0.3, 0])

g_all.shift=var([0,  linvar([PCoin(12, 1, 0.25), PCoin(1, 12, 0.25), 24])], [48, 4])
g_all.dur=var([1/4, linvar([PCoin(1, 1/8, 0.25), PCoin(1/8, 1, 0.25)], 16)], [24, 4])

g_all.hpf=1200
g_all.hpf=0
e1 >> play("%", dur=32, rate=-0.25)
g_all.lpr=0.2

g_all.rate=var([1, PWalk(8, 4, 1)], PRand(16))
g_all.dur=var([1/4, 4], PRand(16))

r2 >> rsin([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], lpr=0.1, oct=PStep(16, 5, (5, 4)), dur=8, amp=PCoin(1, 0, 0.25), crush=0, mix2=0, bits=0, fmod=4, lpf=400, mid=4, spf=4, spfslide=4, chop=4, chopwave=1, chopmix=0.4, spfend=12200).every(8, "shuffle").unison(4)
r1 >> rsin([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 4, (3, 4)), dur=[PDur(4,8), 1/2], amp=1, crush=4, bits=8, fmod=4, lpf=0)

Master().lpf=var([200, 12000], [PRand([1, 5]), 12])
g_all.rate=var([1, linvar([12, 1])], [28, 4])
g_all.shift=var([0,  linvar([PCoin(12, 1, 0.25), PCoin(1, 12, 0.25), 24])], [48, 4])
r3 >> rsin([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 3, (4, 5)), dur=[10, 1, 1, 1, 1, 1/2, 1/2, 1], amp=1, fmod=0, lpf=0).slider().every(4, "shuffle")
r4 >> rsin(var([r3.degree, (0, -2)]), dur=4, amp=1, oct=(3, 4), hpf=[400, 1600], crush=0, chop=4, room2=0, mix2=0, bits=0, fmod=4, lpf=0).slider()

g_all.dur=var([1/4, linvar([PCoin(1, 1/8, 0.25), PCoin(1/8, 1, 0.25)], 16)], [24, 4])
g_all.rate=var([1, PWalk(8, 4, 1)], PRand(16))
g_all.dur=var([1/4, 4], PRand(16))
d5 >> play("x", drive=1, octafuz=1, shape=0, cut=1/4, amp=PCoin(0, 1, 0.1), rate=linvar([4, 1/4]))
r_all.mpf=1200
g_all.stop()

k4 >> play("C.c.....cc.....", sample=1, flanger=1)
k5 >> play("[--]", sample=14, amp=PMorse("fzefk"))
a1 >> sawbass([3, (3, [4, 3])], dur=1/2, oct=(4, 3, 5), scale=Scale.chromatic, drive=[0.5, 0.1], lpf=1600, bpf=linvar([200, 1600, 32], [16, 8, 32]), shape=PTri(0, 1), high=1, mid=1, low=0.1, vol=0.8).unison(8)

d4 >> play("x", dur=4, echo=[0, 0.5], amp=2, sample=4, hpf=1200)
d5 >> play("o", dur=4, echo=[0, 0.5], amp=1, sample=3, lpf=1200, hpf=400)

g_all.stop()
rb >> play("<(X...)(v..(.//))(...(.v))(..v.)><(.r)...><-.><.+><...(.(.:))>",dur=1/2, amp=PBern(16), amplify=var([1,0],[14,1]), sample=6,pan=(0,-0.2,(-1,1),PWhite(-1,1),0.3)).human(20,5,0).often("stutter", PRand(16).rnd(2), delay=(0, 0.25), shape=0.2, mid=0, low=1.5, high=4).every(2, "shuffle")
r_all.stop()
Master().lpf=0


r_all.stop()


r_all.degree=[0, -2, -3, -4]
r_all.hpf=1200
g_all.dur=4 
g_all.dur=PDur(7, 8)
g_all.fold=1

e1 >> play("x.........-.....", dur=0.125, sample=(3,5), amp=1, drive=PCoin(0, 1, 0.1)).every(1, "stutter", 1, rate=2, drive=4)
e2 >> play("..o.", dur=[1, 15]).every(1, "stutter")
e3 >> play("W ")
e9 >> play(".@..", dur=1/2)

r_all.degree=([4, 2, 0])
d1 >> play("W ", drive=0, dur=4, bpf=80, bpr=0.9, amp=PMorse("thisiskickistooloud"),vol=0.5, slide=[0, -4], rate=var([1, linvar([1, 0.2], 4)])).unison(4)
d8 >> play("@ ", dur=PDur(1, 15, 4), echo=0.25)
d2 >> brown(dur=8, cut=1/2, room2=0.2, chop=4, damp2=0.2, fold=0.5, lofi=0.5, hpf=4000)
r1 >> ssaw([3, (3, [4, 3])], scale=Scale.chromatic, dur=1/4, amp=1, crush=8, room2=1, mix2=0.2, bits=8, fmod=4, lpf=0).slider()

g_all.stop()
#drop

a1 >> sawbass([3, (3, [4, 3])], dur=1/2, oct=(4, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=[0.5, 0.1], lpf=1600, bpf=linvar([200, 1600, 32], [16, 8, 32]), shape=PTri(0, 1), high=1, mid=4, low=0.1, vol=0.8).unison(2)
r_all.stop()

a2 >> blip(var([(3, (3, 8)),3, PCoin(3, 4, 0.5), linvar([4, var([4.01, 4])]), [var([1, 7]), 4, 4, 4, 4]], [4]), rate=2, oct=(PStep(3, 4, 5), var([3, 4])), scale=Scale.chromatic, dur=[1/2], vol=0.5, fold=0.5, leg=var([0, a1.drive], [3, 1], echo=[0, 0.1], feed=0), sus=[1/4, 1/2], lpf=1200).unison(4)


a1 >> sawbass([3, (3, [4, var([3, 14], [15, 1])])], slide=a1.degree == 15,dur=[1/2, 1/2, 1], oct=(4, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=var([[0.5, 0.1], [4, 5]], [48, 16]), lpf=(1/a1.drive) * 800, bpf=linvar([200, 3200, 32], [16, 8, 32]), shape=PTri(0, 1), high=1, mid=8, low=0.1, vol=0.5, chop=0).unison(8)
g_all.stop()

a3 >> keys([3, (3, [4, var([3, 14], [15, 1])])], slide=a1.degree == 15,dur=[2, 1/2, 1, 1/2], oct=(7, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=0, lpf=0, bpf=linvar([2000, 6200, 32], [16, 8, 32]), shape=0, high=0, mid=0.1, low=0.1, vol=0.8, chop=0).unison(8)
a5 >> play("-", sample=PCoin(0, 1, 0.5), amp=2)

Master().cut=var([0.01, 0], [3, 1])

o1 >> play("V ", sample=(4, 2))
Root.default = lininf(6, 8, 16)

Master().cut=0
a1 >> sawbass([3, (3, [4, 3])], dur=[1/2, 1/2, 1], oct=(4, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=[0.5, 0.1], lpf=1600, bpf=linvar([200, 1600, 32], [16, 8, 32]), shape=PTri(0, 1), high=1, mid=4, low=0.1, vol=0.8).unison(8)

Master().lpf=lininf(12000, 100, 16)


o2 >> play("XxO.Xx(.0).",lpf=0, sample=(3, 4))
o3 >> play("x ", shape=4, amp=2)
a5 >> play("[--]", sample=PCoin(3, 4, 0.5), amp=2, lpf=0, shape=0.1)


a1.dur=[1/4, 1/4, 1/2, 1/2, 1/2, 1/2]

Scale.default = Scale.chromatic
Root.default=0.1
a3.stop()
e_all.rate=var([-0.5, 1], [1, 7])

Master().lpf=400

e_all.rate=1

Master().lpf=0



e8.stop()

j4 >> play("V ")# 78 / UFUZ
Clock.bpm = 78;

k1 >> donk(dur=[1/4, 4], lpf=400, oct=(3, PStep(4, 4, 5)))

k2 >> play("x", amp=k1.dur==1/4, echo=(0.5, 0.75, 1.25), sample=(2, 4, 1, 3), leg=(0, 120, 4, 128), lpr=0.1, lpf=4000)

k3 >> ikea(4,hpf=400, a=0.5, dur=4, delay=1.5, crush=8, crush_=1, bits=4, bits_=1, cut=1/4, hhat=1, dafilter=120).slider()

k3 >> donk([12, 7, 0],dur=[1/2, 1/4], lpf=400, oct=(3, PStep(4, 4, 5))).every(2, "stutter", degree=[4, 2], echo=0.25).stop()

k5 >> donk(P*[4, 12, 0],dur=[1/4, 1/2], lpf=400, oct=(4, PStep(4, 5, 6))).every(2, "stutter", degree=[4, 2], echo=0.25)
k4 >> play("[xx]", amp=k1.dur==1/4, echo=(0.5, 0.75, 1.25), sample=(8, 4, 7, 1), leg=(0, 120, 4, 128), delay=(2, 3), lpr=0.1, lpf=2000)

k4 >> play("[kk]", amp=k1.dur==4, echo=(0.5, 0.75, 1.25), sample=(8, 4, 7, 1), leg=(0, 120, 4, 128), delay=(2, 3), lpr=0.1, lpf=2000)

k2 >> donk(leg=32, echo=(0.5, 1.5, 3), dubd=0.1, a=0.4, dist2=0.8)
k3 >> scatter(P*[12, 8, _, 16, 21, 4, _], bpf=100, amp=0.2, echo=0.25, dur=(5/3, 1/3, 1/2), oct=(6, 4), lpf=400, hpf=200).chroma()
print(SynthDefs)
Clock.bpm = 96;

a1 >> play("{-*.!//#32}", rate=circ5, sample=2, bpf=(ê *10 )+2000, bpr=0.1, dub=0.5, dubd=0.5, mverb=0.6)
b1 >> lbass(var([[-6, [-4, -2,(1, -4)]], (-8, -12)]),dur=([var([1/2, 1, 1], 8), 1, 1/4], 1/2), lpf=à*2100, lpf_=à*1000)
b2 >> fbass(var([[4, [1, 8,(8, 7)]], (-8, -12)]),dur=([var([4, 2, 1/2], 8), 1, 1/4], 1/2), lpf=à*2100, lpf_=à*1000, leg=[12, 24, 12], leg_=200, oct=7, hpr=0.1, hpf=1200)
b3 >> faim(var([[12, [4, 8,(8, 7)]], (-8, -12)]),dur=([var([1/2, 1/1, 1/2], 8), 1, 1/4], 1/2), lpf=à*2100, beef=P*[1200], lpf_=à*1000, leg=[120, 24, 12], leg_=20, shape=é32/4)

#
b5 >> play("K ", amp=2)
b4 >> dbass()
b1 >> dbass()
b4.dur=1/4
b1.dur=1/2
b1.oct=(4, 5, 6)
b3 >> jbass()
b2 >> nylon(oct=5, dur=PDur(5, 12) * 2, lpf=400)
a1.stop()
b4.stop()
q1 >> rsin(dur=4, lpf=200, lpf_=4000, lpf_d=4, shape=1, a=(0.5, [0.1, 0.7]))

b2 >> donk()
b1 >> cluster(hpf=400, hpr=0.1, dur=2.5)
b3 >> cluster(dur=4)

b4 >> play("xxox", sample=(3, (é4*P[6:12]) + 4))
b1.dur=5

b3 >> dbass()
b2 >> donk(dur=1/2, rate=P[è8/4, à/10]).unison(4)
b1 >> fbass((1/4, 1/2, 0), sus=(4, 8), dur=[4, 2], hpr=0.1, mverb=0.5, hpf=100, hpr_=0.5)

v1 >> play("V ")

q1.stop()

b2 >> dab((1/4, 1/2, 0), sus=(4, 8), dur=[1/2, 1], hpr=0.1, mverb=0.5, hpf=ù5 * 400, hpr_=0.1, lpf=(é8 + 1) * PWhite(0, 800), chop=4, lpr=(è/4), vol=0.4)
b1 >> ews(dur=4, oct=(3, 4, 5))
b4 >> play("x:k%", sample=var([4, 3, 2]), dur=1/4)
x4 >> play("<X[--]><..O>", amp=2, sample=8)
b1.amp=0.1
b2.amp=0.3
b_all.oct=5

<
>

q1.stop()
b4 >> superbass(dur=4, echo=0.5, oct=7, hpf=1200, hpr=0.1)
b2 >> lbass(dur=1, oct=6, lpf=1200, dist2=0.6)
b3 >> play('..o.')
b4 >> play("x ", sample=8)
f1 >> faim(dur=1/2, shape=0.0)

x4 >> play("X ")

some intro 

b1 >> bass(dur=[4, 0.5], sus=4, chopmix=0.5, shape=linvar([0.2, 0.4], 32), a=0.01, leg=-12, leg_=0.1, rate=0.25, chop=(132, 200), lpf=(1200, 4000), lpf_=(3200, 200), chopmix_=1, chop_=(128, 32, 4)).sometimes("stutter", shape=0.5, mverb=1, leg=-128)
b2 >> dbass(dur=[1/2, 1, 1/4], sus=1/2,amp=[1, 0.5,2, 0], tanh=0.8,chopmix=0.5, chop=(132, 200))

b_all.only()

b1 >> click(dur=[1/2, 1/4, 1/2, (1/2, 1)], octer=0.6).every(6, "stutter", oct=3, shape=0.5)
b2 >> click(dur=P*[1/2, 1/4, 1/2, (1/2, 1)], oct=4,octer=0.2, tanh=0.3).every(6, "stutter", oct=3, shape=0.5)
b3 >> click([8, _, 4, 4, 2],dur=1/2, oct=(4, 5), shape=0.5).stop()
b4 >> click([8, _, 4, 4, 2],dur=1/4, oct=(4, 5, PStep(5, 4, 6)), shape=0.5).stop()
k1 >> dbass(dur=b1.dur, shape=0.5).unison(4).sometimes("stutter", oct=6, echo=0.5, mverb=1)

b1.dur=1
b2.dur=1/2

b3.dur=4
b4.degree=[8, _, 8, 8, 4, 4, 2, 1, 2, 3]

b1.degree=b4.degree
b2.shape=0

b4 >> dbass()
b3 >> dab()

b5 >> play("xxox")

b1 >> play("k ")

#3

b1 >> click(dur=[1/2, 1/4, 1/2, (1/2, 1)], octer=0.6, lpf=linvar([400, 4000], 32), lpr=0.4).every(6, "stutter", oct=3, shape=0.5)
b2 >> click(dur=P*[1/2, 1/4, 1/2, (1/2, 1)], oct=4,octer=var([0.2, 1.2], [5, 3]), tanh=0.3).every(6, "stutter", oct=3, shape=0.5, hpf=400)
b3 >> click([8, _, 4, 4, 2],dur=Pvar([1/2, 1/4,4]), oct=(4, 5), shape=0.5, mpf=1800, mverb=0.2)
b4 >> click([8, _, 4, 4, 2],dur=var([1/4, 1, 1/2], [5, 3, 2]), oct=(4, 5, PStep(5, 4, PRand([3, 5]))), shape=0.5).sometimes("offadd", 4)

k1 >> dbass(dur=b1.dur, shape=0.4).unison(4).sometimes("stutter", oct=4, echo=0.5, mverb=1)

b1.dur=1
b2.dur=1/2

b3.dur=4
b4.degree=[8, _, 8, 8, 4, 4, 2, 1, 2, 3]

b1.degree=b4.degree
b2.shape=0

b4 >> dbass()
b3 >> dab()

b2.degree=0
b3.degree=[12, 12, 8, _]
b4.degree=[12, 12, 8, _]

b4.degree=[1/2, 0, 4]

b5 >> play("xxox")

b1 >> play("k ")

b_all.oct=2
b_all.dur=var([1/2, 1/4], [18, 6])

e1 >> lapin(dur=4, lpf=1200)

d1 >> play("-.x-", sample=4, shape=1).often("stutter")

d2 >> play("?.O.", sample=4, rate=0.5, a=0.2, shift=1.4, mverb=1, amp=1)

d_all.solo(1)
b_all.oct=4

c1 >> ikea(dur=2, tanh=1, oct=4)

b_all.dur=8

b_all.stop()

c2 >> dbass(dur=1/8, cut=var([1/4, 1/3, 1/2], [5, 2, 1]), amp=[1, 0.75, 0.5, 0.25], shape=0.45, dist2=0.5)

e1.stop()






x5 >> pianovel(6,dur=1/2, oct=6)
Clock.bpm = 96;
a1 >> play("{-*.!//#32}", rate=circ5, sample=2, bpf=(ê *10 )+2000, bpr=0.1, dub=0.5, dubd=0.5, mverb=0.6)
k1 >> donk(dur=[1/4, 4], lpf=400, oct=(3, PStep(4, 4, 5)))
k2 >> play("x", amp=k1.dur==1/4, echo=(0.5, 0.75, 1.25), sample=(2, 4, 1, 3), leg=(0, 120, 4, 128), lpr=0.1, lpf=4000)
a_all.lpf=400
k3 >> ikea(4,hpf=400, a=0.5, dur=4, delay=1.5, crush=8, crush_=1, bits=4, bits_=1, cut=1/4, hhat=1, dafilter=120).slider()
k3 >> pulse([12, 7, 0],dur=P[4, 2, 2, 1, 1/2,1/2, 1/4], hpf=0,lpf=400, oct=(3, PStep(4, 4, 5))).every(2, "stutter", degree=[4, 2], echo=0.25).stop()
k5 >> donk(P*[4, 12, 0],dur=[1/4, 1/2], lpf=400, oct=(4, PStep(4, 5, 6))).every(2, "stutter", degree=[4, 2], echo=0.25)
k4 >> play("[xx]", amp=k1.dur==1/4, echo=(0.5, 0.75, 1.25), sample=(8, 4, 7, 1), leg=(0, 120, 4, 128), delay=(2, 3), lpr=0.1, lpf=2000)

k4 >> play("[kk]", amp=k1.dur==4, echo=(0.5, 0.75, 1.25), sample=(8, 4, 7, 1), leg=(0, 120, 4, 128), delay=(2, 3), lpr=0.1, lpf=2000)

k2 >> donk(leg=32, echo=(0.5, 1.5, 3), dubd=0.1, a=0.4, dist2=0.8)
k3 >> scatter(P*[12, 8, _, 16, 21, 4, _], bpf=100, amp=0.2, echo=0.25, dur=(5/3, 1/3, 1/2), oct=(6, 4), lpf=400, hpf=200).chroma()
print(SynthDefs)
b1 >> ebass(var([[-6, [-4, -2,(1, -4)]], (-8, -12)]),dur=([var([1/2, 1, 1], 8), 1, 1/4], 1/2), lpf=à*2100, lpf_=à*1000)

b2 >> fbass(var([[4, [1, 8,(8, 7)]], (-8, -12)]),dur=([var([4, 2, 1/2], 8), 1, 1/4], 1/2), lpf=à*2100, lpf_=à*1000, leg=[12, 24, 12], leg_=200, oct=7, hpr=0.1, hpf=1200)

b3 >> faim(var([[12, [4, 8,(8, 7)]], (-8, -12)]),dur=([var([1/2, 1/1, 1/2], 8), 1, 1/4], 1/2), lpf=à*2100, beef=P*[1200], lpf_=à*1000, leg=[120, 24, 12], leg_=20, shape=é32/4)

#
b5 >> play("K ", amp=2)
b4 >> dbass()
b1 >> dbass()
b4.dur=1/4
b1.dur=1/2
b1.oct=(4, 5, 6)
b3 >> jbass()
b2 >> nylon()
a1.stop()
b4.stop()
q1 >> rsin(dur=4, lpf=200, lpf_=4000, lpf_d=4, shape=1, a=(0.5, [0.1, 0.7]))

b2 >> donk()
b1 >> cluster(hpf=400, hpr=0.1, dur=2.5)
b3 >> cluster(dur=4)

b4 >> play("xxox", sample=(3, (é4*P[6:12]) + 4))
b1.dur=5

b3 >> dbass()
b2 >> donk(dur=1/2, rate=P[è8/4, à/10]).unison(4)
b1 >> fbass((1/4, 1/2, 0), sus=(4, 8), dur=[4, 2], hpr=0.1, mverb=0.5, hpf=100, hpr_=0.5)

v1 >> play("V ")

b2 >> dab((1/4, 1/2, 0), sus=(4, 8), dur=[1/2, 1], hpr=0.1, mverb=0.5, hpf=ù5 * 400, hpr_=0.1, lpf=(é8 + 1) * PWhite(0, 800), chop=4, lpr=(è/4), vol=0.4)
b1 >> ews(dur=4, oct=(3, 4, 5))
b4 >> play("x:k%", sample=var([4, 3, 2]), dur=1/4)
x4 >> play("<X[--]><..O>", amp=2, sample=8)
b1.amp=0.1
b2.amp=0.3
b_all.oct=5

<
>
q1.stop()
b4 >> superbass(dur=4, echo=0.5, oct=7, hpf=1200, hpr=0.1)
b2 >> lbass(dur=1, oct=6, lpf=1200, dist2=0.6)
b3 >> play('..o.')
b4 >> play("x ", sample=8)
f1 >> faim(dur=1/2, shape=0.0)

x4 >> play("X ")

some intro 
b1 >> bass(dur=[4, 0.5], sus=4, chopmix=0.5, shape=linvar([0.2, 0.4], 32), a=0.01, leg=-12, leg_=0.1, rate=0.25, chop=(132, 200), lpf=(1200, 4000), lpf_=(3200, 200), chopmix_=1, chop_=(128, 32, 4)).sometimes("stutter", shape=0.5, mverb=1, leg=-128)
b2 >> dbass(dur=[1/2, 1, 1/4], sus=1/2,amp=[1, 0.5,2, 0], tanh=0.8,chopmix=0.5, chop=(132, 200))

b_all.only()

b1 >> click(dur=[1/2, 1/4, 1/2, (1/2, 1)], octer=0.6).every(6, "stutter", oct=3, shape=0.5)
b2 >> click(dur=P*[1/2, 1/4, 1/2, (1/2, 1)], oct=4,octer=0.2, tanh=0.3).every(6, "stutter", oct=3, shape=0.5)
b3 >> click([8, _, 4, 4, 2],dur=1/2, oct=(4, 5), shape=0.5).stop()
b4 >> click([8, _, 4, 4, 2],dur=1/4, oct=(4, 5, PStep(5, 4, 6)), shape=0.5).stop()
k1 >> dbass(dur=b1.dur, shape=0.5).unison(4).sometimes("stutter", oct=6, echo=0.5, mverb=1)

b1.dur=1
b2.dur=1/2

b3.dur=4
b4.degree=[8, _, 8, 8, 4, 4, 2, 1, 2, 3]

b1.degree=b4.degree
b2.shape=0

b4 >> dbass()
b3 >> dab()

b5 >> play("xxox")

b1 >> play("k ")

#3

b1 >> click(dur=[1/2, 1/4, 1/2, (1/2, 1)], octer=0.6, lpf=linvar([400, 4000], 32), lpr=0.4).every(6, "stutter", oct=3, shape=0.5)
b2 >> click(dur=P*[1/2, 1/4, 1/2, (1/2, 1)], oct=4,octer=var([0.2, 1.2], [5, 3]), tanh=0.3).every(6, "stutter", oct=3, shape=0.5, hpf=400)
b3 >> click([8, _, 4, 4, 2],dur=Pvar([1/2, 1/4,4]), oct=(4, 5), shape=0.5, mpf=1800, mverb=0.2)
b4 >> click([8, _, 4, 4, 2],dur=var([1/4, 1, 1/2], [5, 3, 2]), oct=(4, 5, PStep(5, 4, PRand([3, 5]))), shape=0.5).sometimes("offadd", 4)

k1 >> dbass(dur=b1.dur, shape=0.4).unison(4).sometimes("stutter", oct=4, echo=0.5, mverb=1)

b1.dur=1
b2.dur=1/2

b3.dur=4
b4.degree=[8, _, 8, 8, 4, 4, 2, 1, 2, 3]

b1.degree=b4.degree
b2.shape=0

b4 >> dbass()
b3 >> dab()

b2.degree=0
b3.degree=[12, 12, 8, _]
b4.degree=[12, 12, 8, _]

b4.degree=[1/2, 0, 4]

b5 >> play("xxox")

b1 >> play("k ")

b_all.oct=2
b_all.dur=var([1/2, 1/4], [18, 6])

e1 >> lapin(dur=4, lpf=1200)

d1 >> play("-.x-", sample=4, shape=1).often("stutter")

d2 >> play("?.O.", sample=4, rate=0.5, a=0.2, shift=1.4, mverb=1, amp=1)

d_all.solo(1)
b_all.oct=4

c1 >> ikea(dur=2, tanh=1, oct=4)

b_all.dur=8

b_all.stop()

c2 >> dbass(dur=1/8, cut=var([1/4, 1/3, 1/2], [5, 2, 1]), amp=[1, 0.75, 0.5, 0.25], shape=0.45, dist2=0.5)

e1.stop()






x5 >> pianovel(6,dur=1/2, oct=6)

Clock.bpm = 170
g1 >> play(PRand("Xx.xx.xx.xx.xx.x"), room2=.3, amp=0.2, mix2=0.43, revatk=0.1, revsus=0.5, sample=[0,7,4], lpf=8120, leg=PRand(0,42), krush=P*[0,4]).sometimes("stutter", PRand(8), rate=PRand(8)).slider(on=0)
g2 >> play(PRand("Xx.xx.xx.xx.xx.x"), amp=0.3, sample=PRand(20), dur=1/4, lpf=0, leg=var([15, 55],[8, 72]), krush=P*[0,4]).sometimes("stutter").slider()
g3 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), amp=0.2, cut=PWhite(0.1, 1), sample=PRand(20), dur=1/4, lpf=0, leg=20, krush=P*[0,2]).sometimes("stutter").slider()
g4 >> play(PRand("fff".replace("f", "{o-}")), rate=1, sample=PRand(20), dur=1/4, amp=0.4, lpf=0, leg=200, krush=P*[0,8]).sometimes("stutter").slider()

g_all.rate=var([1, linvar([12, 1])], [28, 4])
g_all.shift=var([0,  linvar([PCoin(12, 1, 0.25), PCoin(1, 12, 0.25), 24])], [48, 4])
g_all.dur=var([1/4, linvar([PCoin(1, 1/8, 0.25), PCoin(1/8, 1, 0.25)], 16)], [24, 4])

r1 >> organ(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=PDur(4,8), amp=lininf(0, 1, 32), crush=8, room2=1, mix2=0.2, bits=8, fmod=4, lpf=0)

r1 >> organ([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 4, (5, 6)), dur=PDur(4,8), amp=1, crush=8, room2=1, mix2=0.2, bits=8, fmod=4, lpf=0)

r2 >> organ([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 4, (5, 6)), dur=8, amp=1, crush=0, room2=1, mix2=0.5, bits=0, fmod=4, lpf=0).every(8, "shuffle")

r3 >> organ([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 4, (5, 6)), dur=[10, 1, 1, 1, 1, 1/2, 1/2, 1], amp=1, crush=0, room2=0, mix2=0, bits=0, fmod=4, lpf=0).slider().every(4, "shuffle")

r4 >> organ(var([r3.degree, (0, -2)]), dur=4, amp=1, oct=(3, 4), crush=0, chop=4, room2=0, mix2=0, bits=0, fmod=4, lpf=0).slider()

g_all.rate=var([1, PWalk(8, 4, 1)], PRand(16))

g_all.dur=var([1/4, 4], PRand(16))

d5 >> play("x",leg=55, drive=4, cut=1/4, amp=PCoin(0, 1, 0.1), rate=linvar([4, 1/4]))

r6 >> organ(8, drive=4)
r_all.degree=[0, -2, -3, -4]


r_all.hpf=1200
g_all.dur=4
g_all.dur=PDur(7, 8)
g_all.fold=1

r_all.degree=([4, 2, 0])
d1 >> play("W ", drive=0, dur=4, bpf=80, bpr=0.9, amp=PMorse("thisiskickistooloud"),vol=0.5, slide=[0, -4], rate=var([1, linvar([1, 0.2], 4)])).unison(4)
d8 >> play("@ ", dur=PDur(1, 15, 4), echo=0.25)
d2 >> noise(dur=8, cut=1/2, room2=0.2, chop=4, damp2=0.2, fold=0.5, lofi=0.5, hpf=4000)
r1 >> organ([3, (3, [4, 3])], scale=Scale.chromatic, dur=1/4, amp=1, crush=8, room2=1, mix2=0.2, bits=8, fmod=4, lpf=0).slider()
g_all.stop()
#drop

a1 >> sawbass([3, (3, [4, 3])], dur=1/2, oct=(4, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=[0.5, 0.1], lpf=1600, bpf=linvar([200, 1600, 32], [16, 8, 32]), shape=PTri(0, 1), high=1, mid=4, low=0.1, vol=0.8).unison(2)
r_all.stop()
d4 >> play("x", dur=4, echo=[0, 0.5], amp=2, sample=4, hpf=1200)
d5 >> play("o", dur=4, echo=[0, 0.5], amp=1, sample=3, lpf=1200, hpf=400)
a2 >> blip(var([(3, (3, 8)),3, PCoin(3, 4, 0.5), linvar([4, var([4.01, 4])]), [var([1, 7]), 4, 4, 4, 4]], [4]), rate=2, oct=(PStep(3, 4, 5), var([3, 4])), scale=Scale.chromatic, dur=[1/2], vol=0.5, fold=0.5, leg=var([0, a1.drive], [3, 1], echo=[0, 0.1], feed=0), sus=[1/4, 1/2], lpf=1200).unison(4)

e1 >> play("x.........x.....", dur=0.25, sample=(1,5), amp=1, drive=PCoin(0, 1, 0.1))
e2 >> play("....u.......u...", dur=0.25, sample=3)
e3 >> play("----------------", dur=0.25, sample=3)
e4 >> play("......====......", dur=0.25, sample=var([2, 4], [7, 1]), hpf=4000)

e_all.lpf=0

a1 >> sawbass([3, (3, [4, var([3, 14], [15, 1])])], slide=a1.degree == 15,dur=[1/2, 1/2, 1], oct=(4, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=var([[0.5, 0.1], [4, 5]], [48, 16]), lpf=(1/a1.drive) * 800, bpf=linvar([200, 3200, 32], [16, 8, 32]), shape=PTri(0, 1), high=1, mid=8, low=0.1, vol=0.5, chop=0).unison(8)
g_all.stop()

a3 >> keys([3, (3, [4, var([3, 14], [15, 1])])], slide=a1.degree == 15,dur=[2, 1/2, 1, 1/2], oct=(7, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=0, lpf=0, bpf=linvar([2000, 6200, 32], [16, 8, 32]), shape=0, high=0, mid=0.1, low=0.1, vol=0.8, chop=0).unison(8)
a5 >> play("-", sample=PCoin(0, 1, 0.5), amp=2)

Master().cut=var([0.01, 0], [3, 1])

Master().cut=0
a1 >> sawbass([3, (3, [4, 3])], dur=[1/2, 1/2, 1], oct=(4, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=[0.5, 0.1], lpf=1600, bpf=linvar([200, 1600, 32], [16, 8, 32]), shape=PTri(0, 1), high=1, mid=4, low=0.1, vol=0.8).unison(8)

e1 >> play("x.........-.....", dur=0.25, sample=(3,5), amp=1, drive=PCoin(0, 1, 0.1)).every(1, "stutter", 1, rate=2, drive=4)
e6 >> play("x:")

a1 >> sawbass([3, (3, [4, 3])], dur=1/2, oct=5, scale=Scale.chromatic, drive=[0.5, 0.1], lpf=1600, bpf=linvar([200, 1600, 32], [16, 8, 32]), shape=PTri(0, 1), high=1, mid=4, low=0.1, vol=0.8).unison(8)

a1.dur=[1/4, 1/4, 1/2, 1/2, 1/2, 1/2]

Scale.default = Scale.chromatic
Root.default=0.1
a3.stop()
e_all.rate=var([-0.5, 1], [1, 7])

Master().lpf=0





Clock.bpm = 133;
Root.default = "D#"

d1 >> dbass([3, 4, 4, 8, 4, 7, 4, 4], scale=Scale.chromatic, dur=1/2, rate=([4, 2, 1, 0.5], 0.1), lpf=1200, hpf=600, lpr=0.2)
d2 >> dbass([3, 4, 4, 8, 4, 7, 4, 4], oct=P[5, 6], scale=Scale.chromatic, dur=1/2, echo=0.25).unison(4).sometimes("shuffle").sometimes("amen")
e1 >> plaitsX(P*[3, 4, 4, 8, 4, 7, 4, 4], scale=Scale.chromatic, dur=1/2, oct=5, engine=12, lpf=1200, lpr=0.1)

e1 >> play("x ", sample=4, hpf=40, amp=0.8, lpf=4000, mverb=(0, 0.1))
d_all.oct=(4, 5)
d3 >> play("p", amp=P[1, 1, 1, 1, 0.1, 0.1].stutter(2), sample=5, shape=var([0, 0.5, 1]), vol=2)
d4 >> play("+", amp=P[1, 1, 1, 1, 0.1, 1].stutter(2), dur=PDur([3, 3, 5, 8], 8) * 4, sample=d3.dur, shape=0, rate=P*[1, 2, -1, 1, 1, 2, 4])


d_all.lpr=0.05
d_all.lpf=1000

d1 >> donk(feed=0.5, shape=0.7, oct=3)
d_all.degree=4



d1 >> play("pM", lpf=1200, hpf=1200, dur=var([2, PDur(3, 8)]), lpr=linvar([0.1, 0.8], [8, 16]), rate=(1, 0.5, 0.25), delay=(0, 0.25, 1), amp=1)
d2 >> ebass([0, 0, 0.1, 0, 2], dur=1/2, hpr=0.5, oct=6, hpf=400, mverb=0.01).slider().unison(4) + var([0, 14], [15, 1])

d2.dur=1/2
d2.dist2=1
e1.stop()
d2.lpf=400
d6.lpf=400
d1.lpf=400
e1.lpf=400
d2.mverb=0.5
d3 >> play("p", amp=P[1, 1, 1, 1, 0.1, 0.1].stutter(2), sample=5, shape=var([0, 0.5, 1]), vol=2)
d4 >> play("+", amp=P[1, 1, 1, 1, 0.1, 1].stutter(2), dur=PDur([3, 3, 5, 8], 8) * 4, sample=d3.dur, shape=0, rate=P*[1, 2, -1, 1, 1, 2, 4])
d5 >> dbass([0, 0, 11, [11, 14]], dist2=4, oct=6, dur=1/2, lpf=linvar([100, 6400], [32, 8, 8, 16]), mpf=linvar([2000, 320], 32), bpf=linvar([200, 3200], 16), bpr=linvar([1, 0.1], 8), echo=var([0.5, 0.25, 1], 8), mpr=var([0.1, 0.5, 0.8, 0.3], [4, 8, 2, 16]), lpr=var([0.1, 0.5, 0.8, 0.3], [4, 8, 2, 16]))
d5 >> play("-", lpf=0, hpf=100, dur=1/2, delay=0.5, mverb=0.5, amp=1)
d8 >> play("V ", sample=1, hpf=200, shift=1, cut=1/2)
d7 >> play("X ", hpf=400, sample=5, dur=var([1, 1/2], [3, 4])).often("stutter")


d4.lpf=400
d2.lpf=400

d1 >> dbass(P[-65, -65, -65, -65, 11, 12].stutter(2), dur=1/2, dist2=1, shape=0, revsus=1, mverb=0.5, amp=0.1, oct=(6, 5))
d3 >> faim(P[  P[-2, -4], P[-4, -3]].stutter(4),oct=4, dur=1/2, dist2=0, tanh=linvar([0.5, 0.7], 32), lpf=400).stop()

Root.default = "G"

Master().reset()

########### J1
# B2 
Root.default='C'
Scale.default="minor"
Clock.bpm = lininf(120, 170, 512)


b1 >> lbass(var([0, -2, 0.5], 8), formant=var([0, 0.1], [24, 8]), formantmix=PWhite(0, 0.3), oct=(6, 5, [4, 3]) + var([0, 1], [14, 2]) + PwRand([0, 1, 1.25], [30, 1, 1]), rate=linvar([1.2, 0.3], [32]), fmod=linvar([0, 1], [128]), scale=Scale.chromatic, drive=var([0, (0.1, 0)], [12, 4]), dur=1/2, amp=0.5, mverb=0, mverbdamp=[0.2, 1], mverbdiff=[1, 0.4], hpf=linvar([100, 400], 8)).unison(4).every(8, "stutter", slide=0.01, lpf=linvar([4000, 8000], 16))
q1 >> donk(var([0, -2, 0.5], 8), oct=(6, 4, 5) + var([0, 1], [14, 2]), width=PWhite(0.1, 0.9), rate=linvar([1.2, PWhite(0.3, 8)], [64]), shift=var([0, 1, 1.2], [13, 2, 1]), fmod=linvar([0, PRand(4, 8)], [128]), scale=Scale.chromatic, delay=(0, 0.25, [0.5, 0, 4]), leg=2, dur=P*[1/2, 1, 1, 1/4, 1/4, 1/4], amp=1, hpf=100).unison(0).every(8, "stutter", slide=[2, -2], degree=(-12, 12), echo=(0, 0.125), echotime=1, lpf=linvar([1000, 4000], 16)).every(8, "shuffle")

b1.rate=lininf(1, 0.1, 32)
b2.rate=lininf(1, 8, 32)
b1.mverb=0.0
b3 >> soprano((b1.degree, 0), dur=PRand(1,8), blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(7,6,5)), drive=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), room=0, mix=0.5, amplify=0.5, spin=0).unison(0)
b3 >> lbass(fold=0.5)
b1.lpr=lininf(1, 0.1, 64)
b1.slide=var([0, 1], [28, 4])
b1.degree=0.5

b1.chop=var([0, 1, 1/2], [12, 2, 2])
b2.dur=1/4


b4 >> play("(#....)..(...~)", rate=PWhite(-1,4)*0.25).unison(3, 1,99)
b5 >> play("@", sample=4, hpf=4000).fill(0)
b6 >> play("3", dur=1/2, amp=0.5, sample=(var([3, 4], [4, 4]), 3), glide=1,shift=var([0, 2], [24, 8]), pshift=0).slider()

b7 >> play(var(["-.--", "[--]"], 8), sample=1, rate=0.5, formant=0.4, hpf=7000)
b1.dur=lininf(1/2, 1/4, 16)

b1.lpf=linvar([3200, 1600], 128)
b1.amp=0.6
b8 >> dbass(var([0, -2, 0.5], 8), oct=(6, 5) + var([0, 1], [14, 2]), rate=linvar([1.2, 0.3], [64]), scale=Scale.chromatic, dur=1/2, amp=1, hpf=100).slider().unison(4).solo(0)
##############
e1 >> play("# ", dur=4, rate=(-1, 2)).unison(2).after(4, "stop")
e2 >> play("# ", sample=(1,4), dur=4, rate=(-1, 1)).after(8, "stop")
e3 >> play("& ", sample=5, rate=-2, shift=4, dur=4).after(32, "stop")
e4 >> play("#k", sample=(1,4), dur=4, rate=(-1, 1), mverb=1, room2=0.5,  chop=0.25, chopmix=[0.5, 0], damp2=0.9, revsus=1).after(4, "stop")

d0 >> fbass()
d1 >> fbass()
d8 >> ebass()

d1 >> play("x ", sample=6)
d2 >> play("--=-", sample=[2, 2, 1, 1], dur=1/4, delay=PWhite(-0.01, 0.01))
d3 >> play("+", sample=6, delay=PRand([-1/4, 1/4, 0]))
d4 >> play("c", sample=6, amp=var([0, 1], [12, 4]), amplify=PBin())
d5 >> play("C", sample=0, amp=var([0, 1], [12, 4]), amplify=PBin())

e1 >> play("X ")
