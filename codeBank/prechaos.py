# Prechaos 132


Clock.bpm = 132
# d1 >> dbass(dur=1/2)
q3 >> compkick(punch=0.5, comp=16, release=0.35, click=1.0,drive=0.4, sub=1, body=1.2, tone=0.0, oct=3, echo=0)
b2 >> pumpbass([0], dur=0.5, cutoff=linvar([400,1200],8), pumprate=4, pumpdepth=0.6, growl=0.4, amp=0.55, oct=4)
q1 >> compperc(dur=PDur(5,16), decay=0.17, metal=0.5, amp=1, pan=PWhite(-0.4,0.4))
sb >> hardstab([(0,4,7)], dur=4, fbdelay=0.4, fbtime=0.75, fbfeed=0.5, fbcutoff=2000)
d1 >> sawbass(var([0, a0.degree, -5], [12, 4, 16]), dur=[8, 1, 1, 2, 2, 2], oct=6, lpf=linvar([80, 400], 64), shape=linvar([0.15, 0.5], 32), amp=0.55, sus=var([4, 2], [8, 8])).unison(2, 0.02, 20)
d2 >> dbass(0, dur=1/4, oct=6, amp=[0, 0.5, 0.3, 0.5] * var([1, 0], [14, 2]), lpf=200, pumper=0.7, transient=0.3, shape=1)
# k1 >> play("X", amp=var([[1, 0, 0, 0], [1, 0, [0, 0.7], 0], [1, 0, 0, [0, 0, 0, 0.6]]], [8, 4, 4]), dur=1/4, sample=var([2, 5, 3], [12, 8, 12]), lpf=linvar([4000, 6000], 16), shape=linvar([0.4, 0.7], 32))
p1 >> compperc(dur=PDur(5,16), freq=P[900,1100,1000], metal=4, pumper=1, amp=2)
h1 >> play("-", amp=var([[0.3, 0.3, 0.9, 0.4], [0.5, 0.5, 1, 0.5], [0.4, 0, 0.8, 0.5]], [6, 6, 4]), dur=1/4, sample=var([3, 5, 8], 16), hpf=linvar([4500, 8000], 24), lpf=expvar([7000, 18000], 16), rate=var([1, PWhite(0.85, 1.3)], [12, 4]), pan=PWhite(-0.4, 0.4))
pd >> darkpad([(0,4,7)], dur=8, pumper=0.6, pumprate=1, pumprel=0.25, amp=0.5)
# c0 >> play("o", amp=var([[[0, 1], 0, 0, 0], [[0, 1], 0, [0, 0, 0.5], 0]], [10, 6]), dur=1/4, sample=var([2, 4], [14, 2]), lpf=expvar([1800, 4000], 24), room=PStep(12, 0.5, 0.1))
h1 >> pumphihat(dur=0.25, amp=P[0.4,0.15,0.3,0.15], decay=0.04, metal=0.6, open=P[0,0,0.2,0], amplify=4)
sn >> industrialsnare(dur=2, rattle=0.5, snap=0.7, amp=0.6)
k2 >> play("V", amp=[0, 0, 0, PStep(var([4, 6], 8), PRand([0.6, 0.75]), 0)], dur=1/4, sample=PRand(4), lpf=PRand(500, 1200), shape=0.6, amplify=0.5)
p1 >> compperc(dur=PDur(5,16), freq=P[900,1100,1000], decay=0.06, metal=0.6, ring=0.4, comp=10, amp=1, pan=PWhite(-0.5,0.5))

seq = var([P[0,0,3,0,5,0,0,3], P[0,2,5,2,7,5,2,0], P[-2,0,3,5,7,5,3,0], P[0,0,5,7,10,7,5,0]], [16, 16, 8, 24])
chd = var([(0,4,7), (0,3,7), (-2,2,5), (2,5,9)], [12, 12, 8, 32])

