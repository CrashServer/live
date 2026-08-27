# gabber trone 128
# hiphop

# hiphop intro

Clock.bpm = 128
Scale.default = "minor"
j1 >> bass([12, 11, 1, 0.5, 4, _, 4, _], oct=(4, 5, 6), dur=PDur(3, 8), shape=j1.degree==2,shift=j1.degree==1,dist2=j1.degree==0.5,mverb=(j1.degree==4)/4, echo=0.5, leg=4).unison(4)
j0 >> play("g ", rate=-0.5, a=0.2, delay=4, dur=(4, 2, 1), sample=(2, 7, 8))
j2 >> varsaw(j1.degree,oct=(3, 4, 5, 6), rate=0.5, dur=1/2, dafilter=0.5, lpf=1200, mpf=1200, lpr=0.2).unison(4)
j3 >> bass([12, 11, 4],dur=1/4, amp=j1.degree==4, oct=(4, 5), leg=40, vol=1, dist2=1)
j4 >> bass(P*[12, 11, 4],dur=var([1/2, 1], [3, 1]), shape=j4.dur-1/2, dafilter=0.1, amp=0.7, oct=var([ (4, 5, PRand([3, 4,5, 6])), 3], PRand([4, 8, 16, 32])), leg=PRand(128), vol=1, dist2=1).unison(4)

gu >> loop("cinambi8", dur=8, sample=var([3, 4, 5]), amp=0.91, fx1=0)
tv >> loop("hiphop16", dur=16, sample=[4, 7])
pe >> loop("nobledrum32", dur=32, sample=8, sbrk=0.0)
bo >> loop("dnbfx16", dur=16, sample=4, amp=0.8, fx2=1)

bf >> loop("dnbfx16", lofi=0.5, dur=16, sample=5, amp=0.8, fx2=1).unison(2)
bq >> loop("dnbfx16", dur=16, dist2=0.2, sample=6, amp=0.8, fx2=1)

j1 >> plaitsX(PWhite(-0.15, 0.15)*2, dur=ù5, cutoff=40, oct=(5,6,7), follow=PFr(0.4,20), crush=0, bits=2, comp=0, dafilter=PFr(100,2200), dfm=PFr(200,3000), dfmr=0.95, amp=12, hpf=100).sometimes("stutter")

l1 >> loop("rytm8", dur=8, room=0.1, sample=var([8, 4], 4))
l9 >> loop("hiphop16", dur=16, sample=PRand(8), sbrk=0.0, fx2=0.5, fx1=0.5)

#

hihat
a1 >> play("-", fx2=0, rate=PFr(1,2.4), pan=PWhite(-1,1), dur=0.5, hpf=4000).human(40, 5,5)
x1 >> play("k.K.k..k[kk]", sample=0, valad=PFr(400,2000), valadr=PFr(0.7, 0.9)).sometimes("stutter", PRand(4))
f6 >> lbass((PWhite(-0.125, 0.125),PWhite(-0.125, 0.125)), oct=(2,3,4), fx1=1, dur=8, fx2=1) + PwRand([0,PRand(9)],[75,25])

Voix
x3 >> loop("vocalcrash8", hpf=1200, mverb=0.5, fx1=0.5, pos=PWhite(-1,1), sample=PRand(8),dur=16, a=PWhite(0, 1), fx2=0.5, amp=1, clouds=1, clouds_=PWhite(0, 1), csize=PWhite(0.1, 3), csize_=2, csize_d=4).unison(2)
# [gsynth not registered] x4 >> gsynth("vocalcrash8", size=0.5, mring=1.0, density=10, deg=4, amp=0, rmodel=2, rpoly=4, rpos=PWhite(0, 1))

#high pitch intervention
m2 >> plaitsX([0,5,7,3], preset=12, dur=P*[3,rest(1)], oct=5, hpf=3500, mring=1, rstruct=PWhite(0.2,0.7), rmodel=2, fx2=1)

# flat beat

c1 >> cs80(cutoff=linvar([400, 4000], [8, 4, 8]), dec=0.1, detune=1, oct=(4, PStep(4, 3, 4)), vibspeed=P[0.5,2, 4, 2.1], vibdepth=0.2, glide=0.1, dur=2, shape=0.1, fx1=1).unison(4)

