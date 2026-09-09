# lastlast 120
# live

Master().reset()

Scale.default = "minorPentatonic"
Root.default=4
Clock.bpm = 120;

i3 >> sos(dur=8, lpf=linvar([60,4800],[tmps*1.5, tmps*3]), hpf=expvar([0,500],[tmps*6, tmps*2]), output=40)
r1 >> ews(PTrir(0,8), dur=2, sus=2, squiz=0.8, rel=0.2, fx2=1, oct=PWhite(2,3), amp=0.8, output=30, vol=1)
r2 >> ews([2, (3, 5), (2, 3), [(3, 5), (5, 8)]], dur=2, sus=2, squiz=0.8, rel=0.2, oct=2, amp=1, output=32)
r3 >> ews(linvar([2, 3.1], 4), dur=6, sus=6, rel=0.2, oct=2, amp=1, formant=1, output=34).unison(2)
n1 >> play("{{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{nYNy}{n[yyyN][xxxx]}} ", dur=PRand([1/2, 1/4]), sample=PRand(128), pan=PWhite(-1,1), lpf=PWhite(800, 8000), rate=PwRand([[-1, 0.2, 0.5, 1, 2],linvar([1, 4], 8),linvar([4, 1], 8),linvar([0.25, 4],8)],[16, 8, 4, 4]), echotime=PRand([0, 1, 2, 3, 4]),echo=PRand([0.25, 0, 0, 1, 2, 0.125, 0]), hpf=PWhite(40, 2000), amp=var([0, PWhite(0.0, 0.4)], [PRand([8, 16]), PRand([2, 4, 6])]), output=40)

f1 >> ebass(PWhite(-0.1, 0.1),dur=64, hpf=400, oct=(3, 4), shape=(0, 0.5), output=38, spfslide=16, spfend=1600, spf=1).unison(4)
v1 >> radio(dur=32, hpf=PWhite(1000, 2000), formant=PWhite(1, 2), amp=PMorse("kakaaop"), fx2=1, output=44)
r4 >> ews(PTrir(0,8), dur=2, sus=4, squiz=0, vib=PWhite(0,32), fmod=PWhite(0,4), hpf=80, rel=0.8, oct=PWhite(2,3), amp=0.1, vol=0.2, cutoff=PRand(400,3800), spin=PWhite(-2,2), output=34)

q1 >> quin(dur=8, spf=1, spfend=200, spfslide=0.5, formant=1, crush=1, room2=1)
q2 >> pluck(dur=8, oct=3,echo=0.25)
q3 >> pluck([0, (5.01, (6, 5))], dur=8, delay=4, chop=4, oct=(4, 3),echo=1, echotime=2, hpf=2000)
q4 >> play("W ", dur=8, delay=4, rate=0.5, bpf=200, formant=0, dubd=1).unison(4)
q5 >> play("i ", dur=8, delay=4.25, rate=2, feed=0.5)
q6 >> prof(dur=8, rate=4, oct=(2, 5), chop=128, dist=1, room2=1, mix2=1, amp=0.1, spf=1, spfslide=1, spfend=100, fold=0.1, symetry=1)
q7 >> dab(dur=8, oct=(3, 4), shift=0, leg=4, delay=2, echo=0.5, echotime=4, cut=1/8, slide=4, rate=4).unison(4)
q8 >> pianovel((0, 0.01, [0, 0, 0]), feed=0.5, dubd=0.1, delay=4, spf=40, spfend=1400, spfslide=4, shape=PWhite(0, 1), oct=(3, 4, 5),dur=8).solo(0)
u1 >> play("W ", dur=4, feed=linvar([0.1, 0.5],16), rate=var([1, -1], [7, 1]))
u2 >> play("W ", dur=4, delay=1, feed=linvar([0.1, 0.5],16), shape=0.1,rate=var([1, -1], [7, 1]))
u3 >> play("W ", dur=4, delay=3, feed=linvar([0.1, 0.5],16), shape=0.4, rate=var([ PWhite(1.5, 2.5), -1], [7, 1]),hpf=200, hpr=PWhite(0.1, 0.5))
u4 >> play("W ", dur=4, delay=4, feed=linvar([0.1, 0.5],16), shape=0.6, rate=var([r2.degree, -1], [7, 1]), formant=[0,1], echotime=4, echo=1, echomix=PRand([0.25, 0, 0, 0, 0.5]), hpf=200, hpr=PRand([0.1,  0.2]))
u5 >> play("d ", dur=4, delay=4, hpf=1600, echo=0.25, echotime=2, feed=0.5, amp=u4.feed * PRand([0, 1]), chop=4)