a1 >> acidline(var([seq], [16, 8, 8]), dur=var([0.25, 0.125, 0.25], [24, 4, 4]), cutoff=expvar([300, var([2000, 4000], [16, 16])], 8), res=linvar([0.4, 0.9], 16), drive=linvar([1.5, 4], 32), accent=var([P[0,0,1,0]*0.5, P[1,0,0,1]*0.6, P[0,1,0,1]*0.4], [12, 8, 12]), tubedrive=linvar([0.2, 0.7], 48), amp=var([0.6, 0.8, 0.5], [12, 4, 16]))
a1 >> acidline([0,0,3,0,5,0,0,3], dur=0.25, cutoff=linvar([400,2000],8), res=linvar([0.5,0.8],4), drive=2.5, accent=P[0,0,1,0]*0.5, tubedrive=0.4, amp=0.7)
w1 >> pumpbass(var([seq, seq*-1, seq+var([0,5],[4,4])], [24, 4, 4]), dur=var([0.5, 0.25, 0.5], [16, 8, 8]), cutoff=expvar([300, 1800], 16), pumprate=var([4, 8, 2], [12, 8, 12]), pumpdepth=linvar([0.3, 0.7], 32), growl=linvar([0.2, 0.6], 48), amp=var([1.2, 1.5, 1], [8, 4, 4]))
w2 >> superbass(var([P[0,0,0,3], P[0,0,5,3], P[0,2,0,5]], [16, 8, 8]), dur=var([0.5, 0.25], [24, 8]), cutoff=PFrac(0.5, 0.3, 16, 500, var([1600, 2400], [16, 16])), fdecay=linvar([3, 7], 48), detune=linvar([0.3, 0.6], 32), sub=var([0.6, 0.9, 0.7], [12, 4, 16]), tape=linvar([0.2, 0.6], 64), tapewarm=var([0.2, 0.5], [16, 16]), amp=var([0.45, 0.6, 0.4], [12, 8, 12]))
d2 >> play("-", sample=5, dur=0.25, amp=P[0.4,0.15,0.3,0.15])
d3 >> play("..u.", sample=3, dur=0.5, amp=0.6)
# d1 >> play("X..X.X..", sample=7, dur=0.25, amp=0.9, shape=0.0, tape=1, tapedrive=1)
h1 >> pumphihat(dur=var([0.25, 0.25, 0.125], [24, 4, 4]), amp=var([P[0.4,0.15,0.3,0.15], P[0.5,0.2,0.4,0.2], P[0.3,0.1,0.5,0.1]], [8, 8, 16]), decay=linvar([0.03, 0.08], 32), metal=linvar([0.4, 0.9], 48), open=var([P[0,0,0.2,0], P[0,0,0.4,0], P[0,0,0,0.5]], [12, 8, 12]), pumper=linvar([0.2, 0.6], 32), pumprate=var([4, 8, 2], [16, 8, 8]), amplify=var([3, 4, 3.5], [12, 12, 8]))
h2 >> pumphihat(dur=var([1, 0.5, 2], [16, 8, 8]), amp=var([0.8, 1, 0.6], [8, 4, 4]), decay=linvar([0.1, 0.25], 24), open=linvar([0.3, 0.7], 32), metal=var([0.5, 0.8], [12, 4])).offbeat()
p1 >> prophet([0,2,4,5,7,5,4,2], dur=0.5, cutoff=linvar([2000,6000],16), rq=0.4, rate=0.5, phase=0.5, mverb=0.4, amp=0.35)
gz >> prophet([(0,4,7)], dur=8, wave=linvar([0,60],64), cutoff=linvar([500,3000],32), res1=0.4, lfo1=1, rate1=0.25, depth1=2, oct=5, mverb=0.5, amp=0.3)
cr >> creep(var([7,5],[4,4])+P[0,0,12,0], dur=2, rate=linvar([0.5,2],16), hpf=400, mverb=0.6, amp=0.25)
dl >> darklead(P[0,2,4,7,9,7,4,2], dur=0.25, cutoff=linvar([1500,5000],8), detune=0.01, drive=1.5, sub=0.3, fbdelay=0.3, fbtime=0.5, fbfeed=0.35, oct=4, amp=0.35).sometimes("degree.add", 7)
dp >> darkpad([(0,4,7),(0,3,7)], dur=var([8,8],[8,8]), dark=0.6, movement=linvar([0.2,0.6],32), cutoff=linvar([600,1500],16), pumper=0.4, pumprate=1, amp=0.25)
n1 >> noisehit(dur=PDur(3,16), decay=0.08, filter=linvar([2000,8000],8), type=P[0,1,2,0], comp=12, amp=0.3)
hv >> hoover([(0,4,7)], dur=16, porta=1.5, portadur=0.2, tubedrive=0.5, tubewarm=0.4, amp=0.8, sus=4)
dp >> dopple([0,0,3,5,7,5,3,0], dur=0.25, rate=linvar([0.5,4],16), hpf=300, dist2=2, rhythmgate=0.5, gaterate=4, gatewave=1, oct=5, amp=1)
sn >> industrialsnare(dur=2, rattle=0.6, snap=0.7, drive=4, comp=12, amp=0.9)
b2 >> pumpbass([0,0,0,2], dur=0.5, cutoff=linvar([400,1200],16), pumprate=4, pumpdepth=0.5, growl=0.3, amp=1.5)
k4 >> compkick(dur=1, punch=0.8, click=0.5, comp=12, drive=4, amp=0.9, oct=3, tape=4, tapedrive=2)
b1 >> superbass([0,0,0,3], dur=0.5, cutoff=PFr(600,1800), fdecay=4, detune=0.4, sub=0.8, tape=0.4, tapewarm=0.3, amp=0.5)
h1 >> pumphihat(dur=0.25, amp=P[0.4,0.15,0.3,0.15], decay=0.04, metal=0.6, pumper=0.3, pumprate=4)
h2 >> pumphihat(dur=1, amp=1, decay=0.15, open=0.5, metal=0.7).offbeat()
pr >> prophet(P[0,4,7,11,14,11,7,4], dur=0.25, cutoff=linvar([1500,5000],8), rq=0.35, rate=0.3, mverb=0.35, oct=5, amp=0.35)
px >> plaitsX(var([P[0,2,4],P[4,5,7],P[7,9,11]],[8,8,8]), dur=0.5, preset=var([9,10,11],[8,8,8]), oct=(4,5), chopmix=linvar([0,0.5],16), chopwave=(2,3), mverb=0.4, amp=0.35)
cr >> creep(var([7,5,3,0],[4,4,4,4]), dur=1, rate=linvar([0.5,1.5],8), hpf=500, mverb=0.5, oct=5, amp=0.25)
dl >> darklead(melody(), dur=0.5, cutoff=linvar([1000,4000],8), detune=0.006, sub=0.3, rhythmgate=var([0,0.5],[8,8]), gaterate=4, oct=5, amp=0.3)
gz >> click([(0,4,7)], dur=16, wave=linvar([10,50],64), cutoff=linvar([800,2500],32), lfo1=2, rate1=0.1, depth1=3, mverb=0.6, oct=4, amp=0.25)
dp >> darkpad([(-7,0,4)], dur=16, dark=0.5, movement=0.4, cutoff=800, pumper=0.3, pumprate=1, amp=0.2)
gr >> growl(0, dur=8, rate=0.3, hpf=300, lpf=2000, amp=0.15, pan=PSine(16))