x4 >> play("k{o.}{cuc.}.", bank=1, sample=var([4, 2, 8]), fx1=0.5)
u3 >> pbass(dur=ù, oct=(5,6), dafilter=10 + 2400*é32, pan=0, spin=0.5, darq=è32, mverb=0.5).slider()

y1 >> plaitsX([0,[P+[7,5], P+[1,2,PRand(8),7]]], preset=(11,12), dur=16, oct=(2,3,PStep(5,5,4)), dfm=PRand(900,5200)*1, dfmd=1, tremolo=PStep(8,4,0), tremolo_=0.5, dfmr=0.69, fdecay=1, mverb=0.8, amp=1)

y2 >> superbass(P+(0,[7,5,3],2,[-2,1,4,6,9]), dur=2, oct=var([4, (4,5), (4,5,6)], [16,8,8]), hpf=0, cutoff=PFr(2800,6000), fdecay=PFr(1.0,2.0), sub=2, krush=1)

~p9 >> plaits(P[0,4,8,7], dur=1/4, oct=(3,4), harm=0.50, timbre=0.6, morph=0.94, engine=2, fdecay=1.8, cutoff=9000, bright=PFr(0.9,0.99), aux=0, porta=0.09, dist2=0.6) + var([0,7],8)

~p9 >> plaits(P[0,4,8,7], dur=1/2, oct=PStep(6,P*[5,4],3), harm=0.01, timbre=0.4, morph=0.99, engine=1, fdecay=3, cutoff=4000, bright=PFr(0.5,0.99), aux=1) + var([0,-2],8)

~p9 >> plaits(P[0,4,8,7], dur=1/4, oct=(3), harm=0.50, timbre=0.6, morph=0.84, engine=2, fdecay=1.8, cutoff=9000, bright=PFr(0.8,0.99), aux=0, porta=0.99, dist2=0.8) + var([0,2],8)

h3 >> play("-", dur=[1/4, 1/2],low=0, high=[4, 4, 2, 12,  12], echo=0.25, lpf=4400, amp=32).human(60,6,3)
h4 >> play("d", dur=PDur(3,12,0,1/3), pan=PWhite(-1, 1))

y1 >> plaits([0,[P+[7,5], P+[1,2,PRand(8),7]]], preset=(11,12), dur=4, oct=(2,3,PStep(5,5,4)), dfm=PRand(900,5200)*1, dfmd=1, tremolo=PStep(8,4,0), tremolo_=0.5, dfmr=0.8, fdecay=1, mverb=0.8, amp=0)

# melodic bass with PGroup, play with fdecay
y2 >> supersaw(P+(0,[7,5,3],2,[-2,1,4,6,9]), dur=16, a=0.1, oct=var([4, (4,5), (4,5,3)], [16,8,8]), hpf=0, cutoff=PFr(800,2000), fdecay=PFr(1.0,1.2), sub=2, krush=0.1, mverb=0.7)

~p9 >> plaits(P[0,4,8,7], dur=1/2, oct=PStep(6,P*[5,4],3), harm=0.01, timbre=0.8, morph=0.99, engine=8, fdecay=3, cutoff=4000, bright=PFr(0.5,0.99), aux=1) + var([0,-2],8)

j2 >> cbass(PWhite(-0.15, 0.15)*2, dur=ù5, cutoff=4000, oct=(5,6,7), follow=PFr(0.7,20), crush=0, bits=8, comp=0, dafilter=PFr(4,2200), low=12, leg=12, bpf=120, dfm=PFr(200,5000), dfmr=0.2, amp=0.6, hpf=0).sometimes("stutter")

d2 >> play("-.--.:.-.", dur=1/4).sometimes("trim", 3, cycle=[0,3])

# --------------------
j2 >> cbass(PWhite(-0.15, 0.15)*2, dur=ù5, cutoff=4000, oct=(5,6,7), follow=PFr(0.7,20), crush=0, bits=8, comp=0, dafilter=PFr(4,2200), low=12, leg=12, bpf=120, dfm=PFr(200,5000), dfmr=0.2, amp=0.6, hpf=0).sometimes("stutter")

