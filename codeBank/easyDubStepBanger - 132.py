# easyDubStepBanger - 132
# banger
Clock.bpm=132

y1 >> wavetable( "WT_Bass" ,rate=2.0, degree=0,dur=8,  sample=7, oct=3, detune=0.2, wtpos=0, cutoff=8000, rq=0.8, wtdist=0)

l5 >> loop("dubstepbass32", dur=32, lofi=0, sample=0, mverb=0)
l5.addfx(lofi=0)

z5 >> loop("dubstepbass16", dur=16, amp=1, sample=var(PRand(909),64))
w4 >> loop("dubstepdrum32", dur=32 ,sample=4)

h1 >> loop("gbuild16", dur=16, amp=[0,1], sample=PRand(909))

f2 >> play("X.", amp=2)