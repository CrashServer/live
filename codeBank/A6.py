#A6
Clock.bpm = 170
a1 >> play("[--]. ", hpf=4000 + PRand(-400, 400), mpf=8000, delay=(0, [0,0.25], 1.25), echo=(0.5, 0.25), sample=(3, var([0, (5, 2)]), 5)).sometimes("stutter", degree="[--.:]", sample=1, a=0.1, rate=(1,2))
a2 >> play("--", delay=(0.25,0.5), a=PWhite(0, 0.5)).sometimes("stutter", degree="[c-.-]", sample=4, a=2)
a7 >> play("a ", sample=4, shift=(0, 0.5), feed=0.5, tremolo=4, dur=8, delay=4, lpf=1200, room2=1, damp2=0, revus=8, shape=0.2, amp=0.5, spf=400, spfslide=1, spfend=3200, echo=(0.025,0.25), echotime=8)
a8 >> play("p.", dur=1/2, lpf=1400, amp=1, room2=0.2, damp2=1, sample=0, revus=8, shape=0.1, echo=[0.05, 0.25], echotime=x3.dur).sometimes("stutter", 2, rate=2, amp=0.5, dur=1/4)
a9 >> play("p.", dur=1/4, leg=12,lpf=linvar([800, 1400], 32), sample=0, room2=0.1, damp2=0, revus=2, shape=0, amp=[0.5, 0.7], echo=[0.05, 0.25], echotime=a1.dur).often("stutter", 2, rate=4, amp=1, dur=1/2).sometimes("stutter", 16)
a6 >> play("x ", dur=8, lpf=400, room2=0, damp2=0, revus=8, shape=4, echo=0.05, echotime=8, mverb=0.5)
a7 >> play("//", mverb=0.5, dur=32, sample=1)
a_all.sample=var([7, 0], [4, 28])
