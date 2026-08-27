# live2 90
# live

x1 >> faim(PArp([0,var([2, PArp([(0, 3), (PArp([4, 5, 6, _], PRand(8)), 3,_), 4], PRand(8)), [_, PArp([0, 6,_, 12], PRand(8))], (PArp([0, 2, 4, _], PRand(8)), 0), 3], 8), PRand(8)], PRand(2)), oct=5, rate=1, dur=1/4, scale=Scale.minor,amp=var([0, 1], PRand([2, 4, 8, 16])))
x2 >> faim(PArp([0,var([2, PArp([(0, 3), (PArp([4, 5, 6, _], PRand(8)), 3,_), 4], PRand(8)), [_, PArp([0, 6,_, 12], PRand(8))], (PArp([0, 2, 4, _], PRand(8)), 0), 3], 8), PRand(8)], PRand(2)), mverb=(1, 0), amp=var([0, 1], PRand([2, 4, 8, 16])), sus=1/4, oct=var([5, 6, (4, 5), (5, 6), (3, 5)], [16, 8, 8]), rate=1, dur=var([1/2, 1/4], [24, 8]), scale=Scale.minor).every(4, "shuffle")
x4 >> faim(dur=1/2, oct=4, shape=0.2, beef=1,amp=var([0, 1], PRand([2, 4, 8, 16]))).follow(x1)
x7 >> blip(x2.degree, dur=1/4, oct=5, rate=2,amp=var([0, 1], PRand([2, 4, 8, 16]))).unison(2)
#############A1

a1 >> sos(dur=8, lpf=linvar([60,4800],[PRand(8,64), PRand(8,64)]), hpf=expvar([0,200],[PRand(8,64), PRand(8,64)]),vib=PWhite(0,16), vol=0.3).unison(3,0.5,90)
a2 >> ews(PTrir(0,8), dur=2, sus=2, squiz=0.8, rel=0.2, oct=PWhite(2,3), amp=0.8, vol=1)
a3 >> ews([2, (3, 5), (2, 3), [(3, 5), (5, 8)]], dur=2, sus=2, squiz=0.8, rel=0.2, oct=2, amp=1).sometimes("degree.shuffle")
a4 >> ews(linvar([2, 3.1], 4), dur=6, sus=6, rel=0.2, oct=2, amp=1, formant=1).unison(2)

###########A2
a1 >> play("{{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{n[yyyN][xxxx]}} ", dur=PRand([1/2, 1/4]), sample=PRand(128), pan=PWhite(-1,1), lpf=PWhite(800, 8000), rate=PwRand([[-1, 0.2, 0.5, 1, 2],linvar([1, 4], 8),linvar([4, 1], 8),linvar([0.25, 4],8)],[16, 8, 4, 4]), echotime=PRand([0, 1, 2, 3, 4]),echo=PRand([0.25, 0, 0, 1, 2, 0.125, 0]), hpf=PWhite(40, 2000), amp=var([0, PWhite(0.0, 0.4)], [PRand([8, 16]), PRand([2, 4, 6])]))
a2 >> ebass(PWhite(-0.1, 0.1),dur=64, hpf=400, oct=(3, 4), shape=(0, 0.5), spfslide=16, spfend=1600, spf=1).unison(4)
a3 >> radio(dur=32, hpf=PWhite(1000, 2000), formant=PWhite(1, 2), amp=PMorse("kakaaop"))
a4 >> ews(PTrir(0,8), dur=2, sus=4, squiz=0, vib=PWhite(0,32), fmod=PWhite(0,4), hpf=80, rel=0.8, oct=PWhite(2,3), amp=0.5, vol=0.2, cutoff=PRand(400,3800), spin=PWhite(-2,2))
a5 >> play("W ", dur=4, feed=linvar([0.1, 0.5],16), rate=var([1, -1], [7, 1]))

