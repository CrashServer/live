
z2 >> four((var(PRand(-4,2),8),var(PRand(8),4)), dur=PDur(var([3,5,9],8),11), atk=[0.01,PWhite(0.01,0.03)], oct=(5), fx2=0.5, hpf=120, triode=1, krush=0.2, amp=PStrum()*0.2, kutoff=PRand(400,8400), scale=Scale.yu).sometimes("stutter", 1,oct=(5), drive=PWhite(0.2,0.4), dur=PRand(1,3)).unison(3)
a2.formant=0
a1 >> faim([0, 0, 2, [4, 0, 7]], scale=Scale.harmonicMinor, oct=(3,4), fx1=1, beef=[1,[1,0]], dur=var([PStep(8,2,1/4),PDur(var(PRand(8),8),8,PRand(8))],[[14,6],2]), drive=(0,0.05), amp=P[PWhite(1,1.2), PWhite(0.2,0.7), PWhite(0.5,var([0.7,1],16)), PWhite(0.2,0.5)]).every(6, "stutter", PRand([2,3]), oct=5, delay=0.25, glide=0.3, amp=PWhite(0,0.5)/(1+a2.formant), formant=[0,PWhite(1,6)], room2=0.7, mix2=0.4) + var([0,P*[1,-1,2,-2]],[7,1])

a2 >> play("v(...v.)(.[.v])(.{v.})".replace("v","W"), sample=0, amp=P[1,(a1.amp<0.5)]*0.8, dur=1/2)
a3 >> play("<{Dd}><h>", sample=(1,5), dur=1/4, rate=(PWhite(1,3)), amp=a1.amp > 0.88, hpf=340, pan=(0,PWhite(-1,1))).sometimes("stutter", PRand(4), amp=1)

a4 >> klank([0, 0, 2, [4, 0, 7]], scale=Scale.harmonicMinor, oct=(PStep(7, [4, 3, 3, 3, 4],[3, 3, 5, 3, 6])), fx1=1, beef=[1,[1,0]], dur=var([PStep(8,2,1/4),PDur(var(PRand(8),8),8,PRand(8))],[[14,6],2]), drive=(0,0.05), amp=P[PWhite(1,1.2), PWhite(0.2,0.7), PWhite(0.5,var([0.7,1],16)), PWhite(0.2,0.5)]).every(6, "stutter", PRand([2,3]), oct=5, delay=0.25, glide=0.3, amp=PWhite(0,0.5)/(1+a2.formant), formant=[0,PWhite(1,6)], room2=0.7, mix2=0.4) + var([0,P*[1,-1,2,-2]],[7,1]) + var([0, PWalk(8, 1, 1)], [21, 3])


d3 >> play("[x-].o.", dur=var(PRand([4,3,2,1,1/2,1/4,1/8]),P*[4,2,1,1/2]), sample=(7,8), lpf=50, amp=2)
d5 >> play("<W.[.W].><.q>", sample=(0,2), amp=P(0.5,1), cut=PWhite(0.1,1.2), lpf=8080).sometimes("stutter", PRand(2), rate=PWhite(1,4), amp=0.4, pan=PWhite(-1,1), fx1=1, comp=0.2)