u_all.dur=8
u_all.rate=[2,4,8]
u_all.degree="pl"

q_all.stop()
u_all.cut=1/2
u_all.hpr=0.05

u_all.krush=4
u_all.vol=0.5

Master().lofi=0.1
Master().hpf=2000
u_all.rate=var([-2, 1]) # transition
u_all.stop()
Master().lofi=0

Clock.bpm = 173;
Root.default = var([4.02, 4.0, 4.12])
v1.stop()
r2.stop(8)
r1.stop(16)
r3.stop(24)
r4.stop(12)
i3.stop(32)
u_all.stop()

Master().lofi=0
Master().hpf=0
y0 >> subbass([2,3,[5,7]], dur=16, amp=0.4, crush=(0,PRand(0,4)), bits=PRand(4,16), fx1=0.2, atk=PWhite(0.005,0.1), oct=(4,5), output=20, lpf=4000).unison(2)
q_all.stop()
y9 >> nylon(var( [2,3,[5,7], [9, 0, 9, 2], [12, 4, 2], [12, 2, PWalk(8, 1, 1)]]), dist=0.1, dur=var([14, 1/2] ,[1, 4]), amp=PCoin(0.1, 0.2, 40), crush=(0,PRand(0,4)), bits=PRand(4,16), fx1=0.2, atk=PWhite(0.005,0.1), oct=5, output=20, lpf=[4000, 1600, 8000], feed=var([0, 0.25], [4, 1]), slide=[y0.atk, [-0.1, 0.2, (-0.1, 0.4)]], dubd=PWhite(0, 0.04), fold=var([0, 0.1], [7, 1])).unison(4)
y1 >> klank(y0.degree[0], fx2=1, rate=linvar([8, 16], 64), oct=(3, 4), dur=P*[4, 8, 12], lpf=linvar([400,3800],128), lpr=0.1, amp=linvar([0.5, 0.7], 128), hpf=600, bpm = 80 + PWhite(-20, 20), fdist=1, fdistfreq=PWhite(1200, 2000), output=32).unison(2)
y2 >> total(y0.degree[0],dur=32, chop=PRand([0, 0.5, 1, 0.35]), amp=[1,PWhite(0,1)], fmod=PRand([16, 32, 64, 128]), fx1=0, bpf=PRand(800,4000), bpr=0.1, vib=PRand(16), spin=PWhite(-1,1), output=34, shape=0.01).slider().unison(2)

n1.stop()
y9.after(4, "stop")
f1.stop()
r_all.stop()
y1.stop()

y7 >> jbass(var([PWalk(8, 1, 4),PWalk(15, [1, 4], 1)], [4, 4]) , dur=[15, 1/4, 1/4, 1/4, 1/4], sus=[2, 1/4, 1/4, 1/4, 1/4], oct=PStep(7, [3,5], 6), echo=P*[2, 1, 1, 1, 1], amp=0.5, rate=0.1, fx2=1, fx1=1, crush=P*[0,8], output=36).unison(2).slider(0,PStep(8,1,0))
y3 >> bass(y0.degree[0], leg=0.2, oct=(4,6), dur=[15,1], amp=0.4, fx1=1, delay=PWhite(-1,1).rnd(0.25), echo=[0,P[0,0.25,0.5,0.75]], comp=0.6, output=22)
#f1 >> ebass([ PWhite(-0.1, 0.1),PWhite(5, 3) ], slide=16, dur=64, hpf=400, oct=(3, 4), shape=(0, 0.5), output=38, spfslide=16, spfend=1600, spf=1).unison(4).stop()
y5 >> ambi(P*[y0.degree[0],y0.degree[1],y0.degree[2], (y0.degree[0], y4.degree[1]), (y0.degree[1], y0.degree[2]), (y0.degree[0], y0.degree[2]),P**(y0.degree[0], y0.degree[1], y0.degree[2]),P+(y0.degree[0], y0.degree[1], y0.degree[2]), P/(y0.degree[0], y0.degree[1], y0.degree[2])]    , dur=P*[5,1,1/2,8,3], sus = p1.dur, delay=P*[0,PWhite(0,1)], oct=PwRand([6,5,4,3],[30,35,20,15]), velocity=PRand(40,65), fx2=1, amp=PWhite(0.2,0.3), velhard=PWhite(0.2,1), hard=PWhite(0,2), lpf=PRand(5000,18000), output=24).unison(3).penta()
y4 >> pasha(var([y7.degree, y0.degree, y0.degree + 5], [3, 5]), cut=var([0, 1/4], [8, 8]), oct=(3,6), dur=PDur(var([2,3,4,5],[5,1,1,1]),8), amp=var([0,0.1],PRand(4,16).rnd(2)), sus=y0.dur*PWhite(0.1,0.01), echo=var([0.5,[0.125,0.25,0.75]],[6,2]), pan=y4.dur*P[1,-1], lofi=expvar([0.1,1],[PRand(19),PRand(8)]), output=26) + var([0, var([0,PTrir(0,2,0)],[6,2])], [2, 8])