########### B1
Clock.bpm = 90
b1.shift=0
b1 >> faim(b1.dur, oct=([3, 4], PStep(9,5,[4,5])),dur=var([PDur(var(PRand(5,7),[4,12]),12),4],[24,8]), shape=b1.dur/10, shift=0, slide=b1.dur/4, delay=var([0, (0,(0,[0,0.25]))], [PRand([2, 4, 6, 8]), 4]), amp=PRand([0.5,0.1, 0.25, 1, 0.75])).unison(8).sometimes("stutter", beef=(b1.shift*-1)*120, shift=var([1, 2, (1/2)], [7, 5, 4]))
b2 >> play("{tTPp}", sample=(2,P[0:5]), leg=4, amp=var([b1.dur/4, 1], [4, 4]), room2=1)
b3 >> play("P ", amp=b1.amp, feed=0.2, leg=4, echo=0)

############ B3
Clock.bpm = 70;
Scale.default = "chromatic"
b1 >> bass(-4, oct=6, dur=1/4, lpr=0.1, lpf=4000).human(40, 0, 0).unison(4)
b2 >> bass(8, oct=[5, 5], dur=1/4)
b3 >> feel(18, oct=4, dur=1/4, amp=PWhite(0, 1), pan=PWhite(-1, 1)).unison(2)
b4 >> pluck((15, 20), dur=var([1, 1/8, 1/4, 1/8, 1, 1/8, 1/4, 1/2], [2, 1/4]))
b5 >> pluck(33, dur=1/2, amp=[0, 1])

####### B2
Clock.bpm = 70
p1.stop()
p2.stop()
p_all.amp=var([0.3, 0, 0.1,0.2])

b1 >> pluck(var(PChords(),8), dur=PRand(1,8)/PRand(1,4), blur=PWhite(1,4), decay=PRand(1,4), oct=(3,4,PStep(7,6,5)), shape=PWhite(0,0.1), sus=PRand(1,16), atk=PStep(8,0.2,PRand(1,6)), room2=1)
b2 >> jbass([b1.degree[0],b1.degree[2]], dur=[6,2], amp=1, oct=[5,6,5], glide=P[0:8]*PRand([-1,0,1]), glidedelay=PWhite(0.7,0.99), shape=[0,PWhite(0,1),0.2,0,0.3], echo=(b1.shape>0)*b1.dur/PWhite(0.1,4), echotime=b1.degree, lpf=[4500,5500+b1.shape*1000], hpf=60).every(6, "unison", cycle=[0,4])
b3 >> blip(b1.degree[0] + (0,[2,4]), dur=[1/2,1/2,1/2,P*[0.5,rest(2.5)]], amp=1, oct=(5), rate=PRand(1,4), leg=PRand(0,8),glide=0.5, fmod=4, vib=PRand(2,16), sus=PWhite(0.5,1), echo=[0,0.25], lpf=PRand(400,12888), room=1, mix=PWhite(0,0.5)).unison(3).every(8, "mirror")
b4 >> sawbass(b1.degree[0], dur=8, sus=[8,PRand(1,8)], echo=1/2, mid=2, echotime=PRand(0,12), oct=(5,4,5), shape=(0.01,0,0.01)).unison(3,var(PWhite(0.25,0.30)),var(PRand(99),8))

######### B4

