# nuance

###### SET DEFINTIF NUANCE #####

### LOW TEMPO
## INTRO CHIANTE
Clock.bpm = 128
~j1 >> play("<B.BBv.Bv><v.Bbv.Bv><(...:)>", sample=(6, 6, 4), hpf=(200, var([200, 0, 30, 20]), 0), cut=(0, 0, 0.1), leg=0)
j3 >> play("T..h hh4. Tbbb mbbb", sample=4, cut=1/8)
~j2 >> play("b ", sample=8, dur=PDur(5, 8), cut=1/2, mverb=0.2, hpf=var([0, PWhite(0, 1200)[:4]]))
~j2 >> play("b ", triode=1, octafuz=1, octamix=PWhite(0.2, 0.6), sample=8, dur=PDur(5, 8), cut=1/2, echo=0, mverb=0.2, hpf=var([0, PWhite(0, 1200)[:4]]))
~j1 >> play("<B.BBv.Bv><v.Bbv.Bv><(...:)>", sample=(6, 6, 4), hpf=(200, var([200, 0, 30, 20]), 0),  cut=(0, 0, 0.1), dur=1/2, vadiod=500, vadiodr=0.5, vadiodd=4)
# l4 >> loop("choir16", dur=16, sample=2, coarse=1, mring=1, amp=2, chop=4, rstruct=1, rbright=4, rdamp=0.4, rpos=0.5, rmodel=2, rpoly=1, regg=0.4, rsus=2).unison(2)
j1 >> play("B.BB")
j1 >> play("BVBB")
j1 >> play("<BVBB><:>", echo=1)
m9 >> play("..c.", sample=4)

#####################################
# ALL THAT JAZZ
Clock.bpm=128
u7 >> loop("electrodrum32", dur=32, sample=2, mverb=0)
u4 >> loop("industia16", dur=16, sample=2)

c5 >> loop("jazzc8", dur=8, sample=7, comp=1)
j8 >> loop("jazzguitar8", dur=8, sample=4)
g0 >> noloop("fx4", dur=8, sample=1, rate=.1)

g8 >> play("<k(...[--])><-:><..*.>", sample=1, amp=1, bank=1, dur=1/2, rate=1, cut=1.2).sometimes("stutter")
g8.cut=0

e4 >> play("a", bank=2, dur=PDur([4,3,5],8), sample=PFr(0,88,1664,4), rate=.4, valad=1000, valadr=0.5, valadd=25, valadt=ê*4, valadc=0.2)

s5 >> plaitsX(preset=14, harm=PWhite(-1,1), morph=PWhite(-1,1), pan=PWhite(-1,1))

##### MID TEMPO #######
#N2COREGRAT
Clock.bpm=132
t0 >> loop("gcindrum16", dur=16, sample=2, chop=4, hpf=400, hpr=0.1)
t2 >> loop("xbass16", dur=16, shape=0, sample=5)
t3 >> loop("xxperc8", dur=8, sample=2)
s2 >> loop("ragegtr8", dur=8, sample=3, chop=8, delay=2)
s1 >> loop("core16", dur=16, sample=1)

l4 >> loop("cyber8", dur=8, sample=1, amp=1)
t7 >> play("W.", sample=2)
t0.sample=4
s1.sample=4

#N3RR0R@NU@NC35
Clock.bpm=132
p1 >> loop("uk16", dur=16,pos=0, room=0.1, sample=3, beat_stretch=1, looping=1.0)
p3 >> loop("hiphop16", dur=16,pos=0, room=0.1, sample=0, beat_stretch=1, looping=1.0)
g2 >> loop("xtech8", dur=8, comp=1)
s3 >> play("X.")
s4 >> loop("xvermin16", dur=16, sample=4)
u9 >> loop("wa8", dur=8, comp=1, lofi=0, mverb=.1)
c9 >> loop("synth4", dur=4, sample=3, amp=1, mverb=0.5)
# v1 >> noloop("vocalinfi4", dur=8, sample=[1,0], trig=0, delay=0, mverb=.6, lofi=.8, amp=.7)
c9.sample=6 # 6 7

