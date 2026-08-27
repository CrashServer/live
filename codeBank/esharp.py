# e sharp 122
# live

Root.default = "G"
Master().reset()

Clock.bpm = 122/2;
Scale.default = Scale.minor
Root.default = 6
Clock.bpm = 120;

Clock.bpm = 135;
Scale.default = Scale.minor
Root.default = "F#"

g4 >> ebass(dur=1/4, hpf=(400, 1200), hpr=0.02, echo=(var([0.016, 0.012], [16, 4, 4]), 0.01), shape=0.0, delay=linvar([0, (0.01, 0.03)], 128), lpf=(1200, (400, 4000)), mpf=linvar([200, 2000], [24, 4]))
g5 >> ebass(dur=var([1/4, 1/2], [28, 4]), oct=7, hpf=(400, 1200), hpr=linvar([0.05, 0.1], 128), echo=(var([0.016, 0.012], [16, 4, 4]), 0.01), shape=0.0, delay=linvar([0, (1.01, 1.03)], 128), lpf=(1200, (400, 4000)), mpf=linvar([200, 2000], [24, 4]))
g6 >> fbass(dur=Pvar([1/4, 1/2], [28, 4]) * P[1/2, 4], oct=5, hpf=(4000, 120), hpr=linvar([0.05, 0.1], 128), echo=(var([0.016, 0.012], [16, 4, 4]), 0.01), shape=0.0, delay=linvar([0, (1.01, 1.03)], 128), lpf=(1200, (400, 4000)), mpf=linvar([200, 2000], [24, 4]))

g5 >> play("[--]", hpf=400, dur=1/6, fold=0.2, sample=3, amp=[0.7,0.2], cut=1/4).sometimes("stutter", degree="#", mverb=0.5)
g6 >> play("[--].-", hpf=400, fold=0, sample=P[1, 4], cut=1/4)
g5 >> ebass()
g1.oct=3
g2.oct=5

g7 >> play("Eb..", cut=(1/4, P*[0.125, 0.25, 0.5]), sample=4, echo=(0.25, 0.5), dur=P[PDur(3, 8), 1/2], tanh=0.2)
g8 >> play("w ", sample=4, dur=2, echo=P[0, 0.5], amp=2, hpf=400, dist2=1)
g9 >> play("w ", sample=2)

g0 >> play("[.u]o..", sample=4, dur=2)
g1 >> play("v.o.")
g2 >> play("..c.", dur=4)
g3 >> play("# ", dur=4, mverb=1, cut=1/4, chop=4).unison(2)

t1 >> play("T ")

g7 >> play("k ", cut=(1/4, P*[0.125, 0.25, 0.5]), sample=4, echo=(0.25, 0.5), dur=PDur(3, 8))
g8 >> play("w ", sample=4)
g9 >> play("w ", sample=2)
g0 >> play("[.u]o..", sample=4, dur=2)

e0 >> plaits(melody(),dur=(1/2, 1/4), engine=1, shape=0, mverb=0.8)
e1 >> bass(melody(),dur=[2, 4], lpf=200, sus=4.5, shape=linvar([0, 0.1], 32), mverb=0.8).unison(2)
g2 >> bass(melody() + var([7, 3, [4, 0]]),dur=1/4, shape=0, mverb=0.1).unison(4)
e3 >> bass(melody(),dur=1/4, shape=linvar([0, 0.1], 32), mverb=0.8, delay=var([0, 0.5]), oct=6)
g2 >> dbass(dur=1/4, echo=var([1/3, 0]), lpf=0, cut=0, mverb=0.04, mpf=linvar([200, 12000], 128), vol=0.5, rate=(0.25, 0.5), oct=7, hpf=linvar([2000, 12000], 32), engine=(3,10)).unison(4)
g1 >> dbass(delay=0.25,dur=1/4, dist2=0, lpf=120, cut=1/2, mverb=0.01, mpf=linvar([200, 2000], 128), vol=0.5, rate=(0.5, 1)).unison()
g3 >> lbass(dur=1/4, hpf=400, shape=0.0, lpf=1200, mpf=1600)

a4 >> play("X ", sample=4).drummer()

g2.dur=4
g1.dur=2
g3.dur=4

