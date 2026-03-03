# antenna 61
# interlude


Clock.bpm = 122/2;
Scale.default = Scale.minor
Root.default = "F#"

e0 >> plaits(melody(),dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), drive=0, mverb=0.1, oct=3, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))
e0 >> plaits(melody(),dur=(1/2, 1/4), engine=(1, 4), drive=0, mverb=0.8, oct=5)
e1 >> bass(melody()[:8],dur=var([1/4, 2],[13, 3]), a=PWhite(0, 1), drive=0, amp=0.7, mverb=0.8).unison(2).every(13, "offmul", 2)
e0.every(4, "shuffle")
e1 >> bass(melody(),dur=1/4, oct=5, drive=0, mverb=0.8).unison(0)
e1 >> bass(melody(),dur=1/4, drive=linvar([0, 0.02], 32), mverb=0.8).unison(0)
g2 >> bass(melody() + var([7, 3, [4, 0]]),dur=var([1/4, 1/2]), drive=0, vol=0.5, mverb=0.1).unison(0)
e3 >> lbass(dur=1/2, oct=4, drive=0, mverb=0.8, amp=1, delay=var([0, 0.5]))
e0.engine = var([1, 4, 11], [8, 4, 4])
e0.dur = var([(1/2, 1/4), (1/2, 1/4, 1)], [12, 4])
e1.oct = var([5, 4], [12, 4])
g2.delay = var([0, 0.25], [8, 8])
g2.mverb = linvar([0.1, 0.5], 32)
e3.lpf = linvar([800, 3000], 48)
e3.hpf=1200

Root.default = "E"
e4 >> karp(melody(), dur=PDur(5, 8), oct=var([5, 6], [8, 8]), lpf=linvar([600, 2400], 32), mverb=0.6, amp=var([0, 0.4], [16, 16]), delay=var([0, 0.5], [12, 4]))
e0.mverb = linvar([0.8, 0.3], 16)
e1.dur = var([1/4, (1/4, 1/2)], [8, 8])
g2.degree = melody() + var([7, 3, [4, 0], 5], [4, 4, 4, 4])
e3.delay = var([0, 0.5, 0.25], [8, 4, 4])
l1 >> loop("cinambi8", dur=8, sample=var([3, 5], [8, 8]), amp=var([0, 0.35], [16, 16]), hpf=400, mverb=0.4)
e0.dur = var([(1/2, 1/4), 2, 4], [8, 4, 4])
e0.engine = var([11, 5, 3], [4, 4, 8])
e1.lpf = linvar([4000, 1200], 32)
g2.vol = linvar([0.5, 0.3], 32)
e3.oct = var([4, 5], [12, 4])
e3.fbelay=0.5
e4.oct = var([6, 5, 6], [4, 4, 8])
e4.amp = linvar([0.4, 0.6], 32)
Root.default = "F#"

