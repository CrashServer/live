# live definitif 78
# live

Clock.bpm = 78
v1 >> play("x", bank=2, sample=var([ [41, 45, 48, 24], P[1:100]]),rate=1, dur=1, lpf=0, amp=linvar([0.5, 1,1.5], PRand(16)[:4]), dist2=0.7)
v2 >> play("v ", bank=2, dur=2, sample=14, amp=2)
v3 >> play("v ", bank=2, sample=PRand(128), dur=1/2, rate=(0.5,1,2), echo=0.5)
v3.rate=0.25
v2.rate=0.5
k4 >> loop("long64", dur=64, amp=1, sample=2)
v2 >> loop("dnbfx16", dur=16, amp=0.5, sample=1)

t1 >> play("M[mm]T.", rate=1, leg=1, low=12, amp=PBin(16))

v1 >> play("C ", rate=0.5, hpf=400)
v3 >> loop("indus32", dur=32)
v1 >> loop("indus32", dur=32, sample=PRand(17))

v1.hpf=0

t1 >> dbass(dur=var([1, PDur(3, 8)]), rate=2, shape=0.3)

~v1 >> play("x", bank=2, sample=var([ [41, 45, 48, 24], P[1:100]]),rate=1, dur=1, lpf=0, amp=linvar([0.5, 1,1.5], PRand(16)[:4]), dist2=0.7)
~v2 >> play("v ", bank=2, dur=2, sample=14, amp=2)
~v3 >> play("v ", bank=2, sample=PRand(128), dur=1/2, rate=(0.5,1,2), echo=0.5)
v2 >> loop("xbassphase16", dur=16)
k4 >> loop("xbassphase16", dur=16)

v3.stop()

v_all.only()
k_all.only()
v0 >> play("c ", bank=2, sample=PRand(8), dur=1/4, lpf=400, lpr=0.1, leg=4)
k4.stop()

a2 >> play("B", bank=2,sample=(P[0:10], P[0:50]), dur=4, mverb=0.5, hpf=40, leg=0.5)
v1 >> play("v ", dur=var([2, 4, PDur(5, 8)]), bank=2, sample=P[0:70], mverb=0.5, chop=0, shift=(0.5, 1)).unison(4)
v2 >> play(" V", dur=P[PDur(3, 8), 4], bank=2, sample=P[0:30], mverb=0.5, amp=2, rate=(0.5, 1))
e0 >> play("m ", dur=2, rate=(0.5, 1), bank=2, sample=P[0:70], mverb=0.5, chop=0, sbrk=0).unison(4)

j1 >> bass([12, 11, 1, 0.5, 4, _, 4, _], oct=(4, 5, 6), dur=PDur(3, 8), shape=j1.degree==2,shift=j1.degree==1,dist2=j1.degree==0.5, lpf=3200, lpr=0.1, mverb=(j1.degree==4)/4, echo=0.5, leg=4).unison(4)
j4 >> plaitsX(j1.degree,dur=Pvar([1/2, 1/4], [4, 16])).unison(4)
j3 >> fbass([12, 11, 1, 0.5, 4, _, 4, _], oct=(4, 5, 6), dur=PDur(3, 8), shape=j1.degree==2,shift=j1.degree==1,dist2=j1.degree==0.5,mverb=(j1.degree==4)/4, echo=0.5, leg=4).unison(4)

j_all.only()

k1 >> donk(dur=[1/4, 4], lpf=1200, oct=(3, PStep(4, 4, 5)), chop=21, chopmix=0.5)
k0 >> donk(linvar([6, 0], 8),dur=1/2, lpf=6400, oct=(3, PStep(4, 4, 5)), chop=12, chopmix=0.5)
k2 >> play("x", amp=k1.dur==1/4, echo=(0.5, 0.75, 1.25), sample=(2, 4, 1, 3), leg=(0, 120, 4, 128), lpr=0.1, lpf=4000)
k3 >> play("[xx]", amp=k1.dur==1/4, echo=(0.5, 0.75, 1.25), sample=(8, 4, 7, 1), leg=(0, 120, 4, 128), delay=(2, 3), lpr=0.1, lpf=2000)
k4 >> play("[kk]", amp=k1.dur==4, echo=(0.5, 0.75, 1.25), sample=(8, 4, 7, 1), leg=(0, 120, 4, 128), delay=(2, 3), lpr=0.1, lpf=2000)

