# edge 93
# trance

c1 >> cs80(cutoff=linvar([400, 5300], [8, 4, 8]), dec=1.0, leg=var([0, 4], [31, 1]), detune=0, lpr=0.2, bits=8, crush=8, oct=(4, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=1, dur=1/6, shape=0.2, fx1=1)
c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 5300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=5, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.6,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=0, dur=1/6, shape=0.3, fx1=1, dist2=0.3, low=0).unison(4)
c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 5300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=5, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.6, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=3, dur=1/6, shape=0.3, fx1=1, dist2=0.3, low=0).unison(4)
c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=1, lpr=0.1, bits=0, crush=5, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=3, dur=1/6, shape=0.0, fx1=1, dist2=2.1, low=0).unison(4)
c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 5300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=5, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=3, dur=1/6, shape=0.5, fx1=1, dist2=0.6, low=0).unison(4)

c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=1, lpr=0.1, bits=0, crush=5, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=3, dur=1/6, shape=0.4, fx1=1, dist2=2.1, low=0).unison(4)

c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.2, bits=0, crush=7, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=linvar([20, 100], 8), dur=1/6, shape=0.0, fx1=1, dist2=4.1, low=0).unison(4)

c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.2, bits=0, crush=5, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=3, dur=1/6, shape=0.5, fx1=1, dist2=4.1, low=0).unison(4)

x4 >> play("[--]", dur=1/3, amp=3, sample=8, hpf=1200, hpr=0.9)
c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=5, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=3, dur=1/6, shape=0.5, fx1=1, dist2=4.1, low=0).unison(4)

c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.2, bits=0, crush=8, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=5, dur=1/6, shape=0.5, fx1=1, dist2=12.1, low=0).unison(4)

c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=5, oct=(4, PStep(4, 5, 6)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=0, dur=1/6, shape=0, fx1=0, dist2=1, low=0).unison(4)

c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=5, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=3, dur=1/6, shape=0.5, fx1=1, dist2=4.1, low=0).unison(4)

c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=5, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=3, dur=1/6, shape=0.5, fx1=1, dist2=4.1, low=0).unison(4)

c2 >> cs80([7, 7, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=5, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=3, dur=1/6, shape=0.5, fx1=1, dist2=4.1, low=0).unison(4)

c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), fshift=linvar([1, 4], 32), dec=1.0, leg=0, detune=0, lpr=0.2, bits=0, crush=8, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=5, dur=1/6, shape=0.5, fx1=1, dist2=12.1, low=0).unison(4)

c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), fshift=linvar([1, 4], 32), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=8, oct=(3, PStep(4, 3, 4)), fdist=0, vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([4000, 12000], 128), glide=5, dur=1/6, shape=0.5, fx1=1, dist2=12.1, low=0).unison(4)

c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), fshift=linvar([1, 12], 32), dec=1.0, leg=0, detune=0, lpr=0.2, bits=0, crush=8, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,12, 0.5, 12.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=5, dur=1/6, shape=0.6, fx1=1, dist2=12.1, low=0).unison(4)

~c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.2, bits=0, crush=8, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=5, dur=1/6, shape=0.5, fx1=1, dist2=12.1, low=0).unison(4)
c4 >> dbass(0, dur=[1/3, 1/3,1/6, 1/6], hpf=400, hpr=0.2, dist2=3, sus=1/2, shape=0, oct=5, lofi=0)

d5 >> a_daft([0, 0,0.5],dur=1/6, oct=7, amp=5, dist2=1.2)
a4 >> play("q.q", amp=5, sample=7, dur=1/3, shape=2.2, lpf=linvar([800, 2000], 32), lpr=0.2)

c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), fshift=linvar([1, 12], 32), dec=1.0, leg=0, detune=0, lpr=0.2, bits=0, crush=8, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,12, 0.5, 12.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=5, dur=1/6, shape=0.6, fx1=1, dist2=12.1, low=0).unison(4)

~c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.2, bits=0, crush=8, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=5, dur=1/6, shape=0.5, fx1=1, dist2=12.1, low=0).unison(4)