Clock.bpm = 90
#annihilation suite
b1 >> subbass([2,3,[5,7]], dur=16, amp=0.4, crush=(0,PRand(0,4)), bits=PRand(4,16), fx1=0.2, atk=PWhite(0.005,0.1), oct=(4,5), lpf=4000).unison(4)
b2 >> klank(b1.degree[0], fx2=1, rate=linvar([8, 16], 64), oct=(3, 4), dur=P*[4, 8, 12], lpf=linvar([400,3800],128), lpr=0.1, amp=linvar([0.5, 0.7], 128), hpf=600, bpm = 80 + PWhite(-20, 20), fdist=1, fdistfreq=PWhite(1200, 2000)).unison(2)
b3 >> total(b0.degree[0],dur=32, chop=PRand([0, 0.5, 1, 0.35]), amp=[1,PWhite(0,1)], fmod=PRand([16, 32, 64, 128]), fx1=0, bpf=PRand(800,4000), bpr=0.1, vib=PRand(16), spin=PWhite(-1,1), shape=0.01).slider().unison(2)
b4 >> jbass(var([PWalk(8, 1, 4),PWalk(15, [1, 4], 1)], [4, 4]) , dur=[15, 1/4, 1/4, 1/4, 1/4], sus=[2, 1/4, 1/4, 1/4, 1/4], oct=PStep(7, [3,5], 6), echo=P*[2, 1, 1, 1, 1], amp=0.5, rate=0.1, fx2=1, fx1=1, crush=P*[0,8]).unison(2).slider(0,PStep(8,1,0))
b5 >> bass(b0.degree[0], leg=0.2, oct=(4,6), dur=[15,1], amp=0.4, fx1=1, delay=PWhite(-1,1).rnd(0.25), echo=[0,P[0,0.25,0.5,0.75]], comp=0.6)
b6 >> ebass([ PWhite(-0.1, 0.1),PWhite(5, 3) ], slide=16, dur=64, hpf=400, oct=(3, 4), shape=(0, 0.5), spfslide=16, spfend=1600, spf=1).unison(4)
b7 >> ambi(P*[b0.degree[0],b0.degree[1],b0.degree[2], (b0.degree[0], b4.degree[1]), (b0.degree[1], b0.degree[2]), (b0.degree[0], b0.degree[2]),P**(b0.degree[0], b0.degree[1], b0.degree[2]),P+(b0.degree[0], b0.degree[1], b0.degree[2]), P/(b0.degree[0], b0.degree[1], b0.degree[2])], dur=P*[5,1,1/2,8,3], sus = b1.dur, delay=P*[0,PWhite(0,1)], oct=PwRand([6,5,4,3],[30,35,20,15]), velocity=PRand(40,65), fx2=1, amp=PWhite(0.2,0.3), velhard=PWhite(0.2,1), hard=PWhite(0,2), lpf=PRand(5000,18000)).unison(3).penta()
b8 >> pasha(var([b4.degree, b0.degree, b0.degree + 5], [3, 5]), cut=var([0, 1/4], [8, 8]), oct=(3,6), dur=PDur(var([2,3,4,5],[5,1,1,1]),8), amp=var([0,0.1],PRand(4,16).rnd(2)), sus=y0.dur*PWhite(0.1,0.01), echo=var([0.5,[0.125,0.25,0.75]],[6,2]), pan=y4.dur*P[1,-1], lofi=expvar([0.1,1],[PRand(19),PRand(8)])) + var([0, var([0,PTrir(0,2,0)],[6,2])], [2, 8])
Clock.bpm = 90
Root.default=lininf(4, 0, 32)
Root.default='C'
b9 >> zap(0, dur=8, hpf=40, shape=[PWhite(0.1,0.4),0.2], oct=(3, PStep(9,5,[4, (5, 6)])), chop=4, chopmix=0.25, spf=10, spfend=8000, spfslide=(0.1, PRand(4,8)), octer=1, octersubsub=var([2, PRand(1,15)], [13]), fx1=0, hpfx1=80, amp=P[0.3,0, 0.1, 0, 0.1, 0], vol=0.7).unison(4)
b0 >> sawbass(0, dur=8, sus=[8], echo=1/2, amp=(b1.amp==0), mid=2, echotime=PRand(0,12), oct=(5,4,5), shape=(0.01,0,0.01), vol=0.6).unison(3,var(PWhite(0.25,0.30)),var(PRand(99),8))

########### C2
Clock.bpm = 90
c1.shift=0
c1 >> faim(c1.dur, oct=([3, 4], PStep(9,5,[4,5])),dur=var([PDur(var(PRand(5,7),[4,12]),12),4],[24,8]), shape=c1.dur/10, shift=0, slide=c1.dur/4, delay=var([0, (0,(0,[0,0.25]))], [PRand([2, 4, 6, 8]), 4]), amp=PRand([0.5,0.1, 0.25, 1, 0.75])).unison(8).sometimes("stutter", beef=(c1.shift*-1)*120, shift=var([1, 2, (1/2)], [7, 5, 4]))
c2 >> play("{tTPp}", sample=(2,P[0:5]), leg=4, amp=var([c1.dur/4, 1], [4, 4]), room2=0)
c3 >> play("P ", amp=c1.amp, feed=0.2, leg=4, echo=0)
c4 >> click(0, dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), hpf=40, shape=[PWhite(0.4,0.8),0.2], oct=(3, PStep(9,5,4)), octer=1, octersub=2, octersubsub=var([2, PRand(15,2222)], [15, 1]), triode=4, amp=0.1, amplify=1).unison(3).rarely("stutter",PRand(6), oct=6, pan=[-1,1], mpf=2860, hpf=400)
c5 >> play("<u><t>", sample=(2,P[0:5]), delay=(0,(0,[0,0.25])), dur=c1.dur, crush=[0,0,0,PRand(8)], bits=4, lpf=1500)

