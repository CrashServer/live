# blaze
Root.default = "E"
Scale.default = "minor"
a0 >> dbass([1, var([1, [7, 2, 7, (0, 4, 2)]]), 4, 1, 2], lpf=linvar([400, 3200], 128), dur=[1/2, 1/2, 1/4, 1/4],scale=Scale.minor, vakorg=8400, vakorgr=0.5, vakorgd=0.1, vakorgt=4, oct=(5, var([3,4,6, 5])), sus=[1, 1/2, 1/2]).unison(4).every(4, "shuffle")
b8 >> donk([1, var([_, [7, _, 7, (0, 4, 2)]]), 4, 1, 2], dur=1/2, mverb=0.5, scale=Scale.minor, valad=1000, valadr=0.5, valadd=0.5, valadt=0, oct=(var([2, 3, 2]), var([8,5,6, 7])), beef=2).unison(2).sometimes("shuffle")
a1 >> organ([1, var([_, [7, _, 7, (0, 4, 2)]]), 4, 1, 2], mverb=0.8, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0,dur=1/2, leg=4, scale=Scale.minor, shape=1, oct=(var([5, 4, 6]), var([8,5,6, 7]))).unison(2).sometimes("shuffle")
a0.leg=4
a8 >> play("p.", dur=1/2, lpf=3400, amp=var([0, 1], [24, 8]), room2=0.2, damp2=1, sample=0, revus=8, shape=0.1, echo=[0.05, 0.25], echotime=x3.dur).sometimes("stutter", 2, rate=2, amp=0.5, dur=1/4)
a9 >> play("p.", dur=1/4, leg=12,lpf=linvar([800, 1400], 32), sample=0, room2=0.1, damp2=0, revus=2, shape=0, amp=[0.5, 0.7], echo=[0.05, 0.25], echotime=a1.dur).often("stutter", 2, rate=4, amp=1, dur=1/2).sometimes("stutter", 16)
drop()
a4 >> loop("nsbreak16", sample=3, dur=16, amp=2)
