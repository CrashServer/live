��3�      }�(�server_data�}�(�lieu��	streaming��tmps��16��lang��fr��voice��0��	bpm_intro��48��scale_intro��minor��
root_intro��E��video�K �horo�K u�attack_data�}�(�connect�]�(�Crash Server���Welcome CrAsh ServEr
C0nnect_the_S&rV3r
 -- StageLimiter : Active
 -- Carla : Active
 -- Record : Active
 -- Biniou : Active























































�X}  a = 512
b = expinf(0, 0.5, a * 2)

i1 >> sos(dur=PRand(16), vib=PRand(10600), lpf=linvar([60,4800],[PRand(8,24), PRand(32,48)]), hpf=expvar([0,500],[PRand(64,96), PRand(8,32)]), shift=lininf(1, 2, a)).unison(3,0.75,99)

k1 >> play("g...", vol=0.8, lpf=PWhite(200,8000), room=0.2, mix=PWhite(0.2,0.9), shape=(0,0.2), dur=2)
k2 >> play("g...", delay=4, echo=0.25, amp=0.2, lpf=PWhite(200,8000), room2=1, mix2=PWhite(0.2,0.9), shape=(0,0.2), dur=2)

v1 >> play("E ", dur=16, sample=PRand(200), amp=2)
k3 >> play("x.-x..", echo=0.5, dur=1/2, shape=4, rate=1, octafuz=linvar([0.3,1]), formant=var([1,0,5]), fdist=1).every(3, "stutter")

b1 >> bbass(0, oct=(lininf(2, 3, a), lininf(2, 4, a)), dur=1/4, shape=0, shapemix=0.2, med=0, sus=1, blur=1, amp=1, vol=0.4).unison(3)
v2 >> play("G", sample=PRand(200), dur=2, coarse=0, chop=P*[0,1,4],  chopmix=PWhite(0, 1), chopwave=PRand(8), echo=PwRand([0,PWhite(0, 1)],[50, 1]), shift=PWhite(0.5, 2), rate=PWhite(0.95, 1.05), crush=PWhite(0, 4),bits=PRand(8)+4, lofi=0, room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), formantmix=0.1, formant=PGauss(0, 1), revatk=PWhite(-1,2), pan=PWhite(-1,1), amp=2)

b2 >> abass(0, oct=(lininf(3, 4, a), lininf(4, 5, a)), lpf=400, dur=1/2, sus=1, delay=0.25, blur=1, amp=1, vol=0.4).unison(3)
v3 >> play("E", sample=PRand(200), dur=3, coarse=0, chop=P*[0,1,4],  chopmix=PWhite(0, 1), chopwave=PRand(8), echo=PwRand([0,PWhite(0, 1)],[50, 1]), shift=PWhite(0.5, 2), rate=PWhite(0.95, 1.05), crush=0,bits=PRand(8)+4, lofi=P*[0,PWhite(0,1)], room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1), amp=2)

b3 >> jbass(0, oct=(lininf(3, 5, a), lininf(4, 5, a)), dur=PDur(var(P[1:8],a/8), 8), sus=1, delay=0.25, blur=1, amp=1, fx1=b, fx2=b, vol=0.4).unison(3)
v4 >> play("{EG}", sample=PRand(200), dur=16, coarse=0, chop=P*[0,1,4],  chopmix=PWhite(0,1), chopwave=PRand(8), echo=PwRand([0,PWhite(0, 1)],[50, 1]), shift=PWhite(0.5, 2), rate=PWhite(0.95, 1.05), crush=0, bits=PRand(8)+4, lofi=PWhite(0,1), feed=0.5, room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))










































