# recorded_032026
# recorded

#@intro(64)
l1 >> loop("wardrum16", dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120)

#@build(32)
l1 >> loop("wardrum16", dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120, resonbank=0.1, rbfreq=200, rbdecay=0.5, rbspread=1.0)

#@peak(32)
l1 >> loop("wardrum16", dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120, resonbank=0.1, rbfreq=400, rbdecay=0.5, rbspread=1.0)

#@break(32)
~l2 >> loop("rockriff_16", dur=16, sample=2, low=1, chop=var([0,P*[2,4,8]], [cyH, cyL]), chopi=var(PRand([0, .25, .5, .75]), [32]), mid=1.2, hpf=0)

#@drop(8)
~l2 >> loop("rockriff_16", dur=16, sample=3, low=1, chop=var([0,P*[2,4,8]], [cyH, cyL]), chopi=var(PRand([0, .25, .5, .75]), [32]), mid=1.2, hpf=0)

#@outro(16)
l1.stop()

#@part7(8)
~l2 >> loop("rockriff_16", dur=16, sample=13, low=1, chop=var([0,P*[2,4,8]], [cyH, cyL]), chopi=var(PRand([0, .25, .5, .75]), [32]), mid=1.2, hpf=0)

#@part8(32)
~l2 >> loop("rockriff_16", dur=16, sample=0, low=1, chop=var([0,P*[2,4,8]], [cyH, cyL]), chopi=var(PRand([0, .25, .5, .75]), [32]), mid=1.2, hpf=0)

#@part9(32)
Clock.clear()
soff()
Server.clearFx()

#@part10(16)
rec_stop()

#@endfade(16)