Clock.bpm = 210
print(Clock.bpm)
a2 >> plaitsX([PSine(PWalk(8, 6, PWalk(8, 1, 1)))], oct=PStep(4, P*[3, [5, 4]], 4), tanh=var([0, 0.2], P*[2, 4, 8, 16]), dur=P[1/2, [1/1, 1/2, 1/2]], sus=1/2, lpr=linvar([0.05, 4], P*[1, 2, 4, 8, 16]), preset=(6, 8), lpf=linvar([400, 4000], [24, 8]), amp=1, pan=(linvar([-1, 1], 32), PWhite(-1, 1))).sometimes("stutter", amp=0.5, echo=2, oct=4, sus=1).sometimes("stutter", amp=0.5, echo=0.5, degree=(0, P*[4, 12]), slide=0, dur=1/2, leg=4, mverb=0.8, delay=(0, 4, 0.25)).rarely("stutter", amp=0.2, echo=0.25, degree=((4, P*[6, 12]), linvar([-4, 4], 4)), slide=0, dur=1, dist2=0.0, sus=2, leg=4, mverb=0.8, delay=2).rarely("stutter", amp=0.4, echo=2, oct=6, degree=((4, P*[6, 12]), linvar([-4, 4], 4)), slide=2, slidedelay=2, dur=1, dist2=0.0, sus=2, leg=32, mverb=0.2, delay=(0, 1, 2.25)).unison(4)

a3 >> dbass([PSine(PWalk(8, 6, PWalk(8, 1, 1)))], oct=PStep(4, P*[4, 5], 5), delay=(0, 2), tanh=var([0, 0.2], P*[2, 4, 8, 16]), shape=0.2, rate=1, dur=P[1/2, [1/1, 1/2, 1/2]], sus=1/2, lpr=linvar([0.05, 4], P*[1, 2, 4, 8, 16]), preset=(6, 8), lpf=linvar([400, 4000], [24, 8]), amp=P*[0.5, 1, 0, 1], pan=(linvar([-1, 1], 32), PWhite(-1, 1))).sometimes("stutter", amp=1, echo=2, oct=4, sus=1).sometimes("stutter", amp=0.5, echo=0.5, degree=(0, P*[4, 12]), slide=0, dur=1/2, leg=4, mverb=0.8, delay=(0, 4, 0.25)).rarely("stutter", amp=0.2, echo=0.25, degree=((4, P*[6, 12]), linvar([-4, 4], 4)), slide=0, dur=1, dist2=0.0, sus=2, leg=4, mverb=0.8, delay=2).rarely("stutter", amp=0.4, echo=2, oct=6, degree=((4, P*[6, 12]), linvar([-4, 4], 4)), slide=2, slidedelay=2, dur=1, dist2=0.0, sus=2, leg=32, mverb=0.2, delay=(0, 1, 2.25)).unison(4)
b1 >> varsaw(a2.degree, sus=10, lpf=linvar([3000, 6700], 128), lpr=PWhite(0.2,0.9), blur=2, amp=0.6, dur=var([5,1,1], [6,1,1]), oct=PStep(6,3,4)).unison(2) + var([0, 4, 8], [6, 1, 1])

e0 >> plaits(melody() + PWalk(8, 1, 1),dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), shape=0, mverb=0.1, oct=4, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))
e0 >> plaits(melody(),dur=(1/2, 1/4), engine=3, shape=0, mverb=0.8, oct=5)
e1 >> bass(melody(),dur=var([1/4, 2],[13, 3]), shape=0, mverb=0.8).unison(2).every(13, "offmul", 2)
e0.unison(2)

e0 >> karp(melody(),dur=1/4, oct=5)
e0 >> karp(melody(),dur=1/4, oct=5, spf=400, spfslide=0.5, spfend=4000)
e1 >> bass(melody(),dur=1/4, shape=linvar([0, 0.02], 32), mverb=0.8, hpf=0)
e_all.only()
g2 >> bass(melody() + var([7, 3, [4, 0]]),dur=var([1/4, 1/2]), shape=0, vol=0.5, mverb=0.1).unison(0)
e1 >> plaits(melody(),dur=var([1/2, (1/2, 2)]), mverb=0.8, engine=var([11, 5], [3, 1]), oct=4, amp=PWhite(0, 1))

