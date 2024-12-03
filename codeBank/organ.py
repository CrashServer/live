# organ
Clock.bpm = 128;
Root.default = "E"
Scale.default = Scale.minor;

~r1 >> organ(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([PDur(4,8),PDur([5,3,6],8)], [5,7]), amp=1, crush=1, crush_=4, crush_d=2, bits=6, bits_=var([12, 16]), fmod=1, lpf=2800, lpr=0.4)

r2 >> organ(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([4, PDur(4,8)], [7, 5]), amp=0.8, crush=1, crush_=4, crush_d=2, fx2=0.2, bits=6, bits_=var([12, 8]), oct=(5, 7), fmod=1, lpf=2800, lpr=0.2).unison(2).every(4, "shuffle")

r3 >> bell(P[var([0,-2,-3,-4],8),4,PStep(4,6,8),2], dur=var([4, PDur(4,8)], [9, 3]), amp=0.6, crush=1, crush_=4, crush_d=2, mverb=0.2, bits=6, bits_=var([12, 8]), delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")

r4 >> bell(P*[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([4, PDur(4,8)], [11, 6]), amp=0.5, crush=1, crush_=4, crush_d=2, mverb=0.5, bits=6, bits_=var([12, 8]), r1=0.5, delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")

c2 >> cbass(var([0,-4,-2,-3],8), dur=1/2, cutoff=40, follow=PFr(1,4, 555)).unison(2) + (0, var([0,7], [4,1]))

d1 >> play("x", sample=4, amp=PBin(344))
h3 >> play("s", valad=PFr(1000,3000)).sometimes("stutter", PRand(16))
n2 >> play("..*.", echo=P*[0,PRand([0.125, 0.5, 0.75])], mverb=0.9, hpf=4000)

c2 >> lbass(var([0, -2, linvar([-2,0],[8,0])], [16,8,8]), dur=var([1/2,1/4],[24,8]), cutoff=PFr(4000,12000), detune=0.9, tone=PFr(0.16,0.9), dist2=0, oct=var([5,lininf(5,6,8)],[24,8]), amp=0.5)
x1 >> play("<X.>", sample=10)

s2 >> klank(oct=linvar([5, 6], [128,0]), dur=PDur(3, 8)* 2).slider()
p1 >> supersaw(linvar([0,7], [64,0]), dur=1/4, mverb=0.9, oct=(4,5,6,7), amp=(linvar([0.3, 1], [64,0]), linvar([1, 0.5], [64,0])))

p2 >> play("<E ><p >", sample=0, dur=PDur([3, 5], 8), amp=PWhite(2,1), hpf=220, chop=1/2, leg=PWhite(15), pan=PWhite(-1,1), fx2=1)

r4 >> dab(dur=PDur(var([4,[5,3,8]],[6,2]),8), leg=([0, 5]), cutoff=400, dist2=0.4, hpf=1000, hpr=0.1)