d1 >> play("X.", sample=4, amp=0.9, dur=0.5)
d1 >> play("<X.><X[.X]><X.><[XX].>", sample=4, dur=0.5, amp=0.9)
d2 >> play("-", sample=5, dur=0.25, amp=P[0.4,0.15,0.3,0.15], hpf=4000)
d3 >> play("..C.", sample=2, dur=0.5, amp=0.55)

d1 >> play("X..X.X.X", dur=0.25, sample=4, amp=0.9, shape=0.3)
d2 >> play("-", sample=5, dur=0.25, amp=P[0.5,0.15,0.35,0.15])
d3 >> play("....u...", sample=3, dur=0.25, amp=0.6)
d2 >> play("{-:}", dur=0.25, amp=0.4, hpf=5000)
# d4 >> play("<X.X.><X..X><X.X.><X[.X][.X].>".replace("X", "s"), sample=11, cut=1/4, hpf=0, dur=0.25, rate=1, amp=0.7)
d3 >> play("<....><..u.><....><.u.u>", sample=3, amp=0.55)
# d1 >> play("<X...><X..X><X...><..X.>", dur=0.25, sample=4, amp=0.9)


d1 >> play("X.", dur=0.5, sample=4, amp=0.9)
d1 >> play("X", dur=1, sample=4, amp=0.9)
d1 >> play("X.X.", dur=0.25, sample=4, amp=0.9)
d1 >> play("X...", dur=0.25, sample=4, amp=0.9)
d1 >> play("X..X....", dur=0.25, sample=4, amp=0.9)
d1 >> play("X..X..X.", dur=0.25, sample=4, amp=0.9)
d1 >> play("X..[.X].X.", dur=0.25, sample=4, amp=0.9)
d1 >> play("X.[.X]..X.[.X]..", dur=0.25, sample=4, amp=0.9)
d1 >> play("[XX].X..", dur=0.25, sample=4, amp=0.9)