################ C1
Clock.bpm = 95
Root.default = 4
c0 >> faim([3, 3, 15, 3, 3, 6,3, 3, 15,3, 3, _, 3, 2, 3, 3, 3, 9, 2, 9, _], dur = [1/4, 1/4, 1/2, 1/2, 1/4, 1/4, 1/4, 1/4, 1/2, 1/2, 1/2, 1/4, 1/2, 1/2, 1/4, 3/4, 1/4, 1/4, 1/4, 1/4, 3/4], sus=b0.dur + linvar([0, 0.1], 4) + c0.drive, scale=Scale.chromatic, oct=4 + c0.drive, rate=c0.drive, beef=P[1:4], shape=var([0, 0.5, 1], [30, 1, 1]),mverb=c0.drive, amp=0.5).unison(2)
c1 >> faim([3, 3, 15, 3, 3, 6,3, [3, 7], 15, [3, 2], 3, _, 3, 2, 3, 3, 3, 9, 2, 9, _], octersub=[0.1, 0], octersubsub=[0.4, 0.1], octer=0.1, dur = P[1/4, 1/4, 1/2, 1/2, 1/4, 1/4, 1/4, 1/4, 1/2, 1/2, 1/2, 1/4, 1/2, 1/2, 1/4, 3/4, 1/4, 1/4, 1/4, 1/4, 3/4], amp=0.5, sus=c1.dur + linvar([0, 0.2], 4), mverb=0, scale=Scale.chromatic, oct=PStep(4, 5, 5), slide=(0.01, -0.01))
c2 >> blip([3, 3, 15, 3, 3, 6,3, 3, 15,3, 3, _, 3, 2, 3, 3, 3, 9, 2, 9, _], dur = P[1/4, 1/4, 1/2, 1/2, 1/4, 1/4, 1/4, 1/4, 1/2, 1/2, 1/2, 1/4, 1/2, 1/2, 1/4, 3/4, 1/4, 1/4, 1/4, 1/4, 3/4], sus=c1.dur + linvar([0, 0.2], 4), scale=Scale.chromatic, mverb=1, amp=0.5, shape=0.1).unison(2).every(4, "shuffle")
c4 >> play("c", amp=c2.degree==15, echo=0.5, sample=1, rate=[-1, 1])
c0.dur=2

## D1
d7 >> play(P["x-(-m)"][:8].rotate(var([1,3])), rate=1.5, dur=1/4,amplify=0.8, delay=var([0,(0,0.75)],PRand(8)),sample=1)

#### E1
e1 >> charm(leg=4, oct=3,  sus=1/2, dur=4, echo=0.5, shape=0, dist=0, pan=[-1, 1], amp=0.5, room2=1, revsus=4).unison(2)
e2 >> play("k-", sample=4, hpf=4000)
e3 >> abass(var([0, 0, 1, ([-12, 24], 0), 12, linvar([8, 0], 4)], [4, 4, 4, 4, 4, 2]), lpf=0, slide=0.01,scale=Scale.chromatic,oct=(3, PStep(4, 4, PStep(12, 5, 6))), dur=1/4, sus=[1/4, 1/2], shape=var([0.1, 0.15], [24, 8])).sometimes("stutter", shape=0.4)

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
f9 >> play("<[--]><..U(..[UU])><..o.><.:>", amp=1, sample=4, room2=1, mix2=0.3, revsus=0.5, revatk=-0.3).sometimes("stutter", 4)
f3 >> rsin(Scale.minor,dur=1/2, oct=4, amp=linvar([0, 1]), shape=0.0).every(1, "shuffle").unison(4)
f6 >> soprano(var(PChords(),8), dur=PRand(1,8), blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(7,6,5)), shape=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), room=0.5, mix=0.5, amplify=0.25, spin=0).unison(2)

