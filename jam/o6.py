#really weird & old stuff
Clock.bpm = 133;
Root.default = "D#"

d1 >> dbass([3, 4, 4, 8, 4, 7, 4, [4, 5]], scale=Scale.chromatic, dur=1/3, rate=([4, 2, 1, 0.5], 0.1), lpf=1200, hpf=[1200, 400, 300, 600], lpr=0.4, lofi=1).every(5, "stutter", rate=0.25, oct=6)
d2 >> dbass([3, 4, 4, 8, 4, 7, 4, 4], oct=P[5, 6], scale=Scale.chromatic, flanger=[0.7, 0.9, 0.8, 0.7], dur=1/3, echo=1/3).unison(4).sometimes("shuffle").sometimes("amen").sometimes("stutter", 4, oct=6, shape=1)
e1 >> plaitsX(P*[3, 4, 4, 8, 4, 7, 4, 4], scale=Scale.chromatic, dur=1/2, oct=5, engine=12, lpf=1200, lpr=0.1, amp=2)
e1 >> play("x ", sample=4, hpf=40, amp=0.8, lpf=4000, mverb=(0, 0.1))
d_all.dur=1/3
e2 >> play(": ", sample=4, hpf=40, amp=0.8, lpf=4000, mverb=(0, 0.1),dur=1/3)

d_all.oct=(4, 5)

d3 >> play("p", amp=P[1, 1, 1, 1, 0.1, 0.1].stutter(2), sample=5, shape=var([0, 0.5, 1]), vol=2,  dur=1/3)
d4 >> play("+", amp=P[1, 1, 1, 1, 0.1, 1].stutter(2), dur=PDur([3, 3, 5, 8], 8) * 4, sample=d3.dur, shape=0, rate=P*[1, 2, -1, 1, 1, 2, 4])

d1 >> blip()
d2 >> plaitsX()

d_all.lpr=0.2
d_all.lpf=1000

d1 >> dbass([3, 4, 4, 8, 4, 7, 4, [4, 5]], scale=Scale.chromatic, dur=1/3, rate=([4, 2, 1, 0.5], 0.1), lpf=1200, hpf=[1200, 400, 300, 600], lpr=0.4, lofi=1).every(5, "stutter", rate=0.25, oct=6)
d2 >> dbass([3, 4, 4, 8, 4, 7, 4, 4], oct=P[5, 6], scale=Scale.chromatic, flanger=[0.7, 0.9, 0.8, 0.7], dur=1/3, echo=1/3).unison(4).sometimes("shuffle").sometimes("amen").sometimes("stutter", 4, oct=6, shape=1)
e1 >> plaitsX(P*[3, 4, 4, 8, 4, 7, 4, 4], scale=Scale.chromatic, dur=1/2, oct=5, engine=12, lpf=1200, lpr=0.1, amp=2)
e1 >> play("x ", sample=4, hpf=40, amp=0.8, lpf=4000, mverb=(0, 0.1))
d_all.dur=1/3
e2 >> play(": ", sample=4, hpf=40, amp=0.8, lpf=4000, mverb=(0, 0.1),dur=1/3)

k4 >> play("K ", bank=1, dur=2/3, amp=2)
d_all.hpf=500

k5 >> dbass(dur=1/3, rate=1/4, dist2=0.5)

d1 >> donk(feed=0.5, shape=0.0, oct=3, mverb=0.5, dist2=0, lpr=0.5, lpf=0)
d_all.degree=4