c1 >> cbass(PArp(I, 12), dur=1/2, cutoff=1, follow=20, boost=1, oct=(5,6))

c1.follow=PFr(1, 32, 4, 8)
c1.slider()
c1.leg=0
c1.mverb=0.5
c1.fx1=PFr(0.1, 0.5, 4, 8)

Clock.bpm = 160;

q1 >> loop("nbvarp16", dur=32, sample=6, hpf=1200, hpr=0.1).unison(2)
q2 >> loop("nbvarp16", dur=32, sample=7, hpf=2400, hpr=0.1).unison(2)
q3 >> loop("nbvarp16", dur=64, sample=8, hpf=0, hpr=0.1).unison(2)

q4 >> loop("nbvarp16", dur=64, sample=9, delay=32, shape=0.3, hpf=0, hpr=0.1).unison(2)

c1.leg=PFr(1, 4, 0, 8)
c1.echo=0.5

f3 >> loop("nbvarp16", dur=64, sample=10, delay=16, shape=0.6, hpf=0, hpr=0.1, shift=2).unison(2)
q5 >> loop("nbvarp16", dur=32, sample=5, delay=0, shape=0.0, hpf=0, hpr=0.1).unison(2)

q_all.sample=PRand(16)[:4]

x1 >> play("x ", sample=7, fx2=0.5, amp=2)

b3 >> dbass(P[0, 0, 2, 1, 4, 2, 3, 3], dur=2, fx2=0.2, hpf=400, lpf=1200)
b4 >> superbass( [0,0,7,-12,0,-1,-12,3,0,-2,4,-12], dur=[1.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.75, 0.25, 0.5, 0.25, 0.25, 0.5], sus=[1.2, 0.15, 0.2, 0.4, 0.2, 0.15, 0.6, 0.2, 0.4, 0.15, 0.2, 0.35], amp=P*[0.7, 0.4, 0.5, 0.8, 0.4, 0.5, 0.7, 0.4, 0.6, 0.4, 0.5, 0.8], lpf=sinvar([300,1200], 8), shape=0.3, shape=1,bend=0.1, oct=6, hpf=linvar([40, 1600], [24, 8]), hpr=linvar([0.5, 0.1], 128), lpr=0.5, leg=32, fx1=0.4).unison(8).slider()
h1 >> play("---(-(-=:))", sample=3, dur=1/4, amp=1, lpf=PFr(140, 8000, 440))
u3 >> play("C.(*c)(..(.c)[cc])", sample=4, fx2=1).sometimes("stutter")

b1 >> plaits(0, engine=8, oct=(3,4,5), dfm=linvar([400,1800], [32,0]), dfmr=0.90, harm=0.01, morph=linvar([0.6, 0.99],[32,0]), fdecay=PFr(0.1,1), dur=1/2, delay=0, amp=[0,1], echo=0.22)

k3 >> plaits([0, 0, 4, 2, 4],lpf=12000, dur=1, echo=var([0.25, 0.5], [8, 4]), oct=3, engine=1,  fold=linvar([0.1, 0.6], 32), lpr=linvar([0.05, 0.5], 128), mpf=linvar([500, 4000], 64), mverb=0.2, dist2=1, bpf=1200, cut=1).unison(0)
k4 >> plaits([0, 0, 4, 2, 4],lpf=12000, dur=1, echo=var([0.25, 0.5], [8, 4]), oct=3, engine=1,  fold=linvar([0.1, 0.6], 32), lpr=linvar([0.05, 0.5], 128), mpf=linvar([500, 4000], 64), mverb=0.2, dist2=1, bpf=1200, cut=1).unison(4)

x4 >> play("<X.><..|@4|.>", sample=7, amp=2).every(3, "stutter")
o6 >> play("kk[kpk]KkB",  dur=[1/3, 2/3], sample=(5,4)).sometimes("stutter", shape=0.4)

a1 >> swiss(oct=(3,4), chop=2, detune=0.6, fdist=PFr(400,2000), mverb=0.2, dur=PDur([6,3,2],8), fx=1, amplify=PBin()*0.3, vol=0.4, blur=PFr(0.5,2)).unison(4)

c4 >> play("kfc", dist2=1, sample=3, cut=1, rate=[1,PWhite(-0.4, -0.99)]).sometimes("stutter", 4, crush=3, bits=4)

