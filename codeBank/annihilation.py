# annihilation
# Reisub

Master().reset()
Scale.default = "minorPentatonic"
Root.default=4
Clock.bpm = 120;

i3 >> sos(dur=8, lpf=linvar([60,4800],[PRand(8,64), PRand(8,64)]), hpf=expvar([0,200],[PRand(8,64), PRand(8,64)]), fx1=1, vib=PWhite(0,16), vol=0.3).unison(3,0.5,90)
r1 >> ews(PTrir(0,8), dur=2, sus=2, squiz=0.8, rel=0.2, fx2=1, oct=PWhite(2,3), amp=0.8, vol=1)
r2 >> ews([2, (3, 5), (2, 3), [(3, 5), (5, 8)]], dur=2, sus=2, squiz=0.8, rel=0.2, oct=2, fx2=1, amp=1).sometimes("degree.shuffle")
r3 >> ews(linvar([2, 3.1], 4), dur=6, sus=6, rel=0.2, oct=2, amp=1, formant=1, fx2=1).unison(2)
n1 >> play("{{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{n[yyyN][xxxx]}} ", dur=PRand([1/2, 1/4]), sample=PRand(128), pan=PWhite(-1,1), lpf=PWhite(800, 8000), fx2=1, rate=PwRand([[-1, 0.2, 0.5, 1, 2],linvar([1, 4], 8),linvar([4, 1], 8),linvar([0.25, 4],8)],[16, 8, 4, 4]), echotime=PRand([0, 1, 2, 3, 4]),echo=PRand([0.25, 0, 0, 1, 2, 0.125, 0]), hpf=PWhite(40, 2000), amp=var([0, PWhite(0.0, 0.4)], [PRand([8, 16]), PRand([2, 4, 6])]))

f1 >> ebass(PWhite(-0.1, 0.1),dur=64, hpf=400, oct=(3, 4), shape=(0, 0.5), fx1=0, spfslide=16, spfend=1600, spf=1).unison(4)
v1 >> radio(dur=32, hpf=PWhite(1000, 2000), formant=PWhite(1, 2), amp=PMorse("kakaaop"), fx2=1)
r4 >> ews(PTrir(0,8), dur=2, sus=4, squiz=0, vib=PWhite(0,32), fmod=PWhite(0,4), hpf=80, rel=0.8, oct=PWhite(2,3), amp=0.5, vol=0.2, cutoff=PRand(400,3800), spin=PWhite(-2,2))

u1 >> play("W ", dur=4, feed=linvar([0.1, 0.5],16), rate=var([1, -1], [7, 1]))
u2 >> play("W ", dur=4, delay=1, feed=linvar([0.1, 0.5],16), shape=0.1,rate=var([1, -1], [7, 1]))
u3 >> play("W ", dur=4, delay=3, feed=linvar([0.1, 0.5],16), shape=0.4, rate=var([ PWhite(1.5, 2.5), -1], [7, 1]),hpf=200, hpr=PWhite(0.1, 0.5))
u4 >> play("W ", dur=4, delay=4, feed=linvar([0.1, 0.5],16), shape=0.6, rate=var([r2.degree, -1], [7, 1]), formant=P*[0,1], echotime=4, echo=1, echomix=PRand([0.25, 0, 0, 0, 0.5]), hpf=200, hpr=PRand([0.1,  0.2]))
u5 >> play("d ", dur=4, delay=4, hpf=1600, echo=0.25, echotime=2, feed=0.5, amp=u4.feed * PRand([0, 1]), chop=4)
r1.stop()

u_all.dur=8
u_all.rate=[2,4,8]
u_all.degree="pl"
u_all.cut=1/2
u_all.hpr=0.05
u_all.vol=0.5
Master().lofi=0.1
Master().hpf=2000

u_all.rate=var([-2, 1]) # transition

Root.default = var([4.02, 4.0, 4.12])
v1.stop()
r2.stop(8)
r1.stop(16)
r3.stop(24)
r4.stop(12)
i3.stop(4)
Master().lofi=0
Master().hpf=0
Clock.bpm = lininf(120,173,32);

print(Clock)
r3.stop()
f1.stop()

