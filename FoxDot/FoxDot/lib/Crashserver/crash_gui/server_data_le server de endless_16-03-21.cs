��s      }�(�server_data�}�(�lieu��le server de endless��tmps��16��lang��fr��voice��0��	bpm_intro��48��scale_intro��minor��
root_intro��E��video�K�adresse��192.168.0.18�u�attack_data�}�(�connect�]�(�Crash Server���Welcome CrAsh ServEr
C0nnect_the_S&rV3r
 -- StageLimiter : Active
 -- Carla : Active
 -- Record : Active
 -- Biniou : Active











































���Clock.set_time(0)
print_synth()
print_fx()
print_sample()
print_loops()

i3 >> sos(dur=8, lpf=linvar([60,4800],[tmps*1.5, tmps*3]), hpf=expvar([0,500],[tmps*6, tmps*2]))

































�K e�init�]�(� ��


























��
























�Ke�
aspiration�]�(�
Aspiration��-












































�X�  Master().reset()
Root.default="E"
Clock.bpm = 92

lininf(96, 112, 256)

a4 >> splitter("os32", dur=8, sus=a4.dur*1.5, rd=PWhite(-0.25,0.25), pos=PWhite(0,0.25), amp=0.3, rate=PWhite(-1,4), lpf=PRand(1789,16128))

a2 >> faim(0, oct=(3,4), fx1=1, beef=[1,[1,0]], dur=var([PStep(8,2,1/4),PDur(var(PRand(8),8),8,PRand(8))],[[14,6],2]), drive=(0,0.05), amp=P[PWhite(1,1.2), PWhite(0.2,0.7), PWhite(0.5,var([0.7,1],16)), PWhite(0.2,0.5)]).every(6, "stutter", PRand([2,3]), oct=5, delay=0.25, glide=0.3, amp=PWhite(0,0.5)/(1+a2.formant), formant=[0,PWhite(1,6)], room2=0.7, mix2=0.4) + var([0,P*[1,-1,2,-2]],[7,1])

d1 >> play("v(...v.)(.[.v])(.{v.})".replace("v","W"), sample=0, amp=P[1,(a2.amp<0.5)]*0.8, dur=1/2)
d2 >> play("<{Dd}><h>", sample=(1,5), dur=1/4, rate=(PWhite(1,3)), amp=a2.amp > 0.88, hpf=340, pan=(0,PWhite(-1,1))).sometimes("stutter", PRand(4), amp=1)
d3 >> play("[x-].o.", dur=var(PRand([4,3,2,1,1/2,1/4,1/8]),P*[4,2,1,1/2]), sample=(7,8), lpf=50, amp=1)

d5 >> play("<W.[.W].><.q>", sample=(0,2), amp=P(0.5,1), cut=PWhite(0.1,1.2), lpf=8080).sometimes("stutter", PRand(2), rate=PWhite(1,4), amp=0.4, pan=PWhite(-1,1), fx1=1, comp=0.2)
d6 >> play("<P.[Tt].><.Tq><..J.>", delay=var([0.125, 0], [PRand([7, 5]), 22]), hpf=0, dur=1, rate=[8, 4], echo=0.125, fold=PBern(16), echomix=0.3, amp=PBern(16) , crush=4, sample=PRand(8))
d7 >> play("<..{uuu|r5|}.>", sample=2, amp=1).sometimes("stutter", PRand(8,32), hpf=400)

drop(1, 1)

v9 >> splaffer("cyber", sample=2, dur=1/2, fmod=[0,2,3], pos=0, amp=0.3, rate=8, cut=0, crush=0, bits=0)

z1 >> klank(Scale.yu[0:12].trim(P[1:10]).every(4, "shuffle").arp([0, 2]), dur=PMorse("cable de serveur"), rate=1, oct=(3, PStep(3, 4, 5), 5), chop=4, chopwave=PRand(4), fx2=1, hpf=4000, amp=PBern(16)/4, shift=linvar([1, 12])).unison(4)

z2 >> four((var(PRand(-4,2),8),var(PRand(8),4)), dur=PDur(var([3,5,9],8),11), atk=[0.01,PWhite(0.01,0.03)], oct=(5), fx2=0.5, hpf=120, triode=1, krush=0.2, amp=PStrum()*0.2, kutoff=PRand(400,8400), scale=Scale.yu).sometimes("stutter", 1,oct=(5), drive=PWhite(0.2,0.4), dur=PRand(1,3)).unison(3)

z_all.solo(1)

Master().leg=lininf(0, 256, 32)

v_all.solo(0)
z_all.solo(0)
z_all.amp=0
v_all.amp=0




































�Ke�	attention�]�(�	Attention��!
































�X�
  Root.default = linvar([0, 4, 2, PRand(2)], [PRand([4, 8, 12, 16])])
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

d1 >> play("<X(..{XxK.})X(..X)(X.)>", sample=2, lpf=linvar([500,1500],[32,7]), lpr=PWhite(0.3,1), amp=0.3).every(PRand(1,9), "stutter", PRand([6,8,12,16]), rate=PWhite(1,1.125), pan=[-1,1], bpf=1500, drive=0.2)

r3 >> dbass(PSine(64)*0.3, root=0, dur=PDur(6,11), amplify=0.8*(d1.degree!="X"), leg=PRand(24), sus=1, oct=5, lpf=13000, fx1=lininf(0, 2, 384), hpf=60).unison(3)
d1 >> play("<X(.....{X[XX]xv})><..O.><|x4|.>", amp=0.2, lpf=8000)
d2 >> play("<[-{---[--]|:4|}]><.:>", sample=7, amp=0.5, lpf=0 ,pan=PWhite(-0.5,0.5), rate=PWhite(0.99,1.01)).human(80,3,4).sometimes("stutter", PRand(4))

r4 >> sawbass(r1.degree, dur=[6,2], oct=(4,[5,[6,7]]), leg=16, bend=([4,5],[3,2]), benddelay=([0.85,0.95,0.75],[0.65,1,0.35]), shape=PWhite(0,0.5), cutoff=linvar([2500,6000],24), hpf=50, chop=var([0,4],[[6,14,2],[2,4]])).unison(3, 0.25, 80)

d1 >> play("<X(.....{X[XX]xv})><..O.><|x4|.>", amp=0.2, lpf=8000)
d2 >> play("<[-{---[--]|:4|}]><.:>", sample=7, amp=0.5, lpf=0 ,pan=PWhite(-0.5,0.5), rate=PWhite(0.99,1.01)).human(80,3,4).sometimes("stutter", PRand(4))




















�Ke�	corrosion�]�(�	Corrosion��
























�X/  s3 >> star([0, 3, [3, 7], 0.5, PRand([3, 7, 0, (0.5, 3, 0)])], crush=linvar([128, 0], [16, inf], start=now),dur=1/8, oct=6, scale=Scale.locrianMajor, formant=PRand([0, 4]), amp=0.5) + Pvar([0, 3, 0, 0, 2, 0], [4, 2])
f1 >> faim(PArp([0,1,0.5],11), oct=(3, 4), dur=1/4, lpf=200)

























�Ke�
absolution�]�(�
Absolution��












�X  Clock.bpm = linvar([120,150,120,60],[PRand([4, 8, 16, 2])])
p5 >> pianovel(Pvar([Scale.major, Scale.minor, Scale.locrian]).palindrome(), flanger=PWhite(0, 0.1), oct=P[3:7], lpf=Clock.bpm * 10, delay=(0, 0.5, 0.05), sus=PWhite(0.5,1.2), velocity=PWhite(40,80))











�Ke�annihilation�]�(�Annihilation��















�Xi  j1 >> play("j", sample=PRand(16), room=1, mix=0.5, amp=1, rate=(PSine(16)/100,-0.25), echo=1, echotime=4, drive=PWhite(0,0.1), chop=PWhite(0,4), dur=16, spf=1900, spfslide=4, spfend=4000).spread()
k5 >> play(PEuclid2(3,8,"X","|=2|"), sample=1,rate=var([1,0.7],[16,2]),lpf=linvar([800,5800],[24,0]), triode=PRand(16), lpr=linvar([1,0.05],[24,0])).often("stutter", Cycle([2,3,12]), amp=1, hpf=1800).sometimes("amen")
k6 >> play("X(---=)", amp=2, sample=var([1, 2], [14, 2]))
k7 >> play("<V(-[VX])V-><--(pu)->", sample=3, amp=var([0, 1], [3, 5]), hpf=45).every(7, "stutter", Cycle([2, 3, 1, 2, 3, 4]))


















�Ke�random�]�(h�$random virus























��


















�Ke�42�]�(h�




























��























�Ke�43�]�(h�










��






�Ke�	desynchro�]�(�!emiT��





















��$clip.copy(random_bpm())












�Ke�sin�]�(�	-- Sin --��
















�X  s5 >> sawbass(PSine(64)*0.5, oct=(4,5,6), dur=1, amp=0.7, sus=0.5, rq=0.7, hpf=100, cutoff=linvar([100,4800],64)).offbeat(0.25).unison(4,0.125).every(32, "oct.offadd", 1, 0.25)
n3 >> play("x.", dur=1/2, sample=4, amp=2, amplify=1, room=linvar([0.1,1],[42,0]), mix=expvar([0,0.4],16))
h4 >> play("-[--]-", amplify=1, sample=4, dur=1/2, amp=PBern(16)).spread()
n4 >> play("<k ><..c.>", sample=(3,3), amp=(2.5,1), hpf=60, lpf=3600, lpr=linvar([0.5,0.1],34)).sometimes("stutter", Cycle([2,3,4]), rate=PWhite(-0.1,4), hpf=380)
















�K	e�nucleose�]�(�@ Nucleose @��
















�Xc  a1 >> play("<X[--]><..O.>", amp=4, room=0.7, mix=PRand([0,.4,0])).sometimes("stutter", PRand(8))
s1 >> saw((0,1), oct=(3,[4,5]), lpf=PRand(8800), lpr=PWhite(0.1,0.9), amp=[0,0.4,0], dur=var([4,1/4,2],16), chop=8, drive=0.2, slide=(PWhite(-2,2),PWhite(-1,1))).unison(16, analog=40)
b1 >> dbass(PArp([0,2,-2], 13), dur=1/4, lpf=8000).unison(3)













�Ke�gastro�]�(�Gastro��





















�XT  dd >> play(P["Xx.xx.xx.xx.xx.x"], sample=(0,7,4), krush=0).sometimes("stutter")
ch >> play("#", dur=8, pan=(-1,1), amp=1, rate=[1,-1])
sn >> play("<--o(-[--])>", krush=1, lpf=9900, lpr=PWhite(0.2,0.8), sample=2, pan=PWhite(-1,1))
tt >> play("<[tt]t.t>", sample=PRand(5), pan=PWhite(-1,1), amp=var([0,1],[13,32,48]), amplify=[2.5,PWhite(0.8,2)]).sometimes("trim",2)
fi >> faim(var([-2,0],32), oct=PStep([8,4],[4,2,2],3), dur=1/4, amplify=(dd.degree=="x")*PBern(16)) + var([0,PRand([-1,1,0.5])],[7,1])
kk >> klank(PRand(8), dur=8, rate=linvar([0,1],[128]), amplify=1).unison(3)




















�K
e�zika�]�(�Zika��

















�X  b2 >> dbass(p1.degree+PWhite(0,0.3), lpf=linvar([900,4500],24), dur=[1/2,1/4,1/2,1/4,1/2]).sometimes("dur.shuffle")
p1 >> prof(PSine(64)*0.2, oct=(var([(3,4),[5,6]],[6,2])), dur=PDur([5,7],8), sus=p1.dur*0.7, cutoff=7000, lforate=var([1,2,4],8), lfowidth=linvar([0.1,1],39), pan=[-1,1], amp=0.8)
n1 >> play("..I.", drive=(0,0.9), sample=1, rate=(PWhite(-1,4)), amp=PBern(16), pan=linvar([-1,1],24))
d4 >> play("x(---([::]:[::::]))", amp=1, sample=([0,1,2],[1,2,4])).sometimes("stutter")
d6 >> play("X ", amp=1)

















�Ke�syphy�]�(�//+ SYPHY +//��














�X�  sq >> squish(oct=(3,[4,5]), dur=P*[8,4,2,1,0.5,0.125], echo=sq.dur/PRand([4,2,8]), echotime=sq.echo*PRand([1,2,0.5]), rate=PStep(8,PRand(40),1), triode=0.8, leg=4, lpf=4800, lpr=0.2, room=0.8, mix=0.1, amplify=0.2*PBern(24)).unison(5,0.2,80)
dd >> play("p", dur=1/4, amplify=PTimebin(), sample=PRand(1,4), bpf=linvar([200,4000],32), bpr=1, pan=P*[-1,1])
ds >> play("..O.", lpf=7800, shape=0.1, cut=1/2, sample=6, pan=(0.2,-0.2))
hh >> play("[--]", sample=4, cut=1/P[1:8], pan=PWhite(-1,1), bpf=linvar([1200,8080],36), bpr=PWhite(0.1,0.9), bpnoise=PRand(4)).human(50,-4)
dk >> play("<X.>", triode=(0,8,PRand(8)), sample=(6,3,2), amp=(2,0.5,0.7), lpf=(4800,PRand(120,1450),0), pshift=(-12,0,PRand(12))).sometimes("stutter")











�Ke�slaap�]�(�!/// SLAAP - DARKWATER - REMIX ///��


















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













�Ke�
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


�Ke�--- SECOND PARTS ---�]�(h�


��


�Ke�glitch�]�(h�

















���c1 >> glitcher(oct=PRand(8), rate=PWhite(1, 128), amp=1, dur=8, len=PWhite(1, 16), henA=PWhite(0.01, 4), fmod=0, henB=PWhite(0.1, 0.2), t=[2, 4, 6, 8, 32], crush=PRand(16),bits=16, shape=4.0).unison(2)














�Ke�consolation�]�(�? Consolation ?��













�X�  Clock.bpm = 120
Root.default=12
var.cho = var(PMarkov(I),8)

t9 >> tb303(PArp(var.cho,5), oct=3, dur=1/4, top=linvar([200,10000],128), cutoff=linvar([500,2000],[PRand(24,36),PRand(2,12)]), rq=PWhite(0.1,0.3), sus=PStep(PRand(4,16)[:16],0.5,0.25), amp=0.35, lpf=9000, fx2=0).unison(3)
t9.lpf=linvar([20, 6000],[256, inf], start=now)
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.4, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)

