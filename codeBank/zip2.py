# zip2
Clock.bpm = 122/2
Scale.default = Scale.minor
Root.default = "F#"

e0 >> plaits(melody(), dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var(
    [5, 7, 3], 8), drive=0, mverb=0.1, oct=3, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))
e0 >> plaits(melody(), dur=(1/2, 1/4), engine=(1, 4),
             drive=0, mverb=0.8, oct=5)
e1 >> bass(melody()[:8], dur=var([1/4, 2], [13, 3]), a=PWhite(0, 1),
           drive=0, amp=0.7, mverb=0.8).unison(2).every(13, "offmul", 2)
e0.every(4, "shuffle")

e1 >> bass(melody(), dur=1/4, oct=5, drive=0, mverb=0.8).unison(0)
e1 >> bass(melody(), dur=1/4, drive=linvar([0, 0.02], 32), mverb=0.8).unison(0)
g2 >> bass(melody() + var([7, 3, [4, 0]]),
           dur=var([1/4, 1/2]), drive=0, vol=0.5, mverb=0.1).unison(0)

e1 >> plaits(melody(), dur=var([1/2, (1/2, 2)]), drive=0,
             mverb=0.8, engine=var([11, 5], [3, 1]), oct=5).unison(0)

e0.dur = var([2, 1/4, 1/4, 1/4, 1/4])
e3 >> bass(melody(), dur=1/4,
           drive=linvar([0, 0.05], 32), mverb=0.8, delay=var([0, 0.5]), oct=6)
e3 >> lbass(dur=1/2, oct=4, drive=1, amp=PBin(8))
e0 >> plaits(melody(), dur=(1/2, 1/4), engine=(1, 4),
             drive=0, mverb=0.8, oct=5)

e3 >> lbass(dur=1/4, oct=PRand([4, 5, 6])[:4], drive=0.3)
g2 >> dbass(dur=1/4, echo=var([1/3, 0]), lpf=0, cut=0, mverb=0.04, mpf=linvar([200, 12000], 128),
            vol=0.5, rate=(0.25, 0.5), oct=7, hpf=linvar([2000, 12000], 32), engine=(3, 10)).unison(2)

e3.stop()
g1 >> dbass(delay=0.25, dur=1/4, dist2=0, lpf=120, cut=1/2, mverb=0.01,
            mpf=linvar([200, 2000], 128), vol=0.5, rate=(0.5, 1)).unison()

g3 >> lbass(dur=1/4, hpf=400, drive=0.0, lpf=1200, mpf=1600)
g_all.lpr = linvar([0.5, 0.1], [1, 4, 8])
e3.dist2 = 0.5
g_all.only()

Clock.bpm = 122

g3.dur = lininf(1/2, 1/8, 32)
g3.dist = 0.3
g3.mverb = 0.5

g_all.stop()

p1 >> pluck(var([([7, 0], 0), [(12, 0), ([Scale.chromatic, 0], 0), (0, [12, 7])]]), oct=(3, PStep(16, 3, 4)), dur=PwRand([[4, 1, 1/2], P[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2]], [1, 30]), leg=linvar([0, 4], PRand(16)[:4]),
            pan=linvar([-1, 1], [32]), scale=Scale.chromatic, drive=var([PWhite(0.01, 0.1), [0, (0.01, 0.2)]]), hpf=PWhite(30, 60), hpr=(0.1, 0.9)).sometimes("stutter", 1, mverb=0.6, feed=0.2, rate=0.2, shape=0.2) + var([0, 3, 4], [PRand([24, 128]), 2, 2])

p1.only()

p2 >> tb303([var([7, 4, linvar([P[12, 4], P[4, 0]], 4)], [24, 4, 4]), linvar([0, 1])], oct=(var([6, 7, 5, 4]), (PRand(4), 4)), hpf=linvar([(200, 2400), (2000, 1000)],
            64), hpr=linvar([0.01, 0.2], 32), dur=1/4, drive=linvar([0.4, 1], 64), vol=0.7, mpf=4000, cut=var([1/4, 1/8], [4, 4]), scale=Scale.chromatic).unison(2)

p_all.only()

p3 >> tb303(p2.degree, dur=4, cut=[1/4, 1/2, 1/2, 1/4], oct=(3, 5, 7),
            amp=0.3, echo=P*[0.5, 0, 0.25], shape=1, chop=4).unison(2)
p4 >> soprano(p1.degree, dur=PRand(1, 8), blur=PWhite(0, 4), decay=PRand(4), oct=(3, 4, PStep(3, 4, 5)), drive=PWhite(
    0, 0.1), sus=PRand(16), atk=PRand(4), room=0.5, mix=0.5, amplify=0, spin=0, scale=Scale.chromatic).unison(3)

p5 >> pluck([(0, 7.01), (0.0, 7.02)], dur=[1/4, 1/2, 1/2, 1/4, 1/2], fmod=p5.dur, leg=0,
            cut=linvar([1, 2], 16), oct=((3, 6), (4, 5), (5, 6)), hpf=200, amp=0.4, mpf=0, dist=0).unison(0)
p1 >> pluck(var([(0, 0), [(12, 0), ([6, 0], 0), (0, [12, 7])]]), oct=(3, PStep(16, 3, 4)), dur=[1/2, 1/4, 1/4, 1/4,
            1/2, 1/4, 1/4, 1/2, 1/4, 1/2], leg=1, scale=Scale.chromatic, drive=PWhite(0.54, 0.2), hpf=50, hpr=(0.1, 0.9))

p_all.oct = PRand([2, 3, 4][:4])

