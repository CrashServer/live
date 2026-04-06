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


#@intro(32) 
Clock.bpm = 120
Scale.default="minor"
Root.default=2
var.cho = var([PChain2(chords)],8)
t5 >> faim((0, 4), oct=(3,4),amp=0.5, hpf=120, beef=4, dur=2, echo=[0,PWhite(1.5,1.75)], echomix=PWhite(0,0.9), lpf=[0,PRand(500,4813)]).unison(3)
# warning soprano can be loud

#@build(32)
s1 >> soprano(0, oct=(4,5,[6,2]), dur=PDur([3, 8], [7, 15]), dfm=PRand(400,2400), dfmr=PWhite(0.2,0.8), dfmd=PWhite(12,16), rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, sus=1/2,slide=PStep([12,8,3],1,0), room=0.7, mix=0.7, amp=0.5, amplify=var([0.3,0],[PRand(1,8),PRand(8,32)]), slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")

#@peak(32)
t9 >> charm(PArp(var.cho,5), oct=(4, 5, 6), dur=1/4, top=linvar([200,10000],128), cutoff=linvar([500,2000],[PRand(24,36),PRand(2,12)]), res=PWhite(0.7,0.3), sus=PStep(PRand(4,16)[:16],0.5,0.25), amp=lininf(0, 0.65, 32), lpf=9000).unison(3)

#@break(32)
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.7, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)

#@drop(32)
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.7, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)

