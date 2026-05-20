# recorded_073409
# recorded

#@intro(16)
e0 >> plaits(melody(), dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), drive=0, mverb=0.1, oct=3, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))
e0 >> plaits(melody(), dur=(1/2, 1/4), engine=(1, 4),            drive=0, mverb=0.8, oct=5)

#@build(4)
Clock.clear()
soff()
Server.clearFx()

#@peak(16)
rec_stop()

#@endfade(16)