e0.dur=var([2, 1/4, 1/4, 1/4, 1/4])
e2.dur=4

f4 >> karp(melody(),dur=PDur(11, 15), lpf=1200, shape=linvar([0, 0.05], 32), mverb=0.8, delay=var([0, 0.5]), oct=PStep(5, 4, 5)).unison(2) + var([0, 2, 0, (0, 2)])

e_all.lpf=0
a3.lpf=200
a2.stop()
f4.dur=2
e_all.dur=8
f5 >> lbass(dur=16, oct=4, shape=0.0).unison(2)
e_all.stop()

f6 >> lbass(dur=16, oct=4, shape=1).unison(2)
f7 >> lbass(dur=1/2, sus=1/4, oct=5, leg=12, lpf=800, rate=0.25,amp=PBin(16), hpf=0, dist2=0)
f8 >> dbass(dur=1/4, echo=var([1/3, 0]), lpf=0, cut=0, mverb=0.04, mpf=linvar([200, 12000], 128), vol=0.5, rate=(0.25, 0.5), oct=8, hpf=linvar([2000, 12000], 32), engine=(3,10)).unison(2)

e3.stop()

Root.default = lininf(6, 5, 64)

g0 >> lbass(dur=[1/2, 1/4, 1/4, 1/2, 1/2, 1/4, 1/8, 1/8], lpf=linvar([1200, 4000]), lpr=0.1, sus=1/4, valadd=4, valad=12) + var([0, P[-2, -3]])
g1 >> dbass(delay=0.25, oct=5,dur=PDur(11, 15), dist2=3, lpf=1200, cut=1/2, mverb=0.01, mpf=linvar([200, 2000], 128), vol=0.5, rate=(0.5, 1)).unison(4)
g3 >> lbass(dur=[1/2, 1/3, 1/3, 1/3, 1/2], oct=4, hpf=400, shape=1.4, lpf=12000, mpf=3200, mverb=0)
e3.dist2=0.5

g_all.only()

g_all.only()

Clock.bpm = 122;
g3.dist2=10
g3.dist=40
g3.mverb=0.9
g3.lpf=100
g3.hpf=2000

p_all.only()
p_all.lpf=200

p1 >> pluck(var([([7, 0], 0), [(12, 0), ([Scale.chromatic, 0], 0), (0, [12, 7])]]),oct=(3, PStep(16, 3, 4)), dur=PwRand([[4, 1, 1/2], P[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2]], [1, 30]), leg=linvar([0, 4], PRand(16)[:4]), dist2=0.8, pan=linvar([-1, 1], [32]), scale=Scale.chromatic, shape=var([PWhite(0.01, 0.1), [0, (0.01, 0.2)]]), hpf=PWhite(30, 60), hpr=(0.1, 0.9)).sometimes("stutter", 1, mverb=0.6, feed=0.2, rate=0.2, shape=1) + var([0, 3, 4], [PRand([24, 128]), 2, 2])

g3.lpf=100

p1.only()

p2 >> tb303([var([0, 4, linvar([P[0, 4], P[4, 0]],4)], [24, 4, 4]), linvar([0, 1])], oct=(var([6, 7, 5, 4]), (PRand(4), 4)), hpf=linvar([(200, 2400), (2000, 1000)], 64), hpr=linvar([0.01, 0.2], 32), dur=1/4, shape=linvar([0.4, 1], 64), vol=0.7, mpf=4000, cut=var([1/4, 1/8], [4, 4]), scale=Scale.chromatic).unison(2)

Root.default="F"

p_all.only()

p3 >> tb303(p2.degree, dur=4, cut=[1/4, 1/2, 1/2, 1/4], oct=(3,5, 7), amp=0.3, echo=P*[0.5, 0, 0.25], shape=1, chop=4).unison(2)
p4 >> soprano(p1.degree, dur=PRand(1,8), blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(3,4,5)), shape=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), room=0.5, mix=0.5, amplify=0, spin=0, scale=Scale.chromatic).unison(3)

j1 >> play("X:c ")