l6 >> loop("indus32", dur=32, sample=2, fx=1, amp=2, fx2=1, rate=1)
l5 >> loop("circledrum8", dur=8, sample=1, dist2=0, fx=1)

Clock.bpm = 160;

l1 >> loop("berlin8", dur=8)

q1 >> loop("nbvarp16", dur=32, sample=6, hpf=1200, hpr=0.1).unison(2)
q2 >> loop("nbvarp16", dur=32, sample=7, hpf=2400, hpr=0.1).unison(2)
q3 >> loop("nbvarp16", dur=64, sample=8, hpf=0, hpr=0.1).unison(2)

q4 >> loop("nbvarp16", dur=64, sample=9, delay=32, shape=0.3, hpf=0, hpr=0.1).unison(2)
q9 >> loop("nbvarp16", dur=64, sample=10, delay=16, shape=0.6, hpf=0, hpr=0.1, shift=2).unison(2)

q5 >> loop("nbvarp16", dur=32, sample=5, delay=0, shape=0.0, hpf=0, hpr=0.1).unison(2)

l1 >> loop("rage160", dur=32, sample=1, hpf=1200)

q2 >> loop("rage160", dur=32, sample=2)
l3 >> loop("rage160", dur=32, sample=4, echo=0.5)

l4 >> loop("rage160", dur=32, sample=5, dist2=0.0)

q_all.sample=PRand(16)

l5 >> loop("rage160", dur=32, sample=5)

e1 >> fbass([8, 2],amp=[1, 0.5], dur=1/4, oct=7, hpf=linvar([800, 3200], 64), hpr=0.1)

l6 >> loop("rage160", dur=32, sample=6)
l7 >> loop("long64", dur=32, sample=0)

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

# [breakcore not registered] i2 >> breakcore("psych32", dur=4, shift=0.4)

i_all.only()

q5 >> loop("circlebreak16", dur=16, lofi=1)
l9 >> loop("rage160", dur=32, sample=17)
l9 >> loop("rage160", dur=32, sample=18)

q2 >> loop("core16", dur=32, sample=PRand(8))

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

masterAll("mverb", 0.8)
masterAll("feed", 0.5)

Clock.bpm = 96

p1 >> pianovel(melody()[:4], amp=0.8, mverb=0.5, bpf=200).gtr(1).penta().solo(1)
p2 >> pianovel(melody()[:4], dur=2, oct=6, amp=0.8, mverb=0.5, bpf=linvar([400, 800, 1600])).gtr(1)
p3 >> pianovel(melody()[:8], dur=PDur(3, 8), oct=7, amp=0.8, mverb=0.5, bpf=linvar([400, 800, 1600])).gtr(1)
p4 >> pianovel(melody()[:9], amp=1, mverb=0.5, bpf=200).gtr(1).penta()
p5 >> pianovel(melody()[:10], dur=1/4, oct=6, amp=0.8, mverb=0.5, bpf=linvar([400, 800, 1600])).gtr(1)

masterAll(0,"lpf", 1200)

p2 >> organ()
p3 >> organ()
p3.oct=3
p4 >> bell(oct=4)
p5 >> bell(oct=3)

p_all.dur=1/2
p_all.degree=0

p1 >> faim()

gu >> loop("electrodrum32", dur=32, sample=5, amp=0.6)

chaos(8)

gu >> loop("cinambi8", dur=8, sample=4)
bo >> loop("dnbfx16", dur=16, sample=3)
fo >> play("<V.V....V..V.....><................>", dur=0.25, sample=55, rate=1)
to >> organ(P[0, 7, 0, 0], dur=PRy(16,2,0), oct=[5, 6, 5, 5], fmod = [4.07, 2.25, 1.58, 3.21,2.7, 4.25], ).unison(2)
yh >> play("<..T.............><...m..mm........><..........mm.m..><u...u...u...u...>", dur=1, sample=70, rate=1)
ys >> play(".Zv2.B", dur=PShuf([5, 4, 3]), sample=[5,7,8,4,8,5], rate=[3, 2, -1, 3, 0])

tv >> loop("hiphop16", dur=16, sample=[4, 7])

pe >> loop("nobledrum32", dur=32, sample=8)

