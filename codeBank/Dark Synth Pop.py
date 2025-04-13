# Dark Synth Pop
Scale.default="dorian"
r8 >> donorgan(var([6,5,3,1],[8,4,2,2]), oct=6, cutoff=2600, dur=PDur(3,8), sus=1, blur=2, pong=0, beat_dur=1, pongtime=1, mverb=.2, dist2=.4).unison(3)
e2 >> lbass(var([0,5,6],[8,4,4]), dur=1/2, oct=5, cutoff=PFr(1400, 4000, 512), tone=.8) + var([0, P*[-1,0,1]], [7,1])

o5 >> play("<x-><..><..o.><|k0|.>", sample=7, amp=2).sometimes("stutter")
k4 >> play("X.", amp=2)
