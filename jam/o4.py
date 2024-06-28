#really weird & old stuff
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
