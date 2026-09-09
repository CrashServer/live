# attacks ultimate
# snippets

#A1
Clock.bpm = 48;
a1 >> play("#", dur=8, delay=3.5, feed=0.5, mverb=0.4, amp=2, echo=0.5)
a2 >> play("#", dur=8, feed=0.3, sample=2, delay=0, rate=-1)
a3 >> play("g", dur=8, delay=4.5, feed=0.5, mverb=0.4, amp=1, echo=0.5, lpf=400, lpr=0.1).unison(2)
a4 >> play("e", dur=PDur(3, 8), delay=6, feed=0.7, mverb=0.4, amp=1, echo=0.5, lpf=4000, lpr=0.1).unison(2)
a7 >> play("[ee]", dur=8, slide=var([0, 1]), delay=5.5, feed=0.7, sample=2, rate=-1, mverb=0.4, amp=1, echo=0.25, lpf=4000, lpr=0.1).unison(2)
a8 >> play("[tr]", dur=8, slide=var([0, 1]), delay=0.5, feed=0.7, sample=var([3, 4, 5]), rate=P*[2, 4, 8], mverb=0.4, amp=1, echo=0.25, lpf=4000, lpr=0.1).unison(2)
a_all.feed=0.1
a_all.stop()
a_all.dur=1

#A2
Clock.bpm = 96;
a1 >> plaitsX(dur=var([2, 1], [16, 8]), slide=(0.01, (-0.03, 0.04)), slidedelay=(0.01, 0.1, 4), oct=(3, var([4, 5]), PRand([3, 4, 5, 6])), preset=var([0, 4, 12]), slidefrom=(0, 0.02, 0), sus=var([2, 3, 1], [4, 2]), shift=var([0.5, 1, 0.75]), amp=0.5).unison(2)

# A3
Scale.default = "minorPentatonic"
Root.default=4
Clock.bpm = 120;
a1 >> sos(dur=8, lpf=linvar([60,4800],[PRand(8,64), PRand(8,64)]), hpf=expvar([0,200],[PRand(8,64), PRand(8,64)]), fx1=1, vib=PWhite(0,16), vol=0.3).unison(3,0.5,90)
a2 >> ews(PTrir(0,8), dur=2, sus=2, squiz=0.8, rel=0.2, fx2=1, oct=PWhite(2,3), amp=0.8, vol=1)
a3 >> ews([2, (3, 5), (2, 3), [(3, 5), (5, 8)]], dur=2, sus=2, squiz=0.8, rel=0.2, oct=2, fx2=1, amp=1).sometimes("degree.shuffle")
a4 >> ews(linvar([2, 3.1], 4), dur=6, sus=6, rel=0.2, oct=2, amp=1, formant=1, fx2=1).unison(2)
a5 >> play("{{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{n[yyyN][xxxx]}} ", dur=PRand([1/2, 1/4]), sample=PRand(128), pan=PWhite(-1,1), lpf=PWhite(800, 8000), fx2=1, rate=PwRand([[-1, 0.2, 0.5, 1, 2],linvar([1, 4], 8),linvar([4, 1], 8),linvar([0.25, 4],8)],[16, 8, 4, 4]), echotime=PRand([0, 1, 2, 3, 4]),echo=PRand([0.25, 0, 0, 1, 2, 0.125, 0]), hpf=PWhite(40, 2000), amp=var([0, PWhite(0.0, 0.4)], [PRand([8, 16]), PRand([2, 4, 6])]))
a6 >> ebass(PWhite(-0.1, 0.1),dur=64, hpf=400, oct=(3, 4), shape=(0, 0.5), fx1=0, spfslide=16, spfend=1600, spf=1).unison(4)
a7 >> radio(dur=32, hpf=PWhite(1000, 2000), formant=PWhite(1, 2), amp=PMorse("kakaaop"), fx2=1)
a8 >> ews(PTrir(0,8), dur=2, sus=4, squiz=0, vib=PWhite(0,32), fmod=PWhite(0,4), hpf=80, rel=0.8, oct=PWhite(2,3), amp=0.5, vol=0.2, cutoff=PRand(400,3800), spin=PWhite(-2,2))
a9 >> play("W ", dur=4, feed=linvar([0.1, 0.5],16), rate=var([1, -1], [7, 1]))
a7.stop()
a9 >> play("W ", dur=4, delay=1, feed=linvar([0.1, 0.5],16), shape=0.1,rate=var([1, -1], [7, 1]))
a1 >> play("W ", dur=4, delay=3, feed=linvar([0.1, 0.5],16), shape=0.4, rate=var([ PWhite(1.5, 2.5), -1], [7, 1]),hpf=200, hpr=PWhite(0.1, 0.5))
a2 >> play("W ", dur=4, delay=4, feed=linvar([0.1, 0.5],16), shape=0.6, rate=var([r2.degree, -1], [7, 1]), formant=P*[0,1], echotime=4, echo=1, echomix=PRand([0.25, 0, 0, 0, 0.5]), hpf=200, hpr=PRand([0.1,  0.2]))
a3 >> play("d ", dur=4, delay=4, hpf=1600, echo=0.25, echotime=2, feed=0.5, amp=PRand([0, 1]), chop=4)
a1.stop()
a_all.dur=8
a_all.rate=[2,4,8]
a_all.cut=1/2
a_all.hpr=0.05
a_all.vol=0.5
a_all.rate=var([-2, 1])
Root.default = var([4.02, 4.0, 4.12])

