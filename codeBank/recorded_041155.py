# recorded_041155
# recorded

#@intro(32)
_seq_cancel()
Clock.bpm = 122
Scale.default="minor"
Root.default=2
var.cho = var([PChain2(chords)],8)
t5 >> faim((0, 4), oct=(3,4),amp=0.5, hpf=120, beef=4, dur=2, echo=[0,PWhite(1.5,1.75)], echomix=PWhite(0,0.9), lpf=[0,PRand(500,4813)]).unison(3)

_seq_schedule(32, 1775441231240)

#@build(32)
_seq_cancel()
s1 >> soprano(0, oct=(4,5,[6,2]), dur=PDur([3, 8], [7, 15]), dfm=PRand(400,2400), dfmr=PWhite(0.2,0.8), dfmd=PWhite(12,16), rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, sus=1/2,slide=PStep([12,8,3],1,0), room=0.7, mix=0.7, amp=0.5, amplify=var([0.3,0],[PRand(1,8),PRand(8,32)]), slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")

_seq_schedule(32, 1775441247035)

#@peak(32)
_seq_cancel()
t9 >> charm(PArp(var.cho,5), oct=(4, 5, 6), dur=1/4, top=linvar([200,10000],128), cutoff=linvar([500,2000],[PRand(24,36),PRand(2,12)]), res=PWhite(0.7,0.3), sus=PStep(PRand(4,16)[:16],0.5,0.25), amp=lininf(0, 0.65, 32), lpf=9000).unison(3)
t5 >> faim((0, 4), oct=(3,4),amp=0.5, hpf=120, beef=[4, 1, 1, 2, 1, 4], dur=var([2, PDur(3, 8)]), echo=[0,PWhite(1.5,1.75)], echomix=PWhite(0,0.9), lpf=[0,PRand(500,4813)]).unison(3)


_seq_schedule(32, 1775441262787)

#@break(32)
_seq_cancel()
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.7, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)

_seq_schedule(32, 1775441278544)

#@drop(32)
_seq_cancel()
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.7, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)



_seq_schedule(32, 1775441294299)

