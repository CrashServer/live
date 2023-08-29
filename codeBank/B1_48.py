Clock.bpm = 48;
a_all.stop()
b1 >> play("sC(cq)", sample=9, mid=1, dur=1/4, echo=0.5, hpf=100).often("stutter", amp=1.5, hpf=400, mverb=0.1)
b2 >> play("(x..[xx])[..]-(O.)", dist2=1)
b3 >> play("(t..[T])[.[.]]-(cx.)", dist2=1, dur=1/8).often("stutter", rate=4)
a1.dur=1
b_all.dur=1/2