#A4
Clock.bpm = 135;
Scale.default = Scale.minorPentatonic
Root.default = "G"
a1 >> dafbass([0, 1, 7, 7, 5, 4, 5, 5], dur=PDur(4,8), oct=[4, 5, 5], shape=0, fmod=2, lpf=linvar([200, 8000], [24, 8]), sus=[1, 1/2, 1/2, 1]).rarely("offadd", var([4, 9])).unison(4)

#B4
Clock.bpm = 135;
b1 >> rsin(dur=var([1/4, 1, 1/2, 1/4], [12, 4, 2]), cut=linvar([1/4, 1/2], 32), hpf=linvar([50, 4000], 16), echo=linvar([0.25, 2], 4), oct=3, feed=[0.5, 0.33, 0.33, 0.33], dubd=0.5, dublen=0.01).unison(2)

#C3
Clock.bpm = 120;
c1 >> loop("xtech8", dur=8, sample=8, hpf=var([0, 200], [6, 2]), hpr=linvar([0.1, 0.9],8))
c0 >> loop("xtech8", dur=8, sample=8, lpf=var([10000, 200], [2, 6]), lpr=linvar([0.1, 0.9],32))
c3 >> loop("uk8", dur=16, sample=2, mverb=0.6, dist2=0) #0-3 -2
c4 >> play("x-", fx1=1, sample=P[0, 1], fx2=1, valad=0, amp=4, leg=PFrac(0.3,0.8,8).lmap(4, 1), valadr=0).solo(0)
c6 >> loop("xtech8", dur=16, sample=2)
c7 >> play("XCk-")
c8 >> loop("hiphop16", dur=32, sample=3)
c9 >> play("<b.><....W.......W...><W..W...W.WW.....>", dur=0.25, sample=56, rate=1)
c1 >> donk(P[0, 4, 5, 7], dur=PDur(8,8), oct=[6, 5, 3, 3, 4], rate = linvar([[4.15, 9.01, 10.48, 5.15, 3.02],[10.2, 3.56]],[15.69, 1.96, 26.38, 28.15]), leg=32)
c2 >> donk(P[2, 4, 2, 0, 0, 7, 0, 4, 2, 0, 2, 5, 7, 0, 0, 4], dur=SDur(16), oct=[3, 3, 6, 5, 6, 3], rq = linvar([[0.38, 0.2],[0.17, 0.5, 0.43]],[29.81, 11.72]), )
c3 >> pad2((0,2,var([4,5,7,-2],8)), dur=8, atk=2, blur=1.2, oct=([2, 4, 3],6), fx2=1, rate=8, amp=0.7, chop=4).unison(2)

