#cloudy
Clock.bpm = 122
c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=0.8, cfb=0.8, sus=2, feed=0, cpitch=8, cmode=1, lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=4, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.2, glide=0.1, dur=1/2, shape=0, amp=0.5)