y0 >> subbass([2,3,[5,7]], dur=16, amp=0.4, crush=(0,PRand(0,4)), bits=PRand(4,16), fx1=0.2, atk=PWhite(0.005,0.1), oct=(4,5), lpf=4000).unison(4)
y1 >> klank(y0.degree[0], fx2=1, rate=linvar([8, 16], 64), oct=(3, 4), dur=P*[4, 8, 12], lpf=linvar([400,3800],128), lpr=0.1, amp=linvar([0.5, 0.7], 128), hpf=600, bpm = 80 + PWhite(-20, 20), fdist=1, fdistfreq=PWhite(1200, 2000)).unison(2)
y2 >> total(y0.degree[0],dur=32, chop=PRand([0, 0.5, 1, 0.35]), amp=[1,PWhite(0,1)], fmod=PRand([16, 32, 64, 128]), fx1=0, bpf=PRand(800,4000), bpr=0.1, vib=PRand(16), spin=PWhite(-1,1), drive=0.01).slider().unison(2)

n1.stop()
u_all.stop()

y7 >> jbass(var([PWalk(8, 1, 4),PWalk(15, [1, 4], 1)], [4, 4]) , dur=[15, 1/4, 1/4, 1/4, 1/4], sus=[2, 1/4, 1/4, 1/4, 1/4], oct=PStep(7, [3,5], 6), echo=P*[2, 1, 1, 1, 1], amp=0.5, rate=0.1, fx2=1, fx1=1, crush=P*[0,8]).unison(2).slider(0,PStep(8,1,0))
y3 >> bass(y0.degree[0], leg=0.2, oct=(4,6), dur=[15,1], amp=0.4, fx1=1, delay=PWhite(-1,1).rnd(0.25), echo=[0,P[0,0.25,0.5,0.75]], comp=0.6)

f1 >> ebass([ PWhite(-0.1, 0.1),PWhite(5, 3) ], slide=16, dur=64, hpf=400, oct=(3, 4), shape=(0, 0.5), spfslide=16, spfend=1600, spf=1).unison(4)
y5 >> ambi(P*[y0.degree[0],y0.degree[1],y0.degree[2], (y0.degree[0], y4.degree[1]), (y0.degree[1], y0.degree[2]), (y0.degree[0], y0.degree[2]),P**(y0.degree[0], y0.degree[1], y0.degree[2]),P+(y0.degree[0], y0.degree[1], y0.degree[2]), P/(y0.degree[0], y0.degree[1], y0.degree[2])], dur=P*[5,1,1/2,8,3], sus = p1.dur, delay=P*[0,PWhite(0,1)], oct=PwRand([6,5,4,3],[30,35,20,15]), velocity=PRand(40,65), fx2=1, amp=PWhite(0.2,0.3), velhard=PWhite(0.2,1), hard=PWhite(0,2), lpf=PRand(5000,18000)).unison(3).penta()
y4 >> pasha(var([y7.degree, y0.degree, y0.degree + 5], [3, 5]), cut=var([0, 1/4], [8, 8]), oct=(3,6), dur=PDur(var([2,3,4,5],[5,1,1,1]),8), amp=var([0,0.1],PRand(4,16).rnd(2)), sus=y0.dur*PWhite(0.1,0.01), echo=var([0.5,[0.125,0.25,0.75]],[6,2]), pan=y4.dur*P[1,-1], lofi=expvar([0.1,1],[PRand(19),PRand(8)])) + var([0, var([0,PTrir(0,2,0)],[6,2])], [2, 8])

Clock.bpm = 174
Root.default=lininf(4, 0, 32)

Root.default='C'

z1 >> zap(0, dur=8, hpf=40, drive=[PWhite(0.1,0.4),0.2], oct=(3, PStep(9,5,[4, (5, 6)])), chop=4, chopmix=0.25, spf=10, spfend=8000, spfslide=(0.1, PRand(4,8)), octer=1, octersubsub=var([2, PRand(1,15)], [13]), fx1=0, hpfx1=80, amp=P[0.3,0, 0.1, 0, 0.1, 0], vol=0.7).unison(4)
z2 >> sawbass(0, dur=8, sus=[8], echo=1/2, amp=(z1.amp==0), mid=2, echotime=PRand(0,12), oct=(5,4,5), drive=(0.01,0,0.01), vol=0.6).unison(3,var(PWhite(0.25,0.30)),var(PRand(99),8))
y_all.stop()
f_all.stop()