d1 >> play("x.", feedfreq=[[0,PRand(500)],0], hpf=30, sample=4, amp=0.2, tanh=2, chop=1)
d1.feed=var(P*[0,0.125,0.25,0.5],16)

d7 >> play(P["x-(-m)"][:8].rotate(var([1,3])), rate=1.5, dur=1/4,amplify=0.8, delay=var([0,(0,0.75)],PRand(8)),sample=1)



















�Ke�
snowdation�]�(�:: snowdation ::��







�X   Clock.bpm = 133;

a2 >> sine((0, 2), sinefb=linvar([0, 1.0], 128), amp=0.5, delay=0.5, oct=3, sus=2, hpf=200, pan=linvar([-1, 1], 128))
a4 >> sine((0, 2), sinefb=linvar([0, 0.5], 196), amp=0.3, delay=1, oct=3, sus=1, hpf=400, pan=linvar([1, -1], 128))
a1 >> play("U", dur=16, rate=[0.9, 1.1], sample=PRand([4, 5, 6, 7, 8, 9]), shape=0.1, feed=0.4).unison(2)
d8 >> play("p ", sample=4, rate=0.25, dur=16, delay=2, amp=4, echo=0.25, echotime=4)
d6 >> play("  c ", dur=8, amp=0.7, echo=0.5, room=1, mix=0.5)







�Ke�tabation�]�(�Tabation��


�XO  cl >> click(0, dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), hpf=40, drive=[PWhite(0.4,0.8),0.2], oct=(3, PStep(9,5,4)), octer=1, octersub=2, octersubsub=var([2, PRand(15,2222)], [15, 1]), triode=4, amp=0.1, amplify=1).unison(3).rarely("stutter",PRand(6), oct=6, pan=[-1,1], mpf=2860, hpf=400)
db >> bass(0, dur=c1.dur, leg=12, amp=var([0.5, 0], [12, 4]), rate=PWhite(0.01, 0.2), sus=db.dur*1.5).unison(2)
n1 >> play("<u><t>", sample=(2,P[0:5]), delay=(0,(0,[0,0.25])), dur=cl.dur, crush=[0,0,0,PRand(8)], bits=4, lpf=n1.crush*1500)
















