d1 >> play("X.", dur=0.5, sample=4, amp=0.9, shape=0.2)
d2 >> play("-", dur=0.25, sample=5, amp=P[0.45,0.15,0.32,0.15], hpf=4500)
d3 >> play(".:.", dur=0.5, sample=5, amp=0.3, hpf=3000)
d4 >> play("..u.", dur=0.5, sample=3, amp=0.6)
d5 >> play("<+...><..+.><....><.+..>", dur=0.25, sample=2, amp=0.25)


d2 >> play("-", dur=0.25, sample=5, amp=P[0.4,0.15,0.3,0.15], hpf=4000)
d2 >> play("-", dur=0.25, sample=5, amp=P[0.5,0.12,0.35,0.12], hpf=5000)
d2 >> play("-", dur=0.25, sample=5, amp=P[0.45,0.1,0.3,0.1,0.4,0.12,0.28,0.1], hpf=4500)
d2 >> play("-", dur=0.25, sample=5, amp=P[0.5,0.15,0.4,0.15,0.45,0.15,0.35,0.2], hpf=4000)

d2 >> play("-", dur=0.25, sample=5, amp=P[0.4,0.15,0.3,0.15], hpf=4000)
d3 >> play(".:.", dur=0.5, sample=5, amp=0.35, hpf=3000)
d2 >> play("-.-:", dur=0.25, sample=5, amp=P[0.4,0.15,0.3,0.35], hpf=4000)
d2 >> play("-.-.-.:-", dur=0.25, sample=5, amp=P[0.4,0.15,0.3,0.15,0.35,0.12,0.4,0.3], hpf=4000)
d2 >> play("{-:}", dur=0.25, sample=5, amp=0.35, hpf=4000)
d2 >> play("--:-", dur=0.25, sample=5, amp=P[0.4,0.3,0.45,0.35], hpf=4000)

d2 >> play("<-...><.-..><..-.><-.->" , dur=0.25, sample=5, amp=0.35, hpf=4000)


Root.default = "A"
Scale.default = "minor"
Clock.bpm = linvar([140, 146], [32, 0])

