# recorded_084544
# recorded

#@intro(16)
Clock.bpm = 122
c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=0.8, cfb=0.8, sus=2, feed=0, cpitch=8, cmode=1, lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5)

#@build(16)
c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=0.8, cfb=0.8, sus=2, feed=0, cpitch=4, cmode=1, lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5)
c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=0.8, cfb=0.8, sus=2, feed=0, cpitch=4, cmode=2, lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5)

#@peak(8)
c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=0.8, cfb=0.8, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5)

#@break(8)
c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=0.2, cfb=0.8, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5)

#@drop(4)
c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=0.8, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5)

#@outro(16)
c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5)

#@part7(8)
c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5, sgate=1, sgthresh=1, sgmode=0)

#@part8(4)
c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5, sgate=1, sgthresh=1, sgmode=1)

#@part9(8)
c3 >> cs80(clouds=0.8, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5, sgate=1, sgthresh=1, sgmode=0)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=4, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.2, glide=0.1, dur=1/2, shape=0, amp=0.5)

#@part10(8)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=4, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.3, glide=0.1, dur=1/2, shape=0, amp=0.5)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=4, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.5)

#@part11(8)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=5, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.5)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=6, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.5)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=7, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.5)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=8, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.5)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=9, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.5)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.5)

#@part12(4)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.5,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)

#@part13(16)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.6,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.7,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.8,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=0, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=4, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)

#@part14(32)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=3, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=2, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.1, cut=2, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.2, cut=2, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.3, cut=2, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=2, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)

#@part15(8)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)

#@part16(4)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)

#@part17(4)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=4, rgatewave=0, beat_dur=1)

#@part18(4)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=0, beat_dur=1)

#@part19(8)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1, beat_dur=1)

#@part20(8)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1, leg=4, beat_dur=1)

#@part21(8)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=1, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)

#@part22(32)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=1, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=1, cpitch=1, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=1, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=2, cfb=1, cpitch=1, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=3, cfb=1, cpitch=1, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=1, cpitch=1, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=1, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)

#@part23(4)
c2 >> cs80(cutoff=linvar([4000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=1, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=1, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)

#@part24(16)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=1, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)

#@part25(4)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9, gdel=4, gdeltime=0.5, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.3,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)

#@part26(16)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9, gdel=4, gdeltime=0.6, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.3,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9, gdel=4, gdeltime=0.7, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.3,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9, gdel=4, gdeltime=0.8, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.3,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9, gdel=4, gdeltime=0.9, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.3,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9, gdel=4, gdeltime=1.0, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.3,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9, gdel=4, gdeltime=1.1, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.3,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9, gdel=4, gdeltime=1.1, gdelsize=0.1, gdelsprd=0.5, gdelfb=0.3,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9, gdel=4, gdeltime=1.1, gdelsize=0.2, gdelsprd=0.5, gdelfb=0.3,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9, gdel=4, gdeltime=1.1, gdelsize=0.3, gdelsprd=0.5, gdelfb=0.3,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)
c2 >> cs80(cutoff=linvar([3000, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=1, cfb=1, cpitch=4, leg=2, detune=var([0.5, 1]), oct=(4, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 1.1, 0.2, 0.4, 120, 0.1], vibdepth=0.4, glide=0.1, dur=1/2, shape=1, amp=0.9, gdel=4, gdeltime=1.1, gdelsize=0.4, gdelsprd=0.5, gdelfb=0.3,rgate=4, rgaterate=1, rgatewave=1,  beat_dur=1)

#@part27(32)
c3 >> cs80(clouds=0.7, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5, sgate=1, sgthresh=1, sgmode=0)
c3 >> cs80(clouds=0.6, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5, sgate=1, sgthresh=1, sgmode=0)
c3 >> cs80(clouds=0.5, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5, sgate=1, sgthresh=1, sgmode=0)
c3 >> cs80(clouds=0.4, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5, sgate=1, sgthresh=1, sgmode=0)
c3 >> cs80(clouds=0.3, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5, sgate=1, sgthresh=1, sgmode=0)

#@part28(8)
c3 >> cs80(clouds=0.3, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.5, subenh=4, subhfreq=1000, subhgain=1, sgate=1, sgthresh=1, sgmode=0)

#@part29(8)
c3 >> cs80(clouds=0.3, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.6, subenh=4, subhfreq=1000, subhgain=1, sgate=1, sgthresh=1, sgmode=0)
c3 >> cs80(clouds=0.3, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.7, subenh=4, subhfreq=1000, subhgain=1, sgate=1, sgthresh=1, sgmode=0)
c3 >> cs80(clouds=0.3, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.8, subenh=4, subhfreq=1000, subhgain=1, sgate=1, sgthresh=1, sgmode=0)
c3 >> cs80(clouds=0.3, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.9, subenh=4, subhfreq=1000, subhgain=1, sgate=1, sgthresh=1, sgmode=0)
c3 >> cs80(clouds=0.3, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.9, subenh=4, subhfreq=1000, subhgain=2, sgate=1, sgthresh=1, sgmode=0)

#@part30(8)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.5, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.6, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.7, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.8, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
c1 >> cs80(cutoff=linvar([400, 4000, 40, 120, 3200], [2, 1, 3, 1, 4]), dec=0.4, cut=1, cdens=0, cfb=10, cpitch=8, leg=0, detune=var([0.5, 1]), oct=(3, PStep(4, 3, 4)), cmode=1, vibspeed=P[0.5,2, 40, 0.1, 0.2, 0.4, 120, 0.1], vibdepth=0.9, glide=0.1, dur=1/2, shape=1, amp=0.9,rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)

#@part31(16)
c3 >> cs80(clouds=0.3, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.9, subenh=3, subhfreq=1000, subhgain=2, sgate=1, sgthresh=1, sgmode=0)
c3 >> cs80(clouds=0.3, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.9, subenh=2, subhfreq=1000, subhgain=2, sgate=1, sgthresh=1, sgmode=0)
c3 >> cs80(clouds=0.3, cpos=(0.1, 0.5, 1), dur=4, cdens=4, cfb=4, sus=2, feed=0, cpitch=4, cmode=(2, 1), lpf=linvar([400, 4000], [28, 4]), cgain=12, ctex=0., csize=0.1, oct=var([3, 2], 8), amp=0.9, subenh=1, subhfreq=1000, subhgain=2, sgate=1, sgthresh=1, sgmode=0)

#@part32(8)
c2.solo()

#@part33(8)
Clock.clear()
soff()
Server.clearFx()

#@part34(16)
rec_stop()

#@endfade(16)
