# DDOS 92
# reisub

Root.default="E"
Scale.default="minor"
Clock.bpm = lininf(96, 112, 256)

a2 >> faim(0, oct=(3,4), beef=1, fx1=[0,1], dur=var([PStep(8,2,1/4),PDur(var(PRand(8),8),8,PRand(8))],[[14,6],2]), drive=(0,0.05), amp=P[PWhite(1,1.2), PWhite(0.2,0.7), PWhite(0.5,var([0.7,1],16)), PWhite(0.2,0.5)]/0.7).every(6, "stutter", PRand([2,3]), oct=5, delay=0.25, glide=0.3, amp=PWhite(0,0.5)/(1+a2.formant), formant=[0,PWhite(1,6)], room2=0.7, mix2=0.4).penta() + var([0,P*[1,-1,2,-2]],[7,1])
d1 >> play("v(...v.)(.[.v])(.{v.})".replace("v","W"), sample=0, amp=1, dur=1/2)
d1 >> play("<k><@>", sample=(0,1), dur=1/4, amp=a2.amp > 1, hpf=40)
d3 >> play("--", dur=var(PRand([4,3,2,1,1/2,1/4,1/8]),P*[4,2,1,1/2]), sample=(7,8), lpf=0, amp=1)
x3 >> splitter("cindrum16", sample=5, dur=1/4, sus=PWhite(1/4,1/2), rd=[0,PWhite(0.5)], amp=(a2.amp<(linvar([1,2],[32,0])))/3, room2=1, rate=4, pan=(PWhite(0.5,0.6),PWhite(-0.9,-1)))
x4 >> play("n", sample=PRand(88), amp=2, rate=PWhite(1, 4), pan=PWhite(-1,1), lpf=PRand(5050,9090)).fill()
t1 >> twang(hpf=PWhite(1500, 1900), amp=var([1, 0],[4, 16]), dur=var([1, 1/2], [38, 6]), rate=1.1,spin=linvar([0, 1], [56]), leg=PRand(4, 32), echo=PRand([0, 0, 0, 0.25]))

d5 >> play("<W.[.W].><.q><..{uNNn[NNNNNN]}.>", sample=(2,2,PRand(88)), amp=P(0.5,1), cut=PWhite(0.1,1.2), lpf=8080, output=4).sometimes("stutter", PRand(8,32), rate=PWhite(1,4), amp=1.5, pan=PWhite(-1,1), fx1=1, comp=0.2)

d6 >> play("<P.[Tt].><.Tq><..J.>", delay=var([0.125, 0], [PRand([7, 5]), 22]), hpf=0, dur=1, rate=[8, 4], echo=0.125, fold=PBern(16), echomix=0.3, amp=PBern(16) , crush=4, sample=PRand(8))

d7 >> play("<..{u}.>", sample=2,amp=0.5).sometimes("stutter", PRand(8,32), hpf=400)

drop(1, 1)

v9 >> splaffer("cyber32", sample=2, dur=1/2, fmod=[0,2,3], pos=0, amp=1, rate=8, cut=0, crush=0, bits=0)

z1 >> klank(Scale.yu[0:12].trim(P[1:10]).every(4, "shuffle").arp([0, 2]), dur=PMorse("cable de serveur"), rate=1, oct=(3, PStep(3, 4, 5), 5), chop=4, chopwave=PRand(4), output=8, fx2=1, hpf=4000, amp=PBern(16)/4, shift=linvar([1, 12])).unison(4)
z2 >> four((var(PRand(-4,2),8),var(PRand(8),4)), dur=PDur(var([3,5,9],8),11), atk=[0.01,PWhite(0.01,0.03)], oct=(5), fx2=0.5, hpf=120, triode=1, krush=0.2, amp=PStrum()*0.2, kutoff=PRand(400,8400), output=8, scale=Scale.yu).sometimes("stutter", 1,oct=(5), drive=PWhite(0.2,0.4), dur=PRand(1,3)).unison(3)
z_all.solo(1)