Scale.default = "minor"

p1 >> pianovel(melody()[:4], amp=0.8, mverb=0.5, bpf=200).gtr(1)
p1 >> pianovel(melody()[:4], amp=0.8, mverb=0.5, bpf=200).gtr(1)
p1 >> pianovel(melody()[:4], amp=0.8, mverb=0.5, bpf=200).gtr(1)
p1 >> pianovel(melody()[:4], amp=0.8, mverb=0.5, bpf=200).gtr(1)
p1 >> pianovel(melody()[:4], amp=0.8, mverb=0.5, bpf=200).gtr(1)
p1 >> pianovel(melody()[:4], amp=0.8, mverb=0.5, bpf=200).gtr(1)

##### attack@trone.uqo:~$ #####
a1.revatk=0
a1 >> angst((var([0,-2,-4,2],8),2,PRand(8)), dur=PDur(5,8)*8, oct=(3,4,[5,[6,2,6]]), room2=0.7, mix2=0.5, damp2=PWhite(0.1,0.8), revatk=PWhite(-3,3), revsus=a1.revatk + PRand(3), shape=0, rate=PWhite(0,16), high=2, mid=0.5, hpf=PStep(8,1400,40), lpf=PRand(500,12000)).slider()

b1 >> pbass(dur=PDur(var([4,P*[5,7,3]],[6,2]),8), rate=expvar([0,16],[64,0]), amp=0.8, oct=(4,PStep(32,6,5))).follow(a1, 8) + var([0,PGauss()],[7,1])

d1 >> play("<(xxx(x.))(...(.x))..><.(---.)><..o.><..(...*).><...{---[--]:=[.x][-o]}><|(XXX(X[.X]))0|.>",sample=((7,6),7,(7,2),7), dur=1/2, amp=0.5, room2=P(0,0.3,0.2,0.3,0.5,0), mix2=0.2, revatk=0.2, revsus=PWhite(0.2,1.7), lpf=0).sometimes("stutter", PRand(4).rnd(2)).rarely("trim",3, cycle=8)
d1.lpf=280

BPM = 66
x1 >> play("k ", bank=1, hpf=PwRand([200,0],[80,20]), fx1=1, amp=0.5, sample=PRand(8)[:6]).drummer().sometimes("amen")

lost()

attack("HEAR ME")

##### attack@HEAR ME.fso:~$ #####

p1 >> plaitsX([4, 0, var([4, 12])], dur=1/4, lpf=linvar([1200, 14000], [24, 8]), bright=linvar([0.5, 0.1], [16, 8]), rq=linvar([0.5, 0.1], [16, 18]), cutoff=4000, porta=linvar([0.5, 0.1], [8, 8]), morph=linvar([0.5, 0.1], [16, 8]), oct=var([2, 3], 16), timbre=linvar([0.1, 0.01], 32), harm=0.1, fdecay=2).unison(4, 0.125)

p2 >> plaitsX([12, 0, 1, 11], dur=1/4, lpf=linvar([1200, 4000], [24, 8]), bright=linvar([0.5, 0.1], [16, 8]), rq=linvar([0.5, 0.1], [16, 18]), cutoff=4000, porta=linvar([4, 0.1], [8, 8]), morph=linvar([0.5, 0.1], [16, 8]), oct=var([3, 4]), timbre=linvar([0.5, 0.9], [16, 18]), harm=var([0.5, 0.3, 0.1], [24, 8, 8]), fdecay=2, leg=32).unison(2).slider()

y2 >> supersaw(P+(0,[7,5,3],2,[-2,1,4,6,9]), dur=16, a=0.1, oct=var([4, (4,5), (4,5,3)], [16,8,8]), hpf=0, cutoff=PFr(800,2000), fdecay=PFr(1.0,1.2), sub=2, krush=0.1, mverb=0.7)

p3 >> plaitsX([(12, 4), 0, 1, 11, 21], dur=1/4, lpf=linvar([12000, 4000], [24, 8]), bright=linvar([1, 0.1], [16, 8]), rq=linvar([0.5, 0.1], [16, 18]), cutoff=12000, porta=linvar([0.5, 0.1], [8, 8]), morph=linvar([0.5, 1], [16, 8]), oct=var([3, 4]), timbre=linvar([0.5, 0.9], [16, 18]), harm=var([0.5, 0.3, 0.1], [24, 8, 8]), fdecay=2, leg=0).unison(2)

