# disco punk 192
# Banger

#@start(32)
Clock.bpm =192
Scale.default="minor"
b5 >> compkick([0,4,5,[2, PRand(-2,9)]], dur=1/2, cutoff=PFr(1900,4000), rq=0.6, rqd=0.5, detune=0.5, fdecay=2, rgate=0.5, oct=5, sub=0, amp=0.7, hpf=200, mverb=0.0, mverbmix=0.3).unison(3)
#@bass(32)
e5 >> lbass(var([0, -2, -4, -3], 8) + var([0, -1],[7,1]), oct=(5), dur=1/2, cutoff=PFr(1900,6200), tone=linvar([0.3, 0.9], 33), rel=0.11, hpf=50, shimmer=0.8, shimsize=0.6, shimpitch=0.5, shimmix=0.5)
#@drums(64)
x5 >> play("<kku(...({.u[uu]}))><.->", drcomp=0.5, hpf=1200, leg=4)
#@kick(64)
a5 >> play("k.", amp=1, sample=4, echo=[0.5, 0.25])
#@variation(32)
b5 >> compkick([0,4,5,[2, PRand(-2,9)]], dur=1/2, cutoff=PFr(1900,4000), rq=0.2, rqd=0.8, detune=0.5, fdecay=2, rgate=0.9, drift=0.5, low=0, oct=(5, 4, 6), sub=0, amp=1.4, hpf=200, mverb=0.0, mverbmix=0.3).unison(3)
#@comp(64)
b5.fdecay=linmod(1,7, 64, 5)
b5 >> compkick([0,4,5,[2, PRand(-2,9)]], shape=fb(128, 0.1, 0.8), dur=1/2, cutoff=PFr(1900,4000), rq=0.2, rqd=0.8, detune=0.5, fdecay=2, rgate=0.9, drift=0.5, low=0, oct=(5, 4, 6), sub=0, amp=1.6, hpf=200, mverb=0.0, mverbmix=0.3).unison(3)