z1.synthdef="lazer"
z1.synthdef="zap"
z1.stop()

n2 >> brown(chop=PRand(8), chopwave=PWhite(0,8), dur=PWhite(0.1,4), amp=var([0, expvar([0,2],[6,0])], [14, 2]), pan=PWhite(-1,1), spf=40, spfend=PRand(400,9800), spfslide=n2.dur/2, drive=1, hpf=linvar([3200, 200], [PRand(4,32), 0]), fx2=1, fx1=1, hpr=PWhite(0.1,0.9))
b8 >> ebass([1,0,0,0,0], dur=[1/2,1/2,1,1], oct=(4), pick=0.2, cutoff=linvar([850, 1250],32), decay=1.2, rel=b8.dur*0.5, amp=1, fold=(0, 0.3), vol=0.5).penta()
b7 >> ebass([1,0,0,0], dur=[1/2,1/2,1,1], oct=(3, 4, 5), pick=(0.2,0.5,0.7), cutoff=linvar([250, 1250],32), decay=1.2, rel=b8.dur*0.1, amp=1, fold=(0,0.3,0.2), vol=0.4).penta()
f1 >> click(PWhite(-0.1, 0.1),dur=b8.dur, hpf=var([200, 3200], [4, 4]), oct=(3, 4), hpr=0.2, shape=(1,0.5), amp=b8.degree == 0).unison(0)

b8.shape=0
b8.pick=[0.8, 0.2, 0.2]

i7 >> play("b...", sample=4, vol=0.7, cut=2)
i2 >> play("(K...)(K...)..", dur=1/2, sample=(0,9), cut=PWhite(0.5,5), vol=0.8, fx1=1)
i4 >> play("(O...)(O...)..", dur=1/2, sample=(8), cut=PWhite(0.5,5), vol=0.7)
n4 >> lapin((0,4), amp=var([0, 1], [PRand(8,16),PRand(1,8)]), dur=PDur(var([4,P*[6,5,7]],[6,2]),8), sus=1/8, oct=(5,6), rate=0.8, shape=0.2, fx1=0, fx2=1, drive=0.8, tanh=0).unison(3,0.25,90)

b8 >> ebass([1,0,0,0,0], dur=[1/2,1/2,1,1], oct=(4), lofi=var([0, 0.01], 8), pick=0.2, cutoff=linvar([850, 1250],32), decay=0.6, rel=b8.dur*0.5, amp=1, fold=(0, 0.14), smooth=0.1, lofiwow=1, vol=0.3, tanh=0.2).penta()

g2 >> ssaw([0,0,1,0,0,1,0,0], dur=P[1,1,1.5,1,1,1/2,1,1], hpf=40, echo=0.5, oct=[5,5,7,5,5,7,5,PRand(5,8)], high=2, tanh=4, fold=0, amp=var([0,1],[PRand(8,24),PRand(2,8)]), vol=0.08, leg=0.2, glide=1, glidedelay=0.4, mpf=8480, scale=Scale.chromatic, fx2=1).unison(4,0.25,90).slider(1,[0,1,0,1,0])
m8 >> play("<k..(k.).(.kk.)(k.{.[kk]})(..k.)>", sample=(2,0,7), amp=0.4)
m2 >> play("-.", sample=4, pan=PWhite(-0.7,0.7)).human(50,5,2).often("stutter", 2, room=1, echo=0.25, echotime=1, rate=PWhite(1,2), spin=1)
m7 >> play("<....u..(...u)>", amp=0.2, sample=(3,0,5), rate=(1,1,PWhite(-1,2)))

m6 >> play("<..:.>", sample=(0,6), high=1.5, rate=1.5, amp=0.2, pan=PWhite(-0.4,0.4))
m1 >> play("<X..(.X)(XXX.).(...X).>", sample=(13,2), lpf=0, amp=0.2)
m3 >> play("<(O.)(O.)..O..(...O)>", sample=(13,2,8), lpf=8888, amp=0.2)
d3 >> play("(#....)..(...~)", rate=PWhite(-1,4)*0.25, amp=0.8).unison(3, 1,99)
m4 >> play(".-", sample=7, pan=PWhite(-0.7,0.7)).human(10,-5,2).sometimes("stutter")
z_all.stop()
i4.stop()