x1 >> play("k.K.k..k[kk]", sample=0, valad=PFr(400,2000), valadr=PFr(0.7, 0.9)).sometimes("stutter", PRand(4))

bf >> loop("dnbfx16", lofi=0.5, dur=16, sample=5, amp=0.8, fx2=1).unison(2)
bq >> loop("dnbfx16", dur=16, dist2=0.2, sample=6, amp=0.8, fx2=1)

tv >> loop("hiphop16", dur=16, sample=[4, 7])
pe >> loop("nobledrum32", dur=32, sample=8)

Clock.bpm = 122/2;
Scale.default = Scale.minor
Root.default = "F#"

e0 >> plaits(melody(),dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), shape=0, mverb=0.1, oct=3, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))
e0 >> plaits(melody(),dur=(1/2, 1/4), engine=(1, 4), shape=0, mverb=0.8, oct=5)
e1 >> bass(melody()[:8],dur=var([1/4, 2],[13, 3]), a=PWhite(0, 1), shape=0, amp=0.7, mverb=0.8).unison(2).every(13, "offmul", 2)
e0.every(4, "shuffle")

e1 >> bass(melody(),dur=1/4, oct=5, shape=0, mverb=0.8).unison(0)
e1 >> bass(melody(),dur=1/4, shape=linvar([0, 0.02], 32), mverb=0.8).unison(0)
g2 >> bass(melody() + var([7, 3, [4, 0]]),dur=var([1/4, 1/2]), shape=0, vol=0.5, mverb=0.1).unison(0)

Root.default = "E"
Scale.default = Scale.minor

# Melodic Foundation - Smoother Organ Layers
~r1 >> organ(P[var([0,-2,-3,-4],16), 2, PStep(8,5,4), 2],dur=PDur(6,8),amp=0.7,crush=0.5,bits=8,fmod=0.5,lpf=2000,lpr=0.3,reverb=0.2).spread(2)
# Wider variation
# More breathing room
# Less aggressive bitcrushing
# Higher bit depth
# Gentler frequency modulation
# Lower filter cutoff for warmth
# Softer resonance
# Added subtle reverb
# Wider stereo field

r0 >> organ(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([PDur(4,8),PDur([5,3,6],8)]), amp=1, crush=1, crush_=4, crush_d=2, bits=6, bits_=var([12, 16]), fmod=1, lpf=2800, lpr=0.4).solo(0)
r2 >> organ(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.8, crush=1, crush_=4, crush_d=2, fx2=0.2, bits=6, bits_=var([12, 8]), oct=(5, 7), fmod=1, lpf=2800, lpr=0.2).unison(2).every(4, "shuffle")

e_all.stop()

# Complementary Bell Texture
~r3 >> bell(P[var([0,-2,-3,-4],16), 4, PStep(4,6,8), 2],dur=PDur(5,8),amp=0.5,crush=0.3,mverb=0.3,delay=0.25,oct=(5, 6, 7),lpf=2800,fmod=0.3).every(4, "rotate")
# Slightly irregular rhythm
# Even less aggressive
# Moderate verb
# Subtle echo
# Higher register for airiness
# Brighter top end
# Subtle pattern rotation

e1 >> plaits(melody(),dur=var([1/2, (1/2, 2)]), shape=0, mverb=0.8, engine=var([11, 5], [3, 1]), oct=5).unison(0)