�K e�init�]�(� �� 































��





























�Ke�
aspiration�]�(�
Aspiration��/














































�X�  a2 >> faim(0, oct=(3,4), fx1=1, beef=[1,[1,0]], dur=var([PStep(8,2,1/4),PDur(var(PRand(8),8),8,PRand(8))],[[14,6],2]), drive=(0,0.05), amp=P[PWhite(1,1.2), PWhite(0.2,0.7), PWhite(0.5,var([0.7,1],16)), PWhite(0.2,0.5)]).every(6, "stutter", PRand([2,3]), oct=5, delay=0.25, glide=0.3, amp=PWhite(0,0.5)/(1+a2.formant), formant=[0,PWhite(1,6)], room2=0.7, mix2=0.4) + var([0,P*[1,-1,2,-2]],[7,1])
d1 >> play("v(...v.)(.[.v])(.{v.})".replace("v","W"), sample=0, amp=P[1,(a2.amp<0.5)]*0.8, dur=1/2)
d2 >> play("<{Dd}><h>", sample=(1,5), dur=1/4, rate=(PWhite(1,3)), amp=a2.amp > 0.88, hpf=340, pan=(0,PWhite(-1,1))).sometimes("stutter", PRand(4), amp=1)
d3 >> play("[x-].o.", dur=var(PRand([4,3,2,1,1/2,1/4,1/8]),P*[4,2,1,1/2]), sample=(7,8), lpf=50, amp=1)
d5 >> play("<W.[.W].><.q>", sample=(0,2), amp=P(0.5,1), cut=PWhite(0.1,1.2), lpf=8080).sometimes("stutter", PRand(2), rate=PWhite(1,4), amp=0.4, pan=PWhite(-1,1), fx1=1, comp=0.2)
d6 >> play("<P.[Tt].><.Tq><..J.>", delay=var([0.125, 0], [PRand([7, 5]), 22]), hpf=0, dur=1, rate=[8, 4], echo=0.125, fold=PBern(16), echomix=0.3, amp=PBern(16) , crush=4, sample=PRand(8))
d7 >> play("<..{uuu|r5|}.>", sample=2, amp=1).sometimes("stutter", PRand(8,32), hpf=400)
z2 >> four((var(PRand(-4,2),8),var(PRand(8),4)), dur=PDur(var([3,5,9],8),11), atk=[0.01,PWhite(0.01,0.03)], oct=(5), fx2=0.5, hpf=120, triode=1, krush=0.2, amp=PStrum()*0.2, kutoff=PRand(400,8400), scale=Scale.yu).sometimes("stutter", 1,oct=(5), drive=PWhite(0.2,0.4), dur=PRand(1,3)).unison(3)


�Ke�	attention�]�(�	Attention��"

































�X�  Root.default = linvar([0, 4, 2, PRand(2)], [PRand([4, 8, 12, 16])])
Clock.bpm = lininf(112, 132, 512)
r1 >> rsin((linvar([0,4],16),linvar([2,-2],24), linvar([-4,4],32)), dur=var(PRand([1,1/2,1/4,2]),8), hpf=linvar([30,180],23),oct=var([3, 4, 5], PRand(8)), para1=PWhite(200, 8000), fmod=8,lpf=linvar([3000,8000],19), amp=0.5, sus=r1.dur, fold=var([0.5, 0.1]), fx2=0.5, room2=1, revsus=r1.dur*PWhite(0,2), revatk=-1, damp2=PWhite(0.1,0.9))
r2 >> click(r1.degree, oct=[5,4,3,6], vib=P*[1, 2, 4, 8, 2, 16],echo=PStep([7,[3,6]],0,0.25), dur=[2,4,6,PRand([2, 4, 8])], mult=PRand(16), amp=0.7,shape=PWhite(0.2, 0.3), slide=0.3, pan=PWhite(-1,1), room2=1, damp2=0.1,  spf=8000, spfend=10, spfslide=4)
p1 >> play("<q ><p >", sample=1, dur=PDur([3, 5], 8), amp=PWhite(0.3,0.5), hpf=220, chop=1/2, leg=PWhite(150), pan=PWhite(-1,1))
p2 >> play("(qp) ", sample=2, dur=PDur([1, 6], 8), hpf=200, amp=PWhite(0.3, 0.5), leg=25, pan=PWhite(-0.5,0.5))
p3 >> play("//", sample=67, dur=16, hpf=140, spf=40, spfslide=5, spfend=8000, amp=0.3, rate=[PWhite(-0.5,-0.1), PWhite(2,8)], pan=(PWhite(-1,1),PWhite(-1,1))) # 
p4 >> play("p ", sample=2, dur=1/2, lpf=17000, lpr=0.1, amp=sinvar([0,0.3],37), leg=8, pan=PWhite(-0.25,0.75), hpf=200)
p5 >> play("p ", sample=1, dur=PDur([3, P*[5,7]], 8), lpf=8000, lpr=0.3, amp=sinvar([0,0.4],13), leg=8, pan=PWhite(0.5,-1), hpf=400)
p6 >> play("q ", sample=1, dur=PDur([3, P*[6,7]], 8), amp=0.4, spf=8800, spfend=340, spfslide=2, chop=1/2, leg=PWhite(150), hpf=240, pshift=0, pan=PWhite(-0.4,0.7))
p7 >> play("q ", sample=2, dur=PDur([[1, 6],8], 8), amp=0.5, leg=25, hpf=400, pan=PWhite(-1,1))
d1 >> play("<X(..{XxK.})X(..X)(X.)>", sample=2, lpf=linvar([500,1500],[32,7]), lpr=PWhite(0.3,1), amp=0.3).every(PRand(1,9)
, "stutter", PRand([6,8,12,16]), rate=PWhite(1,1.125), pan=[-1,1], bpf=1500, drive=0.2)
r3 >> dbass(linvar([0,0.6],[64,0]), root=0, mid=2, dur=PDur(8,14), amplify=0.8*(d1.degree!="X"), leg=PRand(4), a=0, sus=0.4, oct=4, lpf=13000, hpf=60).unison(3)
d1 >> play("<X(.....{X[XX]xv})><..O.><|x4|.>", amp=0.2, lpf=8000)
d2 >> play("<[-{---[--]|:4|}]><.:>", sample=7, amp=0.5, lpf=0 ,pan=PWhite(-0.5,0.5), rate=PWhite(0.99,1.01)).human(80,3,4).sometimes("stutter", PRand(4))
















�Ke�	corrosion�]�(�	Corrosion��
























�X/  s3 >> star([0, 3, [3, 7], 0.5, PRand([3, 7, 0, (0.5, 3, 0)])], crush=linvar([128, 0], [16, inf], start=now),dur=1/8, oct=6, scale=Scale.locrianMajor, formant=PRand([0, 4]), amp=0.5) + Pvar([0, 3, 0, 0, 2, 0], [4, 2])
f1 >> faim(PArp([0,1,0.5],11), oct=(3, 4), dur=1/4, lpf=200)

























�Ke�
absolution�]�(�
Absolution��












�X  Clock.bpm = linvar([120,150,120,60],[PRand([4, 8, 16, 2])])
p5 >> pianovel(Pvar([Scale.major, Scale.minor, Scale.locrian]).palindrome(), flanger=PWhite(0, 0.1), oct=P[3:7], lpf=Clock.bpm * 10, delay=(0, 0.5, 0.05), sus=PWhite(0.5,1.2), velocity=PWhite(40,80))











�Ke�annihilation�]�(�Annihilation��

















�X�0  Master().reset()
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


















�Ke�random�]�(h�$random virus























��


















�Ke�42�]�(h�




























��























�Ke�43�]�(h�










��






�Ke�	desynchro�]�(�!emiT��





















��$clip.copy(random_bpm())












�Ke�nucleose�]�(�@ Nucleose @��
















�Xc  a1 >> play("<X[--]><..O.>", amp=4, room=0.7, mix=PRand([0,.4,0])).sometimes("stutter", PRand(8))
s1 >> saw((0,1), oct=(3,[4,5]), lpf=PRand(8800), lpr=PWhite(0.1,0.9), amp=[0,0.4,0], dur=var([4,1/4,2],16), chop=8, drive=0.2, slide=(PWhite(-2,2),PWhite(-1,1))).unison(16, analog=40)
b1 >> dbass(PArp([0,2,-2], 13), dur=1/4, lpf=8000).unison(3)













�Ke�zika�]�(�Zika��

















�X  b2 >> dbass(p1.degree+PWhite(0,0.3), lpf=linvar([900,4500],24), dur=[1/2,1/4,1/2,1/4,1/2]).sometimes("dur.shuffle")
p1 >> prof(PSine(64)*0.2, oct=(var([(3,4),[5,6]],[6,2])), dur=PDur([5,7],8), sus=p1.dur*0.7, cutoff=7000, lforate=var([1,2,4],8), lfowidth=linvar([0.1,1],39), pan=[-1,1], amp=0.8)
n1 >> play("..I.", drive=(0,0.9), sample=1, rate=(PWhite(-1,4)), amp=PBern(16), pan=linvar([-1,1],24))
d4 >> play("x(---([::]:[::::]))", amp=1, sample=([0,1,2],[1,2,4])).sometimes("stutter")
d6 >> play("X ", amp=1)

















�Ke�syphy�]�(�//+ SYPHY +//��














�X�  sq >> squish(oct=(3,[4,5]), dur=P*[8,4,2,1,0.5,0.125], echo=sq.dur/PRand([4,2,8]), echotime=sq.echo*PRand([1,2,0.5]), rate=PStep(8,PRand(40),1), triode=0.8, leg=4, lpf=4800, lpr=0.2, room=0.8, mix=0.1, amplify=0.2*PBern(24)).unison(5,0.2,80)
dd >> play("p", dur=1/4, amplify=PTimebin(), sample=PRand(1,4), bpf=linvar([200,4000],32), bpr=1, pan=P*[-1,1])
ds >> play("..O.", lpf=7800, shape=0.1, cut=1/2, sample=6, pan=(0.2,-0.2))
hh >> play("[--]", sample=4, cut=1/P[1:8], pan=PWhite(-1,1), bpf=linvar([1200,8080],36), bpr=PWhite(0.1,0.9), bpnoise=PRand(4)).human(50,-4)
dk >> play("<X.>", triode=(0,8,PRand(8)), sample=(6,3,2), amp=(2,0.5,0.7), lpf=(4800,PRand(120,1450),0), pshift=(-12,0,PRand(12))).sometimes("stutter")











�Ke�slaap�]�(�!/// SLAAP - DARKWATER - REMIX ///��


















�X.	  Samples.addPath("/mnt/70225B03225ACDAA/CRASH SERVER/Production/Slaap - remix/zbdm version/")
Root.default="C"
Scale.default="minor"
Clock.bpm=176

w1 >> stretch("sl_wind", dur=P[16,32,64], sus=[32,64], lpf=1800, amp=0.2, rate=PWhite(-1,1)).unison(4)
w2 >> loop("sl_voice1", formant=1, dur=12, hpr=0.1, hpf=4000, amp=0.2, room=1, mix=0.6, pan=(-1,1))
w3 >> loop("sl_wind", 4, dur=6, sus=[12, 24], spin=[4, 8, 16, 2], hpr=0.1, hpf=0, amp=0.3, room=1, mix=0.4, pan=(-1,1))

w_all.stop()
g1 >> loop("sl_guit2", dur=32, shape=0)

g9 >> loop("sl_guit2", dur=[8,[16,4]], delay=[12,8,16,24], cut=[1/4,1/2,1/8], sus=16, chop=[16,32], room=0.3, mix=0.2, pan=(-1,1), crush=2)
l3 >> loop("sl_drum1", dur=32)
g3 >> loop("sl_guit3", dur=PRand([16,32]), chopwave=PRand(8), chop=PRand(8), room=1, mix=0.4, lpf=7800).unison(4)
g4 >> loop("sl_guit3", dur=PRand([8,16]), chopwave=PRand(8), chop=PRand(8), room=1, mix=0.4, lpf=7800).unison(4)

y1 >> loop("sl_voice2", dur=[16], shape=0.1, amplify=1).unison(0).after(16,"stop")
y2 >> loop("sl_voice3", dur=12, shape=0.2, amplify=1).after(12, "stop")
y3 >> loop("sl_voice1", dur=16, spin=0.4, amplify=PBern(8), room=1, mix=0.6).after(1, "stop")
y4 >> loop("sl_voice2", dur=15, spin=0.2, amplify=1, octafuz=1, room=1, mix=0.6).after(1, "stop")
y5 >> loop("sl_voice1", dur=14, spin=0.4, amp=PwRand([0, 1], [15, 1]), room=1, mix=0.6).after(1, "stop")

a1 >> play("x-", dur=1, sample=var(P[0:10],64), crush=0, amp=0.2).sometimes("stutter", PRand(8), rate=4).unison(5).sometimes("amen")
v_all.stop()
g_all.stop()
b1 >> loop("sl_bass1", dur=8, sus=8, shape=0.1, lpf=linvar([800,4800],[64,0]), lpr=PWhite(0,1)).unison(3)
b2 >> loop("sl_bass2", dur=16, shape=0.2, sus=16, amp=1.5, cut=[2/3,[0,1/3]], chop=[0,2,4]).unison(2)
b3 >> loop("sl_bass2", dur=16, lpf=800, sus=16)
k1 >> loop("sl_drum2", dur=32, lpf=4800)
k2 >> loop("fill4", sample=2, dur=8, hpf=4000)
k3 >> loop("fill4", sample=4, dur=8, hpf=2000)

b_all.stop()
y_all.stop()
k_all.stop()

p0 >> stretch("sl_guit1", pshift=-7, delay=8, dur=16, pan=-1)
p4 >> stretch("sl_guit1", pshift=-7, dur=8, pan=1)
p1 >> loop("sl_guit1", delay=4, dur=16, sus=32)
f1 >> loop("sl_guit1", dur=32)
p3 >> loop("sl_guit1", dur=16)

l4 >> loop("break16", sample=0, dur=16)
l5 >> loop("core16", sample=3, dur=16, chop=2, lpf=7800, amp=0.5)
l6 >> loop("core16", sample=2, dur=16)













�Ke�
radiocrash�]�(�"RadioHead - Fitter Happier - Cover��























�X"  Scale.default="major"
Root.default="Db"
Clock.bpm = 76
Clock.meter=(3,2)

i1 >> pluck((const(0), PRand(12).rnd(2), PRand(8)), rate=PWhite(0,1), atk=PWhite(0,4), oct=(3,4), dur=PRand(4,16), rel=PWhite(0,8), sus=16, decay=PWhite(0,8), blur=PRand(4), lpf=8000, triode=1, amp=1, room=1, mix=0.3).unison(3,linvar([0.02,0.25],128),99)
y1 >> play("K", sample=PRand(9), rate=(PWhite(-1,-0.3),PWhite(0.1,1)), dur=PRand(3,17), hpf=60, crush=4, room=1, mix=PWhite(0.4,0.7), lpf=1800, pan=(PWhite(-1,1),PWhite(-1,1)))

Voice(lyrics, lang="english", voice=2, rate=125)

p1 >> pianovel([var([(P*[-2,-9],0,5),PRand([(-2.5,-1,5),(-2.5,5),(-5,2.5,-1,5)])],[6,12]),-1,0,-1,0,-1,P*[0,-5],PwRand([5,6,3,-1,P+[5,6,3]],[3,3,3,3,1])], oct=(4.99,5.01), dur=[1,1,1,1,1/2,1/2,1/2,1/2], delay=PWhite(-0.025,0.025), lpf=var(PRand(800,2800),12), lpr=PWhite(0.4,0.8), velhard=PWhite(0.5,0.7), velocity=PRand(38,var([80,60],[1,5])), amplify=var([0,1],[PRand(6),PRand(24)]), room=1, mix=PWhite(0,0.4)).sometimes("stutter",amplify=1, velhard=(1, 0.1), oct=(5, 6), delay=0.125).sometimes("pivot", 5)

b3 >> pianovel(var([-2,0,5,[2,-4]],6), oct=3, dur=6, lpf=1200, hpf=100, velocity=PRand(70,80))
b1 >> faim(var([0,-4,-5,2],[12,12,6,6]), dur=PDur([[9,3],5],12), lpf=PRand(1200,3800), hpf=100, oct=PStep(6,4,3), amplify=PWhite(0.8,1.2)) + var([0,const([-2,2])],[5,1])
p9 >> donk((0, 0.5, [-0.5, 1]), delay=(0, 0.5, 0.75), dur=3, rate=P*[1, 2, 4, 8], room=PWhite(0.5,1), mix=PWhite(0.3,0.8), pan=(PWhite(-1,1),PWhite(-1,1)), hpf=PRand(60,580)).often("stutter").accompany(b1)

s1 >> dab(-2, dur=8, lpf=PRand(800,2000), fmod=PRand(8).rnd(2), oct=PStep(3,6,5), amp=0.5).every(4, "rotate").unison(3,0.25,99).after(8, "only")
d1 >> play("<K..><I...><..O.><[--]><.(.:)>", sample=P[0:9], amp=0.8, cut=PWhite(0,2), rate=(1,PWhite(-1,2))).sometimes("stutter", PRand(8)).every(16, "sample.rotate", PRand(8))
d2 >> play("<X.>", sample=1, amplify=2).every(4, "stutter", PRand(8))
n1 >> dafbass(linvar([0,0.3],[128,0]), dur=PDur([6,8,5],8), oct=[5,6], amplify=[0.5,0,d2.degree!="X",0.2,0.8], fmod=PRand([0,2,PRand(8)])).unison(3)


�Ke�--- SECOND PARTS ---�]�(h�


��


�Ke�glitch�]�(h�

















���c1 >> glitcher(oct=PRand(8), rate=PWhite(1, 128), amp=1, dur=8, len=PWhite(1, 16), henA=PWhite(0.01, 4), fmod=0, henB=PWhite(0.1, 0.2), t=[2, 4, 6, 8, 32], crush=PRand(16),bits=16, shape=4.0).unison(2)














�Ke�consolation�]�(�? Consolation ?��














�X�  Clock.bpm = 120
Root.default=12
var.cho = var(PMarkov(I),8)

t9 >> tb303(PArp(var.cho,5), oct=3, dur=1/4, top=linvar([200,10000],128), cutoff=linvar([500,2000],[PRand(24,36),PRand(2,12)]), rq=PWhite(0.1,0.3), sus=PStep(PRand(4,16)[:16],0.5,0.25), amp=0.35, lpf=9000, fx2=0).unison(3)
t9.lpf=linvar([20, 6000],[256, inf], start=now)
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.4, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)

