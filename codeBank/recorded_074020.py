# recorded_074020
# recorded

#@intro(8)
e0 >> plaits(melody(), dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), drive=0, mverb=0.0, oct=3, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))

#@build(8)
e0 >> plaits(melody(), dur=(1/2, 1/4), engine=(1, 4),            drive=0, mverb=0.0, oct=5)

#@peak(8)
e1 >> bass(melody()[:8], dur=var([1/4, 2], [13, 3]), a=PWhite(0, 1),          drive=0, amp=0.7, mverb=0.0).unison(2).every(13, "offmul", 2)

#@break(4)
e0.every(4, "shuffle")

#@drop(4)
e1 >> bass(melody(), dur=1/4, oct=5, drive=0, mverb=0.0).unison(0)

#@outro(8)
e1 >> bass(melody(), dur=1/4, drive=linvar([0, 0.02], 32), mverb=0).unison(0)

#@part7(8)
g2 >> bass(melody() + var([7, 3, [4, 0]]),   dur=var([1/4, 1/2]), drive=0, vol=0.5, mverb=0.0).unison(0)

#@part8(4)
e1 >> plaits(melody(), dur=var([1/2, (1/2, 2)]), drive=0,   mverb=0.0, engine=var([11, 5], [3, 1]), oct=5).unison(0)

#@part9(4)
e0.dur = var([2, 1/4, 1/4, 1/4, 1/4])

#@part10(4)
e3 >> bass(melody(), dur=1/4,  drive=linvar([0, 0.05], 32), mverb=0.0, delay=var([0, 0.5]), oct=6)

#@part11(8)
e3 >> lbass(dur=1/2, oct=4, drive=1, amp=PBin(8))

#@part12(4)
e0 >> plaits(melody(), dur=(1/2, 1/4), engine=(1, 4),  drive=0, mverb=0, oct=5)

#@part13(4)
e3 >> lbass(dur=1/4, oct=PRand([4, 5, 6])[:4], drive=0.3)