p5 >> pluck([(0, 7.01), (0.0,7.02)], dur=[1/4, 1/2, 1/2, 1/4, 1/2], fmod=p5.dur, leg=0,cut=linvar([1, 2], 16), oct=((3, 6), (4, 5), (5, 6)), hpf=200, amp=0.4, mpf=0, dist=1).unison(0)
p1 >> pluck(var([(0, 0), [(12, 0), ([6, 0], 0), (0, [12, 7])]]),oct=(3, PStep(16, 3, 4)), dur=[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2], leg=1, scale=Scale.chromatic, shape=PWhite(0.54, 0.9), hpf=50, hpr=(0.1, 0.9))

p_all.oct=4
Clock.bpm = 122;

f4.dist2=1.2
f4 >> faim(0.1 ,dur=var([PDur(4, 8),  2], [12, 2]), amp=PBin(8), mpf=2100, oct=5, leg=12, lpr=linvar([0.1, 0.5], 32), dist2=var([0, [1.2, 0.5, 2]], [12, 2]), echo=(f4.dist2==1.2)/2, shift=(f4.dist2==1.2) * P[1.0, 1.12], beef=0, mverb=(f4.dist2==0.5)/0.5, vol=0.7, hpf=(f4.dist2==1.2)*200).every(4, "stutter") + var([0, (-0.1, 0.1)], hpf=400)

f4.dist2=1.2

p3 >> donk(dur=1/4, oct=(5, linvar([4, 8], 64)), hpf=40, amp=Pvar([0.5, 0]), lpf=4000, echo=PCoin(0, 0.25, 0.5), shift=var([0, Scale.minor], [32, 32]))
p4 >> varicelle(oct=(4, 5), cut=1/4, fmod=4, dur=PDur(11, 16), delay=(var([0.25, 0]), var([0.5, 0.25, 0.25])), bit=2, crush=4, leg=4).sometimes("stutter", formant=linvar([1, 4], 8))

f6 >> loop("nssub8", dur=8, sample=2)
f6 >> loop("futur16", dur=8, sample=3)

f7 >> play(".(c.).(C..[kU]).", shape=0, formant=0, dur=2, sample=7)
f8 >> play("[-].-[--]", amp=0.3, sample=5, echo=(0, 0.5))
f4.hpf=3200

Clock.bpm = var([122/2, 122], [1, 1])

d0 >> tb303(0, dur=PDur(var([4,P*[5,7,1]],[6,2]),8), cut=1/2, amp=PBin(), cutoff=var([200, 3200, 4000, 8000], [8, 12, 4, 8]), top=PRand(1200)[:8], rq=0.01, dec=var([0.1, 0.2, 0.5, 12], [4]))
d1 >> tb303(0, dur=var([1/2, 1/4], [4, 8]), cut=1/2, amp=0.5, oct=var([4, 5], [24, 8]), dist2=1, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:16], rq=[0.01, 0.001, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))

Clock.bpm = 122;

k1 >> play("K ")
d0 >> tb303(dur=var([1/2, 1], [4, 8]), cut=1, amp=1, oct=var([3, 7], [24, 8]), dist2=1, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:8], rq=[0.1, 0.3, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]), vol=0.3)
x1 >> play("<X:><->", sample=(15, 7), dur=1)
x2 >> play("..x...x.", sample=4, dur=1/2).every(4, "stutter", shape=4)

d8 >> tb303(dur=1/2, cut=1/2, delay=0.125, lpf=8000, amp=0.5, oct=var([6, 7], [24, 8]), dist2=1, cutoff=var([2000, 3200, 400, 800], [32]), top=PRand(1200)[:8], rq=[0.04, 0.004, 0.2, 0.5, 1], dec=var([0.1, 0.2, 0.5, 12], [4]))
d1 >> tb303(dur=var([1/4, 1/2], [4, 8]), cut=1, amp=0.6, oct=var([3, 7], [24, 8]), dist2=1, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:8], rq=[0.05, 0.005, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))

f4.stop()

drop(4, 1, 1)

d1.stop()

d_all.dur=16

attack("filter")

##### attack@filter.ejc:~$ #####