#@outro(32)
_seq_cancel()
s2 >> dbass(oct=(5,6), dur=[1/2,1.5,1/4,1/4,1/4,1/4,1/2,1/2], lpf=PRand(400,2400), lpr=PWhite(0.2,1), sus=1/4,slide=PStep([12,8,3],1,0), tape=0.7, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1,amplify=var([0.5,0],[PRand(1,8),PRand(8,32)]), room=1, mix=0.5, slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")
b4.lpf=1200

_seq_schedule(32, 1775441310041)

#@part7(32)
_seq_cancel()
s2 >> dbass(oct=(5,6), dur=[1/2,1.5,1/4,1/4,1/4,1/4,1/2,1/2], lpf=PRand(400,2400), lpr=PWhite(0.2,1), sus=1/4,slide=PStep([12,8,3],1,0), tape=0.7, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1,amplify=var([0.5,0],[PRand(1,8),PRand(8,32)]), room=1, mix=0.5, slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")

_seq_schedule(32, 1775441325797)

#@part8(16)
_seq_cancel()
t5.stop()
b4.lpf=400
Root.default=lininf(2, 15, 256)
b4.stop()
s1.solo(8)

_seq_schedule(16, 1775441341540)

#@part9(16)
_seq_cancel()
Root.default=15
s1.unsolo()
t9 >> a_daftlead(PArp(var.cho,8), oct=(4, 5), dur=1/4, top=linvar([200,10000],128), ctf=linvar([500,2000],[PRand(24,36),PRand(2,12)]), res=PWhite(0.1,0.3), sus=PStep(PRand(4,16)[:16],0.5,0.25), amp=0.35, lpf=9000, pan=PWhite(-1, 1)).unison(3)

_seq_schedule(32, 1775441349442)

#@part10(16)
s1.unsolo(8)

#@part11(8)
t9 >> a_daftlead(PArp(var.cho,8), oct=(4, 5), dur=1/4, top=linvar([200,10000],128), ctf=linvar([500,2000],[PRand(24,36),PRand(2,12)]), res=PWhite(0.1,0.3), sus=PStep(PRand(4,16)[:16],0.5,0.25), amp=0.35, lpf=9000, pan=PWhite(-1, 1)).unison(3)

#@part12(8)
_seq_cancel()
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.8, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)

_seq_schedule(16, 1775441365186)

#@part13(8)
s1.solo(-1)

#@part14(16)
_seq_cancel()
s2 >> plaitsX(oct=(5,6), dur=[1/2,1.5,1/4,1/4,1/4,1/4,1/2,1/2], dfm=PRand(400,2400), dfmr=PWhite(0.2,1), dfmd=PWhite(12,16), sus=1/2,slide=PStep([12,8,3],1,0), amplify=var([0.5,0],[PRand(1,8),PRand(8,32)]), mverb=0.4, slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")

_seq_schedule(16, 1775441373073)

#@part15(32)
_seq_cancel()
s1 >> soprano(var.cho[0], oct=(5,6), dur=PDur([3,5],[7,13]), dfm=PRand(200,1800), dfmr=PWhite(0.1,0.6), dfmd=PWhite(8,14), sus=1/3, slide=PStep([12,6,3],1,0), room=0.8, mix=0.6, amp=0.6, amplify=var([0.5,0],[PRand(2,6),PRand(6,24)]), slidedelay=PWhite(0.6,0.85)).unison(3).every(24, "dur.shuffle")

_seq_schedule(32, 1775441380945)

#@part16(16)
_seq_cancel()
t5 >> faim(var.cho[0]+2, oct=(3,4), amp=0.65, hpf=240, dur=1, echo=[0,PWhite(1.25,1.5)], echomix=PWhite(0,0.7), lpf=[0,PRand(800,6400)]).unison(3)

_seq_schedule(16, 1775441396690)

#@part17(16)
_seq_cancel()
b4 >> dbass(var.cho[0], lpf=linvar([800,2400],16), hpf=0, amp=0.55, rate=linvar([0.01,0.15],64), dur=var([1/4,1/2,1/4],[4,2,2]), oct=(3,4)).unison(4)

_seq_schedule(16, 1775441404570)

#@part18(8)
_seq_cancel()
t9.amp=linvar([0.35,0.6],32)

_seq_schedule(8, 1775441412446)

#@part19(8)
_seq_cancel()
s3.drive=0.3+(s2.bend*0.15)

_seq_schedule(8, 1775441416383)

#@part20(16)
_seq_cancel()
Root.default=lininf(15, 12, 32)
t9 >> charm(PArp(var.cho,3), oct=5, dur=1/4, top=linvar([4000,200],32), cutoff=linvar([2000,400],[PRand(12,24),PRand(2,8)]), res=PWhite(0.05,0.2), sus=PStep(PRand(4,16)[:16],0.75,0.5), amp=0.75, lpf=6000).unison(3)

_seq_schedule(16, 1775441420321)

#@part21(16)
_seq_cancel()
s1.stop()
s3 >> plaitsX(bend=PStep([2,4,8],PWhite(0,4),0), benddelay=PWhite(0.3,0.8), oct=(6,7), dur=d2.amp.map({0:4}, default=1/2), chop=8+8*d1.feed, drive=0.4+(s2.bend*0.15), lpf=expvar([12000,2400],[6,0]), lpr=PWhite(0.1,0.7), amp=PBern(8)*(s2.amplify==0)*1.2, hpf=480).unison(3,0.2,99)

_seq_schedule(16, 1775441428199)

#@part22(8)
_seq_cancel()
b4 >> dbass(var.cho[0], lpf=linvar([200,800],8), hpf=0, amp=0.8, rate=0.01, dur=1/4, oct=3).unison(4)

_seq_schedule(8, 1775441436090)

#@part23(16)
_seq_cancel()
d1.feed=var(P*[0,0.25,0.5,0.75],8)
s2.stop()

_seq_schedule(16, 1775441440029)

#@part24(8)
_seq_cancel()
s2.amp=lininf(1, 0, 32)
t9.amp=lininf(0.75, 0, 32)

_seq_schedule(8, 1775441447908)

#@part25(16)
_seq_cancel()
s1 >> soprano(var.cho[0], oct=(4,5), dur=PDur([5,8],[11,19]), dfm=PRand(100,800), dfmr=PWhite(0.1,0.4), dfmd=PWhite(14,20), sus=2/3, slide=PStep([6,3,1],1,0), room=0.9, mix=0.8, amp=0.3, amplify=var([0.4,0],[PRand(4,12),PRand(16,48)]), slidedelay=PWhite(0.8,0.95)).unison(3).every(48, "dur.shuffle")

_seq_schedule(16, 1775441451860)

#@part26(32)
_seq_cancel()
t5 >> faim((0,4), oct=(3,4), amp=0.25, hpf=80, dur=4, echo=[0,PWhite(1.5,1.75)], echomix=PWhite(0.3,0.9), lpf=[0,PRand(200,2400)]).unison(3)

_seq_schedule(32, 1775441459737)

#@part27(16)
_seq_cancel()
s3.stop()
d2.stop()
b4 >> dbass(var.cho[0], lpf=linvar([800,200],32), hpf=0, amp=0.4, rate=linvar([0.01,0.05],64), dur=var([1/2,1],[4,4]), oct=3).unison(4)

_seq_schedule(16, 1775441475483)

#@part28(8)
_seq_cancel()
d1.feed=var(P*[0,0.125],32)
s2 >> plaitsX(oct=(5,6), dur=[1,1.5,1/2,1/2,1,1,1/2,1], dfm=PRand(100,1200), dfmr=PWhite(0.1,0.6), dfmd=PWhite(14,20), sus=2/3, slide=PStep([6,3,1],1,0), amplify=var([0.2,0],[PRand(4,12),PRand(16,48)]), mverb=0.7, slidedelay=PWhite(0.8,0.95)).unison(3).every(48, "dur.shuffle")

_seq_schedule(8, 1775441483382)

#@part29(8)
_seq_cancel()
Root.default=12
s2 >> plaitsX(oct=(5,6), dur=[1,2,1,2], dfm=PRand(50,600), dfmr=PWhite(0.05,0.3), dfmd=PWhite(16,24), sus=1, slide=0, amplify=var([0.15,0],[PRand(8,16),PRand(32,64)]), mverb=0.9, slidedelay=PWhite(0.9,0.99)).unison(3)
b4.stop()

_seq_schedule(8, 1775441487337)

#@part30(8)
_seq_cancel()
s1.amp=linvar([0.3,0],48)
t5.amp=linvar([0.25,0],64)
o1.amp=linvar([0.3,0],32)

_seq_schedule(8, 1775441491293)

#@part31(32)
_seq_cancel()
Clock.future(32*4, s1.stop)
Clock.future(48*4, o1.stop)
Clock.future(56*4, b4.stop)
Clock.future(60*4, t5.stop)
Clock.future(64*4, s2.stop)

_seq_schedule(16, 1775441495231)

#@part32(16)
rec_stop()

#@endfade(16)