r4 >> bell(P[var([0,-2,-3,-4],8),4,PStep(4,6,8),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.6, crush=1, crush_=4, crush_d=2, mverb=0.2, bits=6, bits_=var([12, 8]), delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")
r5 >> bell(P*[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.5, crush=1, crush_=4, crush_d=2, mverb=0.5, bits=6, bits_=var([12, 8]), r1=0.5, delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")

e0.dur=var([2, 1/4, 1/4, 1/4, 1/4])
e3 >> bass(melody(),dur=1/4, shape=linvar([0, 0.05], 32), mverb=0.8, delay=var([0, 0.5]), oct=6)
e3 >> lbass(dur=1/2, oct=4, shape=1, amp=PBin(8))
e0 >> plaits(melody(),dur=(1/2, 1/4), engine=(1, 4), shape=0, mverb=0.8, oct=5)

r2 >> varsaw(oct=(3, PStep(4, 5, 6), 5), cut=4, cutmix=0.2, lpf=(800, linvar([400, 12000], 128)), dur=[6, 2], sus=[4, 8], lpr=0.1, a=0.5).unison(3)

e3.stop()
g1 >> dbass(delay=0.25,dur=1/4, dist2=0, lpf=120, cut=1/2, mverb=0.01, mpf=linvar([200, 2000], 128), vol=0.5, rate=(0.5, 1)).unison()

g3 >> lbass(dur=1/4, hpf=400, shape=0.0, lpf=1200, mpf=1600)
g_all.lpr=linvar([0.5, 0.1], [1, 4, 8])
e3.dist2=0.5

g_all.only()
Clock.bpm = 122;

# Breakbeat Drum Foundation
~h1 >> play("b(3,8)",sample=var([0,1,2],8),cut=0.1,dur=PDur(3,8),amp=0.8,lpf=1200,hpf=200,pan=PWhite(-0.5,0.5))
# Varied drum samples
# Tighter cuts
# Syncopated rhythm
# Filtered for smoothness
# Low-end warmth
# Subtle stereo movement

h3 >> play("s", valad=PFr(1000,3000)).sometimes("stutter", PRand(16))
n2 >> play("..*.", echo=P*[0,PRand([0.125, 0.5, 0.75])], mverb=0.9, hpf=2000)

g3.dur=lininf(1/2, 1/8, 32)
g3.dist=0.3
g3.mverb=0.5

g_all.stop()

p1 >> pluck(var([([7, 0], 0), [(12, 0), ([Scale.chromatic, 0], 0), (0, [12, 7])]]),oct=(3, PStep(16, 3, 4)), dur=PwRand([[4, 1, 1/2], P[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2]], [1, 30]), leg=linvar([0, 4], PRand(16)[:4]), pan=linvar([-1, 1], [32]), scale=Scale.chromatic, shape=var([PWhite(0.01, 0.1), [0, (0.01, 0.2)]]), hpf=PWhite(30, 60), hpr=(0.1, 0.9)).sometimes("stutter", 1, mverb=0.6, feed=0.2, rate=0.2, shape=0.2) + var([0, 3, 4], [PRand([24, 128]), 2, 2])

e3 >> lbass(dur=1/4, oct=PRand([4, 5, 6])[:4], shape=0.3)
g2 >> dbass(dur=1/4, echo=var([1/3, 0]), lpf=0, cut=0, mverb=0.04, mpf=linvar([200, 12000], 128), vol=0.5, rate=(0.25, 0.5), oct=7, hpf=linvar([2000, 12000], 32), engine=(3,10)).unison(2)

b1 >> bass([0, 7, 5, 4], dur=1/2, amp=0.8, shape=0.1, lpf=800, mverb=0.2)

s2 >> klank(oct=linvar([5, 6], 128), dur=PDur(3, 8)* 2).slider()

r4.oct=7
r4 >> lbass()
q1 >> play("[--]", sample=5)
x1 >> play("x.", sample=var([5, 2], [24, 8]), amp=1, lpf=0)
x2 >> play("u ", sample=3, dur=4, amp=2)

b8 >> lbass(var([0, -2, linvar([-2,0],[8,0])], [16,8,8]), dur=var([1/2,1/4],[24,8]), cutoff=PFr(4000,12000), detune=0.9, amp=0.4, tone=PFr(0.16,0.9), dist2=0.9, oct=var([5,lininf(5,6,8)],[24,8])).stop()

# Bass Layer with Liquid Feel
~b1 >> lbass(var([0, -2, linvar([-2,0],[16,0])], [24,8,8]),dur=var([1/2,1/4],[32,8]),cutoff=PFr(2000,6000),detune=0.1,tone=PFr(0.3,0.7),dist2=0.6,oct=var([4,5,linvar(4,5,16)])).stop()
# More unpredictable
# Gentler filter
# Less aggressive
# Smoother timbre
# Less distortion
# Floating octave

# Atmospheric Pad Layer
~p1 >> varsaw(oct=(4, PStep(4, 5, 6), 5),cut=2,amp=0.5,cutmix=0.1,lpf=(600, linvar([400, 8000], 256)),dur=[4, 8],sus=[6, 12],lpr=0.05,reverb=0.4).spread(3)
# Less abrupt
# Softer filter
# Wider, slower filter sweep
# Longer notes
# Extended sustain
# Very gentle resonance
# More atmospheric
# Wide stereo image

# Glitchy Accent Layer
~n1 >> play(".*.",echo=P*[0, PRand([0.125, 0.25])],mverb=0.5,hpf=1500,amp=0.3)
# Subtle echoes
# Medium verb
# Crisp high-end
# Low in mix

# Final Touch - Gentle Klank Texture
~k1 >> klank(dur=PDur(4, 8) * 2,oct=linvar([5, 6], 256),shape=linvar([0.01, 0.03], 64),reverb=0.3).spread(2)
# Irregular rhythm
# Slow octave modulation
# Very subtle drive
# Spacious

Clock.bpm = 124
Scale.default = Scale.minor
Root.default = "E"
# Main Bassline

b1 >> bass([0, 7, 5, 4], dur=1/2, amp=0.8, shape=1, shape=1, lpf=800, mverb=0.2)
p1 >> pluck(var([0, 7, 4], [8, 4, 4]), dur=1/4, amp=0.4, oct=(4, 5), pan=linvar([-1, 1], 16), shape=0.3).sometimes("stutter", 4)
h1 >> play("---[---]-", dur=1/4, amp=0.5)
h2 >> play("s", dur=1/2, amp=0.3)

t1 >> plaits([0, 7, 4], dur=1/2, engine=var([5, 3], 16), oct=5, amp=0.3, mverb=0.4)

Master().hpf = linvar([0, 400], [32, 16])
Master().hpr = 0.4

# Build Transitions
Clock.every(16, lambda: b1.solo())
b1.solo(-1)

Clock.every(32, lambda: p1.shuffle())

# Drop Variation
# @nextBar
# [broken in source] def drop():
d1.stop()
h1 >> play("Xx-", sample=4, amp=0.9)
p1.amp = 0.2
b1 >> bass([0, 7, 5, 4], dur=1/4, amp=0.6, shape=0.2)

# Reset Groove
# @nextBar
# [broken in source] def reset():
d1 >> play("X", dur=1, amp=1.2, sample=2)
p1.amp = 0.4
b1 >> bass([0, 7, 5, 4], dur=1/2, amp=0.8, shape=0.1)

Clock.schedule(reset, Clock.now() + 64)

# Compact Techno Pattern

Clock.bpm = 128
Scale.default = Scale.minor
Root.default = "F#"

# Core rhythmic elements
k1 >> play('x', sample=0, amp=1.5, room=0.3, verb=0.4)  # Kick
h1 >> play('.-', sample=1, amp=0.7, pan=0.5)  # Hi-hats
p1 >> play('<  >', sample=3, amp=0.5, pan=-0.5)  # Percussion

# Lead synth with evolving parameters
l1 >> plaits(melody(),dur=var([1/2, 1/4]),engine=var([5, 7]),oct=5,shape=linvar([0, 0.2], 32),mverb=0.8).unison(2)

# Bass line with variation
b1 >> bass(melody()[:8],dur=var([1/4, 1/2], [13, 3]),oct=4,shape=linvar([0, 0.05], 32),mverb=0.6).every(8, "stutter", 2)

# Additional rhythmic variation
l1.every(4, "shuffle")
b1.every(6, "offmul", 2)

# Global effects and transitions
g_all.lpr = linvar([0.5, 0.1], [4, 8])
# [broken in source] ?g_all.lpf = linvar([200, 2000], 64)

# Texture layers
t1 >> tb303([var([0, 7, 4], [24, 4]), linvar([0, 1])],oct=(var([5, 6]), PRand(4)),hpf=linvar([200, 2400], 64),dur=1/4,shape=linvar([0.4, 1], 64)).unison(2)

# Final arrangement and transitions
p_all.dur = 8
p_all.lpf = linvar([200, 400], 16)