masterAll("lpf", var([0, 4000, 6000, 15000], [24, 4, 2, 2]))
masterAll("hpf", var([0, 20, 30, linvar([3200, 6400], 32)], [24, 4, 2, 2]))
masterAll("cut", var([0, 1, 1/2, linvar([1/4, 1], 32)], [24, 4, 2, 2]))

masterAll("oct", 3)
masterAll("lpf", 800)

masterAll("degree", linvar([1, linvar([0, 2],[4, 0])], 8))
masterAll("rate", 8)
masterAll("dur", P*[1/2, 1, 1, 1/2, 2])

drop(4, 4, 4)

masterAll("reset")
k1 >> play("K.", amp=4, mverb=0.7, lpf=5400)

masterAll("dur", 0.125)

f5 >> play("V.o.", sample=(3, 6), echo=[0,0.125, 0.25, 0.5], bpf=4000, bpr=0.9)
f6 >> play("W ")
f9 >> play(':', amp=2)
f0 >> play('X.U.', amp=1)

drop(1, 1, 1)

k_all.only()

Clock.bpm = 170
k4 >> play("EmptyItem", amp=1, hpf=(400, linvar([200, 1200])), sample=(5, 4), echo=1.25, lpf=1200, lpr=0.2, dur=P*[1/2, 4, 1/2])

k5 >> zap(dur=(PDur(3, 8, 2), PDur(5, 12, 4)),oct=(4, 6), amp=4, shift=var([0, 2], [15, 3]), lpr=0.065, echo=var([0, 0.5]), lpf=400).unison(8)
r2 >> play("u", lpf=linvar([1000, 12000], 32), dur=var([2, 1/2]), mverb=linvar([0.5, 0], 32), high=1, delay=(00.25, 2.25), low=0, sample=var([4, 5], [3, 1]), dist2=2, rate=var([1, 2, 4], [12, 2, 22]))
r3 >> play("b", lpf=linvar([12000, 1200], 32), dur=PDur(3, 4), mverb=0, high=1, delay=(0, 2.25), low=0, sample=var([4, 12], [1, 3]), dist2=1, bits=4, krush=4, rate=4)
k1 >> rsin(lpf=400, dur=4, cut=1/2, sus=2, high=21, hpr=0.01, oct=8, feed=0.5, dist2=0.2,  valad=P*[20, 200, 400], dubd=1, fold=0.1,  phaser=var([0.5, 1], 8), rate=(4, 0.25), mverb=0.0, hpf=linvar([50, 58], 32))

k3 >> bass([0, 0, 4, 2, 4],lpf=12000, dur=1/4, echo=var([0.25, 0.5], [8, 4]), oct=3, engine=4,  fold=linvar([0.1, 0.6], 32), lpr=linvar([0.05, 0.5], 128), mpf=linvar([500, 4000], 64), mverb=0, dist2=1, bpf=1200, cut=1)

e9 >> plaits(e0.degree, dur=8, mpf=2400, dist2=1, chop=4, spf=200, spfend=4000, spfslide=8,blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(3,2,3)), shape=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), mverb=0.2, amplify=12, spin=0, scale=Scale.chromatic).unison(0)

e8 >> play("-:", dur=4, lpf=1200, mverb=0.5, amp=8, sample=5, echo=1.25, echotime=4)
~e4 >> play("ot[uz][xk].k.", dur=1/4, amp=8, shape=0, sample=2)

k3.dur=4
k5 >> saw(3,oct=3, lpf=linvar([400, 1600], 32), dur=[4, 1/3], engine=1)
k6 >> zap(2,oct=3, dur=4, engine=4)
k7 >> bass(7,oct=3, dur=PDur(5, 8, 0), engine=1, delay=1, mverb=0.5, valadd=10, valad=120)
k8 >> lbass([PWalk(Scale.minor, 1, 1), -14, -14 + PArp([-12, var([2, 0], 4), 2])], scale=Scale.minor, sus=2, dur=1,oct=5, rate=2)
k8 >> cluster([0, 7, 1 + PArp([4, var([1, P[1:10]], 4), 2])], scale=Scale.chromatic, dur=1/3, oct=5, pan=linvar([-1, 1])).unison(2, 0.01, 1)
