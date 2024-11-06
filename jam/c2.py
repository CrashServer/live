Clock.bpm = 170;

l0 >> loop("cyber32", dur=32, sample=PRand(32))
a3 >> keys([3, (3, [4, var([3, 14], [15, 1])])], slide=0.05,dur=[2, 1/2, 1, 1/2], oct=(7, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=0, lpf=0, bpf=linvar([2000, 6200, 32], [16, 8, 32]), shape=0, high=0, mid=0.1, low=0.1, vol=0.8, chop=0).unison(8).spread(4)
a2 >> organ([3, (3, [4, var([3, 14], [15, 1])])], slide=0.5,dur=[2, 1/2, 1, 1/2], oct=(7, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=0, lpf=0, bpf=linvar([2000, 6200, 32], [16, 8, 32]), shape=0, high=0, mid=0.1, low=0.1, vol=0.8, chop=0).unison(8).spread(4)
a1 >> sawbass([3, (3, [4, 3])], dur=1/2, oct=(4, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=[0.5, 0.1], lpf=1600, bpf=linvar([200, 1600, 32], [16, 8, 32]), shape=PTri(0, 1), high=1, mid=4, low=0.1, vol=0.8).unison(2)
l1 >> loop("cyber32", dur=32, sample=1, beat_stretch=0, a=0.8)

a3 >> dbass()
a3 >> loop("synth16", dur=16, delay=0, a=0, cut=0.125, leg=8)
l3 >> loop("synth16", dur=16, a=0, pos=PWhite(0, 1), beat_stretch=0, rate=-1)

l4 >> loop("ragegtr16", dur=16, delay=0, a=0, sample=1, cut=0.5, leg=8, mverb=0.5, amp=0.3).unison(4)

a1 >> dab()

l0 >> loop("ragedrone32", pos=linvar([0, PWhite(0.0, 1.0)], [8, 4]), sample=0, dur=1/2, beat_stretch=0)


g_all.cut=1/4

l3 >> loop("bass8", dist2=0.4, pos=linvar([0, PWhite(0.0, 1.0)], [16, 4]), sample=PRand(32)[:16], dur=8, beat_stretch=0)


l1 >> loop("nsbass8", pos=linvar([0, PWhite(0.0, 1.0)], [8, 4]), sample=1, dur=1/2, beat_stretch=0)
l2 >> loop("rock32", dist2=0.4, pos=linvar([0, PWhite(0.0, 1.0)], [16, 4]), sample=PRand(32)[:16], dur=1/2, beat_stretch=0)


l_all.only()

g1.mix2=0

g1 >> play(PRand("Xx.x{Cxxx}.x{c--}.x-.x[xxx].x"), room2=.3, amp=0.4, mix2=PGauss(0.3, 0.1), revatk=(1-g1.mix2), revsus=(g1.mix2 / 0.5), sample=[0,7,4], lpf=8120, leg=PRand(0,(g1.mix * 10)+1), echo=(0, g1.mix2/4), rate=(1, var([1, linvar([[-1, 4], [4, -1]], 16)])), delay=(0.5, 0),pan=PWhite(-1, 1), echomix=g1.mix2, krush=P*[0,4]).sometimes("stutter", PRand(8), low=[(0, 0.5), 0.0], bpm=var([Clock.bpm, Clock.bpm/0.5], 8), rate=PRand(8)).slider(on=0)


l2 >> loop("synth16", dur=16, delay=0, a=0, cut=0.125, leg=8)

##



l3.stop()

l5 >> loop("circlebreak16", dur=16)
l4.sample=3

l4.mverb=0.5
l4.delay=(0, 4)
l4.shift=(0, 0.5)

l3 >> loop("drumglitch32", pos=0, cut=0, dur=32, sample=12)

Root.default = var([3, 8, 4, 11], 4)
Root.default = 6

g1.mix2=0
g1.revsus=0.45
g2 >> play(PRand("{gc.m.5.cc.--.-}"), lpr=2, amp=0.4, sample=PRand(20), dur=1/4, lpf=g1.revsus * 1400, leg=var([15, 55],[8, 72]), krush=P*[0,4]).sometimes("stutter").slider()
l0 >> loop("cyber32", dur=32)
l1 >> loop("cyber32", dur=32, sample=1, beat_stretch=0, a=0.8)


g2.amp=1
g3 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), amp=0.4, cut=PWhite(0.1, 1), sample=PRand(20), dur=1/4, lpf=0, leg=20, krush=P*[0,2]).sometimes("stutter").slider()
g7 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), rate=PRand(-12, 12), amp=1.4, cut=PWhite(0.5, 1), sample=PRand(20), dur=1/2, lpf=0, leg=10, krush=0).sometimes("stutter").slider()

l0 >> loop("ragedrone32", pos=linvar([0, PWhite(0.0, 1.0)], [8, 4]), sample=0, dur=1/2, beat_stretch=0).stop()

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


r_all.stop()

a2 >> blip(var([(3, (3, 8)),3, PCoin(3, 4, 0.5), linvar([4, var([4.01, 4])]), [var([1, 7]), 4, 4, 4, 4]], [4]), rate=2, oct=(PStep(3, 4, 5), var([3, 4])), scale=Scale.chromatic, dur=[1/2], vol=0.5, fold=0.5, leg=var([0, a1.drive], [3, 1], echo=[0, 0.1], feed=0), sus=[1/4, 1/2], lpf=1200).unison(4).stop()


a1 >> sawbass([3, (3, [4, var([3, 14], [15, 1])])], slide=a1.degree == 15,dur=[1/2, 1/2, 1], oct=(4, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=var([[0.5, 0.1], [4, 5]], [48, 16]), lpf=(1/a1.drive) * 800, bpf=linvar([200, 3200, 32], [16, 8, 32]), shape=PTri(0, 1), high=1, mid=8, low=0.1, vol=0.5, chop=0).unison(8)
g_all.stop()

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






l0 >> loop("gdrop8", pos=linvar([0, PWhite(0.0, 1.0)], [8, 4]), sample=0, dur=1/2, beat_stretch=0)



{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=1.0, buf=0, pos=0, room=0.1, sample=0, beat_stretch=1, looping=1.0|




l2 >> noloop("vocalcrash8", dur=[16, 8, 4, 2], lofi=1, start=0.5, rate=1, sample=4)

l2.sample=4
l2.mverb=0.5
l2.echo=2
l1 >> loop("gbreak16", dur=16, hpf=400)
l3.rate=cut=1/4

l1.sample=5
l2.sample=6
l2.feed=0.5
l2.lpf=1600
l2.lpr=0.1

l1 >> loop("gscreechb16", dur=32, mverb=1)
l2 >> loop("ghperc16", dur=16, lpr=0.5)

l3.lpf=400

l2 >> loop("noizebeat16", lpf=0)
