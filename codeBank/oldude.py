#olddude 128
#interlude
Clock.bpm = 128
Scale.default = "minor"
j1 >> bass([12, 11, 1, 0.5, 4, _, 4, _], oct=(4, 5, 6), dur=PDur(3, 8), shape=j1.degree==2,shift=j1.degree==1,dist2=j1.degree==0.5,mverb=(j1.degree==4)/4, echo=0.5, leg=4).unison(2)
j0 >> play("g ", rate=-0.5, a=0.2, delay=4, dur=(4, 2, 1), sample=(2, 7, 8))
j2 >> varsaw(j1.degree,oct=(3, 4, 5, 6), rate=0.5, dur=1/2, dafilter=0.5, lpf=1200, mpf=1200, lpr=0.2).unison(2)
j3 >> bass([12, 11, 4],dur=1/4, amp=j1.degree==4, oct=(4, 5), leg=40, vol=1, dist2=1, shape=0.5)
j4 >> bass(P*[12, 11, 4],dur=var([1/2, 1], [3, 1]), shape=j4.dur-1/2, dafilter=0, amp=1.0, oct=var([ (4, 5, PRand([3, 4,5, 6])), 3], PRand([4, 8, 16, 32])), leg=PRand(128), vol=1, dist2=1).unison(4)
gu >> loop("cinambi8", dur=8, sample=var([3, 4, 5]), amp=0.91, fx1=0)
tv >> loop("hiphop16", dur=16, sample=[4, 7])
pe >> loop("nobledrum32", dur=32, sample=8, sbrk=0.0)
bo >> loop("dnbfx16", dur=16, sample=4, amp=0.8, fx2=1)
bf >> loop("dnbfx16", lofi=0.5, dur=16, sample=5, amp=0.8, fx2=1).unison(2)
bq >> loop("dnbfx16", dur=16, dist2=0.2, sample=6, amp=0.8, fx2=1)
