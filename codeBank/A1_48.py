# A1_48

Clock.bpm = 48;
a1 >> play("#", dur=8, delay=3.5, feed=0.5, mverb=0.4, amp=2, echo=0.5)
a2 >> play("#", dur=8, feed=0.3, sample=2, delay=0, rate=-1)
a3 >> play("g", dur=8, delay=4.5, feed=0.5, mverb=0.4, amp=1, echo=0.5, lpf=400, lpr=0.1).unison(2)
a4 >> play("e", dur=PDur(3, 8), delay=6, feed=0.7, mverb=0.4, amp=1, echo=0.5, lpf=4000, lpr=0.1).unison(2)

a7 >> play("[ee]", dur=8, slide=var([0, 1]), delay=5.5, feed=0.7, sample=2, rate=-1, mverb=0.4, amp=1, echo=0.25, lpf=4000, lpr=0.1).unison(2)
a8 >> play("[tr]", dur=8, slide=var([0, 1]), delay=0.5, feed=0.7, sample=var([3, 4, 5]), rate=P*[2, 4, 8], mverb=0.4, amp=1, echo=0.25, lpf=4000, lpr=0.1).unison(2)
a_all.feed=0.1
a_all.stop()
a_all.dur=1