d1 >> donk([0, 1, (-3, -8)],dur=(4, 8), lpf=(1200, 3200), a=0.5, oct=(5, 6, 7)).slider()
d0 >> donk([0, 1, -12.5], dur=4)
d2 >> donk([0, 1, (-3, -8)],dur=(4, 8), lpf=(8000, 3200), a=0.1, oct=(5, 6, 7)).slider().unison(4)
d3 >> donk([0, 1, (-3, -8)],dur=1/2, lpf=(8000, 3200), a=PWhite(0, 0.5)[:8], oct=(3, 4, 5)).slider().unison(4)

d_all.dur=1/2
d_all.oct=3
d_all.hpf=1200

e1 >> lbass(dur=PDur(5, 15), crush=4, leg=4)
f2 >> plaitsX([6, 7, 11, 6, 7, 11],dur=PDur(9, 15), crush=0, leg=0, amp=6, lpf=linvar([100, 12000], 32), dist2=0, oct=4, preset=10)

d3.dur=2
d3.sus=2
d3.lpf_=3200
d3.degree=-40
d3.shape=4

d0 >> play("u x ")

Clock.bpm = 160;
l1 >> loop("berlin8", dur=8, sample=1)

q1 >> loop("nbvarp16", dur=32, sample=6, hpf=1200, hpr=0.1).unison(2)
q2 >> loop("nbvarp16", dur=32, sample=7, hpf=2400, hpr=0.1).unison(2)
q3 >> loop("nbvarp16", dur=64, sample=8, hpf=0, hpr=0.1).unison(2)

l1.sample=3

q4 >> loop("nbvarp16", dur=64, sample=9, delay=32, shape=0.1, hpf=0, hpr=0.1).unison(2)
q9 >> loop("nbvarp16", dur=64, sample=10, delay=16, shape=0.1, hpf=0, hpr=0.1, shift=2).unison(2)

l1.sample=6
q5 >> loop("nbvarp16", dur=32, sample=5, delay=0, shape=0.0, hpf=0, hpr=0.1).unison(2)

l1 >> loop("rage160", dur=32, sample=1, hpf=1200)

l0 >> blip(PSine(32), dur=1/4, oct=6, amp=PBin(32), echo=0.5, mverb=0.5).stop()

e1 >> loop("ysyn64", dur=64).stop()

q2 >> loop("rage160", dur=32, sample=2)
l3 >> loop("rage160", dur=32, sample=4, echo=0.5)

l4 >> loop("rage160", dur=32, sample=5, dist2=0.0)

q_all.sample=PRand(16)

l5 >> loop("rage160", dur=32, sample=5)

e1 >> fbass([8, 2],amp=[1, 0.5], dur=1/4, oct=7, hpf=linvar([800, 3200], 64), hpr=0.2)

l6 >> loop("rage160", dur=32, sample=6)
l7 >> loop("long64", dur=32, sample=0)

l7 >> loop("rage160", dur=32, sample=14)
#
x1 >> play("K ", amp=16, dur=8)

l8 >> loop("rage160", dur=32, sample=13)

e1.hpr=0.2

l9 >> loop("rage160", dur=32, sample=17)

k4 >> loop("nsbass16", dur=16, amp=2)

x1.dur=[1, 1, 1, 2, 1, 1/2, 1/2]
x2 >> play(".-", amp=16, dur=1/2)

o1 >> organ(dur=x1.dur,  oct=(7, 6))