#@outro(32)
s2 >> dbass(oct=(5,6), dur=[1/2,1.5,1/4,1/4,1/4,1/4,1/2,1/2], lpf=PRand(400,2400), lpr=PWhite(0.2,1), sus=1/4,slide=PStep([12,8,3],1,0), tape=0.7, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1,amplify=var([0.5,0],[PRand(1,8),PRand(8,32)]), room=1, mix=0.5, slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")

#@part7(32)
s2 >> dbass(oct=(5,6), dur=[1/2,1.5,1/4,1/4,1/4,1/4,1/2,1/2], lpf=PRand(400,2400), lpr=PWhite(0.2,1), sus=1/4,slide=PStep([12,8,3],1,0), tape=0.7, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1,amplify=var([0.5,0],[PRand(1,8),PRand(8,32)]), room=1, mix=0.5, slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")

#@part8(32)
t5.stop()
b4.lpf=400
Root.default=lininf(2, 15, 128)

#@part9(32)
Root.default=15
t9 >> a_daftlead(PArp(var.cho,8), oct=(4, 5), dur=1/4, top=linvar([200,10000],128), ctf=linvar([500,2000],[PRand(24,36),PRand(2,12)]), res=PWhite(0.1,0.3), sus=PStep(PRand(4,16)[:16],0.5,0.25), amp=0.35, lpf=9000, pan=PWhite(-1, 1)).unison(3)

#@part10(16)
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.8, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)

#@part11(16)
s2 >> plaitsX(oct=(5,6), dur=[1/2,1.5,1/4,1/4,1/4,1/4,1/2,1/2], dfm=PRand(400,2400), dfmr=PWhite(0.2,1), dfmd=PWhite(12,16), sus=1/2,slide=PStep([12,8,3],1,0), amplify=var([0.5,0],[PRand(1,8),PRand(8,32)]), mverb=0.4, slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")

#@part12(32)
s1 >> soprano(var.cho[0], oct=(5,6), dur=PDur([3,5],[7,13]), dfm=PRand(200,1800), dfmr=PWhite(0.1,0.6), dfmd=PWhite(8,14), sus=1/3, slide=PStep([12,6,3],1,0), room=0.8, mix=0.6, amp=0.6, amplify=var([0.5,0],[PRand(2,6),PRand(6,24)]), slidedelay=PWhite(0.6,0.85)).unison(3).every(24, "dur.shuffle")

#@part13(16)
t5 >> faim(var.cho[0]+2, oct=(3,4), amp=0.65, hpf=240, dur=1, echo=[0,PWhite(1.25,1.5)], echomix=PWhite(0,0.7), lpf=[0,PRand(800,6400)]).unison(3)

#@part14(16)
b4 >> dbass(var.cho[0], lpf=linvar([800,2400],16), hpf=0, amp=0.55, rate=linvar([0.01,0.15],64), dur=var([1/4,1/2,1/4],[4,2,2]), oct=(3,4)).unison(4)

#@part15(8)
t9.amp=linvar([0.35,0.6],32)

#@part16(8)
s3.drive=0.3+(s2.bend*0.15)

#@part17(16)
Root.default=lininf(15, 12, 32)
t9 >> charm(PArp(var.cho,3), oct=5, dur=1/4, top=linvar([4000,200],32), cutoff=linvar([2000,400],[PRand(12,24),PRand(2,8)]), res=PWhite(0.05,0.2), sus=PStep(PRand(4,16)[:16],0.75,0.5), amp=0.75, lpf=6000).unison(3)

#@part18(16)
s1.stop()
s3 >> plaitsX(bend=PStep([2,4,8],PWhite(0,4),0), benddelay=PWhite(0.3,0.8), oct=(6,7), dur=d2.amp.map({0:4}, default=1/2), chop=8+8*d1.feed, drive=0.4+(s2.bend*0.15), lpf=expvar([12000,2400],[6,0]), lpr=PWhite(0.1,0.7), amp=PBern(8)*(s2.amplify==0)*1.2, hpf=480).unison(3,0.2,99)

#@part19(8)
b4 >> dbass(var.cho[0], lpf=linvar([200,800],8), hpf=0, amp=0.8, rate=0.01, dur=1/4, oct=3).unison(4)

#@part20(16)
d1.feed=var(P*[0,0.25,0.5,0.75],8)
# s2 >> dbass(oct=(4,5), dur=[1/4,3/4,1/4,1/4,1/4,1/4,1/4,1/2], dfm=PRand(200,1600), dfmr=PWhite(0.3,1), dfmd=PWhite(10,18), sus=1/4, slide=PStep([8,4,2],1,0), amplify=var([0.6,0],[PRand(1,4),PRand(4,16)]), mverb=0.2, slidedelay=PWhite(0.5,0.8)).unison(3).every(16, "dur.shuffle")

#@part21(8)
s2.amp=lininf(1, 0, 32)
t9.amp=lininf(0.75, 0, 32)

#@part22(16)
s1 >> soprano(var.cho[0], oct=(4,5), dur=PDur([5,8],[11,19]), dfm=PRand(100,800), dfmr=PWhite(0.1,0.4), dfmd=PWhite(14,20), sus=2/3, slide=PStep([6,3,1],1,0), room=0.9, mix=0.8, amp=0.3, amplify=var([0.4,0],[PRand(4,12),PRand(16,48)]), slidedelay=PWhite(0.8,0.95)).unison(3).every(48, "dur.shuffle")

#@part23(32)
t5 >> faim((0,4), oct=(3,4), amp=0.25, hpf=80, dur=4, echo=[0,PWhite(1.5,1.75)], echomix=PWhite(0.3,0.9), lpf=[0,PRand(200,2400)]).unison(3)

#@part24(16)
s3.stop()
d2.stop()
b4 >> dbass(var.cho[0], lpf=linvar([800,200],32), hpf=0, amp=0.4, rate=linvar([0.01,0.05],64), dur=var([1/2,1],[4,4]), oct=3).unison(4)

#@part25(8)
d1.feed=var(P*[0,0.125],32)
s2 >> plaitsX(oct=(5,6), dur=[1,1.5,1/2,1/2,1,1,1/2,1], dfm=PRand(100,1200), dfmr=PWhite(0.1,0.6), dfmd=PWhite(14,20), sus=2/3, slide=PStep([6,3,1],1,0), amplify=var([0.2,0],[PRand(4,12),PRand(16,48)]), mverb=0.7, slidedelay=PWhite(0.8,0.95)).unison(3).every(48, "dur.shuffle")

#@part26(8)
Root.default=12
s2 >> plaitsX(oct=(5,6), dur=[1,2,1,2], dfm=PRand(50,600), dfmr=PWhite(0.05,0.3), dfmd=PWhite(16,24), sus=1, slide=0, amplify=var([0.15,0],[PRand(8,16),PRand(32,64)]), mverb=0.9, slidedelay=PWhite(0.9,0.99)).unison(3)
# b4 >> dbass(var.cho[0], lpf=linvar([400,80],64), hpf=0, amp=linvar([0.4,0],64), rate=0.01, dur=1, oct=3).unison(4)

#@part27(8)
s1.amp=linvar([0.3,0],48)
t5.amp=linvar([0.25,0],64)
o1.amp=linvar([0.3,0],32)

#@part28(16)
Clock.future(32*4, s1.stop)
Clock.future(48*4, o1.stop)
Clock.future(56*4, b4.stop)
Clock.future(60*4, t5.stop)
Clock.future(64*4, s2.stop)