b7.degree = [1, 2.5, [3.125, 0],2.55]
n4.stop()
b7.stop()
f1.stop()

i7 >> play("b...", sample=4, vol=0.7, cut=2)
i2 >> play("(K.)(....)..", dur=1/2, sample=(0,9), cut=PWhite(0.5,5), vol=0.8, fx1=1)

i_all.stop()

p1 >> play("<q ><p >", sample=1, dur=PDur([3, 5], 8), amp=PWhite(0.3,0.5), hpf=220, chop=1/2, leg=PWhite(15), pan=PWhite(-1,1))
p2 >> play("(qp) ", sample=2, dur=PDur([1, 6], 8), hpf=200, amp=PWhite(0.3, 0.5), leg=15, pan=PWhite(-0.5,0.5)) #
p4 >> play("p ", sample=2, dur=1/2, lpf=17000, lpr=0.1, amp=sinvar([0,0.3],37), leg=8, pan=PWhite(-0.25,0.75), hpf=200)
p5 >> play("p ", sample=1, dur=PDur([3, P*[5,7]], var([8,11],32)), lpf=8000, lpr=0.3, amp=sinvar([0,0.4],13), leg=4, pan=PWhite(0.5,-1), hpf=400)
p6 >> play("q ", sample=1, dur=PDur([3, P*[6,7]], 8), amp=0.4, spf=8800, spfend=340, spfslide=2, chop=1/2, leg=PWhite(15), hpf=240, pshift=0, pan=PWhite(-0.4,0.7))
p7 >> play("q ", sample=2, dur=PDur([[1, 6],8], 8), amp=0.5, leg=15, hpf=400, pan=PWhite(-1,1))
b6 >> ssaw(linvar([7,0],[32,0]), oct=[4,5,6], vib=PRand(16),dur=var([rest(1),1],[PRand(4,32).rnd(4),PRand(4,16).rnd(4)]), sus=2.5, amp=1, vol=0.5).unison(4).slider(0,1)

Master().lpf=[400, 0]
Master().cut=[0, 1]
b8.dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8])
b8.sus=b8.dur
b8.amplify=1
z_all.stop()
b8.stop()
f1.stop()

Master().lpf=0
Master().cut=0
i2 >> play("...w", dur=4, sample=5, amp=2, shape=0.3, rate=(PWhite(0.3,1.5),PWhite(0.3,1.5)), pan=(-1,1))
r9 >> rsin([0,0,P[2,3,[5,[6,4,1],P+(PRand(0,8),PRand(0,8))]].palindrome(1)], oct=6, dur=PStep(15,1,1/2), sus=PWhite(1/4,1), amp=1, lpf=z1.amp * 11480, vol=0.5, pan=[0,0,PWhite(-1,1)]).unison(5).after(8, "only")

b6.stop()
g2.stop()
Clock.bpm = lininf(173, 174, 64)
b_all.stop()
t1.leg=0
t1 >> angst(0 * PRand([1/2, 1/4, 1] + [4, 21]), dur=1/2, oct=(t1.leg / 4) + PRand([3, 4]), sus=1/2, fmod=(0,12), lpf=t1.leg * PWhite(400, 2000), fx1=0, vib=0, leg=var([4,1], [PRand([3, 7, 15]), 1]))

l1 >> loop("break8", dur=8, sample=30, amp=P[PCoin(), PCoin(), PCoin(), 0, PCoin(), 0, PCoin(), 0]*0.5)
l3 >> loop("break8", dur=8, sample=29, amp=P[0, 0, 0, PCoin(), 0, 0, 0, 0]*0.5)
l4 >> loop("break8", dur=8, sample=32, amp=P[0, 0, 0, 0, PCoin(), 0, 0, 0]*0.5)
l5 >> loop("break8", dur=8, sample=35, amp=P[0, 0, 0, 0, 0, PCoin(), 0, PCoin()]*0.5)
i7 >> play("b...", sample=4, vol=0.7, cut=2, amp=var([1]))
i2 >> play("(K...)(K...)..", dur=1/2, sample=(0,9), cut=PWhite(0.5,5), vol=0.8).often("stutter", PRand(16), bpf=linvar([400,8000],2), spin=1)
i3 >> play("(O...)(O...)..", dur=1/2, sample=(8), cut=PWhite(0.5,5), vol=0.8).often("stutter", PRand(16), bpf=linvar([400,8000],2), spin=1)

