# recorded_031843
# recorded

#@intro(64)
l1 >> loop("wardrum16", lpf=1200, dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120)

#@build(16)
l1 >> loop("wardrum16", lpf=1200, dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120, lpr=0.2)

#@peak(16)
l1 >> loop("wardrum16", lpf=1200, dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120, lpr=0.2, echo=0.5)

#@break(8)
l1 >> loop("wardrum16", lpf=2400, dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120, lpr=0.2, echo=0.5)

#@drop(16)
l1 >> loop("wardrum16", lpf=2400, dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120, lpr=0.3, echo=0.5)

#@outro(16)
l1 >> loop("wardrum16", lpf=2400, dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120, lpr=0.3, echo=0.25)

#@part7(32)
l1 >> loop("wardrum16", lpf=2400, dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120, lpr=0.3, echo=0.25, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1)

#@part8(32)
l1 >> loop("wardrum16", lpf=2400, dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120, lpr=0.3, echo=0.25, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, leg=32)

#@part9(32)
l1 >> loop("wardrum16", lpf=0, dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120, lpr=0.3, echo=0.25, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, leg=32)

#@part10(16)
l1 >> loop("wardrum16", lpf=0, dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120, lpr=0.3, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, leg=32)

#@part11(32)
~l2 >> loop("rockriff_16", dur=16, sample=2, low=1, chop=var([0,P*[2,4,8]], [cyH, cyL]), chopi=var(PRand([0, .25, .5, .75]), [32]), mid=1.2, hpf=0)

#@part12(16)
Clock.clear()
soff()
Server.clearFx()

#@part13(16)
rec_stop()

#@endfade(16)