a0 >> dbass(var([0, PWalk(7, [1, 3], 2), -3, PWalk(5, 2, 1)], [6, 4, 2, 4]), dur=[3, 1/4, 1/4, 1/2, 1/4, 1/4, 1/4], oct=(4, 5), pumper=linvar([0.2, 0.85], 48), transient=var([0.5, 3, 6], [8, 4, 4]), transattack=linvar([0.5, 3], 32), multicrush=var([1, 3.5], [12, 4]), combres=linvar([0.5, 9], 64), fbdelay=0.6, fbfeed=linvar([0.3, 0.75], 48), stereowidth=6, amp=0.8)
a1 >> fbass(a0.degree * var([1, -1], 8) + var([0, 7, 12], [8, 4, 4]), dur=PDur(var([7, 5, 9], [4, 4, 8]), 16), oct=PStep(6, (3, 4), 5), lpf=expvar([600, 8000], 16), fmod=linvar([4, 28], [32, 0]), sus=var([1/8, 1/4, 1/16], [6, 4, 6]), drive=linvar([0.2, 0.9], 48), amp=1).unison(4)
b1 >> click(var([0, a0.degree, 7], [4, 10, 2]), dur=PDur(var([3, 5, 7], PRand(8, 16)), 16), oct=(PStep(5, 6, 4), 5), drive=var([0.3, PWhite(0.6, 0.95)], [6, 2]), triode=linvar([2, 8], 32), octer=var([0, 1], [14, 2]), octersub=3, hpf=linvar([200, 1200], 48), amp=0.4, mverb=PStep(12, 0.6, 0)).unison(2).sometimes("stutter", PRand(4, 8), pan=[-1, 1])
b2 >> fbass(PRand([0, 3, 5, 7, 10, 12, -2]), dur=PStep(var([4, 6, 8], [8, 4, 4]), 1/4, 0), oct=(5, 6, 7), sus=1/32, lpf=PRand(2000, 12000), fmod=PRand(12, 40), amp=PStep(6, PRand([0.5, 0.7]), 0) * var([1, 0, 1], [6, 2, 8]), pan=PWhite(-1, 1))
c1 >> varsaw((a0.degree, a0.degree + var([4, 3, 5, 7], [8, 8, 4, 12])), dur=var([4, 2, 8], [8, 4, 4]), oct=linvar([4, 4.2], 64), sus=linvar([2, 5], 32), lpf=linvar([500, 3500], 48), amp=linvar([0.15, 0.35], 32), room=linvar([0.4, 0.85], 64), mix=0.45).unison(5, 0.22, 100)
c2 >> pluck(P*[a0.degree, a0.degree + 7, a0.degree + 12, a0.degree - 5], dur=PDur(PRand([3, 5, 7]), 16), oct=PwRand([5, 6, 7, 8], [2, 4, 3, 1]), sus=1/48, lpf=PRand(2000, 16000), hpf=PRand(600, 3000), crush=PStep(6, PRand(3, 6), 0), amp=PRand([0, 0.15, 0.25, 0.3]), pan=PWhite(-1, 1), room=PWhite(0.3, 0.8)).human(20, 0.8)


d3 >> play("..u.", dur=0.5, sample=3, amp=0.6)
d3 >> play("....u...", dur=0.25, sample=3, amp=0.6)
d3 >> play("..C.", dur=0.5, sample=2, amp=0.55)
d3 >> play("....C...", dur=0.25, sample=2, amp=0.55)
d3 >> play("..o.", dur=0.5, sample=3, amp=0.6)
	d3 >> play("....o...", dur=0.25, sample=3, amp=0.6)



  d3 >> play("..u..u..", dur=0.25, sample=3, amp=P[0.6,0.4])
  d3 >> play("..u.[.u]..", dur=0.25, sample=3, amp=0.55)
  d3 >> play("<..u.><....><..u.><.u..>", dur=0.25, sample=3, amp=0.6)
  d3 >> play("<....><..u.><....><u...>", dur=0.25, sample=3, amp=0.6)
  d3 >> play("....u..[.u]", dur=0.25, sample=3, amp=P[0.6,0.4])
  d3 >> play("<..u.><..u.><..u.><[uu].u.>", dur=0.25, sample=3, amp=0.6)



d3 >> play("..u.", dur=0.5, sample=3, amp=0.6)
d4 >> play("[.u].[.u].", dur=0.5, sample=3, amp=0.2)

d3 >> play("....u...", dur=0.25, sample=3, amp=0.6)
d4 >> play(".u.u...u", dur=0.25, sample=3, amp=P[0.15,0.1,0.12,0.1])


d4 >> play("+", dur=0.5, sample=2, amp=0.4)
d4 >> play("+.+.", dur=0.25, sample=2, amp=P[0.4,0.3])
d4 >> play("+..+.+..", dur=0.25, sample=2, amp=0.35)
d4 >> play("<+...><..+.><+...><.+..>", dur=0.25, sample=2, amp=0.35)
d4 >> play("s", dur=0.25, sample=3, amp=P[0.3,0.15,0.25,0.15])
d4 >> play("h", dur=0.25, sample=2, amp=P[0.35,0.15,0.25,0.15], hpf=6000)



d4 >> play("t...m...", dur=0.25, sample=3, amp=0.4)
d4 >> play("<....><t...><....><..m.>", dur=0.25, sample=3, amp=0.4)
d4 >> play("<t...><m...><t...><.m.t>", dur=0.25, sample=3, amp=0.4)
d4 >> play("..t..m..", dur=0.25, sample=3, amp=P[0.4,0.35])

