# mysterious 95
# slow

#D1 #slow drum #95; #mysterious
Clock.bpm = 95;

d1 >> play("v.....(...{v.})(...{.v}))", cut=2, sample=8, hpf=50, shape=(0,var(PWhite(0,0.2)))).sometimes("stutter")
d2 >> loop("cyber16", dur=32, hpf=4000).brk(1)
d3 >> loop("long64", dur=64, sample=1, hpf=1000, shift=0).unison(2).brk(1)
d4 >> play("v.....(...{v[vv].}).", sample=8, delay=0.5, hpf=400, amp=var([0, 1], [28, 4]))
d6 >> play("-{-[--]}-.-{[---][--]}(-.)(-[----])", sample=2, amp=PCoin(PWhite(0, 1),0,0.5), hpf=6000, pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble").sometimes("stutter", PRand(16), rate=PWhite(-1,5))
d7 >> play("#--.-{[---][--]}(-.)(-[----])", hpf=[2000, 4000], sample=4, amp=PCoin(PWhite(0, 1), 0, 0.5), pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble")

Clock.bpm = 135;

x1 >> play("{T[TM]}", amp=[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], echo=0.25, echotime=4, echomix=0.2, dur=1/4, sample=3).unison(4).sometimes("stutter", rate=(2, 1), vol=P*[0, 1], echo=0.5)
x2 >> play(var(["O.o.", "b", "3"], 8), amp=1, dur=1/2, sample=2, dist2=2, format=1, cut=1/2, lpr=linvar([0.1, 0.2], 32), mverb=1, lpf=4000, shift=4, vol=P*[0, 1])
x3 >> play("{[-Q][---][uc].}", amp=[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0], dur=1/4, sample=(4, 2), hpf=linvar([100, 8000], [4,2])).sometimes("stutter", echo=2, echotime=2, vol=P*[0, 1]).unison(2)
x4 >> play("-", amp=[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0], dur=1/8, sample=var([4, 1, 6], [4]), hpf=20, rate=var([1, 2], vol=P*[0, 1]))
x5 >> play("n", amp=[0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0], vol=P*[0, 2], dur=1/4, sample=var([4, 3], 8), mverb=0.5,mverbmix=0.3, mverbdiff=0.1)
x_all.rate=([var([1, 2, 4], [6, 1, 1]), 1,1, 1])
x6 >> play("n", amp=[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], dur=1/4, leg=PWhite(40, 120), sample=1, rate=[1, 2, 4, 8]).unison(4).sometimes("stutter")
x7 >> play("q", amp=[1, 0], sample=4, cut=1/2, dur=var([1/2, 1/4, 1/4])).unison(4)
x8 >> play("b", amp=[1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0]*P[0, 1], leg=4, dur=1/4, sample=var([1, 2]))
x9 >> play("x ", amp=[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*P[0, 1], leg=4, dur=1/4, dist2=4, shift=4, vol=2)
x0 >> play("k", amp=[2, 0], high=12, sample=2, low=4, dur=var([1/2, 2], [1, 1]), dist2=1, shape=0).every(var([1, 2, 4]), "stutter").unison(4)
x1.stop()
x2.stop()
x3.stop()
x4.stop()
x5.stop()
x0 >> play("k", amp=[2, 0], high=12, mid=var([4, 12], 4), sample=2, low=4, dur=var([1/2, 1/4], [1, 1]), dist2=x0.mid, shape=0).every(var([1, 2, 4]), "stutter").unison(4)

Clock.bpm = 180

b1 >> ebass(Pvar([-12, -8, [0, -12], -12, [-12, -12,-12], [-7, ([14, -12, -12], -7)], -14],[2, 0.25]), dur=1/2, oct=(6, PStep(6, 7, 8)), dist2=(12, linvar([2, 12], [8])), slide=(0.01, 1), shape=PWhite(0.4, 0.6), amp=0.2).unison(4).human() + var([0, 12], [7, 1])
b2 >> fbass(Pvar([-12, -8, [0, -12], -12, [4, -12,-12], [-7, ([14, -12, -12], -7)], -14],[2, 0.25]), dur=1/2, delay=0.5, oct=7, echo=0.0125, dist=2,slide=12, formant=0.0, amp=0.05).unison(8)
b3 >> lbass(Pvar([-12, -8, [0, -12], -12, [-12, -12,-12], [-7, ([14, -12, -12], -7)], -14],[2, 0.25]),amp=[1, 0.2, 1, 1, 0.5, 1, 0.2, 1, 0.5, 1, 2], dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), oct=7, low=0.01, high=2, dist2=b1.degree/10).unison(8)
db >> bass(0, dur=c1.dur, leg=12, amp=var([0.5, 0], [12, 4]), rate=PWhite(0.01, 0.2), sus=db.dur*1.5).unison(2)
de >> ebass(dur=1/4, amp=1, shape=8).unison(4)

b1.dur=8
b2.dur=1/2

h_all.amp=var([0, 1], 8)

b1.dur=4

Root.default = "e#"

f1 >> play("x", sample=var([ (9, 6, 4), (3)], [7, 1]), dur=PDur([[1, 3], 4], 8), hpf=400).sometimes("stutter", rate=2, low=4, hpf=0)
f2 >> play("U", sample=(9, 6, 4), dur=1, delay=0.5, mverb=0, shift=var([0.2, 0.5, 1, (2, 0.5)], [1, 2, 4]), chop=4, hpf=0).every(4, "stutter", rate=2, dist=0.2, high=4)
f3 >> play("T", sample=(9, 6, 4), dur=2, delay=1/2, mverb=0.2, cut=1, revsus=0.2, shift=(0.2, 1, 2), amp=linvar([0.4, 1], 32), hpf=0, low=4)
f4 >> play("{[--]-[--][----]}", amp=[1, 0.5, 0.2, 1], delay=1/2, sample=var([3, 4, 2, 4], 16), dur=1, mverb=0.01, echo=0.125, echomix=linvar([0.2, 0.5], 8))
f5 >> play("c", delay=1/2, sample=0, dur=4, mverb=0.1, echo=0.5, echomix=linvar([0.2, 0.5], 8))

Clock.bpm = 170
g1 >> lbass( var([ (4, [-4, 0]), [0,P*[7,8,10,[12,_]]]]), cut=(0.1, 1), dist2=PWhite(0.5, 0.87),r=PGauss(1, 0.2), cutoff=(200, 6400), dur=PRand([1/4, 1/2, 1/2, 1, 1/4]), submix=1, scale=Scale.minorPentatonic).unison(3).sometimes("stutter", oct=6)
g0 >> faim( var([ (4, [-4, 00]), [0,P*[7,8,10,[12,_]]]]), cut=(0.1, 1), dist2=PWhite(0.5, 0.87),r=PGauss(1, 0.2), shape=g0.degree, cutoff=(200, 6400), delay=0.5, beef=1, dur=PRand([1/4, 1/2, 1/2, 1, 1/4]), amp=0.5, submix=1, scale=Scale.minorPentatonic).unison(3).sometimes("stutter", oct=6)

g2 >> lbass(dur=1/2, dist2=4, a=0.24, amp=1, hpf=P*[1200, 1888, 3000])
g1.amp=var([1, 0], [16, 8, 8])
g3 >> lbass(dur=2, submix=linvar([0, 1], 32), cut=PRand([0.5, 0.25, 1, 2]))
g4 >> lbass([ [2, 4, 5], 4, [-4, 2, 4, 5]], amp=1-(g1.amp), dur=P*[4, 1/2], sus=g4.dur, r=4, hpf=400, chop=PRand([1, 2, 4, 8]), chopmix=P*[0, 0.5], cutoff=PWhite(1000, 8000), oct=(7, 6), scale=Scale.minorPentatonic).unison(2)
g0.shape=12

g0.hpf=4000
g3.amp=PWhite(0.1, 1)

g5 >> lbass([12, 4, 5], dur=2, sus=P*[g5.dur, g4.dur], r=4, chop=PRand([1, 2, 4, 8]), oct=var([4, 5, 6, 7, 8]), scale=Scale.minorPentatonic)
g1.stop()
g0.stop()
g6 >> tb303(melody(),dur=1/8, lpf=1200, oct=7, top=linvar([400, 16000]), shift=1, cutoff=400, scale=Scale.minorPentatonic).unison(2)
g1 >> lbass((4, [-4, 0]), dist2=0.5 ,r=PGauss(1, 0.2), amp=var([1, 0], [2, 6]), cutoff=(200, linvar([1200, 6400], 8)), dur=var( [ PRand([1/4, 1/2, 1/2, 1, 1/4]), 1/4, 1], [[10, 2], 4, 2]), submix=1 + PWhite(0.1, -0.1), scale=Scale.minorPentatonic, mverb=1, shape=PGauss(1, 0.1)).unison(3) + var([0, 4, 12])

### attack@gta.mvg:~$ ###Dumping: Virut.Hardware.Stealer , ping=3ms
Root.default = "C"
Clock.bpm=144
Scale.default="dorian"

masterAll("reset")
masterAll("degree", var([0, 1, 2, -12], [6, 1, 1]))
masterAll("oct", var([5, 4, 6, 7], [3, 1]))
t1 >> mpluck([[0, 1, 2, 1, 0, 1 ,0, -1],-3], mverb=lininf(0,0.8,32), amp=0.5, oct=(PStep(8, 5, 6), 5, 7), pan=PWhite(-1,1), cut=1/2, dur=2, delay=0, hpf=400).unison(4)
g2.stop()
masterAll("hpf", 200)
masterAll("lpf", 2400)
t2 >> pianovel([[0, 1, 2, 1, 0, 1 ,0, -1],-3], dur=1/2, velocity=PRand(40,60), hpf=100, velhard=0.2, amp=PGauss(0.4, 0.1), oct=PStep(7,6,5), rate=linvar([0.1,1.8],24), sus=PWhite(0.2,0.3)).unison(3).sometimes("stutter", oct=[6, 8], mverb=0)
t3 >> pianovel(t2.degree + 5, oct=PStep(4, 5, [6, 7]),velhard=[PGauss(0.2, 0.2), 0], hpf=120, velocity=PRand(40,88), delay=var([0,(0.125, 0)], [5, 3]), amp=linvar([0.3, 0.6], [16]), mverb=0.1).accompany(p0).unison(4).human()

t4 >> ssaw([[0, 1, 2, 1, 0, 1 ,0, -1],-3], dist2=1, amp=0.3, hpf=linvar([200, 400]), hpr=0.39, dur=1/2, phase=0, sus=linvar([0.6, 1], 16)).unison(8)
t5 >> ssaw([0,2,P+(3,4),P+(6,7,8,14)], oct=(5.01, 3.99, 7), dist2=1, sawtype=P*[0,1], sawmix=0.5,  lpr=0.7, amp=(0.2, 0.1, 0.2), lpf=7800, dur=8).unison(8)

t6 >> ssaw([0,2,3,(4.5,7)], oct=(4,5), dist2=1, dur=8, lpf=800, slide=0.2, slidedelay=0.8, hpf=90).unison(3)
t7 >> bass([0,0,-1,7,7,-1], dur=[1/2,1/2,[rest(3)]], amp=1, oct=5, echo=0.25, sus=1)
t8 >> jbass(4, dur=1/2, amplify=var([0,1],[3.5,0.5]), amp=2, echo=0.5, oct=4)
t4.stop()

t9 >> dbass(P[3, 4, 4.5, [4, 3]].stutter(2), dur=1/4, oct=(4,5), amplify=var([0, 1], [6, 2]))
t0 >> bass([(0, [7, 3]), (0, [4, -1])], shape=linvar([0, 1], 32), oct=P(3, [4, [5, 6]])+1, room2=0, dur=[1/2, 1/2, [rest(1)]]).unison(2)

#rageNoise
Clock.bpm = 140;
i0 >> loop("choir8", dur=16, mverb=1, amp=[0.3, 0.5, 0.4, 0.7], shift=(0.5, (1, 1.5)), dubd=0.1, chop=4, dublen=PWhite(0.01, 0.5), vol=0.5, hpf=2000)
n1 >> noise(lpf=400, dur=8, echo=0.5, amp=[0, 0.2], delay=2, echotime=8, chop=4, lpr=0.1, hpf=2000)
n2 >> pink(lpf=1200, dur=1, echo=0.5, delay=0.5, pan=PWhite(-1, 1), shift=(2, 1), echotime=2, chop=var([PWalk(8, 1, 1), 4]), lpr=0.1, hpf=linvar([2000, 4000]))
i1 >> loop("intro8", dur=(16, 8), dist2=0, revsus=0, sample=3, mverb=1, mverbdiff=PRand(16), amp=P*[0, 4, 1,1]).brk(2)
i2 >> loop("techfx4", dur=(8, 4), sample=1,echo=[0.25, 0.5], spf=400, spfend=6000, spfslide=4, amp=[0.18, 1, 0.4, 1, 0, 0.2], shift=(2, 1)).unison(2)

i3 >> loop("ragedrum16", dur=16, sample=2, amp=[0, 0.3, 1, 1, 1.2], comp=1, shift=[0, 1], hpf=100, hpr=0.9).unison(2)

i4 >> loop("psych32", dur=32, sample=3, amp=[0.5, 0.5,0.5, 0], feed=0.5, shift=0.5, krush=4, bits=2)
i5 >> loop("impulse32", dur=16, sample=0, amp=[1, 0, 2, 0.2])
i6 >> loop("ragedrum16", dur=16, dist2=0.5, sample=6, amp=[0, 1, 0.5, 1, 1], shift=[0, 1], hpf=100, hpr=0.9).unison(2)
i7 >> loop("nsbreak16", dur=16, dist2=P*[1, 2, 4], sample=2, amp=[1, 1, 1.2, 0.3, 1.2], shift=[0, 1], hpf=100, hpr=0.9).unison(2)

masterAll("dur", 4)
masterAll("reset", 4)

Master().lpf=var([0, 4000, 6000, 15000], [24, 4, 2, 2])
Master().hpf=var([0, 20, 30, linvar([3200, 6400], 32)], [24, 4, 2, 2])
Master().cut=var([0, 1, 1/2, linvar([1/4, 1], 32)], [24, 4, 2, 2])

i0 >> loop("choir8", dur=16, mverb=1, amp=[0.3, 0.5, 0.4, 0.7], shift=(0.5, (1, 1.5)), dubd=0.1, chop=4)
i1 >> brown(lpf=400, a=PWhite(1, 2), dur=8, echo=0.5, delay=2, echotime=8, chop=4, lpr=0.1, hpf=0)
i2 >> pink(lpf=1200, dur=1, echo=0.5, delay=0.5, pan=PWhite(-1, 1), shift=(2, 1), echotime=2, chop=var([PWalk(8, 1, 1), 4]), lpr=PWhite(0.02, 0.1), hpf=linvar([2000, 4000]))
i3 >> loop("intro8", shift=PWhite(4, 2), dur=[(16, 8), 4], delay=4, dist2=0, revsus=0, sample=1, mverb=0, mverbdiff=PRand(5), amp=P*[0.2, 0.5, 0, 1,0]).brk(1)
i4 >> loop("intro8", shift=PWhite(0.5, 1.5), dur=[(16, 8), 4], dist2=1, revsus=0, sample=2, mverb=0.5, mverbdiff=PRand(5), amp=P*[0, 4, 1, 0, 0, 1]).brk(2)
i5 >> loop("techfx4", dur=(8, 4), sample=1,echo=[0.25, 0.5], spf=400, spfend=6000, spfslide=4, amp=[0.18, 1, 0.4, 1, 0, 0.2], shift=(2, 1)).unison(2)
i6 >> loop("ragedrum16", dur=16, sample=2, amp=[0, 0.3, 1, 1, 1.2], shift=[0, 1], hpf=100, hpr=0.9).unison(2)
i7 >> loop("psych32", dur=32, sample=3, amp=[0.5, 0.5,0.5, 0], feed=0.5, shift=0.5, krush=4, bits=2)

i8 >> loop("impulse32", dur=16, sample=0, amp=[1, 0, 2, 0.2])
i9 >> loop("ragedrum16", dur=16, dist2=0.5, sample=6, amp=[0, 1, 0.5, 1, 1], shift=[0, 1], hpf=100, hpr=0.9).unison(2)
i0 >> loop("nsbreak16", dur=16, dist2=P*[1, 2, 4], sample=2, amp=[1, 1, 1.2, 0.3, 1.2], shift=[0, 1], hpf=100, hpr=0.9).unison(2)

Clock.bpm = 150;
masterAll("hpf", 4000)

x1 >> loop("uk8", dur=16, sample=0, amp=P*[1, 1, 1, 0], rate=P*[-1, 1], med=4, low=[0, 4], shift=0, feed=0.5, hpf=1200, hpr=0.95).brk(1).only()
x0 >> loop("uk8", dur=1, sample=1, cut=1/32, amp=P*[1, 1, 1, 0], rate=P*[-1, 1], med=9, low=[0, 1], shift=0, feed=0.5, hpf=1200, hpr=0.95).brk(1)
x2 >> loop("uk8", dur=P*[2, 1, 4], sample=0, cut=P[1/16, 1/8], amp=P*[1, 1, 1, 0], rate=P*[-1, 1], med=1, low=[0, 0], shift=var([1, 4]), feed=0.5, hpf=1200, hpr=0.95).brk(1)
x3 >> loop("berlin8", dur=16, sample=4, amp=1, high=4, med=4, low=[0, 1], echo=[0, 0.5]).unison(4)
x5 >> loop("bass8", dur=8, sample=2).unison(4)

x4 >> loop("electrodrum16", dur=16, sample=1, amp=1.4, shape=0.0)
x9 >> lbass([2, [2, 4], [2, 4, 8]],dur=1/4).unison(4)
b1 >> loop("rvoice16", dur=16, formant=0, sample=2, amp=1, shift=2).unison(4)
b2 >> play("berlin8", dur=8, amp=4, sample=1)
b3 >> play("X ", amp=2)

x1.sample=1
x1.dur=32
x4 >> loop("techfx4", dur=16, formant=1, sample=0, amp=[0, 1, 0, 0 ], rate=2, cut=2, high=1, low=4).brk(1)
x2.shape=P*[1, 0, 0, 0]
x5 >> loop("techfx4", dur=8, sample=2, amp=P*[0, 1, 0, 0 ], rate=2, cut=2, high=1, low=4).brk(1)
x6 >> loop("techfx4", dur=8, shape=1,sample=2, amp=P*[0, 1], rate=4, cut=2, high=0, med=4, low=4).brk(1)

x7 >> play("(...(.p)).((p.)c(p.).)((p.).(p.).)", dur=1/4, sample=4)
x8 >> play("x(x.).(x[.x])", dur=1, sample=3)
x9 >> play("(.......p).(pcp..c..)(p.p.....)", dur=1/4)
x0 >> play("(t.)..(.t.(T.))", dur=1/2)