#### F2
f1 >> faim(dur=var([0.5, 0.25], [7, 1]), oct=(P[7, 6] * var([1, 0.5], 16), var([3, 5], [14, 2]), 4),sus=expvar([3, 0.5], [64, 0]) * P[1, 1, var([1, 2, 3, 4, 5, 6, 7, 8], 8), 4] * 1, lforate=0.005, lfowidth=P[var([0.5, 4], 4), 1, 1, 2] * 0.01,  lpf=expvar([200, 4000], 64), lpr=0.5, amp=P[1, var([0, 0.5], [7, 1]), 0.5, 0.75]) * var([1, 0], [[1, 1, [1, 2], 2], [3, 3, [3, 2], 2]])
f2 >> ssaw(f1.degree,dur=0.5, oct=6, sus=0.05 * var([1, [4, 8]], [7, 1]), room=1, mix=0.1, iphase=1.1, iphase2=0.8, iphase3=0.85, offnote1=P[3, 2, 1, 0], offnote2=1.5, offnote3=0.3, amp=0.8).unison(2)

#### G1
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

##### G2
Clock.bpm = 135;
g1 >> play(".:", sample=8)
g2 >> play("X ", lpf=400)
g3 >> play("K ", hpf=0)
g4 >> play("--")
g5 >> play("V ", sample=4)

#### I1

Clock.bpm = 120;
i1 >> saw((0, 2, 4), dur=8, spf=(400, 800), bpf=800, tremolo=0.1, spfslide=i1.dur, spfend=(1200, 40), room2=0.5, slide=(0, 0.01), lpr=0.1, lpf=3200, revsus=8, ).unison(2)
i2 >> pulse((0, 2, 4), oct=(3, 4 ,5), dur=8, spf=(1200, 200), bpf=800, tremolo=0.1, spfslide=i1.dur, spfend=(1200, 40), echo=0.25, room2=0.5, slide=(-0.01, 0.01), lpr=0.5, lpf=3200, revsus=8).unison(2)
i5 >> subbass(P*[7, 3, 7, 6], hpf=200, sus=[0.5, 1],oct=(4, 5), dur=[3/4, 3/4, 3/4, 2/4, 2/4, 3/4], lpf=(400, 400)).unison(2)
i6 >> pads(var([VI, III]), dur=[4, 1/2, 1/2, 2, 1/2]).unison(4)
i7 >> tb303(dur=1/4, lpf=linvar([200, 1200],16), res=PWhite(0.1, 0.5), hpf=linvar([50, 400], 16)).follow(i1)
i2.oct=PStep(4, 5, 6)
i9 >> rsin([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 4, (3, 4)), dur=[PDur(4,8), 1/2], amp=1, crush=4, bits=8, fmod=4, lpf=0, vol=0.5)
i0 >> rsin([P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2]], oct=PStep(16, 3, (4, 5)), dur=[10, 1, 1, 1, 1, 1/2, 1/2, 1], amp=1, fmod=0, lpf=0, vol=0.5).slider().every(4, "shuffle")
# )

########### J1
# B2
Root.default='C'
Scale.default="minor"
Clock.bpm = lininf(120, 170, 128)

b1 >> faim(var([0, -2, 0.5], 8), formant=var([0, 0.1], [24, 8]), formantmix=PWhite(0, 0.3), oct=(6, 5, [4, 3]) + var([0, 1], [14, 2]) + PwRand([0, 1, 1.25], [30, 1, 1]), rate=linvar([1.2, 0.3], [32]), fmod=linvar([0, 1], [128]), scale=Scale.chromatic, shape=var([0, (0.1, 0)], [12, 4]), dur=1/2, amp=0.5, mverb=0, mverbdamp=[0.2, 1], mverbdiff=[1, 0.4], hpf=linvar([100, 400], 8)).slider().unison(4).every(8, "stutter", slide=2, lpf=linvar([4000, 8000], 16))
b2 >> faim(var([0, -2, 0.5], 8), oct=(3, 4, 5) + var([0, 1], [14, 2]), width=PWhite(0.1, 0.9), rate=linvar([1.2, PWhite(0.3, 8)], [64]), shift=var([0, 1, 1.2], [13, 2, 1]), fmod=linvar([0, PRand(4, 8)], [128]), scale=Scale.chromatic, delay=(0, 0.25, [0.5, 0, 4]), dur=P*[1/2, 1, 1, 1/4, 1/4, 1/4], amp=0.5, hpf=100).slider().unison(2).every(8, "stutter", slide=[2, -2], degree=(-12, 12), echo=(0, 0.125), echotime=1, lpf=linvar([1000, 4000], 16))
b1.rate=lininf(1, 0.1, 32)
b1.mverb=0
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

