# live G 140
# live

############################### LIVE

Clock.bpm = 140;
Root.default = "G"

l1 >> lbass([1, 0, 0, [0, 0, 0, 2]], dur=var([1/2, 2], [3, 1]), sus=var([1/2, 4], [3, 1]), r=1, a=(0.001, linvar([0.1, 0.2]), [8, 4]), dist2=(1, linvar([3, 4], [2, 4])), oct=5).gtr(3).unison(2) + var([0, 3], [15, 1])
l2 >> lbass([1, 0, 0, [0, 0, 0, 2]], dur=var([1/2, 2], [3, 1]), delay=0.5, sus=l2.dur, r=1, a=(0.01, linvar([0, 0.2], [8, 4])), dist2=(1, linvar([3, 4], [2, 4])), oct=6).gtr(3).unison(2) + var([0, 3], [15, 1])
l3 >> lbass(1, dur=2, oct=6).accompany(l1)
l4 >> prof(dur=8, oct=(6, 7), amp=0.3).unison(4)

###################################
Clock.bpm = 170
# [broken in source] g1 >> lbass( var([ (4, [-4, 0]), [0,P*[7,8,10,[12,_]]]]), cut=(0.1, 1), dist2=0.5 ,r=PGauss(1, 0.2), cutoff=(200, 1600), dur=PRand([1/4, 1/2, 1/2, 1, 1/4]), submix=1, scale=Scale.minorPentatonic).unison(3).sometimes("stutter", oct=6))
g2 >> lbass(dur=1/2, dist2=4, a=0.24, amp=1, hpf=P*[1200, 1888, 3000])
g1.amp=var([1, 0], [16, 8, 8])
g3 >> lbass(dur=2, submix=linvar([0, 1], 32), cut=PRand([0.5, 0.25, 1, 2]))
g4 >> lbass([ [2, 4, 5], 4, [-4, 2, 4, 5]], amp=1-(g1.amp), dur=P*[4, 1/2], sus=g4.dur, r=4, hpf=400, chop=PRand([1, 2, 4, 8]), chopmix=P*[0, 0.5], cutoff=PWhite(1000, 8000), oct=(7, 6), scale=Scale.minorPentatonic).unison(2)
g3.amp=PWhite(0.1, 1)
g5 >> lbass([12, 4, 5], dur=2, sus=P*[g5.dur, g4.dur], r=4, chop=PRand([1, 2, 4, 8]), oct=var([4, 5, 6, 7, 8]), scale=Scale.minorPentatonic)
g6 >> tb303(melody(),dur=1/8, lpf=1200, oct=7, top=linvar([400, 16000]), shift=1, cutoff=400, scale=Scale.minorPentatonic).unison(2)
g1 >> lbass((4, [-4, 0]), dist2=0.5 ,r=PGauss(1, 0.2), amp=var([1, 0], [2, 6]), cutoff=(200, linvar([1200, 6400], 8)), dur=var( [ PRand([1/4, 1/2, 1/2, 1, 1/4]), 1/4, 1], [[10, 2], 4, 2]), submix=1 + PWhite(0.1, -0.1), scale=Scale.minorPentatonic, mverb=1, shape=PGauss(1, 0.1)).unison(3) + var([0, 4, 12])

########### drum kit
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

#D1 #slow drum #95; #mysterious
Clock.bpm = 95;