�Ke�
augmendrum�]�(�
Augmendrum��




�Xf  h1 >> play("h", dur=PDur(var([7,8,4],[8,2,2]),8)/var([1,[2,4]],16), sample=PStep(8,1,3), rate=PWhite(1,4), amp=PWhite(0.0, 0.5), pan=PWhite(-1,1)).degrade(0.2)

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




�Ke�augmen2�]�(�augmen2��



�XE  b1 >> faim(var([-2,0],8), dur=1/4, oct=3, krush=[3,PWhite(0,3)], kutoff=linvar([400,9900],[29,11])) + var([0,P*[1,-1,2,-2]],[7,1])
b2 >> faim([3,PRand(7)], dur=PDur(9,11), oct=[[5,6],4], room=0.7, mix=0.3, krush=1.8, amp=PStrum(), kutoff=PRand(400,8400), amplify=var([[1,0,1],0],[16,8])).sometimes("stutter", drive=0.2).unison(4).penta()

sw >> pasha(b2.degree + (0,var(P*[6,3,2],4),4), amplify=[1,b2.amp>0.5], dur=PDur(7,9,2,var(P*[0.25,0.5,1],[6,2,4])), leg=PWhite(0,2), glide=PWhite(0.2,2), swell=0.4, sus=sw.dur*PWhite(0.1,0.9), oct=[5,6], room=1, mix=0.3).unison(4,0.125)




�Ke�
aspirateur�]�(�
aspirateur��


�X�  d1 >> play("<X[--]><..O.>", sample=0, amp=4, room=0.7, mix=PRand([0,.4,0])).sometimes("stutter", PRand(8))
sa >> saw((0,1), oct=(3,[4,5]), lpf=PRand(8800), lpr=PWhite(0.1,0.9), amp=[0,0.4,0], dur=var([4,1/4,2],16), chop=8, drive=0.2, slide=(PWhite(-2,2),PWhite(-1,1))).unison(16, analog=40)
b3 >> dbass(PArp([0,2,-2], 13), dur=1/4, lpf=8000).unison(3)
f1 >> feel([(2, 9, 14), (2, 9, 14, 33), (2, 9, 14, 26, 33), (2, 9, 14, 26, 34), (2, 9, 14, 24, 33), (4)], scale=Scale.chromatic)


�Ke�	suddation�]�(�	Suddation��



�Xh  Clock.bpm=90
Scale.default="minor"

a1 >> sinepad((0,4), formant=PRand(6), flanger=expvar([0.1,0.4],3489), fdecay=linvar([0.4,2],1248), drive=0.1, oct=(3,4,5), dur=8, room=1, mix=0.7, amp=2, chop=1.6, chopwave=PRand(8)).spread()
w2 >> sawbass(PWhite(0,0.3), dur=PDur(var([5,7],[6,2]),8,3), cutoff=PRand(190,1580), oct=(4,5,[6,7]), amp=1)

d1 >> play("V ", dur=4, lpf=0, room=1, mix=0.7, rate=0.7, sample=2, amp=1, pan=(-1,1), octafuz=expvar([0,1],[64,0]), octamix=linvar([0,1],[64,0]))
d4 >> play("r r r [rr] r ", dur=1/4, rate=PRand(2,7), pan=[-1,0.5,0,-0.5,1], formant=0, sample=3)

d6 >> play("..o.", lpf=4000, crush=5, room=1, mix=[0,0.2,0.4], delay=PWhite(-0.1,0.1)).often("stutter", Cycle([2,4,3,6,5,2]), amp=PWhite(0.5,1.1), rate=PWhite(1,2))
d5 >> play("..t.", rate=(1,3))
d3 >> play("..(.z).", shape=0.7, cut=1/2, rate=(1.3,.7), disto=1, pshift=(linvar([0,12],265),0,-12), delay=0.7)

a1 >> bell((0,4), formant=PRand(6), flanger=0, fdecay=linvar([0.4,2],1248), drive=0, oct=(3,4,5), dur=8, room=1, mix=0.7, amp=1, chop=8, chopwave=PRand(8)).spread() + (0,var([-2,-4,-3,-1],8))
y1 >> pasha(a1.degree, oct=(4,5), dur=PDur(var([2,3,4,5],[5,1,1,1]),8), amp=0.3, sus=y1.dur*PWhite(0.5,1.2), echo=var([0.5,[0.125,0.25,0.75]],[6,2]))

k1 >> play("<X.><..o.><..U(.(...O))><[---]><(.:))><[++]>", lpf=0, amp=3)

drop(14,4,4)
w2.cutoff=P[190,linvar([1580,11800],[64,0], start=now)]




�Ke�deambulation�]�(�deambulation��

�X�  Clock.bpm=92
Scale.default="minor"

d1 >> play(PEuclid2(var([3,4],[24,8]),8,"(vv{v@})","(-|=2|)"), dur=1, drive=P*[0,expvar([0.01,0.9],26)], lpf=linvar([800,7800],[64,0]), lpr=linvar([1,0.05],61)).often("stutter", Cycle([2,3,6,12]), pan=PWhite(-1,1))
b1 >> dbass(var([0,[-4,2,-2]],[14,2]), dur=P*[2,6],amp=(d1.degree!="v")*0.8, lpf=linvar([1800,3500],19), lpr=expvar([1,0.2],17), sus=b1.dur*PWhite(0.8,2),fx1=1, fx2=0.0, rate=linvar([0.1,15],23), oct=(PStep(7,6,5),4,PStep(4,6,5))).unison(3)
d2 >> play("<X ><(-[--]-[::])><..|*2|.><..C.>", bits=16, amp=1, dur=2, crush=3, room1=1, mix=PWhite(0,0.5)).rarely("amen").sometimes("stutter", PRand(1,6), rate=PRand([1,6]))

s1 >> sitar(P[0,5,P*[7,8,4],3], oct=P*[5,[6,4,3]], vib=PWhite(6,32), slide=0.01, slidedelay=PWhite(0.2,0.9), sus=s1.dur*PWhite(0.3,0.8), dur=1/4, room=1, mix=PWhite(0,0.2), amp=var([(d1.degree=="@"), (d1.degree!="@")],[28,4]), drive=(0,0.1), fx2=1).spread() + [0,0,P*[2,4],0]


�Ke�	oxydation�]�(�	oxydation��

�X�  Root.default='C'
Scale.default="yu"
Clock.bpm = 78

f1 >> pluck(var(PChords(),8), dur=PRand(1,8)/PRand(1,4), blur=PWhite(1,4), decay=PRand(1,4), oct=(3,4,PStep(7,6,5)), drive=PWhite(0,0.1), sus=PRand(1,16), atk=PStep(8,0.2,PRand(1,6)), room2=1, mix2=0.6, damp2=PWhite(0.1,0.5), revatk=PWhite(0.2,2), revsus=PWhite(1,4), hpf=160, lpf=PRand(1800,9065), amp=0.3).unison(4,0.25)
jb >> jbass([f1.degree[0],f1.degree[2]], dur=[6,2], amp=1, oct=[5,6,5], glide=P[0:8]*PRand([-1,0,1]), glidedelay=PWhite(0.7,0.99), shape=[0,PWhite(0,1),0.2,0,0.3], echo=(jb.shape>0)*jb.dur/PWhite(0.1,4), echotime=jb.degree, lpf=[4500,5500+jb.shape*1000], hpf=60).every(6, "unison", cycle=[0,4])

d3 >> play("(#....)..(...~)", rate=PWhite(-1,4)*0.25).unison(3, 1,99)
d2 >> play("<(v...)(v..(.v))(...(.v))(..v.)><(.{rR.})...><-(...-)><.(.%.).><...(.(.:))>", dur=1/2, sample=([9,2],5,0,PRand(8),3), room=1, mix=(0,PWhite(0.2,0.6),PWhite(0.1,0.3),0.3,0.3), pan=(0,-0.2,(-1,1),PWhite(-0.3,0.3),0.3)).human(20,5,0).often("stutter", PRand(8).rnd(2), rate=[1,PRand(1,6)])
d1 >> play("<x.(...(.x))><..(**.*).><..(.((CCC.).)..)><(-.)->", sample=4, amp=var([1,0,1],[13,1,1]), crush=PRand(8), dur=1/2).sometimes("stutter", PRand(16))

p1 >> blip(f1.degree[0] + (0,[2,4]), dur=[1/2,1/2,1/2,P*[0.5,rest(2.5)]], amp=(b1.sus<6 and (d2.degree[0]!="v")), amplify=d1.degree[1]!="*", oct=(5), rate=PRand(1,4), leg=PRand(0,8),glide=0.5, fmod=4, vib=PRand(2,16), sus=PWhite(0.5,1), echo=[0,0.25], lpf=PRand(400,12888), room=1, mix=PWhite(0,0.5)).unison(3).every(8, "mirror")
b1 >> sawbass(f1.degree[0], dur=8, sus=[8,PRand(1,8)], echo=1/2, mid=2, echotime=PRand(0,12), oct=(5,4,5), drive=(0.01,0,0.01)).unison(3,var(PWhite(0.25,0.30)),var(PRand(99),8))

x1 >> play("<X-><..o.>")

�Ke�mmxx�]�(�MMXX��

�Xn	  Master().reset()
Clock.bpm=113
Root.default = 1
Scale.default= Pvar([Scale.major, Scale.justMajor],PRand([4, 8, 16,32]))

b1 >> varsaw((var([0,-2,-4],16),[1,2,1],var(PRand([5,6,2,4,7],8))), sus=10, lpf=linvar([3000, 6700], 128), lpr=PWhite(0.2,0.9), blur=2, amp=0.4, dur=var([5, 1, 1], [6, 1, 1]), oct=PStep(6, 6, 4), fx2=1, fx2hpf=300, fx2lpf=7800, fold=0.0, output=8).unison(3) + var([0, 4, 8], [6, 1, 1])

b2 >> varsaw((var([0,-2,-4],16),[1,2,1],var(PRand([5,6,2,4,7],8))), sus=1, spfslide=1, spfend=6000, spf=10, lpf=6000, lpr=PWhite(0.2,0.9), blur=2, amp=0.3, dur=var([4, 1/4, 8], [2, 2, 1]), oct=PStep(4,5,3), fx2=1, fold=0.5, output=10,bpm = 80 + PWhite(-20, 20)).unison(4) + var(PRand([0, 4, 8, -4, 6, -3]), [6, 1, 1])

e1 >> klank(b1.degree[0], fx2=1, rate=linvar([8, 16], 64), oct=(3, 5), dur=P*[4, 8, 12], lpf=linvar([400,4800],128), lpr=0.05, amp=0.5, output=12,bpm = 80 + PWhite(-20, 20))

e2 >> klank(b1.degree[1] + var([0, -2, -4, 6]), dur=1, rate=4, oct=var([(5, 6), (4, 7)], 4), lpf=linvar([400,4800],128), hpf=2000, drive=0.0,lpr=0.7, chop=8, chopmix=0.25, lofi=linvar([0.1, 0.5], 32), amp=1, output=14,bpm = 80 + PWhite(-20, 20)).unison(2)

p1 >> pianovel(P*[b1.degree[0],b1.degree[1],b4.degree[2], (b1.degree[0], b1.degree[1]), (b1.degree[1], b1.degree[2]), (b1.degree[0], b1.degree[2]),P**(b1.degree[0], b1.degree[1], b1.degree[2]),P+(b1.degree[0], b1.degree[1], b1.degree[2]), P/(b1.degree[0], b1.degree[1], b1.degree[2])], dur=P*[5,1,1/2,8,3], sus = p1.dur*PWhite(1,1.5), delay=P*[0,PWhite(0,1)], oct=PwRand([6,5,4,3],[30,35,20,15]), velocity=PRand(40,65), fx2=1, amp=PWhite(0.6,0.8), velhard=PWhite(0.2,1), hard=PWhite(0,2), lpf=PRand(5000,18000), output=16).unison(3).penta()

z1 >> total(b1.degree[0],dur=16, amp=[1,PWhite(0,0.5)], fmod=PRand([16, 32, 64, 128]), fx1=0, bpf=PRand(800,4000), bpr=0.1, vib=PRand(16), spin=PWhite(-1,1), output=18).slider()

y4 >> subbass(p1.degree, dur=16, output=6, amp=0.4, crush=(0,PRand(0,4)), bits=PRand(4,16), fx1=1, atk=PWhite(0.005,0.1), oct=(4,5)).unison(3)
y5 >> faim(y4.degree[0], oct=(4,5), dur=[15,1], amp=0.5, fx1=1, delay=PWhite(-1,1).rnd(0.25), echo=[0,P[0,0.25,0.5,0.75]], comp=0.6, output=22)

g1 >> play("G", dur=PRand(32), crush=PRand(16), bits=PRand(4,16), sample=PRand(2020), amp=0.8, output=4)

Scale.default= Pvar([Scale.major, Scale.justMajor, Scale.minor, Scale.justMinor],PRand([4, 8, 16,32]))
Clock.bpm = sinvar([113, 40], 128)

�Ke�endless�]�(�endless�X�  A l'aube d'une ère d'aliénation technologique, les serveurs ont pris le contrôle de la quasi totalité des données humaines.
Identités. Modes de pensée. ADN.
L'humanité semble à la merci de ces forces impalpables, et pourtant un duo de machinistes informatiques livre un combat sans fin contre le méta cerveau central. 
Leur spécialité: surchauffer et faire abdiquer les serveurs audio.
On les appelle, les CRASH SERVER. 
Voici leur histoire. 









�XV  Root.default = -4

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









�Ke�intervention�]�(�intervention��
�X  y1 >> pbass(5, oct=(3,4), dur=8, echo=0.25, echotime=PRand(7,10), drive=0.5, room=1).unison(3)
d9 >> play("k.", dur=[4,1/4,1/4,1/2,1,1/2,1], sample=(0,5)).sometimes("stutter", 3)
d8 >> play("d+d", sample=[2,1], dur=PDur(5,8,2)*2, room=PWhite(0.5,1), mix=0.4)
�Keuu.