#P1
Root.default = 0
Clock.bpm = 70
Scale.default = minor
Root.default = var([2, 0, PWalk(8, 1, 4)], [13, 2, 1])
m1 >> pianovel((var([0,-2,-4],16),[1,2,1],var(PRand([5,6,2,4,7],8))), sus=10, lpf=linvar([3000, 0], 32), lpr=PWhite(0.2,0.9), blur=2, amp=0.4, dur=var([5,1,1], [6,1,1]), scale=Scale.minor, oct=PStep(6,6,4), fx2=1, fx2hpf=300, fx2lpf=7800).unison(3) + var([0, 4, 8], [6, 1, 1])
m2 >> pianovel([m1.degree, 0, (m1.degree, 3)], sus=m2.dur, amp=0.5, dur=var([1/2, PRand([1, 1/2, 1/4]), PRand([1/4, 8]), PRand([1/2, 2]), 1/4, 1/8], [2, 2, 1]), scale=Scale.harmonicMinor, oct=PStep(4,4,5), fx2=1, fold=0,bpm = 70 + PWhite(-20, 20)).unison(2) + var(PRand([0, 4, 8, -4, 6, -3]), [6, 1, 1])
m3 >> pianovel(m1.degree[0], fx2=1, rate=linvar([8, 16], 64), oct=(3, 5), dur=P*[4, 8, 12], lpf=linvar([400,4800],128), lpr=0.05, amp=0.5,bpm = 70 + PWhite(-20, 20))
m4 >> pianovel(m1.degree[1] + var([0, -2, -4, 6]), dur=4, oct=var([(5, 6), (4, 3)], 4), lpf=0, hpf=0, shape=0.0,lpr=0.0, chop=0, chopmix=0, lofi=0, amp=1)
m5 >> pianovel(P*[m1.degree[0],m1.degree[1],m4.degree[2], (m1.degree[0], m1.degree[1]), (m1.degree[1], m1.degree[2]), (m1.degree[0], m1.degree[2]),P**(m1.degree[0], m1.degree[1], m1.degree[2]),P+(m1.degree[0], m1.degree[1], m1.degree[2]), P/(m1.degree[0], bm.degree[1], m1.degree[2])], dur=P*[5,1,1/2,8,3], sus = m1.dur*PWhite(1,1.5), delay=P*[0,PWhite(0,1)], oct=PwRand([6,5,4,3],[30,35,20,15]), velocity=PRand(40,65), fx2=1, amp=PWhite(0.6,0.8), velhard=PWhite(0.2,1), hard=PWhite(0,2), lpf=PRand(5000,18000)).unison(3).penta()

#P2
Clock.bpm = 75;