d1 >> play("v.....(...{v.})(...{.v}))", cut=2, sample=8, hpf=50, shape=(0,var(PWhite(0,0.2)))).sometimes("stutter")
d2 >> loop("cyber16", dur=16, hpf=4000)
d3 >> loop("bass16", dur=16, sample=1, shift=0).unison(2)
d4 >> play("v.....(...{v[vv].}).", sample=8, delay=0.5, hpf=400, amp=var([0, 1], [28, 4]))
d5 >> play("(...(.p)).((p.).(p.).)((p.).(p.).)", dur=1/4, sample=(3, 4), hpf=200, hpr=(var([0.05, 0.5, linvar([0.01, 0.001], 32)]), 0.1), crush=8,bits=8, rate=(1, [1, 2, 1.12, 2.4, 8]), echo=0.5 ,delay=(0.25, 0.5)).sometimes("stutter", rate=0.5)
d6 >> play("-{-[--]}-.-{[---][--]}(-.)(-[----])", sample=2, amp=PCoin(PWhite(0, 4),0,0.5), hpf=6000, pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble").sometimes("stutter", PRand(16), rate=PWhite(-1,5))
d7 >> play("#--.-{[---][--]}(-.)(-[----])", hpf=[2000, 4000], sample=4, amp=PCoin(PWhite(0, 4), 0, 0.5), pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble")

#################
Clock.bpm = 135;

x1 >> play("{T[TM]}", amp=[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], echo=0.25, echotime=4, echomix=0.2, dur=1/4, sample=3).unison(4).sometimes("stutter", rate=(2, 1), vol=P*[0, 1], echo=0.5)
x2 >> play(var(["O.o.", "b", "3"], 8), amp=1, dur=1/2, sample=2, dist2=2, format=1, cut=1/2, lpr=linvar([0.1, 0.2], 32), mverb=1, lpf=4000, shift=4, vol=P*[0, 1])
x3 >> play("{[-Q][---][uc].}", amp=[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0], dur=1/4, sample=(4, 2), hpf=linvar([100, 8000], [4,2])).sometimes("stutter", echo=2, echotime=2, vol=P*[0, 1]).unison(2)
x4 >> play("-", amp=[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0], dur=1/8, sample=var([4, 1, 6], [4]), hpf=20, rate=var([1, 2], vol=P*[0, 1]))
### attack@aspiration.rfp:~$ ###Init: Worm.Kernel.KeyLogger |***--------|
x5 >> faim(0, oct=(3,4), fx1=1, beef=[1,[1,0]], dur=var([PStep(8,2,1/4),PDur(var(PRand(8),8),8,PRand(8))],[[14,6],2]), shape=(0,0.05), amp=P[PWhite(1,1.2), PWhite(0.2,0.7), PWhite(0.5,var([0.7,1],16)), PWhite(0.2,0.5)]).every(6, "stutter", PRand([2,3]), oct=5, delay=0.25, glide=0.3, amp=PWhite(0,0.5)/(1+a2.formant), formant=[0,PWhite(1,6)], room2=0.7, mix2=0.4) + var([0,P*[1,-1,2,-2]],[7,1])

x5 >> play("n", amp=[0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0], vol=P*[0, 2], dur=1/4, sample=var([4, 3], 8), mverb=0.5,mverbmix=0.3, mverbdiff=0.1)
x_all.rate=([var([1, 2, 4], [6, 1, 1]), 1,1, 1])

x6 >> play("n", amp=[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], dur=1/4, leg=PWhite(40, 120), sample=1, rate=[1, 2, 4, 8]).unison(4).sometimes("stutter")
x7 >> play("q", amp=[1, 0], sample=4, cut=1/2, dur=var([1/2, 1/4, 1/4])).unison(4)
x8 >> play("b", amp=[1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0]*P[0, 1], leg=4, dur=1/4, sample=var([1, 2]))
x9 >> play("x ", amp=[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*P[0, 1], leg=4, dur=1/4, dist2=4, shift=4, vol=2)
x0 >> play("k", amp=[2, 0], high=12, sample=2, low=4, dur=var([1/2, 2], [1, 1]), dist2=1, shape=0).every(var([1, 2, 4]), "stutter").unison(4)

########### C2
Clock.bpm = 90
c1.shift=0

c1 >> faim(c1.dur, oct=([3, 4], PStep(9,5,[4,5])),dur=var([PDur(var(PRand(5,7),[4,12]),12),4],[24,8]), shape=c1.dur/10, shift=0, slide=c1.dur/4, delay=var([0, (0,(0,[0,0.25]))], [PRand([2, 4, 6, 8]), 4]), amp=PRand([0.5,0.1, 0.25, 1, 0.75])).unison(8).sometimes("stutter", beef=(c1.shift*-1)*120, shift=var([1, 2, (1/2)], [7, 5, 4]))
c2 >> play("{tTPp}", sample=(2,P[0:5]), leg=4, amp=var([c1.dur/4, 1], [4, 4]), room2=0)
c3 >> play("P ", amp=c1.amp, feed=0.2, leg=4, echo=0)
c4 >> click(0, dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), hpf=40, shape=[PWhite(0.4,0.8),0.2], oct=(3, PStep(9,5,4)), octer=1, octersub=2, octersubsub=var([2, PRand(15,2322)], [15, 1]), triode=[4, 2], amp=0.1, amplify=1).unison(3).rarely("stutter",PRand(6), oct=6, pan=[-1,1], mpf=2860, hpf=400)
c5 >> play("<u><t>", sample=(2,P[0:5]), delay=(0,(0,[0,0.25])), amp=2, dur=c1.dur, crush=[0,0,0,PRand(8)], bits=4, lpf=1500)
c4.amp=0.01
c6 >> ebass(linvar([2, [5, 6]], [4, 0]), shape=linvar([0.01, 0.1], [4, 0]), room2=1, damp2=0.5, scale=Scale.chromatic,dur=1/2, sus=var([1, 2], [28, 4]), fmod=var([8, 32], [60, 4]), oct=5).unison(0)
c1.stop()
c2.stop()
c3.stop()
c7 >> ebass(linvar([2, [5, 6]], [4, 0]), shape=linvar([0.01, 0.3], [14, 2]),scale=Scale.chromatic,dur=1/4, sus=var([1/2, 1/4], [28, 4]), fmod=var([8, 64], [60, 4]), oct=5).unison(0)
c8 >> ebass(linvar([2, [5, 6]], [4, 0]), shape=linvar([0.1, 1], [24, 8]),scale=Scale.chromatic,dur=1/4, sus=var([1/2, 1/4], [28, 4]), fmod=var([8, 64], [60, 4]), oct=6).unison(2)
Scale.default = "chromatic"

b1 >> bass(-4, oct=6, dur=1/4, lpr=0.1, lpf=4000).human(40, 0, 0).unison(4)
b2 >> bass(8, oct=[5, 5], dur=1/4)
b3 >> feel(0, oct=[4, [3, 4.01, 3.99, 4]], lpr=0.1, lpf=4000, dur=1/4, amp=PWhite(0, 1), pan=PWhite(-1, 1)).unison(2)
b4 >> pluck((0, 20), dur=var([1, 1/8, 1/4, 1/8, 1, 1/8, 1/4, 1/2], [2, 1/4]), amp=0.2)
b5 >> pluck(0, dur=1/2, amp=[0, 0.1])
c1 >> faim(c1.dur, oct=([3, 4], PStep(9,5,[4,5])),dur=var([PDur(var(PRand(5,7),[4,12]),12),4],[24,8]), shape=c1.dur/10, shift=0, slide=c1.dur/4, delay=var([0, (0,(0,[0,0.25]))], [PRand([2, 4, 6, 8]), 4]), amp=PRand([0.5,0.1, 0.25, 1, 0.75])).unison(8).sometimes("stutter", beef=(c1.shift*-1)*120, shift=var([1, 2, (1/2)], [7, 5, 4]))
b4.stop()

c_all.stop()
c5 >> play("<u><t>", sample=(2,P[0:5]), delay=(0,(0,[0,0.25])), dur=c1.dur, crush=[0,0,0,PRand(8)], bits=4, lpf=1500)
x7 >> play('h', sample=18, dur=0.25, pan=PWhite(-0.5, 0.5), amp=0.25 * expvar([0.25, 1], [1, 0]) * var([1, 0], [[3, 0.5], 1, 1, 1, 2, 1, 0, 2, [3, 0.5], 0, 1, 0]) * expvar([0, 0, 1, 1], 64))

####
########### J1
r1 >> rsin([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], lpr=0.1, oct=PStep(16, 5, (5, 4)), dur=8, amp=PCoin(1, 0, 0.25), crush=0, mix2=0, bits=0, fmod=4, lpf=4000, mid=40, spf=4, spfslide=4, chop=4, chopwave=1, chopmix=0.4, spfend=12200).every(8, "shuffle").unison(2)
r2 >> rsin([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 4, (3, 4)), dur=[PDur(4,8), 1/2], amp=1, crush=4, bits=8, fmod=4, lpf=0)
r_all.lpf=var([200, 12000], [PRand([1, 5]), 12])
r_all.rate=var([1, linvar([12, 1])], [28, 4])
r_all.only()
r_all.shift=var([0,  linvar([PCoin(12, 1, 0.25), PCoin(1, 12, 0.25), 24])], [48, 4])
r3 >> rsin([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 3, (4, 5)), dur=[10, 1, 1, 1, 1, 1/2, 1/2, 1], amp=1, fmod=0, lpf=0).slider().every(4, "shuffle")
r4 >> rsin(var([r3.degree, (0, -2)]), dur=4, amp=1, oct=(3, 4), hpf=[400, 1600], crush=0, chop=4, bits=0, fmod=4, lpf=0).slider()
r_all.rate=var([1, PWalk(8, 4, 1)], PRand(16))

########### J1
# B2
Root.default='C'
Scale.default="minor"
Clock.bpm = lininf(120, 170, 128)

b1 >> faim(var([0, -2, 0.5], 8), formant=var([0, 0.1], [24, 8]), formantmix=PWhite(0, 0.3), oct=(6, 5, [4, 3]) + var([0, 1], [14, 2]) + PwRand([0, 1, 1.25], [30, 1, 1]), rate=linvar([1.2, 0.3], [32]), fmod=linvar([0, 1], [128]), scale=Scale.chromatic, shape=var([0, (0.1, 0)], [12, 4]), dur=1/2, amp=0.5, mverb=0, mverbdamp=[0.2, 1], mverbdiff=[1, 0.4], hpf=linvar([100, 400], 8)).unison(4).every(8, "stutter", slide=0.01, lpf=linvar([4000, 8000], 16))
b2 >> faim(var([0, -2, 0.5], 8), oct=(3, 4, 5) + var([0, 1], [14, 2]), width=PWhite(0.1, 0.9), rate=linvar([1.2, PWhite(0.3, 8)], [64]), shift=var([0, 1, 1.2], [13, 2, 1]), fmod=linvar([0, PRand(4, 8)], [128]), scale=Scale.chromatic, delay=(0, 0.25, [0.5, 0, 4]), dur=P*[1/2, 1, 1, 1/4, 1/4, 1/4], amp=0.5, hpf=100).unison(2).every(8, "stutter", slide=[2, -2], degree=(-12, 12), echo=(0, 0.125), echotime=1, lpf=linvar([1000, 4000], 16))
b1.rate=lininf(1, 0.1, 32)
b1.mverb=0.0
b3 >> soprano((b1.degree, 0), dur=PRand(1,8), blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(7,6,5)), shape=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), room=0.5, mix=0.5, amplify=0.5, spin=0).unison(2)

