# connect
a = 512
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