p1 >> pianovel(var( [ P*[III, I, II, IV], [(0.5, 0,3)]]), dur=PRand([2, 4, 8, 1/4, 6, 1/4, 1/4,1/2, 3]), echo=[0.5, P*[0.25, 2]], echotime=4, velhard=var([1, PRand(100)], [4, 4]), delay=( PRand([0, 0.25, 0.5, 1, 2]), PRand([2, 0.25, 0.5, 1, 1/4])), velocity=PWhite(10,50), slide=0, oct=PStep(4, [(5, 4), (5, 6, 7), (4, 7, 2)], [4, 5, 6]), root=var([0,7]), amp=PWhite(0, 1)).unison(0)
p2 >> pianovel(P[0:10], dur=PRand([2, 4, 6, 1/2]), echo=[5, 2.5], ecotime=8, velhard=var([1, PRand(100)], [32, 4]), delay=(0, 0.25, 0.5, 1, 2), velocity=PWhite(10,50), slide=0, oct=PStep(4, [(3, 4), (5, 6, 7), (4, 7, 2)], [4, 5, 6]), root=var([0,7]), amp=var([PWhite(0, 0.5), 0]), scale=Scale.blues).unison(0)
p3 >> pianovel([VI, VI, IV, II], dur=var([ PDur(3, 8), 2], [3, 1]) * P[4, 1, 2] * P[1, 2, 4], flanger=0, root=p1.root, velhard=0.1 ,scale=Scale.minorPentatonic, velocity=PWhite(1, 120), delay=(0, 2, 0.5, 1, 2), slide=0, oct=PStep(4, [(3, 4), (4, 7, 3), (4, 6, 2)], [4, 5, 6]), amp=PWhite(0, 0.5)).unison(0)
p4 >> pianovel([0, Scale.minor, Scale.minorPentatonic[:4]] , root=p1.root, hpf=var([400, 1200]), dur=var([ PDur(3, 8), 2, 4], [3, 1] * 2), velocity=PWhite(10, 110), flanger=0, velhard=0.1, delay=(0, 0.25, 0.5, 1, 2), pan=-0,slide=4, oct=PStep(4, [(3, 4), (4, 5, 4), (4, 5, 2)], [3, 5, 6]), amp=var([PWhite(0, 0.3), 0], [5, 3])).unison(0)
p5 >> pianovel(PRand([V, III, VII]), dur=var([ 2, 2, 1, 1, 1/4, 1/4, 1/4, 1/4, 1/4, 4, 2, 1/4,1/2,1/4, 3, 1], [3, 1]), velhard=PWhite(0, 1), delay=(0, 0.25, 0.5, 1, 2), velocity=PWhite(10,50), slide=0, oct=PStep(4, [(3, 4), (5, 6, 7), (4, 7, 2)], [4, 5, 6]), amp=PWhite(0,2)).unison(0)

###

#H1
Clock.bpm = 135;
h1 >> ebass(linvar([2, [5, 6]], [4, 0]), shape=linvar([0.01, 0.1], [4, 0]), room2=1, damp2=0.5, scale=Scale.chromatic,dur=1/2, sus=var([1, 2], [28, 4]), fmod=var([8, 32], [60, 4]), oct=5).unison(0)
h2 >> ebass(linvar([2, [5, 6]], [4, 0]), shape=linvar([0.01, 0.3], [14, 2]),scale=Scale.chromatic,dur=1/4, sus=var([1/2, 1/4], [28, 4]), fmod=var([8, 64], [60, 4]), oct=5).unison(0)
h3 >> ebass(linvar([2, [5, 6]], [4, 0]), shape=linvar([0.1, 1], [24, 8]),scale=Scale.chromatic,dur=1/4, sus=var([1/2, 1/4], [28, 4]), fmod=var([8, 64], [60, 4]), oct=6).unison(2)

#X1
x1 >> play(PRand("Xx.xx.xx.xx.xx.x"), room2=.3, amp=0.2, mix2=0.43, revatk=0.1, revsus=0.5, sample=[0,7,4], lpf=8120, leg=PRand(0,42), krush=P*[0,4]).sometimes("stutter", PRand(8), rate=PRand(8)).slider(on=0)
x2 >> play(PRand("Xx.xx.xx.xx.xx.x"), amp=0.3, sample=PRand(20), dur=1/4, lpf=0, leg=var([15, 55],[8, 72]), krush=P*[0,4]).sometimes("stutter").slider()