Root.default="C"
z1 >> zap(0, dur=8, hpf=40, shape=[PWhite(0.1,0.4),0.2], oct=(3, PStep(9,5,[4, (5, 6)])), chop=4, chopmix=0.25, spf=10, spfend=8000, spfslide=(0.1, PRand(4,8)), octer=1, octersubsub=var([2, PRand(1,15)], [13]), fx1=0, hpfx1=80, amp=P[0.3,0, 0.1, 0, 0.1, 0], vol=0.7, output=28).unison(4)

z2 >> sawbass(0, dur=8, sus=[8], echo=1/2, amp=(z1.amp==0), mid=2, echotime=PRand(0,12), oct=(5,4,5), shape=(0.01,0,0.01), vol=0.6, output=18).unison(3,var(PWhite(0.25,0.30)),var(PRand(99),8))
y_all.stop()
f_all.stop()

z1 >> lazer(0, dur=8, hpf=40, shape=[PWhite(0.1,0.4),0.2], oct=(3, PStep(9,5,[4, (5, 6)])), chop=4, chopmix=0.25, spf=10, spfend=8000, spfslide=(0.1, PRand(4,8)), octer=1, octersubsub=var([2, PRand(1,15)], [13]), fx1=0, hpfx1=80, amp=P[0.3,0, 0.1, 0, 0.1, 0], vol=0.5, output=28).unison(4) #just once / get back to zap

n1 >> brown(chop=P[1:16:2], dur=4, amp=linvar([0,1],[32,0]), pan=[-1,1], output=34, hpf=linvar([3200, 200], [32, 0]), hpr=PWhite(0.1,0.5))
n4 >> lapin(dur=16, shape=0.1).after(16, "stop")

Clock.bpm = 173

b4 >> ebass([1,0,0,0,0], dur=[1/2,1/2,1,1], oct=(4), pick=0.2, lofi=0, cutoff=linvar([850, 1250],32), decay=1.2, rel=b8.dur*0.5, amp=1, fold=(0, 0.3), room2=0, tanh=0, vol=0.5, output=22).penta()

b4 >> ebass([1,0,0,0,0], dur=[1/2,1/2,1,1], oct=(4), lofi=var([0, 0.01], 8), pick=0.2, cutoff=linvar([850, 1250],32), decay=0.6, rel=b8.dur*0.5, amp=1, fold=(0, 0.14), room2=1, revsus=0.2, smooth=0.1, lofiwow=1, vol=0.3, output=22, tanh=0.2, leg=0).penta()

bv >> pluck([0,0,0,0,[[0, 0, 0, 12], 0, [4, 4.1]]], dur=[1/2,1.5, 1], oct=(4, 5), lofi=var([0.1, 1], 8), cutoff=linvar([850,4000],32), decay=0.1, rel=b8.dur*0.5, amp=1, vol=0.2, output=22, cut=0.1, tanh=4, leg=0).penta()

bw >> pluck(([12, 13, 0, 15, 12], 0.1), dur=[1/2, 1/2, 1, 2], oct=(4, PStep(4, 5, (5, 7))), lofi=var([0.1, 1], 8), cutoff=linvar([850,4000],32), decay=0.1, rel=b8.dur*0.5, amp=PCoin(1, 0, 0.80), vol=0.1, output=22, cut=0, tanh=4, leg=0).penta()

