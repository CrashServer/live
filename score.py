# score — 60 bpm, C minor, philharmonic
# Zimmer / Williams / Morricone: piano ostinato, string swells, brass theme, choir climax
Clock.bpm = 60
Scale.default = "minor"
Root.default = "C"

#@#@ score

#@ prelude

os >> piano([0,6,5,6], oct=3, dur=1, sus=0.88, amp=0.42, room=0.7, mix=0.6)

pt >> pianovel([0,3,5,7,5,3,7,5], oct=5, dur=var([1,1,1,0.5,1,1,2,2],[1,1,1,1,1,1,1,2]), sus=var([0.8,0.8,0.8,0.4,0.8,0.8,1.5,1.5],[1,1,1,1,1,1,1,2]), amp=0.5, room=0.75, mix=0.65, pan=sinvar([-0.2,0.2],16))

vi >> viola([0,5,3,4], oct=3, dur=1, sus=0.15, amp=0.22, room=0.7, mix=0.6, pan=-0.3)

#@ theme

sw >> swell([(0,3,5),(6,1,3),(5,0,3),(4,6,1)], oct=4, dur=4, sus=5, amp=sinvar([0.1,0.4],32), rate=0.3, wide=0.7, room=0.95, mix=0.88)

vc >> viola([0,-2,3,2,0,5,3,4], oct=4, dur=var([2,1,1,1,2,1,1,2],[2,1,1,1,2,1,1,2]), sus=var([1.8,0.8,0.8,0.8,1.8,0.8,0.8,1.8],[2,1,1,1,2,1,1,2]), amp=sinvar([0.15,0.35],24), room=0.9, mix=0.8, vibrato=sinvar([0,0.25],16))

hp >> karp([0,3,5,7,5,3, 6,1,3,6,3,1, 5,0,3,5,3,0, 4,6,1,4,1,6], oct=5, dur=0.5, sus=PRand([0.4,0.6,0.8],6), amp=0.28, cheapverb=0.5, cvdecay=2, pan=sinvar([-0.4,0.4],6))

#@ development

br >> brass2([0,3,5,7,5,3,7,5, 0,3,5,7,9,7,5,3], oct=5, dur=var([1,0.5,0.5,1,0.5,0.5,1,2],[1,1,1,1,1,1,1,1]), sus=var([0.85,0.4,0.4,0.85,0.4,0.4,0.85,1.8],[1,1,1,1,1,1,1,1]), amp=sinvar([0.3,0.6],16), bright=0.75, growl=sinvar([0.1,0.45],16), vibrate=4.5, vibdepth=0.018, room=0.6, mix=0.5)

cx >> cs80([(0,3,5),(6,1,3),(5,0,3),(4,6,1)], oct=4, dur=4, sus=5, amp=sinvar([0.12,0.32],32), cutoff=sinvar([1000,3500],24), vibspeed=3.5, vibdepth=0.012, room=0.9, mix=0.8)

tm >> gong([0,rest(0),rest(0),rest(0),5,rest(0),rest(0),rest(0),3,rest(0),rest(0),rest(0),4,rest(0),rest(0),rest(0)], oct=2, dur=1, sus=sinvar([0.5,1.2],16), amp=sinvar([0.2,0.55],16), room=0.6, mix=0.5)

ch >> choir([0,5,3,4], oct=4, dur=4, sus=sinvar([4,6],16), amp=sinvar([0,0.22],32), room=0.99, mix=0.95, lpf=linvar([500,2000],64))

#@ climax

ch >> choir([(0,3,5),(6,1,3),(5,0,3),(4,6,1)], oct=4, dur=4, sus=5.5, amp=sinvar([0.3,0.55],16), room=0.99, mix=0.95, lpf=linvar([800,3000],32))

al >> sinepad([0,3,5,4], oct=6, dur=4, sus=6, amp=sinvar([0.05,0.22],16), room=0.99, mix=0.95, shimmer=0.5)

cl >> bell2([7,9,12,7,5,3,7,9,12], oct=6, dur=PRand([0.5,1,2],9), sus=PRand([0.3,0.5,1],9), amp=sinvar([0.1,0.3],8), cheapverb=0.7, cvdecay=3)

pe >> compperc([rest(0),rest(0),0,rest(0),rest(0),rest(0),0,rest(0)], dur=0.5, amp=sinvar([0.3,0.65],16), tone=0.4, body=0.5, noise=0.5, decay=0.12, drive=1.2, room=0.4, mix=0.35)

sw.amp = sinvar([0.5, 0.75], 8)
br.amp = sinvar([0.55, 0.85], 8)
os.amp = sinvar([0.4, 0.65], 8)
cx.amp = sinvar([0.25, 0.5], 16)

#@ resolution(96)

br.amp = linvar([0.6, 0], 32)
ch.amp = linvar([0.45, 0], 32)
al.amp = linvar([0.2, 0], 24)
cl.amp = linvar([0.25, 0], 24)
pe.amp = linvar([0.5, 0], 16)
tm.amp = linvar([0.4, 0], 16)
cx.amp = linvar([0.3, 0], 32)
hp.amp = linvar([0.25, 0], 40)
sw.amp = linvar([0.5, 0.1], 64)
vc.amp = linvar([0.3, 0.05], 64)
os.amp = linvar([0.4, 0.15], 64)
pt.amp = linvar([0.45, 0.08], 96)
