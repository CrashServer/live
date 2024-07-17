Clock.bpm = 128
Scale.default = "minor"
j1 >> bass([12, 11, 1, 0.5, 4, _, 4, _], oct=(4, 5, 6), dur=PDur(3, 8), shape=j1.degree==2,shift=j1.degree==1,dist2=j1.degree==0.5,mverb=(j1.degree==4)/4, echo=0.5, leg=4).unison(4)
j0 >> play("g ", rate=-0.5, a=0.2, delay=4, dur=(4, 2, 1), sample=(2, 7, 8))
j2 >> varsaw(j1.degree,oct=(3, 4, 5, 6), rate=0.5, dur=1/2, dafilter=0.5, lpf=1200, mpf=1200, lpr=0.2).unison(4)
j3 >> bass([12, 11, 4],dur=1/4, amp=j1.degree==4, oct=(4, 5), leg=40, vol=1, dist2=1)
j4 >> bass(P*[12, 11, 4],dur=var([1/2, 1], [3, 1]), shape=j4.dur-1/2, dafilter=0.1, amp=0.7, oct=var([ (4, 5, PRand([3, 4,5, 6])), 3], PRand([4, 8, 16, 32])), leg=PRand(128), vol=1, dist2=1).unison(4)

