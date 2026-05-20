# recorded_101701
# recorded

#@intro(16)
Clock.bpm = 93
p5 >> darkpad([0, 6], dur=8, oct=5, sus=8, atk=.1, dark=0.2, detune=0.02, amp=linvar([0.7, 0.35], 32), lpf=linvar([300, 3200], 4), room=0.9, mix=0.7)

#@build(16)
p2 >> ethpad([0, 1, 7], dur=8, oct=5, attack=4, release=4, amp=linvar([0, 0.3], 48), room=0.9, mix=0.6)

#@peak(32)
c2 >> cs80([0, 0, 0.5], cutoff=linvar([200, 1500], [16, 8, 16]), dec=0.2, leg=0, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5, 0.1, 0.5, 0.1], vibdepth=0.1, lpf=linvar([200, 1200], 64), dur=1/6, shape=0, amp=var([0, 0.15], [24, 8]), room=0.2, mix=0.5).unison(2)

#@break(8)
c2 >> cs80([0, 0, 0.5], cutoff=linvar([200, 1500], [16, 8, 16]), dec=0.1, leg=0, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5, 0.1, 0.5, 0.1], vibdepth=0.1, lpf=linvar([200, 1200], 64), dur=1/6, shape=0, amp=var([0, 0.15], [24, 8]), room=0.2, mix=0.5).unison(2)

#@drop(32)
~c2 >> cs80([0, 0, 0.5],cutoff=linvar([1200, 15300], [8, 4, 8]), fshift=linvar([1, 4], 32), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=1, oct=(3, PStep(4, 3, 5)), fdist=0, vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([4000, 12000], 128), glide=1, dur=1/6, shape=8, fx1=1, dist2=0, low=0).unison(3)

#@outro(8)
~c2 >> cs80([0, 1, 0.5],cutoff=linvar([1200, 15300], [8, 4, 8]), fshift=linvar([1, 4], 32), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=1, oct=(3, PStep(4, 3, 5)), fdist=0, vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([4000, 12000], 128), glide=1, dur=1/6, shape=8, fx1=1, dist2=0, low=0).unison(3)

#@part7(8)
~c2 >> cs80([0, 1, 0.5],cutoff=linvar([1200, 15300], [8, 2, 8]), fshift=linvar([1, 4], 32), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=1, oct=(3, PStep(4, 3, 5)), fdist=0, vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([4000, 12000], 128), glide=1, dur=1/6, shape=8, fx1=1, dist2=0, low=0).unison(3)

#@part8(8)
~c2 >> cs80([0, 1, 0.5],cutoff=linvar([1200, 15300], [2, 2, 8]), fshift=linvar([1, 4], 32), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=1, oct=(3, PStep(4, 3, 5)), fdist=0, vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([4000, 12000], 128), glide=1, dur=1/6, shape=8, fx1=1, dist2=0, low=0).unison(3)

#@part9(4)
~c2 >> cs80([0, 1, 0.5],cutoff=linvar([1200, 15300], [2, 2, 8]), fshift=linvar([1, 4], 32), dec=1.0, leg=0, detune=0, lpr=0.2, bits=0, crush=1, oct=(3, PStep(4, 3, 5)), fdist=0, vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([4000, 12000], 128), glide=1, dur=1/6, shape=8, fx1=1, dist2=0, low=0).unison(3)

#@part10(16)
~c2 >> cs80([0, 1, 0.5],cutoff=linvar([1200, 15300], [2, 2, 8]), fshift=linvar([1, 4], 32), dec=1.0, leg=0, detune=0, lpr=0.3, bits=0, crush=1, oct=(3, PStep(4, 3, 5)), fdist=0, vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([4000, 12000], 128), glide=1, dur=1/6, shape=8, fx1=1, dist2=0, low=0).unison(3)

#@part11(8)
~c2 >> cs80([0, 1, 1],cutoff=linvar([1200, 15300], [8, 4, 8]), fshift=linvar([1, 4], 32), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=1, oct=(3, PStep(4, 3, 5)), fdist=0, vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([4000, 12000], 128), glide=1, dur=1/6, shape=8, fx1=1, dist2=0, low=0).unison(3)

#@part12(16)
c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=5, oct=(3, PStep(3, 5, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=0, dur=1/6, shape=0, fx1=0, dist2=1, low=0).unison(3)

#@part13(8)
c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 15300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=4, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.5,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([4000, 4000], 128), glide=4, dur=1/6, shape=0.5, fx1=1, dist2=4.1, low=0).unison(3)

#@part14(8)
c4 >> dbass(0, dur=[1/3, 1/3,1/6, 1/6], hpf=400, lpf=1700, hpr=0.2, dist2=3, sus=1/2, shape=0, oct=5, lofi=0).unison(2)

#@part15(16)
c2 >> cs80([0, 0, 0.5],cutoff=linvar([400, 5300], [8, 4, 8]), dec=1.0, leg=0, detune=0, lpr=0.1, bits=0, crush=5, oct=(3, PStep(4, 3, 4)), vibspeed=P[0.6,2, 0.5, 1.1], vibdepth=0.1, lpf=linvar([400, 4000], 128), glide=12, dur=1/6, shape=2.0, fx1=1, dist2=2.1, low=0).unison(3)

#@part16(16)
rec_stop()

#@endfade(16)