#@part14(4)
g2 >> dbass(dur=1/4, echo=var([1/3, 0]), lpf=0, cut=0, mverb=0, mpf=linvar([200, 12000], 128),

#@part15(4)
g2 >> dbass(dur=1/4, echo=var([1/3, 0]), lpf=0, cut=0, mverb=0, mpf=linvar([200, 12000], 128),   vol=0.5, rate=(0.25, 0.5), oct=7, hpf=linvar([2000, 12000], 32), engine=(3, 10)).unison(2)

#@part16(8)
e3.stop()

#@part17(4)
g1 >> dbass(delay=0.25, dur=1/4, dist2=0, lpf=120, cut=1/2, mverb=0,mpf=linvar([200, 2000], 128), vol=0.5, rate=(0.5, 1)).unison()

#@part18(4)
g3 >> lbass(dur=1/4, hpf=400, drive=0.0, lpf=1200, mpf=1600)

#@part19(4)
g_all.lpr = linvar([0.5, 0.1], [1, 4, 8])

#@part20(4)
e3.dist2 = 0.5

#@part21(4)
g_all.only()

#@part22(4)
Clock.bpm = 122

#@part23(4)
g3.dur = lininf(1/2, 1/8, 32)

#@part24(4)
g3.dist = 0.3
g3.mverb = 0.5

#@part25(4)
g_all.stop()

#@part26(4)
p1 >> pluck(var([([7, 0], 0), [(12, 0), ([Scale.chromatic, 0], 0), (0, [12, 7])]]), oct=(3, PStep(16, 3, 4)), dur=PwRand([[4, 1, 1/2], P[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2]], [1, 30]), leg=linvar([0, 4], PRand(16)[:4]),

#@part27(8)
p1 >> pluck(var([([7, 0], 0), [(12, 0), ([Scale.chromatic, 0], 0), (0, [12, 7])]]), oct=(3, PStep(16, 3, 4)), dur=PwRand([[4, 1, 1/2], P[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2]], [1, 30]), leg=linvar([0, 4], PRand(16)[:4]),            pan=linvar([-1, 1], [32]), scale=Scale.chromatic, drive=var([PWhite(0.01, 0.1), [0, (0.01, 0.2)]]), hpf=PWhite(30, 60), hpr=(0.1, 0.9)).sometimes("stutter", 1, mverb=0.6, feed=0.2, rate=0.2, shape=0.2) + var([0, 3, 4], [PRand([24, 128]), 2, 2])

#@part28(4)
p1.only()

#@part29(4)
p2 >> tb303([var([7, 4, linvar([P[12, 4], P[4, 0]], 4)], [24, 4, 4]), linvar([0, 1])], oct=(var([6, 7, 5, 4]), (PRand(4), 4)), hpf=linvar([(200, 2400), (2000, 1000)],         64), hpr=linvar([0.01, 0.2], 32), dur=1/4, drive=linvar([0.4, 1], 64), vol=0.7, mpf=4000, cut=var([1/4, 1/8], [4, 4]), scale=Scale.chromatic).unison(2)

#@part30(8)
p_all.only()

#@part31(4)
p3 >> tb303(p2.degree, dur=4, cut=[1/4, 1/2, 1/2, 1/4], oct=(3, 5, 7),amp=0.3, echo=P*[0.5, 0, 0.25], shape=1, chop=4).unison(2)

#@part32(4)
p4 >> soprano(p1.degree, dur=PRand(1, 8), blur=PWhite(0, 4), decay=PRand(4), oct=(3, 4, PStep(3, 4, 5)), drive=PWhite(

#@part33(4)
p4 >> soprano(p1.degree, dur=PRand(1, 8), blur=PWhite(0, 4), decay=PRand(4), oct=(3, 4, PStep(3, 4, 5)), drive=PWhite(   0, 0.1), sus=PRand(16), atk=PRand(4), room=0.5, mix=0.5, amplify=0, spin=0, scale=Scale.chromatic).unison(3)

#@part34(4)
p5 >> pluck([(0, 7.01), (0.0, 7.02)], dur=[1/4, 1/2, 1/2, 1/4, 1/2], fmod=p5.dur, leg=0,

#@part35(4)
p5 >> pluck([(0, 7.01), (0.0, 7.02)], dur=[1/4, 1/2, 1/2, 1/4, 1/2], fmod=p5.dur, leg=0,          cut=linvar([1, 2], 16), oct=((3, 6), (4, 5), (5, 6)), hpf=200, amp=0.4, mpf=0, dist=0).unison(0)

#@part36(4)
p1 >> pluck(var([(0, 0), [(12, 0), ([6, 0], 0), (0, [12, 7])]]), oct=(3, PStep(16, 3, 4)), dur=[1/2, 1/4, 1/4, 1/4,

#@part37(4)
Clock.clear()
soff()
Server.clearFx()

#@part38(4)
attack("zip")

#@part39(4)
attack("zip")
##### attack@zip.aij:~$ #####
Clock.bpm = 122/2;
Scale.default = Scale.minor
Root.default = 6

#@part40(4)
##### attack@zip.qur:~$ #####
Clock.bpm = 122/2;
Scale.default = Scale.minor
Root.default = 6

#@part41(4)
f0 >> plaits(melody(),dur=(1/2, 1/4), engine=3, drive=0, mverb=0.8)

#@part42(4)
e1 >> bass(melody(), lpf=1200,dur=var([2, 1, 1/4], [1, 2, 4]), drive=linvar([0, 0.1], 32), mverb=0.5, mverbdiff=0.4).slider()

#@part43(4)
e3 >> bass(melody() + var([7, 3, [4, 0]]),dur=P[1/2, 2], drive=0, oct=4).unison(2).slider()

#@part44(8)
e0 >> plaits(melody() + PWalk(8, 1, 1),dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), drive=0, mverb=0.1, oct=4, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))

#@part45(4)
e0 >> plaits(melody(),dur=(1/2, 1/4), engine=3, drive=0, mverb=0.2, oct=5)

#@part46(4)
e0.dur=4

#@part47(4)
e3 >> bass(melody(),dur=1/4, drive=linvar([0, 0.1], 32), mverb=0.8, delay=var([0, 0.5]), oct=6)

#@part48(4)
e2 >> bass(melody(),dur=var([1/4, 2],[13, 3]), drive=0, mverb=0).unison(2).every(13, "offmul", 2)

#@part49(4)
f0.stop()

#@part50(4)
e1.stop()

#@part51(4)
e0.unison(2)

#@part52(4)
e3.stop()

#@part53(4)
Root.default="G"

#@part54(4)
Root.default="F#"
Root.default="Eb"

#@part55(4)
g2 >> bass(melody() + var([7, 3, [4, 0]]),dur=var([1/4, 1/2]), drive=0, vol=0.5, mverb=0.1).unison(0)

#@part56(4)
g2 >> dbass(dur=1/4, echo=var([1/3, 0]), lpf=0, cut=0, mverb=0.04, mpf=linvar([200, 12000], 128), vol=0.5, rate=(0.25, 0.5), oct=7, hpf=linvar([2000, 12000], 32), engine=(3,10)).unison(4)

#@part57(4)
e1 >> plaits(melody(),dur=var([1/2, (1/2, 2)]), mverb=0.8, engine=var([11, 5], [3, 1]), oct=4, amp=PWhite(0, 1))

#@part58(4)
g1 >> dbass(delay=0.25,dur=1/4, dist2=0, lpf=120, cut=1/2, mverb=0.01, mpf=linvar([200, 2000], 128), vol=0.5, rate=(0.5, 1)).unison()

#@part59(8)
g3 >> lbass(dur=1/4, hpf=400, drive=0.0, lpf=1200, mpf=1600)

#@part60(32)
Clock.clear()
soff()
Server.clearFx()

#@part61(4)
attack("zip")

#@part62(4)
attack("zip2")

#@part63(4)
attack("zip2")

#@part64(4)
Clock.clear()
soff()
Server.clearFx()

#@part65(16)
rec_stop()

#@endfade(16)