#D2
Clock.bpm=92
Scale.default="minor"
d1 >> play(PEuclid2(var([3,4],[24,8]),8,"(vv{v@})","(-|=2|)"), dur=1, shape=P*[0,expvar([0.01,0.9],26)], lpf=linvar([800,7800],[64,0]), lpr=linvar([1,0.05],61)).often("stutter", Cycle([2,3,6,12]), pan=PWhite(-1,1))
d2 >> dbass(var([0,[-4,2,-2]],[14,2]), dur=P*[2,6],amp=(d1.degree!="v")*0.8, lpf=linvar([1800,3500],19), lpr=expvar([1,0.2],17), sus=b1.dur*PWhite(0.8,2),fx1=1, fx2=0.0, rate=linvar([0.1,15],23), oct=(PStep(7,6,5),4,PStep(4,6,5))).unison(3)
d3 >> play("<X ><(-[--]-[::])><..|*2|.><..C.>", bits=16, amp=1, dur=2, crush=3, room1=1, mix=PWhite(0,0.5)).rarely("amen").sometimes("stutter", PRand(1,6), rate=PRand([1,6]))
d4 >> sitar(P[0,5,P*[7,8,4],3], oct=P*[5,[6,4,3]], vib=PWhite(6,32), slide=0.01, slidedelay=PWhite(0.2,0.9), sus=s1.dur*PWhite(0.3,0.8), dur=1/4, room=1, mix=PWhite(0,0.2), amp=var([(d1.degree=="@"), (d1.degree!="@")],[28,4]), shape=(0,0.1), fx2=1).spread() + [0,0,P*[2,4],0]

#D3
Clock.bpm = 135;
d1 >> dbass(PDur([3, 5, 7], 11), dur=PDur([3, 7, 5], 11), shift=(var([0, 0.5, 1, 1]), 0), leg=128, fmod=0, spr=0.1,spf=(10, (2500, 12)), spfslide=(0.1, 1), spfend=(10000, (10, 12500)), echo=var([0.25, 0.5, 0.75, 1]), hpf=(200, 1200)).unison(4)
d1.hpf=0
d1.mverb=0.5
d1.dist2=0.2
d1.mverb=0
d1.often("shuffle")
d1.sus=1
d1.oct=5
d1.lpf=400
d1.lpr=0.2
d1.dur=4
d1.dist2=0
d1.sus=4
d2 >> play("X ")
d3 >> dbass(PDur([3, 5, 7], 11), dur=PDur([3, 7, 5], 11), shift=(var([0, 4, 1, 1]), 0), leg=0, fmod=0, spr=0.1,spf=(10, (2500, 12)), spfslide=(0.1, 1), spfend=(100, (10, 1250)), echo=var([0.25, 0.5, 0.75, 1]), hpf=(2000, 1200), dist2=1).unison(4)