i_all.stop()
l1.stop()
l3.stop()
m_all.stop()
l5 >> loop("break8", dur=8, sample=30, rate=0.5, amp=P[0, 0, 0, 0.5])
l4 >> loop("break8", dur=8, sample=35, amp=P[0.5, 0.5, 0.5, 0], lofi=[0.3,0.5,0.7,0])
l2 >> play("<@>", dur=var([8, 1/4], [8, 4]), drive=var([0, linvar([0.1, 0.2],8)], [8, 4]), sample=2 ,formant=PWhite(0.7, 1.2), delay=0.0, amp=PCoin(), fold=PWhite(0.5,1), dist=0.0, hpf=8000, cut=var([1/4, 0.5]), rate=var([1, linvar([1, 0.5], 4)]))

l_all.stop()

a1.dur=4
a1.stop()

v2 >> play("V ", sample=4, lpf=100, cut=0, amp=0.5, hpf=40)
v3 >> play("O ", hpf=6000, lpf=2000, rate=0.3, cut=1/2, amp=0.5)
v4 >> play("@ ", sample=11, hpf=50, rate=0.1, amp=0.5, cut=PWhite(0.01, 0.06))
v7 >> play("g ", sample=1, hpf=2200, lpf=8000, amp=0.3, drive=0)
v8 >> play("V.", sample=4, hpf=12000, amp=PWhite(0.5, 0.9))
v5 >> play(".n", sample=4, spfend=PRand(4700,14000), spf=var([200,8000],[6,2]), spfslide=P*[1/4,1/2,1])
v9 >> play("X.", sample=(8,4), lpf=800, hpf=140, amp=0.4)

k5 >> play(PEuclid2(3,8,"X","{|=2|*}"), sample=(1,4),rate=var([1,0.7],[16,2]),lpf=linvar([800,5800],[PRand(0,32),PRand(0,16)]), triode=PRand(4), lpr=PWhite(0.1,1), amp=1, vol=0.3).often("stutter", Cycle(PTrir(1,8,0)), vol=0.1, hpf=1800).sometimes("amen")
d1 >> play(PEuclid2(var([3,4],[24,8]),8,"(vv{v@})","(-|=2|)"), dur=1, drive=P*[0,expvar([0.01,0.1],26)], amp=1, vol=0.6, lpf=linvar([800,7800],[64,0]), lpr=linvar([1,0.05],61)).often("stutter", Cycle([2,3,6,12]), pan=PWhite(-1,1), amp=0.1, bpf=500)

v_all.dur=PCoin(1/2,1/4,0.7)
v_all.dur=1/2

d1.stop()
k5.stop()

l_all.stop()

v0 >> play("V ", octafuz=0.3, amp=1)
f2 >> play("[--]", sample=3, hpf=12000)
m3 >> play("<....O..(...O)>", sample=(13,2), lpf=8888, amp=0.2)
m9 >> play("X ", amp=1, vol=0.2, sample=(1, 5))

a1 >> tb303([0.02, 0.01, 0.01, 2, 2, PTrir(0.01, 0.03, 0.02), linvar([0.1, 0.3], 16), PStep(4, 0.2, 0.24)], oct=(4, var(PTrir(3,6,5), 8)), top=linvar([1600, 100], 8), cutoff=linvar([200, 800], [24, 8]), amp=var([0,expvar([0,1],[64,0])],[64,64]), pan=linvar([0.8, -0.4], [PRand([8, 4, 8])]), drive=([0.2, 0.01, 0.1, 0.3], [32, 4, 8, 8]), lpf=1200, dur=1/4, vol=0.4)

Clock.bpm=lininf(173, 40, 8)
Master().delay=(0, 0.25, 0.5)

f8 >> faim(PArp([0,1,0.5],11) + PGauss(0, 0.2) + P[0, 0, 0, [0.1, 0.1]], oct=(4, 5), beef=(1,0), dur=PDur(var([4,[5,3,8]],[6,2]),8), sus=f1.dur*PWhite(0.5,1), lpf=0, amp=0.5)

Clock.swing(var([PWhite(-1,1)],8))
Clock.swing(0)