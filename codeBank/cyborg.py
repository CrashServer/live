# cyborg
o4 >> splitter("cyborg8", sample=2, dur=4, pos=PWhite(0,1), rd=PWhite(0,0.8), sus=8, hpf=4000)
o5 >> splitter("cyborg8", sample=3, delay=2, dur=4, pos=0, rd=0, sus=4, hpf=2000)

k3 >> play("(Cc)", dur=12, delay=3, rate=PwRand([-1, 1], [1, 9]), room=0.4, mix=0.2, sample=PRand(2) + 2).often("stutter", leg=PWhite(50,128), slide=PWhite(0.9, 1.1), echo=PwRand([0, 1], [8, 2]), pan=(-1,1))
d5 >> play("..w.", sample=2, hpf=20).sometimes("stutter", leg=PWhite(50,128), slide=PWhite(0.2, -.02), rate=PWhite(0.4,1), echo=PwRand([0, 1, 0.25], [8, 2, 1]))
d6 >> play("...w.", sample=6, hpf=10).often("stutter", leg=PWhite(50,128), slide=PWhite(0.9, 1.1), echo=PwRand([0, 1], [8, 2]), pan=(-1,1))

ji >> faim(P[0, 2, 4, 4, 2, 7], hpf=400, amp=1, room=1, fx2=var([0, 0.01]), mix=0.1+jj.degree*0.05, leg=(0, PWhite(0,4)), bend=(ji.dur==1)*PWhite(0.1,0.4), rate=8, lpf=PRand([400,7000]), lpr=PWhite(0.2,0.7), oct=4, dur=P[rest(1), 1/2, 1, 1/2, 1/2], pan=PSine(32)*PSine(13)).sometimes("dur.shuffle")

jn >> faim(ji.degree, leg=0, oct=4, hpf=530, sus=P[1, 1/4, 1/2, 1/2, 2], dur=P[rest(12), 1/4, 1/4, 1/4, 1/4], fx2=1, formant=0.0,room=1, mix=ji.bend * 0.5).unison(2).often("stutter", leg=PWhite(50,128), slide=PWhite(0.9, 1.1), echo=PwRand([0, 1], [8, 2])).unison(2) + var([0, PRand(-2, 2)])

o7 >> loop("ambi8", dur=[16,32], sample=2, lpf=linvar([3000,9000],[128]), lpr=0.4, echo=0.75, hpf=300, echomix=4, shape=0, amplify=var([0.6,0],[16,32]), room=1, mix=0.2, flanger=0.7)

o9 >> play(".(.o)(O.).", crush=linvar([0, 4], [8]), hpf=linvar([400, 4000], [128])).every(4, "stutter")

d4 >> play("tm", sample=0, hpf=400, lpf=8800, amplify=PRand([0,1]), cut=1/PWhite(0.1,0.9), pan=[-1,1], mix=0.2, room=1, delay=0)