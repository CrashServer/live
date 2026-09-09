# dereliction 90
# reisub

Clock.bpm=90
Scale.default="minor"
Root.default=6

a1 >> sinepad((0,4), formant=PRand(6), flanger=expvar([0.1,0.4],3489), fdecay=linvar([0.4,2],1248), drive=0.1, oct=(3,4,5), dur=8, room=1, mix=0.7, amp=2, chop=1.6, chopwave=PRand(8)).spread()
w2 >> sawbass(PWhite(0,0.3), dur=PDur(var([5,7],[6,2]),8,3), cutoff=PRand(190,1580), oct=(4,5,[6,7]), amp=1)

d4 >> play("r r r [rr] r ", dur=1/4, rate=PRand(2,7), pan=[-1,0.5,0,-0.5,1], formant=0, sample=3)

d6 >> play("..o.", lpf=4000, crush=5, room=1, mix=[0,0.2,0.4], delay=PWhite(-0.1,0.1)).often("stutter", Cycle([2,4,3,6,5,2]), amp=PWhite(0.5,1.1), rate=PWhite(1,2))
d5 >> play("..t.", rate=(1,3))

a1 >> bell((0,4), formant=PRand(6), flanger=0, fdecay=linvar([0.4,2],1248), drive=0, oct=(4,5,6), dur=8, room=1, mix=0.7, amp=3, chop=8, chopwave=PRand(8)).unison(2) + (0,var([-2,-4,-3,-1],8))
y1 >> pasha(a1.degree, oct=(4,5), dur=PDur(var([2,3,4,5],[5,1,1,1]),8), amp=0.5, sus=y1.dur*PWhite(0.5,1.2), echo=var([0.5,[0.125,0.25,0.75]],[6,2])).unison(3)

k1 >> play("<X.><..o.><..U(.(...O))><[---]><(.:))><[++]>", lpf=3400, amp=2)