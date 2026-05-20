# recorded_040635
# recorded

#@intro(32)
_seq_cancel()
Clock.bpm = 120
Scale.default="minor"
Root.default=2
var.cho = var([PChain2(chords)],8)
t5 >> faim((0, 4), oct=(3,4),amp=0.5, hpf=120, beef=4, dur=2, echo=[0,PWhite(1.5,1.75)], echomix=PWhite(0,0.9), lpf=[0,PRand(500,4813)]).unison(3)

_seq_schedule(32, 1775441049903)

#@build(8)
t5 >> faim((0, 4), oct=(3,4),amp=0.5, hpf=120, beef=2, dur=2, echo=[0,PWhite(1.5,1.75)], echomix=PWhite(0,0.9), lpf=[0,PRand(500,4813)]).unison(3)

#@peak(8)
_seq_cancel()
s1 >> soprano(0, oct=(4,5,[6,2]), dur=PDur([3, 8], [7, 15]), dfm=PRand(400,2400), dfmr=PWhite(0.2,0.8), dfmd=PWhite(12,16), rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, sus=1/2,slide=PStep([12,8,3],1,0), room=0.7, mix=0.7, amp=0.5, amplify=var([0.3,0],[PRand(1,8),PRand(8,32)]), slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")

_seq_schedule(32, 1775441065923)

#@break(32)
t5 >> faim((0, 4), oct=(3,4),amp=0.5, hpf=120, beef=[2, 4, 2, 3], dur=2, echo=[0,PWhite(1.5,1.75)], echomix=PWhite(0,0.9), lpf=[0,PRand(500,4813)]).unison(3)

#@drop(32)
_seq_cancel()
t9 >> charm(PArp(var.cho,5), oct=(4, 5, 6), dur=1/4, top=linvar([200,10000],128), cutoff=linvar([500,2000],[PRand(24,36),PRand(2,12)]), res=PWhite(0.7,0.3), sus=PStep(PRand(4,16)[:16],0.5,0.25), amp=lininf(0, 0.65, 32), lpf=9000).unison(3)

_seq_schedule(32, 1775441081940)

#@outro(32)
_seq_cancel()
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.7, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)

_seq_schedule(32, 1775441097953)

#@part7(32)
_seq_cancel()
b4 >> dbass(var.cho[0], lpf=linvar([464,1664],13), hpf=0, amp=0.7, rate=linvar([0.01, 0.1], 128), dur=var([1/4,1/2],[6,2]), oct=(3,4)).unison(4)

s1.


_seq_schedule(32, 1775441113969)

#@part8(32)
_seq_cancel()
s2 >> dbass(oct=(5,6), dur=[1/2,1.5,1/4,1/4,1/4,1/4,1/2,1/2], lpf=PRand(400,2400), lpr=PWhite(0.2,1), sus=1/4,slide=PStep([12,8,3],1,0), tape=0.7, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1,amplify=var([0.5,0],[PRand(1,8),PRand(8,32)]), room=1, mix=0.5, slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle")



_seq_schedule(32, 1775441129976)

#@part9(32)
_seq_cancel()

_seq_schedule(32, 1775441146001)

#@part10(32)
_seq_cancel()
s1 >> soprano(0, oct=(4,5,[6,2]), dur=PDur([3, 8], [7, 15]), dfm=PRand(400,2400), dfmr=PWhite(0.2,0.8), dfmd=PWhite(12,16), rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, sus=1/2,slide=PStep([12,8,3],1,0), room=0.7, mix=0.7, amp=0.5, amplify=var([0.3,0],[PRand(1,8),PRand(8,32)]), slidedelay=PWhite(0.7,0.9)).unison(3).every(32, "dur.shuffle").solo(8)

_seq_schedule(32, 1775441162006)

#@part11(16)
Clock.clear()
soff()
Server.clearFx()
_seq_cancel()
Clock.clear()
soff()
Server.clearFx()

#@part12(16)
rec_sto(p)
rec_stop()

#@endfade(16)
