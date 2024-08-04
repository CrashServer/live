Clock.bpm = 122/2;
Scale.default = Scale.minor
Root.default = 6
b1 >> bass(melody() + var([7, 3, [4, 0]]),dur=var([1/4, 1/2]), drive=0, vol=0.5, mverb=0.1).unison(0)
b2 >> plaits(melody(),dur=var([1/2, (1/2, 2)]), mverb=0.8, engine=var([11, 5], [3, 1]), oct=4, amp=PWhite(0, 1))
b3 >> plaits(melody(),dur=(1/2, 1/4), engine=1, drive=0, mverb=0.8)
b4 >> bass(melody(),dur=var([2, 1, 1/4], [1, 2, 4]), drive=linvar([0, 0.1], 32), mverb=0.5, mverbdiff=0.4).slider()
b5 >> bass(melody() + var([7, 3, [4, 0]]),dur=P[1/2, 2], drive=0, oct=4).unison(2).slider()
b6 >> plaits(melody() + PWalk(8, 1, 1),dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), drive=0, mverb=0.1, oct=4, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))
b7 >> plaits(melody(),dur=(1/2, 1/4), engine=3, drive=0, mverb=0.2, oct=5)
b8 >> bass(melody(),dur=1/4, drive=linvar([0, 0.1], 32), mverb=0.8, delay=var([0, 0.5]), oct=6)
b9 >> bass(melody(),dur=var([1/4, 2],[13, 3]), drive=0, mverb=0).unison(2).every(13, "offmul", 2)