b7 >> ebass(var([ [1,0,0,0], [([1.1, 12], 0), 0, [1, 0], 0] ], [28, 4]), dur=var([ [1/2,1/2,1,1], [2, 4], [1/4, 1/2, 1/4,1/4]], [10, 4, 2]), oct=(3, 4, 5), pick=(0.2,0.5,0.7), cutoff=linvar([250, 1250],32), decay=1.2, rel=b8.dur*0.1, amp=1, fold=(0,0.3,0.2), vol=0.4, output=20).penta().stop()

f1 >> click(PWhite(-0.1, 0.1),dur=b8.dur, hpf=var([200, 3200], [4, 4]), oct=(3, 4), hpr=0.2, shape=(1,0.5), output=38, amp=b8.degree == 0).unison(0)
f2 >> viola((0, PWhite(4, 4.1)),dur=32, hpf=var([200, 3200], [4, 4]), delay=2, cut=1/4, sus=1/4, oct=(3, 4),output=38, amp=b8.degree == 0)

z1.stop()
z2.stop()
g2 >> ssaw([0,0,1,0,0,1,0,0], dur=P[1,1,1.5,1,1,1/2,1,1], feed=0.5, sus=2, hpf=40, oct=[5,5,7,5,5,7,5,PRand(5,8)], high=2, tanh=4, fold=0, amp=var([0,1],[PRand(8,24),PRand(2,8)]), vol=0.08, leg=0.2, glide=1, glidedelay=0.4, mpf=8480, scale=Scale.chromatic, output=32).unison(4,0.25,90).slider(1,[0,1,0,1,0])
m8 >> play("<k..(k.).(.kk.)(k.{.[kk]})(..k.)>", sample=(2,0,7), amp=0.4, output=4)
m7 >> play("<....u..(...u)>", amp=0.2, sample=(3,0,5), rate=(1,1,PWhite(-1,2)), output=8)
m2 >> play("-.", sample=4, pan=PWhite(-0.7,0.7), output=12).human(50,5,2).often("stutter", 2, room=1, echo=0.25, echotime=1, rate=PWhite(1,2), spin=1)

n1.stop()
b4 >> alva(dur=([6, 1/4, 1/4, 1/4, 1/4]), hpf=400, lpf=400, lpr=0.9).after(4, "stop").unison(4)

f2.stop()
f1.stop()
m6 >> play("<..:.>", sample=(0,6), high=1.5, rate=1.5, amp=0.2, pan=PWhite(-0.4,0.4), output=12)
m1 >> play("<X..(.X)(XXX.).(...X).>", sample=(13,2), lpf=0, amp=0.2, output=6)
m3 >> play("<....O..(...O)>", sample=(13,2), lpf=8888, amp=0.2, output=10)
d3 >> play("(#....)..(...~)", rate=PWhite(-1,4)*0.25, amp=0.8, output=10).unison(3, 1,99)
m4 >> play(".-", sample=7, pan=PWhite(-0.7,0.7), output=12).human(10,-5,2).sometimes("stutter")
z_all.stop()

bv.stop()
bw.stop()
#b1 >> faim(([3, 3, PWalk(8, 1, 0)], 0) + var([0, 0, 4, 1]), cut=1/4, octafuz=1, dur=[1/2, 1/2,3, 1/4, 1/4, 1/2, 1/2, 2], oct=(5, 5), beef=0.5).unison(2).stop()

b8 >> ebass([var([0, 3], [31, 1]),0,0,PTri(0,var([8, 12], [5, 1]),2)], dur=var([ var([1/2,P*[1/2,1,2]],[14,2]), var([1/2,P*[1/4,1,1/4]],[14,2]) ], [23, 18]), oct=P[4,4,P*[4,4,3]], pick=0.7,cutoff=linvar([250, 1250],32), decay=0.9, rel=b8.dur*P[P*[0.5,2],0.5,0.5,2], amp=1, fold=(0, 0.2), vol=0.6, output=22).penta().stop()
b7.stop()
f1.stop()

