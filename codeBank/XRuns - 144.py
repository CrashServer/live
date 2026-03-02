# XRuns - 144
# banger

Clock.bpm=144
Root.default = 2
Scale.default="minor"

p6 >> choir(h4.degree[0],dur=8,  atk=1, rel=1, bendc=0.1, vow=PTuple(PWhite(0.0, 5.0), 3), oct=(3,4,5), fx2=1, amp=1, hpf=140, high=1.2) + PWhite(-0.1,.1)
h4 >> dbass([(0, 2, 5), (0, 5, 6), (2, 5, 9), (0, 2, 6)], mverb=0.2, dur=8, sus=8, glide=0.15, amp=var([1, 0.8], [8, 8]), oct=var([6, (6, 7)], 8), cutoff=12200, vib=2, pan=PWhite(-0.6, 0.6), hpf=200, fbdelay=0.25, rgate=0)
j3 >> dbass(var([0,[2, -2]], 16), dur=1/2, oct=(4,5), rate=0.5, valad=800, valadr=0.3, valadd=15, valadt=0, valadc=0.2, hpf=(0, expvar([85,PRand(200,500)],33)), lpr=0.09,  bell=0.5, bellf=3000, bellq=0.9).unison(3) + var([0, PGauss(0, 4)], [14,2])

h4 >> dbass([(0, 5, 12), (2, 6, 12), (0, 2, 9), (5, 6, 12)],  chop=4, chopmix=0.5, glide=0.25,  rgate=1)

h4 >> dbass([0, 11, 4, 0, 2, 4, 5, 0], dur=[21, 0.5, 0.5, 1, 0.5, 0.5, 1, 1], sus=2, amp=var([1, 0.8], [8, 8]), oct=var([6, (6, 7)], 8), cutoff=12200, vib=2, pan=PWhite(-0.6, 0.6), hpf=800, fbdelay=0.25, glide=0, rgate=0)
p6.hpf=1200

h4 >> plaitsX([0, 11, 4, 0, 2, 4, 5, 0], dur=[21, 0.5, 0.5, 1, 0.5, 0.5, 1, 1], sus=2, preset=8, amp=var([1, 0.8], [8, 8]), oct=var(P*[5, 6, (6, 7)], 8), cutoff=12200, vib=12, pan=PWhite(-0.6, 0.6), hpf=200, fbdelay=0.25, glide=0, rgate=0, a=0.3)

s2 >> play("<-[--]>", sample=7, pan=PWhite(-1,1), hpf=240, rate=PWhite(1, 1.04)).sometimes("stutter", PRand(8))
p0 >> play("{[--][---]}:", dur=1/2, pan=PWhite(-.5,.5), sample=0, hpf=1400, hpr=PFr(0.1, 0.4, 404, 32), lofi=0 ).human(40, 2)

p6 >> choir(h4.degree[0],oct=(3,4,6)) + PWhite(-0.1,.1)

##############
p6.stop()
p1 >> pluck(P(var([0, -2], 32),var([P*[3,5], 4, 2], 8)), dur=PDur([4,5], 8), lpf=0, sus=2, blur=2, chop=4, fmod=2, rate=2,  hpf=PFr(150,4000), oct=PStep(16,P+(6,[3,4]),5), cutoff=1300, tape=0.5, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1, eb=0.25, ebfeed=0.5, ebmix=0.3, ebmode=1, ebwow=0.1, ebflutter=0.15, ebsat=0.3, amp=1).unison(3)

p1.dur=1/2
p1.oct=PStep(1,P+(6,[3,4]),5)

q1 >> cbass(7, dur=PDur(var(P*[4,5,7,8], [32]),8), cutoff=10, rq=0.2, rgate=0.5, boost=1.5, detune=0.01, follow=linvar([1, 8], 41), tanh=0.1,  oct=5, hpf=200, bell=0.5, bellf=3000, bellq=0.9, pan=expvar([-.9,.9], 13))