#D4
Clock.bpm = 135;
d7 >> loop("hiphop16", dur=16)
d6 >> play("C:.Cc.", sample=(5, 4), lpf=(1200, 4000), hpf=1200).sometimes("stutter")
d0 >> play("<X ><O.><-.>", dur=8, sample=4, echo=2).rarely("stutter", 4, fold=1)
d7 >> loop("nsbass16", dur=16, sample=1, hpf=400)
d1 >> loop("hiphop16", dur=16, sample=2)
d0.sample=4
d6.sample=1
d0.hpf=1700
d6.hpf=3200
d2 >> loop("hiphop16", dur=16, sample=4, hpr=0.9, hpf=1200)
d2.sample=3
d2.hpf=0
d7.sample=2
d1.sample=4
d7 >> loop("nsbass16", dur=16, sample=1, hpf=400, echo=4, mverb=0.5)
d7.shift=1
d7.chop=32
d7.chopmix=0.2
d7.shift=0
d9 >> loop("psych32", dur=32, sample=2, lpf=4000, mverb=0.5)
d0.hpf=0
d0.echo=(1, 2.25)
d0.dur=2
d9 >> play("X[::]", amp=1, sample=4)
d8 >> loop("psych32", dur=32, sample=3, lpf=4000)
d7 >> loop("core16", dur=16, sample=3, hpf=200)
d1 >> play("..U.")
d2 >> play("XK.V.", dist2=1)
d3 >> play("[--]", amp=4)
d9 >> loop("gab16_10sec_180", dur=32, sample=1, hpf=400)
d8 >> loop("ravebass8", dur=8, sample=5, shape=0.0, amp=1, hpf=4000)
d7.stop()
d8.stop()
d4 >> play("V ", amp=4)
d0.dur=2
d8.stop()
d9.stop()
d0.dur=1/2
d3.sample=1
d2.sample=2
d1.sample=0
d4 >> play(".cC.",dur=1/2, dist2=1)
d6 >> play("X ", amp=2)
d5 >> dbass((0, 2, var([4, 6], [8]))).unison(4)
d9.hpf=400
d0.dist2=0
d1.echo=0
d1.lpf=linvar([200, 1200], 32)
d6.dur=4
d4.stop()

#E2
Root.default='C'
Scale.default="minor"
Clock.bpm = lininf(120, 170, 128)
b1 >> lbass(var([0, -2, 0.5], 8), formant=var([0, 0.1], [24, 8]), formantmix=PWhite(0, 0.3), oct=(6, 5, [4, 3]) + var([0, 1], [14, 2]) + PwRand([0, 1, 1.25], [30, 1, 1]), rate=linvar([1.2, 0.3], [32]), fmod=linvar([0, 1], [128]), scale=Scale.chromatic, shape=var([0, (0.1, 0)], [12, 4]), dur=1/2, amp=0.5, mverb=0, mverbdamp=[0.2, 1], mverbdiff=[1, 0.4], hpf=linvar([100, 400], 8)).unison(4).every(8, "stutter", slide=0.01, lpf=linvar([4000, 8000], 16))
b2 >> faim(var([0, -2, 0.5], 8), oct=(3, 4, 5) + var([0, 1], [14, 2]), width=PWhite(0.1, 0.9), rate=linvar([1.2, PWhite(0.3, 8)], [64]), shift=var([0, 1, 1.2], [13, 2, 1]), fmod=linvar([0, PRand(4, 8)], [128]), scale=Scale.chromatic, delay=(0, 0.25, [0.5, 0, 4]), dur=P*[1/2, 1, 1, 1/4, 1/4, 1/4], amp=0.5, hpf=100).unison(2).every(8, "stutter", slide=[2, -2], degree=(-12, 12), echo=(0, 0.125), echotime=1, lpf=linvar([1000, 4000], 16))
b1.rate=lininf(1, 0.1, 32)
b1.mverb=0.0
b3 >> soprano((b1.degree, 0), dur=PRand(1,8), blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(7,6,5)), shape=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), room=0.5, mix=0.5, amplify=0.5, spin=0).unison(2)
b1.lpr=lininf(1, 0.1, 64)
b1.slide=var([0, 1], [28, 4])
b1.degree=0.5
b1.chop=var([0, 1, 1/2], [12, 2, 2])
b2.dur=1/4
b4 >> play("(#....)..(...~)", rate=PWhite(-1,4)*0.25).unison(3, 1,99)
b5 >> play("@", sample=4, hpf=4000).fill(0)
b6 >> play("3", dur=1/2, amp=0.5, sample=(var([3, 4], [4, 4]), 3), glide=1,shift=var([0, 2], [24, 8]), pshift=0).slider()
b7 >> play(var(["-.--", "[--]"], 8), sample=1, rate=0.5, formant=0.4, hpf=7000)
b1.dur=lininf(1/2, 1/4, 16)
b1.lpf=linvar([3200, 1600], 128)
b1.amp=0.6
b8 >> dbass(var([0, -2, 0.5], 8), oct=(6, 5) + var([0, 1], [14, 2]), rate=linvar([1.2, 0.3], [64]), scale=Scale.chromatic, dur=1/2, amp=1, hpf=100).slider().unison(4).solo(0)
e1 >> play("# ", dur=4, rate=(-1, 2)).unison(2).after(4, "stop")
e2 >> play("# ", sample=(1,4), dur=4, rate=(-1, 1)).after(8, "stop")
e3 >> play("& ", sample=5, rate=-2, shift=4, dur=4).after(32, "stop")
e4 >> play("#k", sample=(1,4), dur=4, rate=(-1, 1), mverb=1, room2=0.5,  chop=0.25, chopmix=[0.5, 0], damp2=0.9, revsus=1).after(4, "stop")
d0 >> fbass()
d1 >> fbass()
d8 >> ebass()
d1 >> play("x ", sample=6)
d2 >> play("--=-", sample=[2, 2, 1, 1], dur=1/4, delay=PWhite(-0.01, 0.01))
d3 >> play("+", sample=6, delay=PRand([-1/4, 1/4, 0]))
d4 >> play("c", sample=6, amp=var([0, 1], [12, 4]), amplify=PBin())
d5 >> play("C", sample=0, amp=var([0, 1], [12, 4]), amplify=PBin())
e1 >> play("X ")