l9 >> loop("rage160", dur=32, sample=18)

l_all.dur=16
l_all.amp=0.5

l_all.sample=PRand(16)[:4]

o1 >> varsaw(lpf=400)

i1 >> loop("rageclean32", dur=32, sample=4)
i2 >> loop("ragegrowl16", dur=16, sample=2, mverb=0.6)

q1 >> loop("nsbass16", dur=16)
l_all.stop()

# [breakcore not registered] i2 >> breakcore("psych32", dur=4, shift=0.4)

i_all.only()

p1 >> play("X[xx]")

q5 >> loop("circlebreak16", dur=16, lofi=1)
l9 >> loop("rage160", dur=32, sample=17)
l9 >> loop("rage160", dur=32, sample=18)

q4 >> play("X ", shape=1)

b1 >> plaitsX(dur=var([2, 1], [16, 8]), slide=(0.01, (-0.03, 0.04)), slidedelay=(0.01, 0.1, 4), oct=(3, var([4, 5]), PRand([3, 4, 5, 6])), preset=var([0, 4, 12]), slidefrom=(0, 0.02, 0), sus=var([2, 3, 1], [4, 2]), shift=var([0.5, 1, 0.75]), amp=2).unison(2)

attack("trap")

##### attack@trap.ndn:~$ #####
d0 >> play(".{...u}..u...", sample=5, hpf=var(PRand(4000)+10), rate=(.5,2)).sometimes("stutter")
d1 >> play(".{...c}..c...", sample=5, mverb=0, flanger=0, chorus=var(PWhite(0, 1)), amp=P*[0, 1], rate=(P*[.5,.5,.5,-1],2))
d2 >> play("v.....(...{v.})(...{.v}))", cut=2, sample=8, hpf=50, shape=(0,var(PWhite(0,0.2)))).sometimes("stutter")
d3 >> play("v.....(...{v[vv].}).", sample=8, delay=0.5, hpf=400, amp=var([0, 1], [28, 4]))
d4 >> play("(...(.p)).((p.).(p.).)((p.).(p.).)", dur=1/4, sample=4, crush=8,bits=8)
d5 >> play("-{-[--]}-.-{[---][--]}(-.)(-[----])", sample=2, amp=PCoin(PWhite(0, 1),0,0.5), hpf=6000, pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble").sometimes("stutter", PRand(16), rate=PWhite(-1,5))

b1.sbrk=0.4
d6 >> play("---.-{[---][--]}(-.)(-[----])", hpf=5000, sample=10, amp=PCoin(PWhite(0, 1), 0, 0.5), pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble")
d7 >> play("---.-{[---][--]}(-.)(-[----])", pan=PWhite(-1, 1), hpf=4000, amp=PCoin(PWhite(0, 1), 0, 0.5), sample=8).sometimes("amen").sometimes("bubble").every(4, "shuffle")

d_all.only()

lost()

attack("A2")

##### attack@A2.zuh:~$ #####
Scale.default="minor"
a1 >> bass([(0, 4, 2), [V, III, II, III, II]], amp=1, dur=4, a=2, oct=var([5, 7, [5,4, 5]]))

a2 >> lbass((0, 4, 2) + var([2, 4]), amp=0.5, dur=var([1/2, PDur(3, 8)]), a=var([0.5, 1, 0], [8, 4, 2]))

a3 >> varsaw(dur=8, lpf=1000,mverb=0.6, a=2, oct=(5, 6, 7), hpf=200).unison(4)

lost()

attack("A2_96")

##### attack@A2_96.zru:~$ #####

##### attack@zika.qya:~$ #####

p1 >> ebass(PSine(64)*0.2, oct=(var([(3,4),[5,6]],[6,2])), dur=PDur([5,7],8), sus=p1.dur*0.7, cutoff=7000, lforate=var([1,2,4],8), lfowidth=linvar([0.1,1],39), pan=[-1,1], amp=2)

los
s
