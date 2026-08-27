# generators 132
# industrial

#@intro(16)
Clock.bpm = 132
Scale.default = "minor"
Root.default = "D"
k1 >> compkick(0, dur=1, oct=3, amp=linvar([0.4, 1], 16), punch=0.9, comp=0.95, click=0.5, sub=0.9, body=0.8, tone=0.45)

#@kit_in(16)
kt = pkit("industrial", seed=7, evolve=4)
d1 >> play(kt.kick, dur=1/4, sample=2, amp=0.9, shape=0.1)
h1 >> play(kt.hat, dur=1/4, sample=3, amp=Pacc("offbeat"), hpf=6000, pan=PWhite(-0.3, 0.3))

#@grow(16)
b1 >> dbass(PGrowArp(0, max_notes=5, growth_rate=8), dur=1/2, oct=5, amp=1.1, shape=0.2, cutoff=linvar([400, 1600], 32), sus=PSustain(PDur(5, 8), 0.8))

#@clave(16)
p1 >> click(0, dur=PClave("son"), sus=0.03, amp=0.5, rate=16, hpf=4000, pan=PWhite(-0.5, 0.5))
s1 >> play(kt.snare, dur=1/4, sample=5, amp=0.8, shape=0.15, cheapverb=0.3, cvdecay=1.2)

#@drop(16)
d1 >> play(pbuild("industrial", evolve=8, density=0.9, seed=7), dur=1/4, sample=2, amp=1.1, shape=0.2, multicrush=0.6, mclowdrive=4, mcmiddrive=2, mchighdrive=1.5, mclofreq=200, mchifreq=4000)
b1 >> dbass(PGrowArp(0, max_notes=7, growth_rate=4, direction="diverge"), dur=1/2, oct=5, amp=1.3, shape=0.35, cutoff=fb(16, 500, 2600), res=0.2, tape=0.4, tapedrive=1.6)

#@poly(16)
euA, euB = PPolyEuclid(3, 8, 5, 8)
n1 >> noisehit(0, dur=euA, oct=5, amp=0.6, hpf=3000, pan=-0.4, sus=0.08)
n2 >> noisehit(0, dur=euB, oct=6, amp=0.45, hpf=5000, pan=0.4, sus=0.05)

#@odd(16)
d1 >> play(pat("i2"), dur=PAdditive(2, 2, 3, unit=0.25), sample=2, amp=1.0, shape=0.2)
b1 >> dbass(PMelody([0, 3, 7], style=4, length=16, seed=5), dur=PAdditive(2, 2, 3, unit=0.25), oct=5, amp=1.1, shape=0.3, cutoff=sinvar([600, 2200], 16))

#@break(16)
d1.stop()
h1.stop()
b1.stop()
q1 >> darkpad(PCircle(0, steps=8), dur=8, oct=5, sus=7.5, amp=linvar([0, 0.5], 16), cutoff=linvar([600, 2400], 32), cheapverb=0.8, cvdecay=5)
m1 >> bell(PMelody([0, 3, 7], style=1, length=12, seed=9), dur=1/2, oct=6, amp=0.5, sus=PArticulation("staccato", 8), shimmer=0.3, echo=0.4, fbdelay=0.4, fbtime=0.375, fbfeed=0.6, fbcutoff=5000, beat_dur=1)

#@rebuild(16)
k1 >> compkick(0, dur=1, oct=3, amp=1, punch=0.95, comp=0.95, click=0.6, sub=0.9, body=0.9, tone=linvar([0.4, 1.1], 32))
d1 >> play(pbuild("techno", evolve=8, density=0.8, seed=3), dur=1/4, sample=2, amp=1.0, shape=0.2)
g1 >> plaitsX(PMelody([0, 3, 7, 10], style=5, length=16, seed=4), dur=PGroove("techno", 0.8), oct=6, amp=0.7, shape=fb(32, 0.2, 0.8), hpf=1200, mverb=0.4, pan=PWhite(-1, 1))

#@peak(32)
d1 >> play(pbuild("industrial", evolve=8, fill=4, density=1.0, seed=7), dur=1/4, sample=2, amp=1.2, shape=0.3, multicrush=1.0, mclowdrive=8, mcmiddrive=3, mchighdrive=2, mclofreq=200, mchifreq=6000)
b1 >> dbass(PMelody([0, 3, 7], style=4, length=16, seed=5), dur=PPoly(3, 4), oct=5, amp=1.3, shape=0.4, cutoff=fb(8, 700, 3200), res=0.25, tape=0.6, tapedrive=2.0, resonbank=0.4, rbfreq=var([300, 400, 600], 8), rbdecay=0.5)
p1 >> click(0, dur=PClave("rumba"), sus=0.03, amp=0.6, rate=18, hpf=5000, pan=PWhite(-0.6, 0.6))

#@outro(16)
g1.stop()
p1.stop()
n1.stop()
n2.stop()
d1 >> play(pbuild("industrial", evolve=4, density=0.5, seed=7), dur=1/4, sample=2, amp=linvar([1.0, 0], 32), shape=0.2)
b1 >> dbass(PGrowArp(0, max_notes=3, growth_rate=8), dur=1/2, oct=5, amp=linvar([1.1, 0], 32), shape=0.2, cutoff=linvar([1600, 300], 32))
k1 >> compkick(0, dur=1, oct=3, amp=linvar([1, 0], 32), punch=0.9, comp=0.95, click=0.5, sub=0.9, body=0.8, tone=0.45)

#@end(4)
Clock.clear()