#### E2
e1 >> charm(leg=4, oct=3,  sus=1/2, dur=4, echo=0.5, shape=0, dist=0, pan=[-1, 1], amp=0.5, room2=1, revsus=4).unison(2)
e2 >> play("k-", sample=4, hpf=4000)
e3 >> abass(var([0, 0, 1, ([-12, 24], 0), 12, linvar([8, 0], 4)], [4, 4, 4, 4, 4, 2]), lpf=0, slide=0.01,scale=Scale.chromatic,oct=(3, PStep(4, 4, PStep(12, 5, 6))), dur=1/4, sus=[1/4, 1/2], amp=linvar([(0, 1), (1, 0.5)], 128), shape=var([0.1, 0.15], [24, 8])).sometimes("stutter", shape=0.4)

#### F1
Clock.bpm = 135;
f1 >> play("k", sample=2, dur=1, mverb=1, mverbdamp=[0.8, linvar([0.5, 0.8])], mverbdiff=[0.4, 0.1, 0.1, PWhite(0, 1)], amp=0.5)
f2 >> play("x", amp=0.5, sample=var([3, 4], 4), dur=2, cut=0, mverb=1, mverbdamp=[0.1, 0.5, 0.9], mverbdiff=0.1)
f3 >> soprano([VI, II], amp=0.5, mverb=1, cut=1/2, dur=8, oct=(3, 4), root=[0, PStep(4, 0, 4)], shape=0.1).unison(2)
f4 >> play("n", mverb=1, sample=PRand(12), bpf=400, dur=12, cut=1/4, delay=2, rate=0.25, pan=-1, amp=0.5)
f5 >> play("n", mverb=1, sample=2, dur=24, cut=1/4, delay=4, rate=0.25, pan=1)
f6 >> soprano([III, VII], amp=0.5, mverb=1, slide=0.1, cut=1, dur=8, oct=(3, 4), root=[0, PStep(4, 0, 4)], shape=0.1).unison(2)
f7 >> soprano([III, VII], amp=0.5, mverb=1, slide=2, cut=4, dur=8, oct=(3, 4), root=[0, PStep(4, 0, 4)], shape=0.1).unison(2)
f3.stop()
f8 >> loop("xtbass16", dur=16, sample=2, amp=1)
f6.stop()
f7.stop()
f3 >> rsin(Scale.minor,dur=1/2, oct=4, amp=linvar([0, 1]), shape=0.0).every(1, "shuffle").unison(2)
f9 >> play("<[--]><..U(..[UU])><..o.><.:>", amp=1, sample=4, room2=1, mix2=0.3, revsus=0.5, revatk=-0.3).sometimes("stutter", 4)
f6 >> soprano(var(PChords(),8), dur=PRand(1,8), blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(7,6,5)), shape=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), room=0.5, mix=0.5, amplify=0.25, spin=0).unison(2)