Clock.bpm = 134
d1 >> play("X.", dur=0.5, sample=4, amp=0.9)
d2 >> play("-", dur=0.25, sample=5, amp=P[0.4,0.15,0.3,0.15], hpf=4000)
d3 >> play("..u.", dur=0.5, sample=3, amp=0.6)

Clock.bpm = 134
d1 >> play("X...", dur=0.25, sample=4, amp=0.9)
d2 >> play("-", dur=0.25, sample=5, amp=P[0.4,0.15,0.3,0.15], hpf=4000)
d3 >> play(".:.", dur=0.5, sample=5, amp=0.3, hpf=3000)
d4 >> play("....u...", dur=0.25, sample=3, amp=0.6)

d1 >> play("X.", dur=0.5, sample=4, amp=0.9, tape=0.2, tapedrive=4, tapewarm=0.3)

Root.default = "D"
Scale.default = "minor"
Clock.bpm = linvar([132, 136], [64, 0])

# === FOUNDATION ===


k2 >> play("V", amp=[0,0,0,[0,0,0,PRand([0,1])]], dur=1/4, sample=1, lpf=800, amplify=0.6)
r1 >> dab(0, oct=4, dur=1, amp=0.7, lpf=120, room=0.8, mix=0.6, sus=0.8, shape=0.3)



Root.default = "E"
Scale.default = "minor"
Clock.bpm = linvar([132, 138], [64, 0])



# k1 >> compkick(dur=var([1, 1, P[1,1,1,1/2,1/2]], [16, 8, 8]), punch=linvar([0.5, 0.95], 48), click=var([0.4, 0.7, 0.5], [8, 4, 4]), comp=var([8, 14], [24, 8]), drive=linvar([2, 6], 64), amp=0.85, oct=var([3, 3, 2], [14, 2, 16]))
# k2 >> play("V", amp=var([[0,0,0,PStep(4,0.7,0)], [0,0,PStep(6,0.6,0),0], [0,0,0,0]], [12, 8, 12]), dur=1/4, sample=PRand(5), lpf=var([PRand(500,1200), PRand(800,2000)], [8, 8]), shape=linvar([0.4, 0.8], 32), amplify=0.5)


# p1 >> compperc(dur=var([PDur(5,16), PDur(7,16), PDur(3,8)], [16, 8, 8]), freq=var([P[900,1100,1000], P[700,1200,900], P[1100,800,1300]], [8, 8, 16]), decay=linvar([0.04, 0.1], 24), metal=linvar([0.4, 0.9], 48), ring=var([0.3, 0.6, 0.4], [12, 4, 16]), comp=var([8, 14], [16, 16]), amp=var([0.8, 1, 0.7], [8, 4, 4]), pan=PWhite(-0.6, 0.6))

# n1 >> noisehit(dur=var([PDur(3,16), PDur(5,16), 0], [12, 12, 8]), decay=linvar([0.05, 0.15], 16), filter=expvar([1500, 10000], 24), type=var([P[0,1,2,0], P[1,0,1,2], P[2,2,0,1]], [8, 8, 16]), comp=linvar([8, 16], 32), amp=var([0.25, 0.4, 0], [12, 12, 8]))


dl >> darklead(var([seq, seq+7, seq*-1+12], [16, 8, 8]), dur=var([0.25, 0.5, 0.125], [16, 8, 8]), cutoff=expvar([1000, 6000], 12), detune=linvar([0.005, 0.02], 32), drive=linvar([1, 3], 48), sub=var([0.2, 0.4, 0.3], [12, 8, 12]), fbdelay=var([0.25, 0.375, 0.5], [8, 8, 16]), fbtime=linvar([0.3, 0.7], 24), fbfeed=linvar([0.2, 0.5], 32), rhythmgate=var([0, 0.5, 0.7, 0], [12, 8, 4, 8]), gaterate=var([4, 8, 2], [16, 8, 8]), oct=var([4, 5, 4], [16, 8, 8]), amp=var([0.3, 0.4, 0.25], [12, 8, 12])).sometimes("stutter", 4, pan=[-1,1])
cr >> creep(var([7, 5, 3, 0, 9], [4, 4, 4, 4, 16]) + var([0, P[0,0,12,0], P[0,12,0,12]], [16, 8, 8]), dur=var([2, 1, 0.5], [16, 8, 8]), rate=linvar([0.4, 2.5], 24), hpf=linvar([300, 800], 32), mverb=linvar([0.4, 0.8], 48), oct=var([5, 6, 4], [12, 8, 12]), amp=var([0.2, 0.35, 0.15], [12, 8, 12]))