p1 >> play("<q ><p >", sample=1, dur=PDur([3, 5], 8), amp=PWhite(0.3,0.5), hpf=220, chop=1/2, leg=PWhite(15), pan=PWhite(-1,1), output=14)
p2 >> play("(qp) ", sample=2, dur=PDur([1, 6], 8), hpf=200, amp=PWhite(0.3, 0.5), leg=15, pan=PWhite(-0.5,0.5), output=14) #
p4 >> play("p ", sample=2, dur=1/2, lpf=17000, lpr=0.1, amp=sinvar([0,0.3],37), leg=8, pan=PWhite(-0.25,0.75), hpf=200, output=14)
p5 >> play("p ", sample=1, dur=PDur([3, P*[5,7]], var([8,11],32)), lpf=8000, lpr=0.3, amp=sinvar([0,0.4],13), leg=4, pan=PWhite(0.5,-1), hpf=400, output=14)
p6 >> play("q ", sample=1, dur=PDur([3, P*[6,7]], 8), amp=0.4, spf=8800, spfend=340, spfslide=2, chop=1/2, leg=PWhite(15), hpf=240, pshift=0, pan=PWhite(-0.4,0.7), output=14)
p7 >> play("q ", sample=2, dur=PDur([[1, 6],8], 8), amp=0.5, leg=15, hpf=400, pan=PWhite(-1,1), output=14)

print(Clock)
m2.stop()
i5.stop()
d3.stop()
m4.stop()
m7.stop()
i7.stop()
i2.stop()
i3.stop()
i4.stop()

b6 >> ssaw(linvar([7,0],[32,0]), oct=[4,5,6], vib=PRand(16),dur=var([rest(1),1],[PRand(4,32).rnd(4),PRand(4,16).rnd(4)]), sus=2.5, amp=1, vol=0.5, output=28).unison(4).slider(0,1)

Master().lpf=0
i2 >> play("...w", dur=4, sample=5, amp=2, shape=0.3, rate=(PWhite(0.3,1.5),PWhite(0.3,1.5)), pan=(-1,1), output=16).stop()
r9 >> rsin([0,0,P[2,3,[5,[6,4,1],P+(PRand(0,8),PRand(0,8))]].palindrome(1)], oct=6, dur=PStep(15,1,1/2), sus=PWhite(1/4,1), amp=1, lpf=z1.amp * 11480, vol=0.5, pan=[0,0,PWhite(-1,1)], output=24).unison(5)
#!works
g3.cut=1/2
b6.stop()
g2.stop()
Clock.bpm = lininf(173, 178, 64)
b_all.stop()
t1.leg=0
t1 >> angst(0 * PRand([1/2, 1/4, 1] + [4, 21]), dur=1/2, oct=(t1.leg / 4) + PRand([3, 4]), sus=1/2, fmod=(0,12), lpf=t1.leg * PWhite(400, 2000), fx1=0, vib=0, leg=var([4,1], [PRand([3, 7, 15]), 1]), output=28)
g3.stop()
t2 >> play("G", dur=32, delay=-0.125, shift=(12, 32), formant=(1, 4),spf=1, spfslide=32, spfend=8000, feed=0.5, sample=(3, 4), rate=(0.5, 2), chop=(0, 2))

Master().lpf=[400, 0]
Master().cut=[0, 1]
g3.dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8])
g3.sus=g3.dur
g3.amplify=1
z_all.stop()
b8.stop()
f1.stop()

t3 >> play("TtTt{Mm}Mm", sample=PRand(4)+2, dur=var([ PDur(var([1, 3, 7], [12, 3, 4]), 8), 8], [2 ,14]), amp=PCoin(1, 0.0, 0.25), echo=0.5, shape=0, rate=var([1, linvar([1, PRand(8) + 1])], [5, 3]), hpf=100, hpr=0.80, pan=PWhite(-1, 1))

l1 >> loop("break8", dur=8, sample=30, amp=P[PCoin(), PCoin(), PCoin(), 0, PCoin(), 0, PCoin(), 0]*0.5, output=42)
l3 >> loop("break8", dur=8, sample=29, amp=P[0, 0, 0, PCoin(), 0, 0, 0, 0]*0.5, output=42)
l4 >> loop("break8", dur=8, sample=32, amp=P[0, 0, 0, 0, PCoin(), 0, 0, 0]*0.5, output=42)
l5 >> loop("break8", dur=8, sample=35, amp=P[0, 0, 0, 0, 0, PCoin(), 0, PCoin()]*0.5, output=42)