d1 >> play("x.", feedfreq=[[0,PRand(500)],0], hpf=30, sample=4, amp=0.2, tanh=2, chop=1)
d1.feed=var(P*[0,0.125,0.25,0.5],16)

d7 >> play(P["x-(-m)"][:8].rotate(var([1,3])), rate=1.5, dur=1/4,amplify=0.8, delay=var([0,(0,0.75)],PRand(8)),sample=1)




















�K	e�
snowdation�]�(�:: snowdation ::��







�X   Clock.bpm = 133;

a2 >> sine((0, 2), sinefb=linvar([0, 1.0], 128), amp=0.5, delay=0.5, oct=3, sus=2, hpf=200, pan=linvar([-1, 1], 128))
a4 >> sine((0, 2), sinefb=linvar([0, 0.5], 196), amp=0.3, delay=1, oct=3, sus=1, hpf=400, pan=linvar([1, -1], 128))
a1 >> play("U", dur=16, rate=[0.9, 1.1], sample=PRand([4, 5, 6, 7, 8, 9]), shape=0.1, feed=0.4).unison(2)
d8 >> play("p ", sample=4, rate=0.25, dur=16, delay=2, amp=4, echo=0.25, echotime=4)
d6 >> play("  c ", dur=8, amp=0.7, echo=0.5, room=1, mix=0.5)







�Ke�tabation�]�(�Tabation��



�XP  cl >> click(0, dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), hpf=40, drive=[PWhite(0.4,0.8),0.2], oct=(3, PStep(9,5,4)), octer=1, octersub=2, octersubsub=var([2, PRand(15,2222)], [15, 1]), triode=4, amp=0.1, amplify=1).unison(3).rarely("stutter",PRand(6), oct=6, pan=[-1,1], mpf=2860, hpf=400)
db >> bass(0, dur=c1.dur, leg=12, amp=var([0.5, 0], [12, 4]), rate=PWhite(0.01, 0.2), sus=db.dur*1.5).unison(2)
n1 >> play("<u><t>", sample=(2,P[0:5]), delay=(0,(0,[0,0.25])), dur=cl.dur, crush=[0,0,0,PRand(8)], bits=4, lpf=n1.crush*1500)

















































