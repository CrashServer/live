# recorded_073528
# recorded

#@intro(8)
e0 >> plaits(melody(), dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), drive=0, mverb=0.1, oct=3, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))

#@build(8)
e1 >> bass(melody()[:8], dur=var([1/4, 2], [13, 3]), a=PWhite(0, 1),          drive=0, amp=0.7, mverb=0.8).unison(2).every(13, "offmul", 2)

#@peak(8)
e1 >> bass(melody()[:8], dur=var([1/4, 2], [13, 3]), a=PWhite(0, 1),          drive=0, amp=0.9, mverb=0.8).unison(2).every(13, "offmul", 2)

#@break(4)
e1 >> bass(melody()[:8], dur=var([1/4, 2], [13, 3]), a=PWhite(0, 1),          drive=0, amp=0.7, mverb=0.8).unison(2).every(13, "offmul", 2)

#@drop(4)
e0.every(4, "shuffle")

#@outro(8)
e1 >> bass(melody(), dur=1/4, oct=5, drive=0, mverb=0.8).unison(0)

#@part7(8)
e1 >> bass(melody(), dur=1/4, drive=linvar([0, 0.02], 32), mverb=0.8).unison(0)

#@part8(8)
g2 >> bass(melody() + var([7, 3, [4, 0]]),   dur=var([1/4, 1/2]), drive=0, vol=0.5, mverb=0.1).unison(0)

#@part9(4)
e1 >> plaits(melody(), dur=var([1/2, (1/2, 2)]), drive=0,   mverb=0.8, engine=var([11, 5], [3, 1]), oct=5).unison(0)

#@part10(4)
e0.dur = var([2, 1/4, 1/4, 1/4, 1/4])

#@part11(8)
Clock.clear()
soff()
Server.clearFx()

#@part12(16)
rec_stop()

#@endfade(16)
