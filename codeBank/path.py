
# path

#b1 >> bass(dur=[4, 0.5], sus=4, chopmix=0.5, shape=linvar([0.2, 0.4], 32), a=0.01, leg=-12, leg_=0.1, rate=0.25, chop=(132, 200), lpf=(1200, 4000), lpf_=(3200, 200), chopmix_=1, chop_=(128, 32, 4)).sometimes("stutter", shape=0.5, mverb=1, leg=-128)
#b2 >> dbass(dur=[1/2, 1, 1/4], sus=1/2,amp=[1, 0.5,2, 0], tanh=0.8,chopmix=0.5, chop=(132, 200))

b_all.only()
#-->
b1 >> click(dur=[1/2, 1/4, 1/2, (1/2, 1)], octer=0.6, oct=5, leg=0.2).every(6, "stutter", oct=3, shape=0.1, amp=1)
b2 >> click(dur=P*[1/2, 1/4, 1/2, (1/2, 1)], oct=2, octer=0.2, tanh=0.1).every(6, "stutter", oct=3, shape=0.5, amp=1)
b3 >> click([8, _, 4, 4, 2],dur=[4, 1/2, 1/2, 3], oct=(1, 3), shape=0.2, amp=1)
b4 >> click([8, _, 4, 4, 2],dur=1, oct=(4, 5, PStep(2, 3, 6)), shape=0.2, amp=1)
b5 >> dbass(dur=b1.dur, shape=0.5).unison(4).sometimes("stutter", oct=6, echo=0.5, mverb=1, amp=1).unison(4)


b1 >> click(dur=[1/2, 1/4, 1/2, (1/2, 1)], octer=0.6, lpf=linvar([400, 4000], 32), lpr=0.4).every(6, "stutter", oct=3, shape=0.5)
b2 >> click(dur=P*[1/2, 1/4, 1/2, (1/2, 1)], oct=4,octer=var([0.2, 1.2], [5, 3]), tanh=0.3).every(6, "stutter", oct=3, shape=0.5, hpf=400)
b3 >> click([8, _, 4, 4, 2],dur=Pvar([1/2, 1/4,4]), oct=(4, 5), shape=0.5, mpf=1800, mverb=0.2)
b4 >> click([8, _, 4, 4, 2],dur=var([1/4, 1, 1/2], [5, 3, 2]), oct=(4, 5, PStep(5, 4, PRand([3, 5]))), shape=0.5).sometimes("offadd", 4)
k1 >> dbass(dur=b1.dur, shape=0.4).unison(4).sometimes("stutter", oct=4, echo=0.5, mverb=1)
b_all.oct=3



k1.stop()

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

d2 >> play("?.O.", sample=4, rate=0.5, a=0.2, shift=1.4, mverb=1, amp=1, dur=4)

d_all.solo(1)
b_all.oct=4

c1 >> ikea(dur=2, tanh=1, oct=4).stop()

b_all.dur=8

b_all.stop()

c2 >> dbass(dur=1/8, cut=var([1/4, 1/3, 1/2], [5, 2, 1]), amp=[1, 0.75, 0.5, 0.25], shape=0.45, dist2=0.5)

e1.stop()



