# Pump 122
# trance
Clock.bpm = 122
d1 >> dbass(0, pumper=linvar([0.3, 0.9], 64), pumprate=0.9, transient=linvar([0.1, 4], 64), transattack=2, multicrush=2.5, combres=linvar([0.1, 14], 32), oct=5, fbdelay=0.5, fbtime=0.3, fbfeed=linvar([0.5, 0.9], 64), stereowidth=8, dur=[1, 1/2, 1/2, 1/4, 1/2])
d2 >> dbass((0, 4, 4, ([7.5, 0, 4], [0, 0, 0, 4, 4, 0])),pumper=linvar([0.3, 0.9], 64), pumprate=0.9, transient=var([1, 2, 4, 8], 8), transattack=var([0.5, 2], [[6, 7], [2, 1]]), multicrush=1, combres=5.0, oct=5, fbdelay=0.7, fbtime=0.3, fbfeed=0.44, stereowidth=8, dur=1/2)
d3 >> dbass((0, 4),pumper=linvar([0.3, 0.9], 64), pumprate=0.9, transient=0.7, transattack=2, multicrush=2.5, amp=0.3, combres=2.6, oct=7, fbdelay=[0.5, 0.8], fbtime=0.6, fbfeed=0.54, stereowidth=8, dur=8, gate=1).slider()
