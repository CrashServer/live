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

e3 >> lbass(dur=1/2, oct=4, drive=1, mverb=0.8, amp=1, delay=var([0, 0.5]))

