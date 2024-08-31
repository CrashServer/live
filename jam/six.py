
Clock.bpm = 160;

l1 >> loop("berlin8", dur=8)

d1 >> dbass(-3, dur=var([1/2, 4]),oct=6, dist2=1, amp=0.25, lpf=1200, lpr=0.3).chroma().solo(0)
d2 >> abass([0, -3], dur=var([1/2, 4]),oct=(4, 5), dist2=1, amp=0.125, lpf=1200, lpr=0.3).chroma()

q1 >> loop("nbvarp16", dur=32, sample=6, hpf=1200, hpr=0.1).unison(2)
q2 >> loop("nbvarp16", dur=32, sample=7, hpf=2400, hpr=0.1).unison(2)
q3 >> loop("nbvarp16", dur=64, sample=8, hpf=0, hpr=0.1).unison(2)

q4 >> loop("nbvarp16", dur=64, sample=9, delay=32, shape=0.3, hpf=0, hpr=0.1).unison(2)
q9 >> loop("nbvarp16", dur=64, sample=10, delay=16, shape=0.1, hpf=0, hpr=0.1, shift=2).unison(2)

q5 >> loop("nbvarp16", dur=32, sample=5, delay=0, shape=0.0, hpf=0, hpr=0.1).unison(2)

l1 >> loop("rage160", dur=32, sample=1, hpf=1200)

d1.dur=PDur(3,8)
d2.dur=PDur(5,8)

d2.hpf=4000

q2 >> loop("rage160", dur=32, sample=2)
l3 >> loop("rage160", dur=32, sample=4, echo=0.5)

d3 >> dbass([-2, -2, -3, _], dur=[1/2, 1/2, 1/2, 1.5], sus=[1/2, 1/2, 1.5, 1], oct=7).chroma()

l4 >> loop("rage160", dur=32, sample=5, dist2=0.0)

q_all.sample=PRand(16)

l5 >> loop("rage160", dur=32, sample=5)

e1 >> fbass([8, 2],amp=[1, 0.5], dur=1/4, oct=7, hpf=linvar([800, 3200], 64), hpr=0.1)

l6 >> loop("rage160", dur=32, sample=6, amp=0.5)
l7 >> loop("long64", dur=32, sample=0, amp=0.5)

e4 >> blip([10,7, 6, 10, 7, 6, 10, 7, 4], dur=1,amp=2, mverb=1).chroma().solo(0)   
l7 >> loop("rage160", dur=32, sample=14)
#
l8 >> loop("rage160", dur=32, sample=13)

e1.hpr=0.05

l9 >> loop("rage160", dur=32, sample=17)

#
l9 >> loop("rage160", dur=32, sample=18)

l_all.dur=16
l_all.amp=0.5

l_all.sample=PRand(16)[:4]

i1 >> loop("rageclean32", dur=32, sample=4)
i2 >> loop("ragegrowl16", dur=16, sample=2, mverb=0.6)

q1 >> loop("nsbass16", dur=16)
l_all.stop()

i2 >> breakcore("psych32", dur=4, shift=0.4)

i_all.only()

q5 >> loop("circlebreak16", dur=16, lofi=1)
l9 >> loop("rage160", dur=32, sample=17)
l9 >> loop("rage160", dur=32, sample=18)


q2 >> loop("core16", dur=32, sample=PRand(8))

q4 >> play("X ", shape=1)

b1 >> plaitsX(dur=var([2, 1], [16, 8]), slide=(0.01, (-0.03, 0.04)), slidedelay=(0.01, 0.1, 4), oct=(3, var([4, 5]), PRand([3, 4, 5, 6])), preset=var([0, 4, 12]), slidefrom=(0, 0.02, 0), sus=var([2, 3, 1], [4, 2]), shift=var([0.5, 1, 0.75]), amp=2).unison(2)