f4.dist2 = 0.1
f4 >> faim(0.1, dur=var([PDur(4, 8),  2], [12, 2]), mpf=2100, oct=3, leg=12, lpr=linvar([0.1, 0.5], 32), dist2=var([0, [1.2, 0.5, 2]], [12, 2]), echo=(
    f4.dist2 == 1.2)/2, shift=(f4.dist2 == 1.2) * P[1.0, 1.12], beef=0, mverb=(f4.dist2 == 0.5)/0.5, vol=1, hpf=(f4.dist2 == 1.2)*200).every(4, "stutter") + var([0, (-0.1, 0.1)], hpf=400)

f4.dist2 = 0.1


j0 >> tb303(0, dur=PDur(var([4, P*[5, 7, 1]], [6, 2]), 8), cut=1/2, amp=PBin(), cutoff=var(
    [200, 3200, 4000, 8000], [8, 12, 4, 8]), top=PRand(1200)[:8], rq=0.01, dec=var([0.1, 0.2, 0.5, 12], [4]))
j4 >> tb303(0, dur=var([1/2, 1/4], [4, 8]), cut=1/2, amp=0.5, oct=var([4, 5], [24, 8]), dist2=0, cutoff=var(
    [2000, 32000, 400, 800], [32]), top=PRand(1200)[:16], rq=[0.01, 0.001, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))

k1 >> play("K ")

f7 >> play("c...", drive=1, formant=0, dur=2)
f8 >> play("[--]", amp=2)


d_all.solo(0)

j9 >> tb303(dur=var([1/4, 1/2], [4, 8]), cut=1, amp=1, oct=var([3, 7], [24, 8]), dist2=0, cutoff=var([2000, 32000,
            400, 800], [32]), top=PRand(1200)[:8], rq=[0.1, 0.3, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]), vol=0.3)

j3 >> tb303(dur=1/2, cut=1/2, delay=0.125, lpf=8000, amp=0.5, oct=var([6, 7], [24, 8]), dist2=0.2, cutoff=var(
    [2000, 3200, 400, 800], [32]), top=PRand(1200)[:8], rq=[0.04, 0.004, 0.2, 0.5, 1], dec=var([0.1, 0.2, 0.5, 12], [4]))
j4 >> tb303(dur=var([1/4, 1/2], [4, 8]), cut=1, amp=0.6, oct=var([3, 7], [24, 8]), dist2=0.5, cutoff=var(
    [2000, 32000, 400, 800], [32]), top=PRand(1200)[:8], rq=[0.05, 0.005, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))

x1 >> play("<Xs><->", sample=(15, 1), amp=4)
x2 >> play("..x...x.", sample=4, dur=1/4).every(4, "stutter", drive=4)


d1.stop()

d_all.dur = 16

attack("filter")

##### attack@filter.ejc:~$ #####

masterAll("lpf", var([0, 4000, 6000, 15000], [24, 4, 2, 2]))
masterAll("hpf", var([0, 20, 30, linvar([3200, 6400], 32)], [24, 4, 2, 2]))
masterAll("cut", var([0, 1, 1/2, linvar([1/4, 1], 32)], [24, 4, 2, 2]))

masterAll("oct", 3)
masterAll("lpf", 800)

masterAll("degree", linvar([1, linvar([0, 2], [4, 0])], 8))
masterAll("rate", 8)
masterAll("dur", P*[1/2, 1, 1, 1/2, 2])

drop(4, 4, 4)

masterAll("reset")
k1 >> play("K.", amp=4, mverb=0.7, lpf=5400)


masterAll("dur", 0.125)

f5 >> play("V.o.", sample=(3, 6), echo=[
           0, 0.125, 0.25, 0.5], bpf=4000, bpr=0.9)
f6 >> play("W ")
f9 >> play(':', amp=2)
f0 >> play('X.U.', amp=1)


drop(1, 1, 1)

k4 >> play("B ", amp=1, sample=(5, 4), echo=1.25, lpf=400)
k5 >> play("B ", amp=1, dur=2, sample=(1, 2), echo=1.25, lpf=1400)

k_all.only()

k1 >> rsin(lpf=400, dur=4, cut=1/2, sus=2, high=12, hpr=0.01, oct=7, feed=0.5,  valad=P *
           [20, 200, 400], dubd=1, fold=0.1,  phaser=var([0.5, 1], 8), rate=(1, 0.25), mverb=0.2, hpf=linvar([50, 58], 32))
k3 >> plaits([0, 0, 4, 2, 4], lpf=12000, dur=1, echo=var([0.25, 0.5], [8, 4]), oct=3, engine=1,  fold=linvar(
    [0.1, 0.6], 32), lpr=linvar([0.05, 0.5], 128), mpf=linvar([500, 4000], 64), mverb=0.2, dist2=1, bpf=1200, cut=1).unison(0)
k3.dur = 4
k5 >> plaits(3, oct=4, dur=4, engine=10)
k6 >> plaits(2, oct=3, dur=4, engine=8)
k7 >> plaits(7, oct=5, dur=PDur(5, 8, 0), engine=1,
             delay=1, mverb=0.5, valadd=10, valad=120)
k8 >> lbass([PWalk(Scale.minor, 1, 1), -14, -14 + PArp([-12, var([2, 0], 4), 2])],
            scale=Scale.minor, sus=2, dur=1, oct=5, rate=2)
k8 >> dbass([0, 7, 1 + PArp([4, var([1, P[1:10]], 4), 2])],
            scale=Scale.chromatic, dur=1/4, oct=6)
k1 >> pianovel(amp=2)
k2 >> faim(Scale.minor[:4], dur=PDur(5, 11)).every(4, "shuffle")

k1.stop()

p_all.dur = 8

p_all.lpf = linvar([200, 400], 16)
s_all.lpf = linvar([200, 1200], [4, 2, 5, 3])
f_all.lpf = linvar([1200, 400], [4, 2])

p_all.spin = 0
