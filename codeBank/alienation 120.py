# alienation 120
# reisub

Clock.bpm = 120
Scale.default="minor"
Root.default=12
var.cho = var([PChain2(chords)],8)

t5 >> faim((0, 4), oct=(3,4),amp=0.4, hpf=120, dur=2, echo=[0,PWhite(1.5,1.75)], echomix=PWhite(0,0.9), lpf=[0,PRand(500,4813)]).unison(3)
s1 >> soprano(0, oct=(4,5,[6,2]), dur=PDur([3, 8], [7, 15]), dfm=PRand(400,2400), dfmr=PWhite(0.2,0.8), dfmd=PWhite(12,16), sus=1/2,slide=PStep([12,8,3],1,0), room=0.7, mix=0.7, amp=0.5, amplify=var([0.3,0],[PRand(1,8),PRand(8,32)]), slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")
d8 >> play("z", dur=P*[1,1.5,2], hpf=60, amp=0.6, rate=PWhite(-0.9,1.2), pan=(-1,1))

t9 >> tb303(PArp(var.cho,5), oct=3, dur=1/4, top=linvar([200,10000],128), cutoff=linvar([500,2000],[PRand(24,36),PRand(2,12)]), res=PWhite(0.1,0.3), sus=PStep(PRand(4,16)[:16],0.5,0.25), amp=0.65, lpf=9000).unison(3)
t9.lpf=linvar([20, 6000],[256, inf], start=now)
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.4, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)

d1 >> play("x.", feedfreq=[[0,PRand(500)],0], hpf=30, sample=4, amp=0.2, tanh=2, chop=1+d1.feed)
d4 >> play("o.", dur=1, delay=0.5, rate=0.5, bpr=0.2, bpf=4000)

d1.feed=var(P*[0,0.125,0.25,0.5],16)
t5.stop()

d8.stop()
d8.hpf=7000;
d8.stop()

o1 >> play("--C--{-[-c][---]}C", sample=7, amp=0.6+d2.amp/4, lpf=PRand(400,15800), hpf=300, lpr=[PWhite(0.2,1),1], pan=[PWhite(-1,1),0,PWhite(-1,1)], room=PWhite(0,1), mix=PWhite(0,0.7))

d2 >> play("<(xxx.)(...{.[xx]x})><..o.>", amp=var([0, 1], 32), sample=(4,4), amplify=(1,1))
o2 >> play("o", amp=2*(d2.amp>0), sample=3, pan=PWhite(-1,1), room=0.7, mix=.3).fill()

d_all.stop()
t9.stop()
s2 >> sitar(oct=(5,6), dur=[1/2,1.5,1/4,1/4,1/4,1/4,1/2,1/2], lpf=PRand(400,2400), lpr=PWhite(0.2,1), sus=1/4,slide=PStep([12,8,3],1,0), amplify=var([0.25,0],[PRand(1,8),PRand(8,32)]), room=1, mix=0.5, slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")
s3 >> snick(bend=PStep([2,4,8],PWhite(0,3),0), benddelay=PWhite(0.4,0.9), oct=(6,7), dur=d2.amp.map({0:8}, default=1), chop=16+16*d1.feed, drive=0.2+(s2.bend*0.1), lpf=expvar([16800,3480],[8,0]), lpr=PWhite(0.2,0.8), amp=PBern(16)*(s2.amplify==0)*1, hpf=360).unison(3,0.25,99)
b4.lpf=400

Root.default=15
t9 >> tb303(PArp(var.cho,8), oct=3, dur=1/4, top=linvar([200,10000],128), ctf=linvar([500,2000],[PRand(24,36),PRand(2,12)]), res=PWhite(0.1,0.3), sus=PStep(PRand(4,16)[:16],0.5,0.25), amp=0.35, lpf=9000).unison(3)
t9.lpf=linvar([20, 6000],[256, inf], start=now)
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.4, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)

Master().cut=P*[1,2,3,4]/4
Master().cut=0
Master().feed=0

d7 >> play(P["x-(-m)"][:8].rotate(var([1,3])), rate=1.5, dur=1/4,amplify=0.8, delay=var([0,(0,0.75)],PRand(8)),sample=1)

s3.stop()

Clock.bpm=var([120,60,30,7.5],[60,2,1,1]) # wait for the drop! 
Clock.bpm=120;

Root.default = -24
Master().bpm = 120

#### les restes du monde
s2 >> sitar(oct=(5,6), dur=[1/2,1.5,1/4,1/4,1/4,1/4,1/2,1/2], dfm=PRand(400,2400), dfmr=PWhite(0.2,1), dfmd=PWhite(12,16), sus=1/4,slide=PStep([12,8,3],1,0), amplify=var([0.25,0],[PRand(1,8),PRand(8,32)]), room=1, mix=0.5, slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")