p1 >> prophet(var([P[0,4,7,11,14,11,7,4], P[0,3,7,10,14,10,7,3], P[0,5,9,12,14,12,9,5]], [16, 8, 8]), dur=var([0.25, 0.125, 0.5], [16, 8, 8]), cutoff=expvar([1200, var([4000, 7000], [24, 8])], 12), rq=linvar([0.25, 0.5], 32), rate=linvar([0.2, 0.6], 48), phase=var([0.5, 0.25, 0.75], [12, 8, 12]), mverb=linvar([0.25, 0.6], 32), oct=var([5, 6, 4], [16, 8, 8]), amp=var([0.3, 0.45, 0.25], [12, 8, 12]))

px >> plaitsX(var([seq, chd, P[0,7,12,7]], [12, 12, 8]), dur=var([0.5, 0.25, 1], [16, 8, 8]), preset=var([9, 10, 11, 8], [8, 8, 8, 8]), oct=var([(4,5), (5,6), (3,4)], [16, 8, 8]), chopmix=linvar([0, 0.7], 24), chopwave=var([(2,3), (1,4), (3,5)], [12, 8, 12]), bright=linvar([0.3, 0.9], 48), mverb=linvar([0.3, 0.7], 32), amp=var([0.3, 0.45, 0.2], [12, 8, 12]))

dp >> darkpad(var([chd, [(0,3,7)], [(-2,2,5)]], [16, 8, 8]), dur=var([8, 4, 16], [16, 8, 8]), dark=linvar([0.4, 0.8], 48), movement=linvar([0.2, 0.7], 32), cutoff=expvar([500, 2000], 24), pumper=linvar([0.2, 0.6], 32), pumprate=var([1, 2, 0.5], [16, 8, 8]), amp=var([0.2, 0.35, 0.15], [12, 8, 12]))

gz >> prophet(var([chd, [(0,4,7,11)], [(0,5,9)]], [16, 8, 8]), dur=var([8, 4, 16], [16, 8, 8]), wave=linvar([10, 60], 64), cutoff=expvar([600, 3500], 32), res1=linvar([0.3, 0.6], 48), lfo1=var([1, 2, 0.5], [16, 8, 8]), rate1=linvar([0.1, 0.4], 32), depth1=linvar([1, 4], 48), mverb=linvar([0.4, 0.8], 64), oct=var([4, 5, 3], [16, 8, 8]), amp=var([0.25, 0.35, 0.2], [12, 8, 12]))

hv >> hoover(var([chd, [(0,7,12)], [(0,4,11)]], [24, 4, 4]), dur=var([16, 8, 32], [16, 8, 8]), porta=linvar([0.5, 2.5], 48), portadur=linvar([0.1, 0.4], 32), tubedrive=linvar([0.3, 0.7], 48), tubewarm=linvar([0.2, 0.6], 64), amp=var([0.6, 0.8, 0.5], [16, 8, 8]), sus=linvar([3, 8], 48))

do >> dopple(var([seq,  seq+P[0,0,0,0,7,7,7,7]], [16, 8, 8]), dur=var([0.25, 0.125, 0.5], [16, 8, 8]), rate=expvar([0.3, 5], 16), hpf=linvar([200, 600], 32), dist2=linvar([1, 4], 48), rhythmgate=var([0, 0.5, 0.8], [16, 8, 8]), gaterate=var([4, 8, 2], [12, 8, 12]), gatewave=var([1, 2, 0], [8, 8, 16]), oct=var([5, 6, 4], [16, 8, 8]), amp=var([0.8, 1, 0.6], [12, 8, 12]))
