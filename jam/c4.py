c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=0.4, cfb=0.8, sus=2, cpitch=8, cmode=2, lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.01, oct=3)

c1 >> cs80(cutoff=linvar([400, 4000], [8, 4, 8]), dec=0.1, detune=1, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 4, 0.1], vibdepth=0.2, glide=0.1, dur=1/2, shape=0)