#X2
Clock.bpm = 170
x1.mix2=1;
x1 >> play(PRand("Xx.x{Cxxx}.x{c--}.x-.x[xxx].x"), room2=.3, amp=0.4, mix2=PGauss(0.3, 0.1), revatk=(1-x1.mix2), revsus=(x1.mix2 / 0.5), sample=[0,7,4], lpf=8120, leg=PRand(0,(x1.mix * 10)+1), echo=(0, x1.mix2/4), rate=(1, var([1, linvar([[-1, 4], [4, -1]], 16)])), delay=(0.5, 0),pan=PWhite(-1, 1), echomix=x1.mix2, krush=P*[0,4]).sometimes("stutter", PRand(8), low=[(0, 0.5), 0.0], bpm=var([Clock.bpm, Clock.bpm/0.5], 8), rate=PRand(8)).slider(on=0)
x2 >> play(PRand("{gc.m.5.cc.--.-}"), lpr=x1.mix2, amp=0.4, sample=PRand(20), dur=1/4, lpf=x1.revsus * 1400, leg=var([15, 55],[8, 72]), krush=P*[0,4]).sometimes("stutter").slider()
x3 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), amp=0.4, cut=PWhite(0.1, 1), sample=PRand(20), dur=1/4, lpf=0, leg=20, krush=P*[0,2]).sometimes("stutter").slider()
x4 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x".replace("x", "o")), rate=2, amp=0.4, cut=PWhite(0.5, 1), sample=PRand(20), dur=1/2, lpf=0, leg=10, krush=0).sometimes("stutter").slider()
x5 >> play("-", sample=4, rate=linvar([PRand([1, 2, 4, 8, 16]), 1], PRand([1, 2, 4, 8])), dur=var([PRand([4, 16, 32]), 1/4]), shift=PRand([2, 4, 8]))
x6 >> play("x", sample=8, dur=PRand([1/4, 1/2]), krush=8, bits=(2, 0), crush=(8, 1), lpf=PRand([1200, PWhite(400, 12000)]), hpf=var([1000, 200, 4000], [2, 14, 2]), amp=0.1, pan=(PWhite(-1, 1), linvar([-1, 1])))
x7 >> play("x", sample=8, dur=PRand([1/4, 1/2]), krush=8, bits=(2, 0), crush=(8, 1), lpf=PRand([1200, PWhite(400, 12000)]), hpf=var([1000, 200, 4000], [2, 14, 2]), amp=0.3, pan=(PWhite(-1, 1), linvar([-1, 1])))

#X3

Clock.bpm = 170
x1 >> play('Po', rate=1, sample=8, dur=var([1, 0.5], [31, 1]), delay=0, lpf=P[1000, 800], krush=1.25, amp=0.35 * P[1.1, 1, 1, 1]).unison(4)
x2 >> play('X', rate=1.5, sample=6, dur=x1.dur, delay=x1.delay, krush=1, amp=0.5 * expvar([1, 0.25], [30, 2]) * 1.0)
x3 >> play('T', rate=1, sample=var([4, 8, 2], 8), dur=var([0.5, 0.25], [7, 1]), delay=[0, [0.5, 0.75]], sus=([1, 0.1], [2, 0.5]),hpf=500, amp=1, lpf=expvar([200, 4000], 64), lpr=0.5,)
x4 >> play('U', rate=1.1, dur=x1.dur, delay=x1.delay, sample=9, sus=0.25, amp=0.5 * 0.6)
x4 >> play('-', sample=3, dur=0.25, echo=P[[0.125, 0, 0], 0, 0, 0], echotime=2, delay=0.5, amp=0.2 * expvar([1, 0.5], 1/3) * var([0, 1], [32, 64, 64, 128, 32, 128, 64, 64]) * var([1, 0], [[7, 6], [1, 2]]))
x5 >> faim(dur=2, sus=0.5, delay=0.5, cutoff=5050, amp=1 * var([0, 1], [64, 64, 128, 128]) * 0.5)
x6 >> play('u', sample=(2, 1), dur=2, echo=P[[0.25, 0], 0, 0, 0], room=0.5, mix=0.1, amp=0.7)
x7 >> play('h', sample=18, dur=0.25, pan=PWhite(-0.5, 0.5), amp=0.25 * expvar([0.25, 1], [1, 0]) * var([1, 0], [[3, 0.5], 1, 1, 1, 2, 1, 0, 2, [3, 0.5], 0, 1, 0]) * expvar([0, 0, 1, 1], 64))
x8 >> play('v', dur=5, delay=0.5, krush=1, lpf=800, sus=0.1, amp=1)
x9 >> play('-', sample=1, dur=0.5, room=1, mix=0.15, amp=P[1, [0, 0, 0, [0, 1]], 0, 0, 0, 1, 0, 0] * 0.8)
x9 >> play('-', sample=9, dur=1, delay=0.5, amp=0.5 * var([1, 0], [64, 128, 32, 64, 64, 64, 128, 128]))