#G1
Clock.bpm = 120;
g4 >> ebass(linvar([(-4, 4), (4, -4)], 128),dur=1/4, hpf=400, hpr=0.05, shape=0.0, lpf=1200, mpf=1600, lpr=0.1)
g5 >> play("[--]", hpf=400, fold=0.2, sample=3, cut=1/4)
g6 >> play("[--].-", hpf=400, fold=0, sample=P[5, 7], cut=1/4)
g5 >> ebass()
g1.oct=3
g2.oct=5
g7 >> play("k ", cut=(1/4, P*[0.125, 0.25, 0.5]), sample=4, echo=(0.25, 0.5), dur=PDur(3, 8))
g8 >> play(".. ", sample=4)
g9 >> play("q ", sample=2)
g1 >> play("[.u]u..", sample=4, dur=2)
g2 >> play("v[--]", sample=9)

#J2
j1 >> play("x", dur=PDur(var([P[11, 7], 8]), [13, 14], 0), lpf=0, vol=0.2, valad=PStep(3, 1, 10200, PWalk(8, 1, 1)), valadd=P*[4, 16, 32,64][:8], bpf=0, hpf=40, sample=0)
j2 >> play("b", dur=PDur(var([P[11, 7], 8]), [13, 14], 0), lpf=0, valad=PStep(3, 1, 10200, PWalk(8, 1, 1)), valadd=P*[4, 16, 32,64][:8], bpf=0, hpf=400, sample=var([5, [6, 7]], [12, 4]), vol=0.2)
j4 >> play("db ", sample=2, amp=1)
j5 >> plaits(oct=5, dur=4, amp=1, vol=0.5, mverb=1, engine=var([3, 4, 5, 6]))
j6 >> play("{e-}", sample=11, leg=2, dur=8, rate=(0.1, 0.5, 0.25, 1), sus=2, hpf=40, mverb=0.5)
j7 >> play(var([":", ":-"], [7, 1]), delay=1, sample=4, leg=var([0, 12]), dur=8, rate=(0.1, 0.5, 0.25, 1), sus=2, hpf=40, mverb=0.8)

Clock.bpm = 135;
g1 >> play("W ", sample=2, mverb=1)
g2 >> play("W:", sample=2, mverb=1, lofi=linvar([0.1, 1], [48, 16]), pan=[-1, 1])
g3 >> play("WV", sample=2,lofi=0.7, hpf=[0, 4000, (2000, 0), 12000])
f_all.hpf=1200
a8 >> play(".:", sample=8)
a9 >> play("X ", lpf=400)
e1 >> play("K ", hpf=0)
e2 >> play("--")
e3 >> play("V ", sample=4)
g9 >> loop("half16", dur=16, sample=2 , lpf=0)
g4 >> play("[--]-[-^]^^", coarse=1, fold=0, symetry=1, chop=4, cut=1/2)
g5 >> play("+", amp=P*[1,1,1,1.5,3,1/2,1/2,1,1.5]*1.3, dur=1/4, hpf=2000, lpf=6400, amplify=0.5 + PWhite(-0.2, 0.2), pan=(PWhite(-1,1), PWhite(-1,1)))
g6 >> play("ccc.", sample=2, fdistfreq=4000, fdist=1, rate=[PWhite(0.9, 1.1), 1, 1, 1])
g7 >> play("C.c.....cc.....", sample=1, flanger=1)
g8 >> play("[--]", sample=3, amp=PMorse("fzefk"))