t1.stop()
i_all.stop()
l1.stop()
l3.stop()
m_all.stop()
l5 >> loop("break8", dur=8, sample=30, rate=0.5, amp=P[0, 0, 0, 0.5], output=42)
l4 >> loop("break8", dur=8, sample=35, amp=P[0.5, 0.5, 0.5, 0], lofi=[0.3,0.5,0.7,0], output=42)
l2 >> play("<@>", dur=var([8, 1/4], [8, 4]), shape=var([0, linvar([0.1, 0.2],8)], [8, 4]), sample=2 ,formant=PWhite(0.7, 1.2), delay=0.0, amp=PCoin(), fold=PWhite(0.5,1), dist=0.0, hpf=8000, cut=var([1/4, 0.5]), rate=var([1, linvar([1, 0.5], 4)]), output=46)
x1 >> play("[xxxxxxx]", dur=1/4, amp=PWhite(0.1, 0.3), echo=0.5 ,slide=0.1, feed=0.5, echotime=4, rate=PWhite(1, 4), output=38).after(4, "stop")
l_all.stop()
t3.stop()
t2.stop()

a0 >> play("x.........x...x.", shape=0.5, sample=(0, 4)).sometimes("stutter")
a2 >> play("....o.......o...", shape=1, sample=(0, 4))
a3 >> play("-.-.-.-.-.-.---.", dur=1/4, shape=1, dist=[0, 1])
a4 >> bass([0, var([0.1, 0.2, 0.4], [PRand(16), PRand(8), 4])], dur=PDur(3, 8), shape=4, octafuz=linvar([0.5, 2], [24, 8]), amp=2, dist=1)
n1.stop()
a5 >> play(".[GG].........[G]...[G]", shape=0.4, sample=(1, 4), cut=1/2, hpf=PWhite(1200, 3200)).sometimes("stutter")
a4.shape=var([0, 2, 4, 8], [5, 1, 1, 1])

t1.dur=8
t1.delay=4
t1.oct=(5, 6, 7)

t1.echo=0.5
t1.lofi=1
t1.echotime=4

t1.degree=[0 * PRand([1/2, 1/4, 1] + [4, 21]), (0, 12)]
t1.feed=0.5

r9.dur=var([1/2, 1], [5, 3])
r9.every(4, "shuffle")
t1.every(4, "shuffle")

v2 >> play("V ", sample=4, lpf=100, cut=0, amp=0.5, output=6, hpf=40)
v3 >> play("O ", hpf=6000, lpf=2000, rate=0.3, cut=1/2, amp=0.5, output=6)
v4 >> play("@ ", sample=11, hpf=50, rate=0.1, amp=0.5, cut=PWhite(0.01, 0.06), output=6)
v7 >> play("g ", sample=1, hpf=2200, lpf=8000, amp=0.3, shape=0, output=6)
v8 >> play("V ", sample=4, hpf=12000, amp=PWhite(0.5, 0.9), output=6)
v9 >> play("X.", sample=(8,4), lpf=800, hpf=140, amp=0.4, output=6)

k5 >> play(PEuclid2(3,8,"X","{|=2|*}"), sample=(1,4),rate=var([1,0.7],[16,2]),lpf=linvar([800,5800],[24,0]), triode=PRand(16), lpr=linvar([1,0.05],[24,0]), amp=0.2, output=46).often("stutter", Cycle(PTrir(1,8,0)), amp=0.1, hpf=1800).sometimes("amen")
d1 >> play(PEuclid2(var([3,4],[24,8]),8,"(vv{v@})","(-|=2|)"), dur=1, shape=P*[0,expvar([0.01,0.1],26)], output=4, amp=0.4, lpf=linvar([800,7800],[64,0]), lpr=linvar([1,0.05],61)).often("stutter", Cycle([2,3,6,12]), pan=PWhite(-1,1), amp=0.1, bpf=500)
a4.stop()

t1.feed=0.7
t1.oct=5
t1.chop=1

v0 >> play("V ", octafuz=0.5, output=4)
f2 >> play("[--]", output=4, sample=3, hpf=12000)
m3 >> play("<....O..(...O)>", sample=(13,2), lpf=8888, amp=0.2, output=10)
m8 >> play(".:", sample=4)

