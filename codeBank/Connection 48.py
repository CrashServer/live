# Connection 48
# resiub

Clock.bpm = 48
Scale.default="locrian"
Root.default=4

a = 32
b = expinf(0, 0.5, a * 2)
i3 >> sos(dur=PRand(16), vib=PRand(10600), lpf=linvar([60,4800],[PRand(8,24), PRand(32,48)]), hpf=expvar([0,500],[PRand(64,96), PRand(8,32)]),fx1=b, fx2=b, output=4, shift=lininf(1, 2, a)).unison(3,0.75,99)

g1 >> play("g...", sample=0, vol=0.8, lpf=PWhite(200,8000), room=0.2, mix=PWhite(0.2,0.9), shape=(0,0.2), dur=2, output=6)
g2 >> play("g...", delay=4, echo=0.25, amp=0.2, sample=0, lpf=PWhite(200,8000), room2=1, mix2=PWhite(0.2,0.9), shape=(0,0.2), dur=2, output=6)
z4 >> play("E ", dur=16, sample=PRand(200), amp=2, output=22)
x2 >> play("x.-x..", echo=0.5, dur=1/2, shape=.4, rate=1, octafuz=linvar([0.3,1]), formant=var([1, 0,5]), fdist=1, output=10).every(3, "stutter")

i5 >> bbass(0, oct=(lininf(2, 3, a), lininf(2, 4, a)), output=18, dur=1/4, shape=0, shapemix=0.2, med=0, sus=1, blur=1, amp=1, fx1=b, fx2=b, vol=0.4).unison(3)
# z1 >> play("G", sample=PRand(200), dur=2, coarse=0, chop=P*[0,1,4],  chopmix=PWhite(0, 1), chopwave=PRand(8), echo=PwRand([0,PWhite(0, 1)],[50, 1]), shift=PWhite(0.5, 2), rate=PWhite(0.95, 1.05), crush=PWhite(0, 4),bits=PRand(8)+4, lofi=0, room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), formantmix=0.1, formant=PGauss(0, 1), revatk=PWhite(-1,2), pan=PWhite(-1,1), amp=2, output=24)

i6 >> abass(0, oct=(lininf(3, 4, a), lininf(4, 5, a)), lpf=400, output=16, dur=1/2, sus=1, delay=0.25, blur=1, amp=1, fx1=b, fx2=b, vol=0.4).unison(3)
z2 >> play("E", sample=PRand(200), dur=3, coarse=0, chop=P*[0,1,4],  chopmix=PWhite(0, 1), chopwave=PRand(8), echo=PwRand([0,PWhite(0, 1)],[50, 1]), shift=PWhite(0.5, 2), rate=PWhite(0.95, 1.05), crush=0,bits=PRand(8)+4, lofi=P*[0,PWhite(0,1)], room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1), amp=2, output=26)

i7 >> jbass(0, oct=(lininf(3, 5, a), lininf(4, 5, a)), output=14, dur=PDur(var(P[1:8],a/8), 8), sus=1, delay=0.25, blur=1, amp=1, fx1=b, fx2=b, vol=0.4).unison(3)
z3 >> play("{EG}", sample=PRand(200), dur=16, coarse=0, chop=P*[0,1,4],  chopmix=PWhite(0,1), chopwave=PRand(8), echo=PwRand([0,PWhite(0, 1)],[50, 1]), shift=PWhite(0.5, 2), rate=PWhite(0.95, 1.05), crush=0, bits=PRand(8)+4, lofi=PWhite(0,1), feed=0.5, room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1), output=28)

z_all.amp=PWhite(1,2)
   
z_all.solo(1)

#list des mots qui sont biens; 

voitxt = ["crash server","technology", "augmentation", "destruction", "aspiration", "mmxx", "virus", "network", "information", "evolution", "transformation", "reboot",  "dereliction", "alienation", "migration", "control", "identities", "human", "forces", "computer", "machinist", "endless", "battle", "metabrain", "overheating", "abdiction", "O S", "system", "processor", "digital", "social"]

lng = ['af', 'br', 'cr', 'cz', 'nl', 'en', 'ee', 'fr', 'de', 'gr', 'hu', 'id', 'it', 'la', 'ic', 'mx', 'ir', 'pl', 'pt', 'ro', 'es', 'sw', 'tr', 'us', 'vz']

