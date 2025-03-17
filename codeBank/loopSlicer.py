# loopSlicer
mydur = 16
note= PWhite(0,mydur).rnd(.25)[:4]
u7 >> loop("losthighway16", note, sample=1, dur=2, cut=2/mydur, sus=mydur, a=0, r=0, hpf=0, comp=1, valad=3500, valadr=0.8, valadd=15, valadt=0, valadc=0.3, mverb=0)
r9 >> play("<x.><....>", sample=4, comp=1, amp=3, cut=1).sometimes("stutter")