b1.lpr=lininf(1, 0.1, 64)
b1.slide=var([0, 1], [28, 4])
b1.degree=0.5
b1.chop=var([0, 1, 1/2], [12, 2, 2])
b7.oct=(3, 5)
b2.dur=1/4

b4 >> play("(#....)..(...~)", rate=PWhite(-1,4)*0.25).unison(3, 1,99)
b5 >> play("@", sample=4, hpf=4000).fill(0)
b6 >> play("3", dur=1/2, amp=0.5, sample=(var([3, 4], [4, 4]), 3), glide=1,shift=var([0, 2], [24, 8]), pshift=0).slider()

b7 >> play(var(["-.--", "[--]"], 8), sample=1, rate=0.5, formant=0.4, hpf=7000)
b1.dur=lininf(1/2, 1/4, 16)
b1.lpf=linvar([3200, 1600], 128)
b1.amp=0.6
b8 >> dbass(var([0, -2, 0.5], 8), oct=(6, 5) + var([0, 1], [14, 2]), rate=linvar([1.2, 0.3], [64]), scale=Scale.chromatic, dur=1/2, amp=1, hpf=100).slider().unison(4).solo(0)

##############
e1 >> play("# ", dur=4, rate=(-1, 2)).unison(2).after(4, "stop")
e2 >> play("# ", sample=(1,4), dur=4, rate=(-1, 1)).after(8, "stop")
e3 >> play("& ", sample=5, rate=-2, shift=4, dur=4).after(32, "stop")
e4 >> play("#k", sample=(1,4), dur=4, rate=(-1, 1), mverb=1, room2=0.5,  chop=0.25, chopmix=[0.5, 0], damp2=0.9, revsus=1).after(4, "stop")

### rythm
x1 >> play("(...(.p)).((p.)c(p.).)((p.).(p.).)", dur=1/4, sample=4)
x2 >> play("x(x.).(x[.x])", dur=1, sample=3)
x3 >> play("(.......p).(pcp..c..)(p.p.....)", dur=1/4)
x4 >> play("(t.)..(.t.(T.))", dur=1/2)
x5 >> play("[.[--]].", dur=1)
x6 >> play("(...(.p)).((p.)c(p.).)((p.).(p.).)", dur=1/4, sample=7)
x8 >> play("(.......p).(pcp..c..)(p.p.....)", dur=1/4, sample=7)
x9 >> play("(t.)..(.t.(T.))", dur=1/2, sample=7)
y1 >> play("[.[--]].", dur=1)
y2 >> play("Tt", dur=var([1/4, 8], [4, 1]), sample=[4, 3, 2, 1], amp=2)
y3 >> play("//", rate=0.5, crush=4, dur=8, amp=0.5)
y4 >> play("nN", sample=PRand(404), lpf=PRand(400,18000), amp=0.2).fill()
