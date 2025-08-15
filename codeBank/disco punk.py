# disco punk
Clock.bpm =192
Scale.default="minor"
b5 >> superbass([0,4,5,[2, PRand(-2,9)]], dur=1/2, cutoff=PFr(1900,4000), rq=0.3, rqd=0.5, detune=0.5, fdecay=5, sub=1, amp=0.7, hpf=200, mverb=0.7, mverbmix=0.3).unison(3)
e5 >> lbass(var([0, -2, -4, -3], 8) + var([0, -1],[7,1]), oct=(5), dur=1/2, cutoff=PFr(1900,6200), tone=linvar([0.3, 0.9], 33), rel=0.11, hpf=50)
x5 >> play("<kku(...({.u[uu]}))><.->", drcomp=0.5)
a5 >> play("X.", amp=1)