�Ke�
augmendrum�]�(�
Augmendrum��





�Xg  h1 >> play("h", dur=PDur(var([7,8,4],[8,2,2]),8)/var([1,[2,4]],16), sample=PStep(8,1,3), rate=PWhite(1,4), amp=PWhite(0.0, 0.5), pan=PWhite(-1,1)).degrade(0.2)

d1 >> play("(x.)(.x).(..x)", sample=(4,2), hpf=30, dur=var([2,1/4], 8), spf=[14000,60,300], spfslide=PSine(64)*0.35, spfend=P*[500,1700,200])
d2 >> play("(.v)(.V|w0|).(.v.)", sample=3, hpf=50, dur=var([4,1],16), crush=1, echo=P*[0.5,0.25], echomix=linvar([0,1],[19,0]), lpf=4800)
p1 >> play("j", amp=var([0,0.5], [3,1]), crush=8, sample=PRand(8), rate=linvar([8,PRand(16)*-1],[8,0]), leg=25, dur=1/4, echotime=1, echo=1)
p2 >> play("p", sample=PRand(8), crush=4, amp=p1.rate>=0, amplify=PWhite(0.1, 1), leg=PWhite(10, 25), room=1, mix=0.3, dur=1/8, echotime=1, echo=1, pan=[-1,1])
h2 >> play("[--]", sample=PRand(8), rate=var([0.7, linvar([1,4],8)]), leg=1, dur=1/4, amp=var([0,0.5], [3,4]), hpf=5600).spread()

p3 >> play("(XP)", sample=PRand(8), rate=[0.7,1.1], leg=PRand([16,64,32]), dur=1/4, amp=var([0,p2.amp==1],[8,16]), mpf=6500)
s1 >> play("(yL) ", sample=(PRand(8), PRand(8)), dur=2, rate=(0.4, -2), delay=(0, 1), slide=(4, 1), bpf=(800,4800), bpr=(0.2,0.8))
d3 >> play("K", dur=var([32,1/4], [1,[4,8]]), rate=linvar([2,1], 4), echo=var([0.75,0.5,0.25,0.125], P*[0.25,1,0.5,0.125]), cut=0.9)

a1 >> play("I ",rate=(0.25,PWhite(0.15,0.3)), triode=PRand(9), dur=4, spin=0.25, amp=0.5, room=1, mix=(0,0.6), hpf=350).after(4, "stop")

a2 >> play("(kc){.@}(..)P", amp=1, rate=4).sometimes("trim",3).every(13, "stutter", Cycle([4,13,2]), hpf=4000, pan=[-1,1])
a3 >> play("(+.)(.+)", room=0.5, mix=0.2, sample=5, amplify=P*[0,1], rate=[-0.5,1], delay=[PWhite(0,0.12),0])





�Ke�augmen2�]�(�augmen2��



�XE  b1 >> faim(var([-2,0],8), dur=1/4, oct=3, krush=[3,PWhite(0,3)], kutoff=linvar([400,9900],[29,11])) + var([0,P*[1,-1,2,-2]],[7,1])
b2 >> faim([3,PRand(7)], dur=PDur(9,11), oct=[[5,6],4], room=0.7, mix=0.3, krush=1.8, amp=PStrum(), kutoff=PRand(400,8400), amplify=var([[1,0,1],0],[16,8])).sometimes("stutter", drive=0.2).unison(4).penta()

sw >> pasha(b2.degree + (0,var(P*[6,3,2],4),4), amplify=[1,b2.amp>0.5], dur=PDur(7,9,2,var(P*[0.25,0.5,1],[6,2,4])), leg=PWhite(0,2), glide=PWhite(0.2,2), swell=0.4, sus=sw.dur*PWhite(0.1,0.9), oct=[5,6], room=1, mix=0.3).unison(4,0.125)




�Ke�
aspirateur�]�(�
aspirateur��


�X�  d1 >> play("<X[--]><..O.>", sample=0, amp=4, room=0.7, mix=PRand([0,.4,0])).sometimes("stutter", PRand(8))
sa >> saw((0,1), oct=(3,[4,5]), lpf=PRand(8800), lpr=PWhite(0.1,0.9), amp=[0,0.4,0], dur=var([4,1/4,2],16), chop=8, drive=0.2, slide=(PWhite(-2,2),PWhite(-1,1))).unison(16, analog=40)
b3 >> dbass(PArp([0,2,-2], 13), dur=1/4, lpf=8000).unison(3)
f1 >> feel([(2, 9, 14), (2, 9, 14, 33), (2, 9, 14, 26, 33), (2, 9, 14, 26, 34), (2, 9, 14, 24, 33), (4)], scale=Scale.chromatic)


�Ke�	suddation�]�(�	Suddation��





�Xp  a = var(PWhite(2, 4), 4)
b = var(PWhite(2, 4), 4)
c = linvar([a, b], 2)
d = var([a, c, b], [8, 2, 6])
Clock.bpm=90+d*2
Scale.default="minor"
Root.default = d

a1 >> sinepad((PSine(4)|PSine(16)|PSine(32),4), formant=PRand(4), flanger=PWhite(0,0.4), fdecay=PWhite(0,4), drive=0.1, fold=0.2, oct=(3,4,5), dur=8, room=1, mix=0.7, amp=1, chop=1.6, chopwave=PRand(8)).unison(5,0.25)
w2 >> sawbass(PWhite(0,0.3), dur=PDur(var([5,7],[6,2]),8,var(PRand(8),36)), cutoff=PRand(190,1580), oct=(4,5,[6,7]), amp=1)
w3 >> play("k ", sample=0, dur=4, echo=0.5, amp=1, hpf=120).every(4,"stutter").sometimes("amen")
d4 >> play("r r r [rr] r ", amp=[1, 0.8, 1, 0.4] * P[0.5], dur=1/4, rate=PRand(2,7), pan=[-1,0.5,0,-0.5,1], sample=3)
d6 >> play("..u.", lpf=4000, crush=5, room=[0.5,1,0.8], mix=[0,0.2,0.4], sample=0, delay=PWhite(-0.1,0.1)).often("stutter", Cycle([2,4,3,6,5,2]), amp=PWhite(0.5,1.3), rate=PWhite(1,2))
d5 >> play("..g..", sample=16, rate=(1,0.33), dur=1, hpf=1500, hpr=0.1 + PWhite(-0.01, 0.01))
k1 >> play("<X.><..o.><..U(.(...{O.[.O][Oo]}))><..x>", amp=1, sample=0).sometimes("stutter")
h1 >> play("<{[---][--{.-}][-{.-}-][{.-}--]}><(.:)><..+>", hpf=180, lpf=0, amp=1, sample=(3,11,1), pan=PWhite(-1,1), lofi=0).human(40,5)
d3 >> play("..(.z).", shape=0.7, cut=1/2, rate=(1.3,.7), pshift=(linvar([0,12],265),0,-12), delay=0.7, lofi=PWhite(0.3,0.9))
a2 >> bell(a1.degree, formant=(0,PRand(6)), formantmix=0.8, oct=(3,4,5), dur=8, room=1, mix=0.7, amp=1, chop=8, chopwave=PRand(8)).spread() + (0,var([-2,-4,-3,-1],8))
y1 >> pasha(a1.degree, delay=var([0, 0.25],[3, 1]), oct=(4,5), dur=PDur(var([2,3,4,5],[5,1,1,1]),8), amp=1, sus=y1.dur*PWhite(0.5,1.2), echo=var([0.5,[0.125,0.25,0.75]],[6,2])).unison(0).sometimes("unison", cycle=3).slider()
p1 >> play("s ", sample=3, dur=1/8, hpf=expvar([5400, 5600], 32), amp=PWhite(0.8, 1), pan=PWhite(-1,1))
w2.cutoff=P[190,linvar([1580,11800],[64,0], start=now)]


�Ke�deambulation�]�(�deambulation��


�X�  Clock.bpm=92
Scale.default="minor"

d1 >> play(PEuclid2(var([3,4],[24,8]),8,"(vv{v@})","(-|=2|)"), dur=1, drive=P*[0,expvar([0.01,0.9],26)], lpf=linvar([800,7800],[64,0]), lpr=linvar([1,0.05],61)).often("stutter", Cycle([2,3,6,12]), pan=PWhite(-1,1))
b1 >> dbass(var([0,[-4,2,-2]],[14,2]), dur=P*[2,6],amp=(d1.degree!="v")*0.8, lpf=linvar([1800,3500],19), lpr=expvar([1,0.2],17), sus=b1.dur*PWhite(0.8,2),fx1=1, fx2=0.0, rate=linvar([0.1,15],23), oct=(PStep(7,6,5),4,PStep(4,6,5))).unison(3)
d2 >> play("<X ><(-[--]-[::])><..|*2|.><..C.>", bits=16, amp=1, dur=2, crush=3, room1=1, mix=PWhite(0,0.5)).rarely("amen").sometimes("stutter", PRand(1,6), rate=PRand([1,6]))

s1 >> sitar(P[0,5,P*[7,8,4],3], oct=P*[5,[6,4,3]], vib=PWhite(6,32), slide=0.01, slidedelay=PWhite(0.2,0.9), sus=s1.dur*PWhite(0.3,0.8), dur=1/4, room=1, mix=PWhite(0,0.2), amp=var([(d1.degree=="@"), (d1.degree!="@")],[28,4]), drive=(0,0.1), fx2=1).spread() + [0,0,P*[2,4],0]



�Ke�	oxydation�]�(�	oxydation��


�X�  Scale.default="yu"
Clock.bpm = var([175,175/4],[56,8])
f1 >> pluck(var(PChords(),8), dur=PRand(1,8)/PRand(1,4), blur=PWhite(1,4), decay=PRand(1,4), oct=(3,4,PStep(7,6,5)), drive=PWhite(0,0.1), sus=PRand(1,16), atk=PStep(8,0.2,PRand(1,6)), room2=1, mix2=0.6, damp2=PWhite(0.1,0.5), revatk=PWhite(0.2,2), revsus=PWhite(1,4), hpf=160, lpf=PRand(1800,9065), amp=0.3).unison(4,0.25)
jb >> jbass([f1.degree[0],f1.degree[2]], dur=[6,2], amp=1, oct=[5,6,5], glide=P[0:8]*PRand([-1,0,1]), glidedelay=PWhite(0.7,0.99), shape=[0,PWhite(0,1),0.2,0,0.3], echo=(jb.shape>0)*jb.dur/PWhite(0.1,4), echotime=jb.degree, lpf=[4500,5500+jb.shape*1000], hpf=60).every(6, "unison", cycle=[0,4])
d3 >> play("(#....)..(...~)", rate=PWhite(-1,4)*0.25).unison(3, 1,99)
d1 >> play("<x.(...(.x))><..(**.*).><..(.((CCC.).)..)><(-.)->", sample=4, amp=var([1,0,1],[13,1,1]), crush=PRand(8), dur=1/2).sometimes("stutter", PRand(16))
p1 >> blip(f1.degree[0] + (0,[2,4]), dur=[1/2,1/2,1/2,P*[0.5,rest(2.5)]], amp=(b1.sus<6 and (d2.degree[0]!="v")), amplify=d1.degree[1]!="*", oct=(5), rate=PRand(1,4), leg=PRand(0,8),glide=0.5, fmod=4, vib=PRand(2,16), sus=PWhite(0.5,1), echo=[0,0.25], lpf=PRand(400,12888), room=1, mix=PWhite(0,0.5)).unison(3).every(8, "mirror")
b1 >> sawbass(f1.degree[0], dur=8, sus=[8,PRand(1,8)], echo=1/2, mid=2, echotime=PRand(0,12), oct=(5,4,5), drive=(0.01,0,0.01)).unison(3,var(PWhite(0.25,0.30)),var(PRand(99),8))

�Ke�mmxx�]�(�MMXX��



�X 	  Master().reset()
Clock.bpm=113
Root.default = 1
Scale.default= Pvar([Scale.major, Scale.justMajor],PRand([4, 8, 16,32]))

b1 >> varsaw((var([0,-2,-4],16),[1,2,1],var(PRand([5,6,2,4,7],8))), sus=10, lpf=linvar([3000, 6700], 128), lpr=PWhite(0.2,0.9), blur=2, amp=0.4, dur=var([5,1,1], [6,1,1]), oct=PStep(6,6,4), fx2=1, fx2hpf=300, fx2lpf=7800).unison(3) + var([0, 4, 8], [6, 1, 1])

b2 >> varsaw((var([0,-2,-4],16),[1,2,1],var(PRand([5,6,2,4,7],8))), sus=1, spfslide=1, spfend=6000, spf=10, lpf=6000, lpr=PWhite(0.2,0.9), blur=2, amp=0.3, dur=var([4, 1/4, 8], [2, 2, 1]), oct=PStep(4,5,3), fx2=1, fold=0.5,bpm = 80 + PWhite(-20, 20)).unison(4) + var(PRand([0, 4, 8, -4, 6, -3]), [6, 1, 1])

e1 >> klank(b1.degree[0], fx2=1, rate=linvar([8, 16], 64), oct=(3, 5), dur=P*[4, 8, 12], lpf=linvar([400,4800],128), lpr=0.05, amp=0.5,bpm = 80 + PWhite(-20, 20))

e2 >> klank(b1.degree[1] + var([0, -2, -4, 6]), dur=1, rate=4, oct=var([(5, 6), (4, 7)], 4), lpf=linvar([400,4800],128), hpf=2000, drive=0.0,lpr=0.7, chop=8, chopmix=0.25, lofi=linvar([0.1, 0.5], 32), amp=1,bpm = 80 + PWhite(-20, 20)).unison(2)

p1 >> pianovel(P*[b1.degree[0],b1.degree[1],b4.degree[2], (b1.degree[0], b1.degree[1]), (b1.degree[1], b1.degree[2]), (b1.degree[0], b1.degree[2]),P**(b1.degree[0], b1.degree[1], b1.degree[2]),P+(b1.degree[0], b1.degree[1], b1.degree[2]), P/(b1.degree[0], b1.degree[1], b1.degree[2])], dur=P*[5,1,1/2,8,3], sus = p1.dur*PWhite(1,1.5), delay=P*[0,PWhite(0,1)], oct=PwRand([6,5,4,3],[30,35,20,15]), velocity=PRand(40,65), fx2=1, amp=PWhite(0.6,0.8), velhard=PWhite(0.2,1), hard=PWhite(0,2), lpf=PRand(5000,18000)).unison(3).penta()

z1 >> total(b1.degree[0],dur=16, amp=[1,PWhite(0,0.5)], fmod=PRand([16, 32, 64, 128]), fx1=0, bpf=PRand(800,4000), bpr=0.1, vib=PRand(16), spin=PWhite(-1,1)).slider()

y4 >> subbass(p1.degree, dur=16, amp=0.4, crush=(0,PRand(0,4)), bits=PRand(4,16), fx1=1, atk=PWhite(0.005,0.1), oct=(4,5)).unison(3)
y5 >> faim(y4.degree[0], oct=(4,5), dur=[15,1], amp=0.5, fx1=1, delay=PWhite(-1,1).rnd(0.25), echo=[0,P[0,0.25,0.5,0.75]], comp=0.6)

g1 >> play("G", dur=PRand(32), crush=PRand(16), bits=PRand(4,16), sample=PRand(2020), amp=0.8)

Scale.default= Pvar([Scale.major, Scale.justMajor, Scale.minor, Scale.justMinor],PRand([4, 8, 16,32]))
Clock.bpm = sinvar([113, 40], 128)



�K
e�intervention�]�(�intervention��
�X  y1 >> pbass(5, oct=(3,4), dur=8, echo=0.25, echotime=PRand(7,10), drive=0.5, room=1).unison(3)
d9 >> play("k.", dur=[4,1/4,1/4,1/2,1,1/2,1], sample=(0,5)).sometimes("stutter", 3)
d8 >> play("d+d", sample=[2,1], dur=PDur(5,8,2)*2, room=PWhite(0.5,1), mix=0.4)
�Ke�mbr�]�(�MBR OVERDRIVE��

�X_  Root.default ="C"
Scale.default="minor"
Clock.bpm = linvar([131, 134],[32,0]);

s1 >> dab((0,-2), dur=32,fx1=1, amp=0.9, fx2=1, lpf=PRand(800,8000), fmod=PRand(8).rnd(2), oct=PStep(3,6,5), cut=0).every(4, "rotate").unison(3,0.25,99)
b8 >> fbass(oct=(4,5,6), echo=0, lpf=PRand(800,10800), hpf=40, drive=linvar([0,0.7],[16,0]), dur=PDur(var([8,P*[5,7,6]],[6,2]),8), sus=1/6, vol=1)
v1 >> play("K", amp=[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0], dur=1/4, output=8, sample=0, cut=0)
v3 >> play("@", amp=[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], dur=1/4)
v4 >> play("N", amp=[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0], dur=1/4, shape=1, sample=PRand(99)[:12], cut=1, lpf=200, amplify=1)
v5 >> play("[-]", amp=[0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,1], dur=1/4, sample=8, rate=PWhite(-0.5,3), hpf=180, vol=0.8, pan=PWhite(-1,1))
x3 >> play("s", amp=linvar([0.5, 1]), sample=0, dur=1/4, amplify=[0.76, 0.2, 0.4], lpf=PRand(8000,18000), pan=PWhite(-1,1)).human(40,.8)
x4 >> play("c", amp=[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0], dur=1/4, shape=PWhite(0.2,2), lpf=P*[200,linvar([40,18200],[32,0])])
x9 >> play("X ", sample=5, lpf=5800, amp=2)
v6 >> play("I", sample=4, hpf=PRand(2000,8000), rate=PWhite(-1,2), dur=P*[1,1/2], amp=[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0], pan=PWhite(-1,1))
v2 >> play("t", amp=[0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0], lpf=P*[200,2000], dur=1/4)
z1 >> play("K", amp=[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0], dur=1/4)
z2 >> play("o", amp=[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0], lpf=200, dur=1/4)
z3 >> play("-", amp=[0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0], dur=1/4, amplify=[0.76, 0.2, 0.4], rate=PWhite(1,4), pan=PWhite(-1,1))
z4 >> play("-", sample=1, amp=[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0], dur=1/4, shape=1, lpf=2200, rate=PWhite(1,4), pan=PWhite(-1,1))
z6 >> play("t", hpf=12000, dur=1/4, amp=[1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1], sample=2, amplify=PGauss(4, 0.1), echo=0.125, echomix=var([0, 0.125], 4))
f2 >> pluck(linvar([0, 0.4], [4, 0]),oct=(linvar([6,6.2],[32,0]),5), dur=1/4, sus=linvar([1/8,1/4],[32,0]), vol=0.5).unison(4).human(80,0.5)
x1 >> play("K", amp=[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0], dur=1/4)
x2 >> play("--", amp=[0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0], lpf=200, dur=1/4, pan=linvar([-1, 1], 16))
x5 >> play("o", amp=[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0], dur=1/4, sample=2)
x7 >> play("p", hpf=8000, dur=1/4, amp=[0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0])
l1 >> play("V ", sample=3, cut=1, output=20)
f3 >> varsaw(linvar([1, 2.4], [8, 0]), leg=4,oct=(linvar([6,6.2],[64,0]),5), dur=1/2, sus=linvar([1/8,1/4],[32,0]), lpf=0, vol=0.5).unison(4).human(80,0.5)
Master().cut=0

�Ke�hyperstatic�]�(�hyperstatic��













�X\  Root.default = -4

g1 >> faim([2,3,[5,7]], dur=([[1,1,1/2],2,1/2,4,1/2]*PRand([2,3,1,4])), slide=var([0,[-4,4]], [7,1]), leg=PWhite(0,4), sus=g1.dur*PWhite(0.2,1.5), oct=5, chop=P*[0,4,16], hpf=var([1000, 0], [PRand(2,11), PRand(12,19)]), fx1=1, fx2=1, fx1hpf=150, amp=0.5, room=1, mix=PWhite(0.2,0.5)).unison(2).sometimes("shuffle") + (0,[2,[4,6]])
b1 >> faim(var([-2,0],8), dur=P[1,1,1,0, 1,0,0,1]*1/2, amp=0.5,hpf=var([0, 1000], [PRand(4,16), PRand(4,9)]), oct=(3,4)).sometimes("stutter") + var([0,PGauss()],[6,2])

h1 >> play("h", dur=PDur(var([7,8,4],[8,2,2]),8)/var([1,[2,0.5]],16), sample=PStep(8,1,3), rate=PWhite(1,4), amp=PWhite(0.0, 0.5), pan=PWhite(-1,1)).degrade(0.2)
d1 >> play("<(x.)(.x).(..x)><(k.)(.M).(..O)>", delay=0, sample=(2, 4), rate=(1, 0.5), hpf=30, dur=var([2,1/4], 8), spf=P*[14000,60,300], spfslide=PSine(64)*0.35, spfend=P*[500,1700,200])
d2 >> play("(.v)(.V|w0|).(.v.)", sample=3, hpf=50, dur=var([4,1],16), crush=1, echo=P*[0.5,0.25], echomix=linvar([0,1],[19,0]), lpf=4800)
p1 >> play("j", amp=var([0,0.5], [3,1]), crush=8, sample=PRand(8), rate=linvar([8,PRand(16)*-1],[8,0]), leg=PRand(25), dur=1/4, echotime=1, echo=1, pan=PWhite(-0.5,0.5))
p2 >> play("p", sample=PRand(8), crush=4, amp=p1.rate>=0, amplify=PWhite(0.1, 1), leg=PWhite(10, 25), room=1, mix=0.3, dur=1/8, echotime=1, echo=1, pan=[-1,1])
h2 >> play("[--]", sample=PRand(8), rate=var([0.7, linvar([1,4],8)]), leg=1, dur=1/4, amp=var([0,0.5], [3,4]), hpf=5600).spread()

p3 >> play("(Xs)", sample=PRand(8), rate=[0.7,1.1], leg=PRand([16,64,32]), dur=1/4, amp=var([0,p2.amp==1],[8,16]), mpf=PRand(6500,14000))
s1 >> play("(yL) ", sample=(PRand(8), PRand(8)), dur=2, rate=(0.4, -2), delay=(0, 1), slide=(4, 1), bpf=(800,4800), bpr=(0.2,0.8))
d3 >> play("K", dur=var([32,1/4], [1,[4,8]]), rate=linvar([2,1], 4), echo=var([0.75,0.5,0.25,0.125], P*[0.25,1,0.5,0.125]), cut=0.9)















�Ke�A1�]�(h�


�X�  a0 >> loop("cosmic16", dur=16, sample=2, hpf=(300, PRand([400, 300])), room2=1, revsus=18, shift=var([(0.5, 1), 1], [4, 4]), beat_dur=1).unison(2)
a1 >> play("c", dur=4, hpf=8000, leg=4, echotime=4, echo=0.5, echomix=0.25, pan=PWhite(-1, 1))
a2 >> loop("sub4", dur=4, sample=9, amp=PWhite(0.5, 0) + 0.5, shift=(0, 1.01), hpf=0, drive=var([0, 0.1], [3, 1]))
a3 >> play("o ", amp=2, dur=4, sample=2, room2=1, lpf=400, hpf=400, echotime=4, echo=0.25, echomix=0.2)
a4 >> loop("perc8", dur=8, sample=3, amp=1 - a1.amp, hpf=4000, pan=PWhite(-1, 1))
a5 >> loop("berlin4", dur=8, sample=11, hpf=PRand(100, 1000), amp=PWhite(0, 1), room2=1, revsus=4, leg=0)
a6 >> loop("berlin4", dur=8, sample=4, hpf=PRand(100, 1000), amp=PWhite(0, 1), room2=[1, 0], revsus=4)
a7 >> loop("berlin4", dur=8, sample=5, hpf=PRand(100, 1000), amp=PWhite(0, 1), room2=1, revsus=4)
a8 >> loop("futur8", dur=16, sample=4, amp=P[1, 1, 1, 0] / 1.5)
a9 >> loop("berlin4", dur=8, sample=2, echo=var([0, 0.5], [3, 1]), amp=P[0, 0, 0, 1] / 1.5)


�Ke�B1�]�(h�

�X�  b1 >> loop("cosmic16", dur=16, echotime=8, echo=4, sample=3, hpf=40, amp=0.5).unison(4)
b2 >> loop("sweep16", dur=32, echotime=8, echo=4, spf=200, spfend=8000, spfslide=8, sample=0, hpf=40, amp=0.2).unison(4)
b3 >> loop("cosmic16", dur=16, sample=3, amp=0.5, echotime=4, echo=2, shift=PStep(4, 1, 0.5), hpf=400).unison(4)
b4 >> loop("hiphop8", dur=16, sample=4)
b5 >> loop("atmo8", dur=8, sample=1, amp=[0, 0, 0.7, 0.5] * 2) #
b6 >> play("Pp", dur=PDur(3, 8), sample=2, hpf=PWhite(2000, 4000))
b7 >> loop("atmo32", dur=32, sample=2).unison(2)
b8 >> loop("atmo32", dur=32, sample=1, delay=8, hpf=4000).unison(2)
b9 >> loop("nszap8", sample=1, dur=16)
b0 >> loop("nsbreak16", sample=2, dur=16) #

�K"e�C1�]�(h�

�X  c1 >> loop("core16", dur=16, sample=1, cut=1, lpf=0)
c2 >> loop("xvermin16", dur=16, sample=2).unison(2)
c3 >> loop("xbassphase16", dur=16, sample=2).unison(2)
c4 >> loop("nspad16", dur=16, sample=1, amp=0.5)
c5 >> loop("electrodrum32", dur=32, sample=0, lpf=0)
c6 >> loop("break32", dur=32, sample=2, lpf=0)
c7 >> loop("break32", dur=1/4, cut=0.1, sample=PRand(8), pan=PWhite(0.1, 0.5), lpf=0)
c8 >> play("w", dur=4, echo=2, sample=6, amp=1)
c9 >> loop("drum4", dur=4, sample=1, amp=[1, 0])
c0 >> loop("drum4", dur=4, sample=0, amp=[0, 1])

�K#e�D1�]�(h�

�X*  d1 >> loop("ravebass4", dur=8, sample=4)
d2 >> loop("ravebass8", dur=8, sample=5, drive=0.0, amp=0.5, hpf=4000)
d3 >> loop("ravebass8", dur=16, sample=0, shift=PRand(1, 2), room2=0, drive=0, revsus=0, amp=0.5).unison(2)
d4 >> loop("ravebass4", dur=4, sample=0, room2=0.5, drive=0, revsus=4).unison(2)
d5 >> loop("ravebass4", dur=4, sample=0, room2=0.5, drive=0, revsus=8).unison(0)
d6 >> play("X:", sample=(5, 4), lpf=(1200, 4000)).sometimes("stutter")
d7 >> loop("nsbass16", dur=16, sample=1, hpf=400)
d8 >> loop("psych32", dur=32, sample=3, lpf=4000)

�K$e�E1�]�(h�

�X�  e1 >> play("K ", hpf=0)
e2 >> play("--")
e3 >> loop("fill16", dur=16, sample=4, hpf=400, amp=[1, 1, 1, 0])
e4 >> loop("nshits16", dur=16, sample=0, hpf=600, amp=[0, 0, 0, 1])
e5 >> loop("nshits16", dur=16, sample=3, hpf=600, amp=[0, 0, 0, 0, 0, 0, 0, 1])
e6 >> play("x ", dur=8, lpf=400, room2=1, damp2=0, revus=8, shape=0.1, echo=0.05, echotime=8)
e7 >> play("a ", sample=4, shift=(0, 0.5), feed=0.2, tremolo=4, dur=8, delay=4, lpf=1200, room2=1, damp2=0, revus=8, shape=0.1, amp=0.2, spf=400, spfslide=4, spfend=3200, echo=(0.025,0.25), echotime=8)
e8 >> play("p.", dur=1/2, lpf=1400, room2=0.2, damp2=1, sample=0, revus=8, shape=0.1, echo=[0.05, 0.25], echotime=x3.dur).sometimes("stutter", 2, rate=2, amp=1.5, dur=1/4)
e9 >> play("p.", dur=1/4, lpf=linvar([800, 1400], 32), sample=0, room2=0.1, damp2=0, revus=2, shape=0, amp=[0.5, 0.7], echo=[0.05, 0.25], echotime=x3.dur).often("stutter", 2, rate=2, amp=1.5, dur=1/2)

�K%e�F1�]�(h�

�X  f1 >> loop("half16", dur=16, sample=2 , lpf=0)
f2 >> loop("xtbass16", dur=16, sample=0, amp=1)
f3 >> loop("noizebeat8", dur=16, sample=3, amp=[0.5, 0])
f4 >> loop("noizebeat8", dur=16, sample=4, amp=[0, 1], chop=4)
f5 >> play("<[--]><..U(..[UU])><..o.><.:>", amp=1, sample=4, room2=1, mix2=0.3, revsus=0.5, revatk=-0.3).sometimes("stutter", 4)
f6 >> play("..C.", amp=1)
f7 >> play("V ", sample=2, amp=1)
f8 >> loop("grat8", dur=16, sample=1, amp=0.3)
f9 >> loop("grat8", dur=16, sample=1, shift=(1, 3), amp=0.2).unison(4)

�K&e�G1�]�(h�

�X  g1 >> play("V ", sample=4, lpf=1200)
g2 >> dbass(dur=1/4, drive=0).unison(4)
g3 >> play("[--]", sample=4)
g4 >> loop("noizebeat8", dur=8, sample=4, amp=[0.5, 0.5, 0, 0.5])
g5 >> loop("noizebeat8", dur=8, sample=6, amp=[0, 0, 0.5, 0])
g6 >> loop("noizebeat8", dur=8, sample=5, amp=[0, 0, 0, 1])
g7 >> play("..C.", sample=4, amp=2, room2=linvar([0, 1], 8), feed=0, revsus=linvar([1, 4], 4),hpf=400)
g8 >> play(PRand("Xx.xx.xx.xx.xx.x"), room2=.3, amp=0.2, mix2=0.43, revatk=0.1, revsus=0.5, sample=[0,7,4], lpf=0, leg=PRand(0,42), krush=P*[0,4]).sometimes("stutter", PRand(8), rate=PRand(8)).slider(on=0)
g9 >> play("<Oo><[Pp.@]>", sample=PRand(8), cut=PRand([1/2, 1/4, 0]), krush=PRand([0, 12]), bits=PRand([2, 12, 0]), crush=(8, 1), amp=1, lpf=PRand([1200, 3200, 15000]), hpf=4000)

�K'e�H1�]�(hh���h1 >> loop("xxpiano16", dur=16, sample=2, lpf=lininf(1, 1200, 64))
h2 >> loop("xhop16", dur=32, sample=0, lpf=0)
h3 >> loop("xvermin16", dur=16)
h4 >> loop("ragedrum16", dur=16, sample=2)
�K(e�doom�]�(�	DOOM E1M1�h�Xj  g1 >> faim(P[-5,-5,7,-5, -5,5,-5,-5, 3,-5,-5,1, -5,-5,2,3, -5,-5,7,-5, -5, 5,-5,-5, 3,-5,-5, P(-5,1)], dur=P[1/2].stutter(27) | 2.5, lpf=[PRand(400,2280),0,0], lpr=PWhite(0.1,0.5), drive=0.3, shape=0.3).gtr(2) 
g2 >> faim(Pvar([P[21,19,18,21, 24,22,21,18, 21,22,24,26, 24,22,21,18], P[26,22,19,22, 26,22,26,31, 26,22,26,22, 26,31,34,38]],32), dur=1/4, amp=var([0,1],[28,4]), drive=0.3, shape=0.3).gtr(2)
g3 >> faim(var([0,P*[3,5,7,0]],[14,2]), oct=5, dur=1/2, lpf=300, lpr=0.4, beef=2).gtr(1)
g4 >> play("<k(.k)u.><->", sample=(9,5), amp=1).human(40,0).every(14, "stutter", 8, cycle=16, degree="u", amp=PWhite(0.3,1))
�K)e�metro�]�(�METRO�h�XM  f1 >> faim([(0,12),15, P*(5,8,14), _, P*(3,7,12),_, P*(2,5,11),_, (0,12),15, P*((5,17),15,14),_, P*((3,15),14,12),_, (2,14), 11], dur=1.5, hpf=PRand(250,400), hpr=PWhite(0.2,0.5), sus=2.5, mverb=0, room=1, mix=0.3).gtr(1)
f2 >> faim([5,8,P*(10,8,7),7,P*(8,7,5),5, 7, 4], dur=1.5, drive=0.2, amp=0.5, room=1, mix=.5).gtr(5)
f2 >> faim([5,5,8,8,1,1,0,[0,-4]],dur=1.5).gtr(5) 
f3 >> faim(var([0,3,5],12), dur=0.5).gtr(1)
f4 >> play("<k..kk.><--(...[.-----])><..u>", sample=(9,5,9), amp=1).human(40,0).every(14, "stutter", PRand(1,6), cycle=16, degree=PRand(["u","-","k"]), amp=PWhite(0.3,1))
�K*e�mirror�]�(�MIRROR�h�XE  p1 >> pianovel([11,11,9, 6,6,4, 9,9,2, 1,1,-1], dur=P[4,2,2], echo=1, echotime=1.5, velocity=PRand(48,68), echomix=0.5, mverb=0.5).gtr(6)
p2 >> varsaw((var([-11,-9,0,-4],16),6,6,p1.degree),oct=(3,4,5,6), sus=10, blur=2, shape=PWhite(0.0,0.1), dur=8, lpf=PRand(400,1200), lpr=PWhite(0.2,0.5), amp=0.6).unison(18,0.25).gtr(1)

�K+e�gta�]�(hh�X�  Root.default = "C"
Clock.bpm=144
Scale.default="dorian"

t1 >> mpluck([[0, 1, 2, 1, 0, 1 ,0, -1],-3], mverb=lininf(0,0.8,32), amp=0.5, oct=(PStep(8, 5, 6), 5, 7), pan=PWhite(-1,1), cut=1/2, dur=2, delay=0, hpf=400).unison(4)
t2 >> pianovel([[0, 1, 2, 1, 0, 1 ,0, -1],-3], dur=1/2, velocity=PRand(40,60), hpf=100, velhard=0.2, amp=PGauss(0.4, 0.1), oct=PStep(7,6,5), rate=linvar([0.1,1.8],24), sus=PWhite(0.2,0.3)).unison(3).sometimes("stutter", oct=[6, 8], mverb=0).stop()
t3 >> pianovel(t2.degree + 5, oct=PStep(4, 5, [6, 7]),velhard=[PGauss(0.2, 0.2), 0], hpf=120, velocity=PRand(40,88), delay=var([0,(0.125, 0)], [5, 3]), amp=linvar([0.3, 0.6], [16]), mverb=0.1).accompany(p0).unison(4).human()

t4 >> ssaw([[0, 1, 2, 1, 0, 1 ,0, -1],-3], amp=0.3, hpf=linvar([200, 400]), hpr=0.39, dur=1/2, phase=0, sus=linvar([0.6, 1], 16)).unison(8)

t5 >> ssaw([0,2,P+(3,4),P+(6,7,8,14)], oct=(5.01, 3.99, 7), sawtype=P*[0,1], sawmix=0.5,  lpr=0.7, amp=(0.2, 0.1, 0.2), lpf=7800, dur=8).unison(8)
t6 >> ssaw([0,2,3,(4.5,7)], oct=(4,5), dur=8, lpf=800, slide=0.2, slidedelay=0.8, hpf=90).unison(3)

t7 >> bass([0,0,-1,7,7,-1], dur=[1/2,1/2,[rest(3)]], amp=1, oct=5, echo=0.25, sus=1)
t8 >> jbass(4, dur=1/2, amplify=var([0,1],[3.5,0.5]), amp=1, echo=0.5, oct=4)
t9 >> dbass(P[3, 4, 4.5, [4, 3]].stutter(2), dur=1/4, oct=(4,5), amplify=var([0, 1], [6, 2]))
t0 >> bass([(0, [7, 3]), (0, [4, -1])], drive=linvar([0, 1], 32), oct=P(3, [4, [5, 6]])+1, room2=0, dur=[1/2, 1/2, [rest(1)]]).unison(2)

�K,e�trap�]�(hh�X  d0 >> play(".{...u}..u...", sample=5, hpf=var(PRand(4000)+10), rate=(.5,2)).sometimes("stutter")
d1 >> play(".{...c}..c...", sample=5, mverb=0, flanger=0, chorus=var(PWhite(0, 1)), amp=P*[0, 1], rate=(P*[.5,.5,.5,-1],2))
d2 >> play("v.....(...{v.})(...{.v}))", cut=2, sample=8, hpf=50, drive=(0,var(PWhite(0,0.2)))).sometimes("stutter")
d3 >> play("v.....(...{v[vv].}).", sample=8, delay=0.5, hpf=400, amp=var([0, 1], [28, 4]))
d4 >> play("(...(.p)).((p.).(p.).)((p.).(p.).)", dur=1/4, sample=4, crush=8,bits=8)
d5 >> play("-{-[--]}-.-{[---][--]}(-.)(-[----])", sample=2, amp=PCoin(PWhite(0, 1),0,0.5), hpf=6000, pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble").sometimes("stutter", PRand(16), rate=PWhite(-1,5))
d6 >> play("---.-{[---][--]}(-.)(-[----])", hpf=5000, sample=10, amp=PCoin(PWhite(0, 1), 0, 0.5), pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble")
d7 >> play("---.-{[---][--]}(-.)(-[----])", pan=PWhite(-1, 1), hpf=4000, amp=PCoin(PWhite(0, 1), 0, 0.5), sample=8).sometimes("amen").sometimes("bubble").every(4, "shuffle")
�K-e�filter�]�(h�

�X`  masterAll("lpf", var([0, 4000, 6000, 15000], [24, 4, 2, 2]))
masterAll("hpf", var([0, 20, 30, linvar([3200, 6400], 32)], [24, 4, 2, 2]))
masterAll("cut", var([0, 1, 1/2, linvar([1/4, 1], 32)], [24, 4, 2, 2]))
masterAll("degree", linvar([1, linvar([0, 2],[4, 0])], 8))
masterAll("rate", 2) 
masterAll("dur", P*[1/2, 1, 1, 1/2, 2])
masterAll("reset")



�K.e�A2�]�(hh�X�  #annihilation intro
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

�K e�A3�]�(hh�X
  Clock.bpm = lininf(120,173,32);
Root.default = var([4.02, 4.0, 4.12])
y0 >> subbass([2,3,[5,7]], dur=16, amp=0.4, crush=(0,PRand(0,4)), bits=PRand(4,16), fx1=0.2, atk=PWhite(0.005,0.1), oct=(4,5), lpf=4000).unison(4)
y1 >> klank(y0.degree[0], fx2=1, rate=linvar([8, 16], 64), oct=(3, 4), dur=P*[4, 8, 12], lpf=linvar([400,3800],128), lpr=0.1, amp=linvar([0.5, 0.7], 128), hpf=600, bpm = 80 + PWhite(-20, 20), fdist=1, fdistfreq=PWhite(1200, 2000)).unison(2)
y2 >> total(y0.degree[0],dur=32, chop=PRand([0, 0.5, 1, 0.35]), amp=[1,PWhite(0,1)], fmod=PRand([16, 32, 64, 128]), fx1=0, bpf=PRand(800,4000), bpr=0.1, vib=PRand(16), spin=PWhite(-1,1), drive=0.01).slider().unison(2)
y3 >> jbass(var([PWalk(8, 1, 4),PWalk(15, [1, 4], 1)], [4, 4]) , dur=[15, 1/4, 1/4, 1/4, 1/4], sus=[2, 1/4, 1/4, 1/4, 1/4], oct=PStep(7, [3,5], 6), echo=P*[2, 1, 1, 1, 1], amp=0.5, rate=0.1, fx2=1, fx1=1, crush=P*[0,8]).unison(2).slider(0,PStep(8,1,0))
y3 >> bass(y0.degree[0], leg=0.2, oct=(4,6), dur=[15,1], amp=0.4, fx1=1, delay=PWhite(-1,1).rnd(0.25), echo=[0,P[0,0.25,0.5,0.75]], comp=0.6)
y4 >> ebass([ PWhite(-0.1, 0.1),PWhite(5, 3) ], slide=16, dur=64, hpf=400, oct=(3, 4), shape=(0, 0.5), spfslide=16, spfend=1600, spf=1).unison(4)
y5 >> ambi(P*[y0.degree[0],y0.degree[1],y0.degree[2], (y0.degree[0], y4.degree[1]), (y0.degree[1], y0.degree[2]), (y0.degree[0], y0.degree[2]),P**(y0.degree[0], y0.degree[1], y0.degree[2]),P+(y0.degree[0], y0.degree[1], y0.degree[2]), P/(y0.degree[0], y0.degree[1], y0.degree[2])], dur=P*[5,1,1/2,8,3], sus = p1.dur, delay=P*[0,PWhite(0,1)], oct=PwRand([6,5,4,3],[30,35,20,15]), velocity=PRand(40,65), fx2=1, amp=PWhite(0.2,0.3), velhard=PWhite(0.2,1), hard=PWhite(0,2), lpf=PRand(5000,18000)).unison(3).penta()
y6 >> pasha(var([y4.degree, y0.degree, y0.degree + 5], [3, 5]), cut=var([0, 1/4], [8, 8]), oct=(3,6), dur=PDur(var([2,3,4,5],[5,1,1,1]),8), amp=var([0,0.1],PRand(4,16).rnd(2)), sus=y0.dur*PWhite(0.1,0.01), echo=var([0.5,[0.125,0.25,0.75]],[6,2]), pan=y4.dur*P[1,-1], lofi=expvar([0.1,1],[PRand(19),PRand(8)])) + var([0, var([0,PTrir(0,2,0)],[6,2])], [2, 8])

y7 >> zap(0, dur=8, hpf=40, drive=[PWhite(0.1,0.4),0.2], oct=(3, PStep(9,5,[4, (5, 6)])), chop=4, chopmix=0.25, spf=10, spfend=8000, spfslide=(0.1, PRand(4,8)), octer=1, octersubsub=var([2, PRand(1,15)], [13]), fx1=0, hpfx1=80, amp=P[0.3,0, 0.1, 0, 0.1, 0], vol=0.7).unison(4)
y8 >> sawbass(0, dur=8, sus=[8], echo=1/2, amp=(y71.amp==0), mid=2, echotime=PRand(0,12), oct=(5,4,5), drive=(0.01,0,0.01), vol=0.6).unison(3,var(PWhite(0.25,0.30)),var(PRand(99),8))

Root.default=lininf(4, 0, 32)
�K!e�anniriff�]�(h�

�Xi  n1 >> zap(0, dur=8, hpf=40, drive=[PWhite(0.1,0.4),0.2], oct=(3, PStep(9,5,[4, (5, 6)])), chop=4, chopmix=0.25, spf=10, spfend=8000, spfslide=(0.1, PRand(4,8)), octer=1, octersubsub=var([2, PRand(1,15)], [13]), fx1=0, hpfx1=80, amp=P[0.3,0, 0.1, 0, 0.1, 0], vol=0.7).unison(4)
n2 >> sawbass(0, dur=8, sus=[8], echo=1/2, amp=(n1.amp==0), mid=2, echotime=PRand(0,12), oct=(5,4,5), drive=(0.01,0,0.01), vol=0.6).unison(3,var(PWhite(0.25,0.30)),var(PRand(99),8))
n1.synthdef="lazer"
n2.synthdef="zap"
n3 >> brown(chop=PRand(8), chopwave=PWhite(0,8), dur=PWhite(0.1,4), amp=var([0, expvar([0,2],[6,0])], [14, 2]), pan=PWhite(-1,1), spf=40, spfend=PRand(400,9800), spfslide=n3.dur/2, drive=1, hpf=linvar([3200, 200], [PRand(4,32), 0]), fx2=1, fx1=1, hpr=PWhite(0.1,0.9))
n4 >> ebass([1,0,0,0,0], dur=[1/2,1/2,1,1], oct=(4), pick=0.2, cutoff=linvar([850, 1250],32), decay=1.2, rel=n4.dur*0.5, amp=1, fold=(0, 0.3), vol=0.5).penta()
n5 >> ebass([1,0,0,0], dur=[1/2,1/2,1,1], oct=(3, 4, 5), pick=(0.2,0.5,0.7), cutoff=linvar([250, 1250],32), decay=1.2, rel=n4.dur*0.1, amp=1, fold=(0,0.3,0.2), vol=0.4).penta()
n6 >> click(PWhite(-0.1, 0.1),dur=b8.dur, hpf=var([200, 3200], [4, 4]), oct=(3, 4), hpr=0.2, shape=(1,0.5), amp=n4.degree == 0).unison(0)
n4.shape=0
n4.pick=[0.8, 0.2, 0.2]
n7 >> play("b...", sample=4, vol=0.7, cut=2)
n6 >> play("(K...)(K...)..", dur=1/2, sample=(0,9), cut=PWhite(0.5,5), vol=0.8, fx1=1)
n8 >> play("(O...)(O...)..", dur=1/2, sample=(8), cut=PWhite(0.5,5), vol=0.7)
n9 >> lapin((0,4), amp=var([0, 1], [PRand(8,16),PRand(1,8)]), dur=PDur(var([4,P*[6,5,7]],[6,2]),8), sus=1/8, oct=(5,6), rate=0.8, shape=0.2, fx1=0, fx2=1, drive=0.8, tanh=0).unison(3,0.25,90)
n0 >> ebass([1,0,0,0,0], dur=[1/2,1/2,1,1], oct=(4), lofi=var([0, 0.01], 8), pick=0.2, cutoff=linvar([850, 1250],32), decay=0.6, rel=n4.dur*0.5, amp=1, fold=(0, 0.14), smooth=0.1, lofiwow=1, vol=0.3, tanh=0.2).penta()


�K/e�C2�]�(hh�X�  c1 >> sawbass([3, (3, [4, 3])], dur=1/2, oct=(4, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=[0.5, 0.1], lpf=1600, bpf=linvar([200, 1600, 32], [16, 8, 32]), shape=PTri(0, 0), high=1, mid=4, low=0.1, vol=0.8).unison(2)
c2 >> blip(var([(3, (3, 8)),3, PCoin(3, 4, 0.5), linvar([4, var([4.01, 4])]), [var([1, 7]), 4, 4, 4, 4]], [4]), rate=2, oct=(PStep(3, 4, 5), var([3, 4])), scale=Scale.chromatic, dur=[1/2], vol=0.5, fold=0.5, leg=var([0, c1.drive], [3, 1], echo=[0, 0.1], feed=0), sus=[1/4, 1/2], lpf=1200).unison(4)
c3 >> sawbass([3, (3, [4, var([3, 14], [15, 1])])], slide=c1.degree == 15,dur=[1/2, 1/2, 1], oct=(4, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=var([[0.5, 0.1], [4, 5]], [48, 16]), lpf=(1/c1.drive) * 800, bpf=linvar([200, 3200, 32], [16, 8, 32]), shape=PTri(0, 1), high=1, mid=8, low=0.1, vol=0.5, chop=0).unison(8)
c4 >> keys([3, (3, [4, var([3, 14], [15, 1])])], slide=c1.degree == 15,dur=[2, 1/2, 1, 1/2], oct=(7, var([5, 6], [24, 8]), linvar([5.99, 6.01])), scale=Scale.chromatic, drive=0, lpf=0, bpf=linvar([2000, 6200, 32], [16, 8, 32]), shape=0, high=0, mid=0.1, low=0.1, vol=0.8, chop=0).unison(8)

�K0euu.