v_all.dur=4

v_all.dur=1/2
q1 >> dbass(PSine(64) * 0.1, dur=1/4, beef=1, tanh=0.1, shape=0.2, hpf=linvar([400, 1600], 128)).unison(4)
m9 >> play("X ", bpf=0, sample=(3, 5)).sometimes("stutter", shape=4, dur=4)

print(Clock)

r9.stop()
v_all.stop()
m_all.stop()
q_all.stop()

q1.dur=0.5
q1.oct=(5,linvar([6, 6.05], [32,0]))

a1 >> tb303([0.02, 0.01, 0.01, 2, 2, PTrir(0.01, 0.03, 0.02), linvar([0.1, 0.3], 16), PStep(4, 0.2, 0.24)], oct=(4, var(PTrir(3,6,5), 8)), top=linvar([1600, 100], 8), cutoff=linvar([200, 800], [24, 8]), amp=1, pan=linvar([0.8, -0.4], [PRand([8, 4, 8])]), output=22, shape=([0.2, 0.01, 0.1, 0.3], [32, 4, 8, 8]), lpf=0, dur=1/4, fdist=1.8, fdistfreq=linvar([2000, 6000]), vol=0.4).sometimes("stutter", feed=0.65).slider(0,0)

q6 >> play("..X:", sample=12)
q8 >> play("V:", fdist=1, fdistfreq=400, shape=0.1)

a1 >> faim(PArp([0,1,0.5],11) + PGauss(0, 0.2) + P[0, 0, 0, [0.1, 0.1]], oct=(4, 6), stut=0.5, stutlen=[0.1, 0.2], beef=(1,0), dur=PDur(var([4,[5,3,8]],[6,2]),8), sus=f1.dur*PWhite(0.5,1), lpf=0, amp=1, output=18)

k8 >> pianovel([([4, 4, 7], [4, 4, [0, 7]]), (4, [5, (5, 0)]), (4, [4, [7, 4, 4], [3, 4, (7, (11, 10.01))]])], oct=4, scale=Scale.minor, dur=[4, 1/4, 1/4, 2, 1/2, 1], bpm = Clock.bpm /2).unison(2)
k9 >> pianovel((4, [4, 7, 0, [0, [7, 4, 14]]]), bpm = Clock.bpm /2, oct=5, scale=Scale.minor, dur=[1/4, 4, 2, 1/4, 1, 2]).unison(2)
k0 >> pianovel(([[7, 4, [12, 0]], [7.01, 4.01, 0.01]], 0), oct=(4, 5), bpm = Clock.bpm/2, delay=0.125, scale=Scale.minor, dur=4).unison(2)
k6 >> pianovel([0, 0, -3, -4], amp=0.5, dur=[7, 1/2, 1/2], oct=(7, 8), bpm = Clock.bpm /2).every(1, "stutter")
Clock.bpm = 173
k7 >> pianovel([[0, [-0.01, 0.02]], (0.01, 0)], dur=16, oct=(3, 4, 2), velocity=(80, 90), echo=1, echomix=k7.spfslide, spf=(1, 4000), spfend=(k7.spfslide * 1000, 1), spfslide=(PRand( [PWhite(1, 4),PWhite(0.01, 3)])), velhard=(1, 30))
k4 >> pianovel([4, 3, (2, 4), 4, [3, 8, 7]], dur=1/4, amp=[0, linvar([0, 1], 16)])
k5 >> dbass(k8.degree * PWhite(0.1, -0.1), lofi=0, lfp=1200, rate=0.5, hpf=100, dur=1/4).unison(4)
k6 >> dbass(k8.degree * PWhite(0.1, -0.1), lofi=0, lfp=1200, rate=(0.5, 1), hpf=100, dur=1/4).unison(4)

k_all.lpf=lininf(8000, 5, 32)

q4 >> latoo(([0, 1, (4, 1), 1, (4, 4)], [3, [4, 2, 0]]), dur=[1, 1/2, 1/2, 1/2, 1/2], rate=4, lpf=0, hpf=0, spin=1, crush=24, formantmix=0.01, formant=4, bits=4).unison(4)

v_all.stop()
m_all.stop()
