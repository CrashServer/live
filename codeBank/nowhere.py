#hereisnowhere
d4 >> dbass(0,feed=0.5, echo=[0.2, 0.4, 0.3, 0.6], dur=8, dubd=0.4, sus=8, dublen=0.1, mverb=0.5, dubl=0.1, lpr=0.2, dafilter=2400, lpf=linvar([200, 1200], 32), oct=(6, 5, 4), shape=0.7, dist2=0.9, valad=1500, valadr=0.5, valadd=5, valadt=0, valadc=0.3)
d9 >> play("X ", lpf=2400, amp=4, sample=3, leg=1, lofi=0)
d5 >> dbass([4, 5, 6] ,dur=1/2, oct=7).unison(8) + var([0, 3], 8)

#merge with gesa code
