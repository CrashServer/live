# recorded_073344
# recorded

#@intro(8)
Clock.bpm = 122/2
Scale.default = Scale.minor
Root.default = "F#"

#@build(8)
e0 >> plaits(melody(), dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), drive=0, mverb=0.1, oct=3, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))

#@peak(8)
e0 >> plaits(melody(), dur=(1/2, 1/4), engine=(1, 4),            drive=0, mverb=0.8, oct=5)

#@break(4)
e1 >> bass(melody()[:8], dur=var([1/4, 2], [13, 3]), a=PWhite(0, 1),
           drive=0, amp=0.7, mverb=0.8).unison(2).every(13, "offmul", 2)
e0.every(4, "shuffle")

#@drop(8)
Clock.clear()
soff()
Server.clearFx()
e0 >> plaits(melody(), dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), drive=0, mverb=0.1, oct=3, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))

#@outro(4)
e0 >> plaits(melody(), dur=(1/2, 1/4), engine=(1, 4),            drive=0, mverb=0.8, oct=5)

#@part7(4)
Clock.clear()
soff()
Server.clearFx()

#@part8(16)
rec_stop()

#@endfade(16)