f2 >> play("k.", sample=0, amp=1, delay=var([0, PWhite(0,.2)], [7,1]), rate=PwRand([1, -1], [19, 1]), hpf=50, hpr=0.5)
s1 >> play("<x(...x)><..o.>", sample=(1,9), drcomp=0.2, mverb=(0,.1), vol=1, amp=([1,.2],2), hpf=(50, 300), hpr=(0.5, .9)).sometimes("stutter")
j3.a = [0.7,0]

z8 >> play(".(...[o.])..(..(.([o.])))", sample=5, bank=1, hpf=440, amp=1, fbdelay=0.15, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02).sometimes("stutter", PRand(2,6), amp=PWhite(0.3,0.6), rgate=0.5)

~h4 >> dbass([0,3,5,0,3,5,7,0], dur=[21,0.5,0.5,1,0.5,0.5,1,1], sus=2, amp=var([1,0.8],[8,8]), oct=var([6, (6, 7)], 8), cutoff=12200, vol=1, vib=2, pan=PWhite(-0.6, 0.6), hpf=200, mverb=0.2, fbdelay=0.0, pong=0.5, a=0.2, pongtime=1,rgate=0)

h4 >> dbass([0, 12, 5, 0, 2, 5, 6, 0], dur=[21, 0.5, 0.5, 1, 0.5, 0.5, 1, 1], sus=2, mverb=0.2, amp=var([1, 0.8], [8, 8]), oct=var([6, (6, 7)], 8), cutoff=12200, vib=2, pan=PWhite(-0.6, 0.6), hpf=800, fbdelay=0.25, glide=0, rgate=0)

h4 >> dbass([0, 12, 5, 0, 2, 5, 6, 0], dur=8, mverb=0.2, sus=8, amp=var([1, 0.8], [8, 8]), oct=var([6, (6, 7)], 8), cutoff=12200, vib=2, pan=PWhite(-0.6, 0.6), hpf=200, fbdelay=0.25, glide=0, rgate=0)

Root.default=var( [2, 2*PWhite(0,1)], [3.5, 0.5])

p0.stop()
h4.stop()
p1 >> pluck(P(var([0, -2], 32),var([[3,5,6], 4, 2], 8)), dur=1, lpf=0, sus=4, blur=4, chop=0, fmod=0, rate=1, hpf=linvar([150,2000],32), oct=PStep(16,P+(6,[3,4]),5), cutoff=linvar([1300,400],32), tape=1.0, tapedrive=0.8, tapewarm=0.8, vol=1.3, tapewobble=0.5, eb=0.5, ebfeed=0.7, ebmix=0.5, ebmode=1, ebwow=0.2, ebflutter=0.2, ebsat=0.2, amp=linvar([1,0.5],32)).unison(3)

o5 >> play("7...", bank=0, sample=PRand(909), cut=1, pan=PWhite(-1,1))

##### Descente #######
Clock.bpm = 77
Root.default = lininf(0, -7, 16)

q1.stop()
p2 >> svdk(var([0,4,2,3,1], [8,4,4,2,2]) , dur=1/4, vol=0.5, fenv=0.2, oct=(4), cutoff=linvar([260, 2200], [24, 8]), a=[0.5,0])
j3.a = [0.2,0]

k8 >> loop("breakcore160_16", dur=8, sample=var([PRand(808)], [64, 64])).lclip(0)

f2 >> play("X.", sample=0, dur=1/4, amp=1, delay=0, rate=1, hpf=0)

h4 >> plaitsX([0, 11, 4, 0, 2, 4, 5, 0], dur=P[21, 0.5, 0.5, 1, 0.5, 0.5, 1, 1]*1/2, sus=1, preset=8, amp=var([1, 0.8], [8, 8]), oct=var(P*[5, 6, (6, 7)], 8), cutoff=12200, vib=12, pan=PWhite(-0.6, 0.6), hpf=200, fbdelay=0.25, glide=0, rgate=0, a=0.3)

p2 >> svdk(var([0,4,2,3,1], [8,4,4,2,2]) , dur=1/4, sus=1/8, rel=0.2, vol=0.5, fenv=0.2, oct=PStep([16,8,4,4], 5,4), track=0.5,res=linvar([0.5, 0.9],44), cutoff=linvar([260,1200], [24, 8]), a=[0.5,0])


# Server.addFx(tstop=1, tstoptime=16)