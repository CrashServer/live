# break the wave - 132
Clock.bpm=132

g1 >> wavetable("WT_Metallic", rate=PTuple(PWhite(0.0,10.0), 3), degree=var(PTime(), [8]), dur=8, oct=(4,2,3), sample=var(PRand(999),64), detune=0.7, wtpos=0, cutoff=PRand(200,3000), rq=PTuple(PWhite(0.01,.1), 3), wtdist=.4, wshape=4, wgain=1, wmix=0.5, amp=0.7, wide=1, mverb=PWhite(.2, 0.9), leg=PWhite(0,4), csweep=P*[0,0,0,0.5], cswfreq=PRand(20, 220), cswdepth=0.08, cswrate=PWhite(.015,.9), cswdecay=0.5, blur=P*[1,2,0.5]).unison(3)

t8 >> loop("breakcore155_16", dur=16, sample=var([PRand(999)], [64]), drcomp=.5, amp=2, sbrk=0.5, t_reset=0, sbrkdur=0.5, sbrkmix=1.0)
t9 >> loop("breakcore160_16", dur=16, sample=var([PRand(339)], [64]), drcomp=.5, amp=2, sbrk=0, t_reset=0, sbrkdur=.25, sbrkmix=1.0)

n3 >> play("X.", amp=2, lpf=2400)