###########
#N4PsyTransse 
Clock.bpm = 148;

e9 >> loop("seq16", dur=16, sample=10, comp=1)
i4 >> loop("psybass32", dur=32,pos=0, amp=1, room=0.1, sample=8, beat_stretch=1, looping=1.0)
i5 >> loop("psydrum32", dur=32, sample=8) #[0-5-8]
z4 >> loop("psych32", dur=32, sample=4, fx1=0, fx=0, hpf=200)
y8 >> four(linvar([0,2],64), fx2=0, tremolo=P*[2,4,8], amp=.8, mverb=0.5, shape=.5, pan=PWhite(-1, 1))
x8 >> play("<k.><.>", hpf=0, amp=2)

h8 >> loop("pad16", dur=16, sample=1)
x4 >> tb303([0,4,2,P*[6,7]], dur=1/4, wave=0, cutoff=PFr(300,1600), rq=PFr(0.1,.9), dec=1.0, top=1500, mverb=.2, oct=PStep(8,4,5) + var([0,-1],16))


############################
#### HIGH TEMPO
###########################
# postGabber
Scale.default="minor"
Clock.bpm=163
l8 >> plaitsX([var([0,3,5], 8),7,14,[15,17]], shape=.2, dur=1/2, lpf=PFr(400,2800), preset=(3,12), oct=(4,5,6)).gtr()
a1 >> lbass(var([0,3,5], 8), dur=1/2,oct=5, cutoff=PFr(400,3200)).gtr()
j5 >> loop("gbreak16", dur=16, sbrk=[0,.5], sbrkdur=.5, comp=0)
g2 >> play("<x.><..o.>", sample=4, lpf=PFr(400,1000), lpr=var([.5,.1],[6,2,5,1]), bank=0, vol=0.6, hpf=0)
# t2 >> loop("gscreecha16", dur=32, mverb=.2, sample=PRand(88))

#N5GLITCHCORE/BREAK
l1 >> loop("gab16", dur=16, sample=3)
r5 >> play("<x..(...x)><.><....>", sample=0, amp=3).sometimes("stutter")
i0 >> loop("drumglitch32", dur=32, sample=var([PRand(88)],64))
p5 >> noloop("oldies8", dur=8, sample=var(PRand(88),32), comp=0, fx1=0, shape=.0, trig=0, mverb=0)

p4 >> loop("gbuild16", dur=16)

i5 >> play("l ", bank=1, sample=1, dur=1/2, hpf=0, amp=1, cut=1)
o5 >> loop("gapr16", dur=32, sample=3, mverb=.5)
i4 >> loop("gscreecha16", dur=16, sample=4, mverb=0.5, hpf=800)




##########################
# totoBan
Clock.bpm=173
f8 >> loop("beats8", dur=8, sample=5)
c1 >> loop("berlin8", dur=8, sample=4)
m0 >> loop("cinambi8", dur=8, sample=var([3,2],[24,8]), hpf=200)
v3 >> loop("circlebreak16", dur=16, sample=7, comp=1, sbrk=.5, sbrkdur=.5)
b4 >> loop("nbvarp16", dur=32, sample=5, hpf=120)

x4 >> loop("ragedrum16", dur=32, sample=5, amp=1, comp=1, fx=1)
r9 >> loop("electrodrum16", dur=16, sample=3, comp=1)

p6 >> play("<x.><.><..o.><k.>", sample=1, amp=1, bank=0).sometimes("stutter")
p6.bank=1

#### GARBAGE 
~x4 >> play("x ", sample=3, amp=9)
e9 >> loop("housebass24", dur=32, sample=7, hpf=0, octer=0, shift=0, octersub=à, octersubsub=0, room=.1).unison(4)

e9 >> loop("housebass24", dur=32, sample=7, hpf=800, hpf_=10, hpf_d=0.8, lofi=0.1, lofi_=0.9, lofi_d=32, octer=0, shift=0, octersub=à, octersubsub=0, room=.1).unison(4)

