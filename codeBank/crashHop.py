# crashHop
y1 >> play("<k.><..C.><-><.|B6|>", amp=5000, hpf=linvar([0,0,4000],[24,8,0]), vol=5, feed=[.25, 0, 0, ], echo=[0, 0, 0, 0.5], leg=[0, 0, PWhite(0,5)], rate=(1+PBin(262)*-2)).sometimes("trim", Cycle=[0,1,2]).every(16, "trim", 0)

o4 >> play("{[----][----][--------][--]......}", rate=PSine(64) * 0.1 + 2,amp=4020, pan=PWhite(-1, 1), sample=21)

x9 >> play("X ", dur=1/4, amp=4000, sample=7, shift=2, rate=12, echo=[0.5, 0.25], flanger=4, mverb=0.5)
x8 >> play("X ", dur=1/8, amp=4000, sample=5, shift=[2, 4], rate=12, echo=[0.5, 0.25, (1, 0.5)], flanger=4, mverb=0.5)
j6 >> jbass([0,-2], oct=4, dist2=1, dur=8, amp=3)