Clock.every(4, lambda: voicegen())

def voicegen():
    Voice(choice(voitxt) + " " + choice(voitxt), amp=1.5, lang="en", rate=int(PRand(1,5)), voice=int(PRand(0,5)), pitch=int(PRand(12)), octave=0, gap=0, record="crashvoix")


x1 >> play("x.-x..", echo=2, shape=0.5, rate=0.5, octafuz=0.5, formant=var([3,0, 5]), fdist=1, mpf=2300).every(3, "stutter")

x2 >> play("x.-x..", echo=0.5, dur=1/2, shape=4, rate=1, octafuz=linvar([0.3,1]), formant=var([3, 0,5]), fdist=1).every(3, "stutter").stop()

x3 >> loop("fill4", dur=2).stop()

x4 >> loop("metaldrum8", dur=8).stop()

z4 >> play("E ", dur=16, sample=PRand(200))
z1 >> play("G", sample=PRand(200), dur=2, coarse=0, chop=P*[0,1,4],  chopmix=PWhite(0, 1), chopwave=PRand(8), echo=PwRand([0,PWhite(0, 1)],[50, 1]), shift=PWhite(0.5, 2), rate=PWhite(0.95, 1.05), crush=PWhite(0, 4),bits=PRand(8)+4, lofi=0, room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), formantmix=0.2, formant=PGauss(0, 1), revatk=PWhite(-1,2), pan=PWhite(-1,1))
z2 >> play("E", sample=PRand(200), dur=3, coarse=0, chop=P*[0,1,4],  chopmix=PWhite(0, 1), chopwave=PRand(8), echo=PwRand([0,PWhite(0, 1)],[50, 1]), shift=PWhite(0.5, 2), rate=PWhite(0.95, 1.05), crush=0,bits=PRand(8)+4, lofi=P*[0,PWhite(0,1)], room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))
z3 >> play("{EG}", sample=PRand(200), dur=16, coarse=0, chop=P*[0,1,4],  chopmix=PWhite(0, 1), chopwave=PRand(8), echo=PwRand([0,PWhite(0, 1)],[50, 1]) shift=PWhite(0.5, 2), rate=PWhite(0.95, 1.05), crush=0,bits=PRand(8)+4, lofi=PWhite(0,1), feed=0.5, room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))
g1 >> play("g...", sample=0, lpf=PWhite(200,8000), room=1, mix=PWhite(0.2,0.9), shape=(0,0.2), dur=2)
v1 >> play("G", sample=PRand(0,66), dur=PWhite(1,8), rate=PWhite(-1,2), room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), shift=PWhite(0.6, 1.6), pan=PWhite(-1,1))

v2 >> play("G", sample=PRand(0,66), dur=PWhite(3,16), rate=PWhite(-1,2), room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))

v3 >> play("G", sample=PRand(0,66), dur=PWhite(3,16), rate=PWhite(-1,2), room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))
v4 >> play("G", sample=PRand(0,66), dur=PWhite(3,16), rate=PWhite(-1,2), room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))
v5 >> play("G", sample=PRand(0,66), dur=PWhite(3,16), rate=PWhite(-1,2), room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))
v7 >> play("G", sample=PRand(0,66), dur=PWhite(1,5), rate=PWhite(1,1.5), room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))
v8 >> play("G", sample=PRand(0,66), dur=PWhite(1,9), rate=PWhite(0.8,1.2), room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))
v9 >> play("G", sample=PRand(0,66), dur=PWhite(1,5), rate=PWhite(-1,2), room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))
v0 >> play("G", sample=PRand(0,66), dur=PWhite(1,11), rate=PWhite(-1,2), room2=PWhite(0,1), mix2=PWhite(0,0.5), revsus=PWhite(1,4), revatk=PWhite(-1,2), pan=PWhite(-1,1))

v_all.crush=lininf(0,16,64)
v_all.bits=lininf(16,2,64)


i3 >> sos(dur=8, lpf=linvar([60,4800],[tmps*1.5, tmps*3]), shift=0, hpf=expvar([0,500],[tmps*6, tmps*2]))
