#olddude 128
#interlude #todo

Clock.bpm = 128
Scale.default = "minor"
j1 >> bass([12, 11, 1, 0.5, 4, _, 4, _], oct=(4, 5, 6), dur=PDur(3, 8), shape=j1.degree==2,shift=j1.degree==1,dist2=j1.degree==0.5,mverb=(j1.degree==4)/4, echo=0.5, leg=4, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1).unison(2)
j0 >> play("g ", rate=[-0.5, 0.5,1, -1], a=0.2, delay=4, dur=(4, 2, 1), sample=(2, 7, 8), bitrot=1, rotbits=8, rotrate=0.5, rotjitter=0.1)
j3 >> bass([12, 11, 4],dur=1/4, amp=j1.degree==4, oct=(4, 5), leg=40, vol=1, dist2=2, shape=0.5, cheapverb=0.2, cvdecay=0.5, cvdamp=0.5)
~j2 >> loop("hiphop16", dur=16, sample=[4, 7])
j4 >> bass(P*[12, 11, 4],dur=var([1/2, 1], [3, 1]), shape=j4.dur-1/2, dafilter=1, amp=1.0, oct=var([ (4, 5, PRand([3, 4,5, 6])), 3], PRand([4, 8, 16, 32])), leg=PRand(128), vol=1, dist2=1, tape=1, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1).unison(4)

u3 >> compperc(tone=0.6, noise=4, comp=5,drive=4, ring=0.25, metal=12, body=0.4, bend=1.3)
pe >> loop("nobledrum32", dur=32, sample=8, sbrk=0.0)

bo >> loop("dnbfx16", dur=16, sample=4, amp=0.8, fx2=1)
bf >> loop("dnbfx16", lofi=0.5, dur=16, sample=5, amp=0.8, fx2=1).unison(2)
bq >> loop("dnbfx16", dur=16, dist2=0.2, sample=6, amp=0.8, fx2=1)

v4 >> play("X:")
j1.stop()
j2 >> a_vpad(j1.degree,oct=(3, 4, 5, 6), rate=4, dur=1/2, dafilter=2, amp=2, lpf=6400, mpf=1200, lpr=0.1).unison(2)
j4 >> subbass(P*[12, 11, 4],dur=var([1/2, 1], [3, 1]), shape=j4.dur-1/2, dafilter=1, amp=1.0, oct=var([ (4, 5, PRand([3, 4,5, 6])), 3], PRand([4, 8, 16, 32])), leg=PRand(128), vol=1, dist2=1, tape=1, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1).unison(4)





# j4 >> alva()


j1.stop()


# j1 >> acidline(oct=3)