Clock.bpm = 135;
g1 >> play(".:", sample=8)
g2 >> play("X ", lpf=400)
g3 >> play("K ", hpf=0)
g4 >> play("--")
g5 >> play("V ", sample=4)

#### I1

#P1
Scale.default = Scale.chinese
Root.default = "B#"
Clock.bpm = 48;

p1 >> mpluck((PWalk(8, 1, 1), melody()), dist2=0.2, dur=P[1/4, 1/4, 1/4,(1/4, 1/2), 1/2], rate=1, sus=P*[1/2, 2, 1, 1/4, 1], delay=(0, 0.25, 0.5), amp=PwRand([1, 0.5], [1, 12]), oct=PStep(4, [4, 5], 6)).penta()
p2 >> pluck((PWalk(8, 1, 1), melody()), dur=P[(1/4, 1/2), var([1/4, 1/8], [11, 2, 3])], rate=1, sus=P*[1/2, 2, 1, 1/4, 1], delay=(0, 0.25, PRand([0.25, 0.5, 0])), amp=PwRand([1, 0.5], [1, 12]), oct=4)
p1 >> jbass()
p2 >> dbass(melody(),oct=6, dist2=0, amp=PBern(4), lpf=12000).unison(4)
p2 >> pluck((PWalk(8, 1, 1), melody()), dur=P[(1/4, 1/2), var([1/4, 1/8], [11, 2, 3])], rate=1, sus=P*[1/2, 2, 1, 1/4, 1], delay=(0, 0.25, PRand([0.25, 0.5, 0])), amp=PwRand([1, 0.5], [1, 12]), oct=4).strum(4)
p1 >> play("X.-:").strum()
p2.dur=1/8

p2>>fbass(amp=0.3, stut=0.2).strum(4)
p1 >> fbass().strum(4)
p2 >> fbass(4, dur=2, mverb=1)
p1 >> fbass(dur=1/8, oct=var([6, 4, 3, 2]), fold=0.2, amp=linvar([0.01, 0.2], 128)).slider()
p2 >> donk()

p3 >> dbass(leg=128, cut=1/8, dur=PDur(3, 8), echo=0.25)
p4 >> dbass(mverb=1, cut=1, dur=PDur(5, 13), oct=5)

p3 >> mpluck(p1.degree,dur=2, sus=4).accompany(p1)

#S4
superbass = SynthDef("superbass")
superbass1 = SynthDef("superbass1")

s1 >> superbass(dur=8, oct=((4, 1)), leg=(0, 128), mverb=0.5, cutoff=(400, 5000), chop=(4, 0.25, 0.33), fold=0, rq=linvar([0.4, 0.7], 32), rqd=1, detune=4, dist2=linvar([0.01, 0.5], 128)).strum(8)
# [superbass1 not registered] s1 >> superbass1(oct=5)
# [superbass1 not registered] s1 >> superbass1(dur=4, oct=4, spf=linvar([10000, (100, PRand(100, 1000))], [8, 3]), spfend=linvar([100, 8000], [8, 3]),spfslide=linvar([2, 1], [8, 3]), sus=6, detune=0.1, rqd=0.2, rq=0.9)
s2 >> superbass(dur=var([2, 1/2], [4, 12]), cut=1/2, amp=0.1, dist2=0, echo=(0.25, 0.5), oct=5, spf=linvar([10000, (100, PRand(100, 1000))], [8, 3]), chop=4, spfend=linvar([100, 8000], [8, 3]),spfslide=linvar([2, 1], [8, 3]), sus=6, detune=0.1, rqd=0.2, rq=0.9)
s1 >> superbass()
s1.cut=0
