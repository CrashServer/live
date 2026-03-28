# blaze 122
# epic


#not really epic, but need a category
Root.default = "E"
Scale.default = "minor"
a0 >> dbass([1, var([1, [7, 2, 7, (0, 4, 2)]]), 4, 1, 2], lpf=linvar([400, 3200], 128), dur=[1/2, 1/2, 1/4, 1/4],scale=Scale.minor, vakorg=8400, vakorgr=0.5, vakorgd=0.1, vakorgt=4, oct=(5, var([3,4,6, 5])), sus=[1, 1/2, 1/2]).unison(4).every(4, "shuffle")
c9 >> donk([1, var([_, [7, _, 7, (0, 4, 2)]]), 4, 1, 2], dur=1/2, mverb=0.5, scale=Scale.minor, valad=1000, valadr=0.5, valadd=0.5, valadt=0, oct=(var([2, 3, 2]), var([8,5,6, 7])), beef=2).unison(2).sometimes("shuffle")

a1 >> organ([1, var([_, [7, _, 7, (0, 4, 2)]]), 4, 1, 2], mverb=0.8, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0,dur=1/2, leg=4, scale=Scale.minor, shape=0, oct=(var([5, 4, 6]), var([8,5,6, 7]))).unison(2).sometimes("shuffle")
a0.leg=4
a8 >> play("p.", dur=1/2, lpf=3400, amp=var([0, 1], [24, 8]), room2=0.2, damp2=1, sample=0, revus=8, shape=0.1, echo=[0.05, 0.25], echotime=x3.dur).sometimes("stutter", 2, rate=2, amp=0.5, dur=1/4)
a9 >> play("p.", dur=1/4, leg=12,lpf=linvar([800, 1400], 32), sample=0, room2=0.1, damp2=0, revus=2, shape=0, amp=[0.5, 0.7], echo=[0.05, 0.25], echotime=a1.dur).often("stutter", 2, rate=4, amp=1, dur=1/2).sometimes("stutter", 16)
drop()
a4 >> loop("nsbreak16", sample=3, dur=16, amp=2)


#@intro(32)
Root.default = "E"
Scale.default = "minor"
a0 >> dbass([1, var([1, [7, 2, 7, (0, 4, 2)]]), 4, 1, 2], lpf=linvar([400, 3200], 128), dur=[1/2, 1/2, 1/4, 1/4],scale=Scale.minor, vakorg=8400, vakorgr=0.5, vakorgd=0.2,oct=(5, var([3,4,6, 5])), sus=[1, 1/2, 1/2]).unison(4).every(4, "shuffle")

#@build(16)
a0 >> dbass([1, var([1, [7, 2, 7, (0, 4, 2)]]), 4, 1, 2], lpf=linvar([400, 3200], 128), dur=[1/2, 1/2, 1/4, 1/4],scale=Scale.minor, vakorg=2400, vakorgr=0.5, vakorgd=0.2,oct=(5, var([3,4,6, 5])), sus=[1, 1/2, 1/2]).unison(4).every(4, "shuffle")

#@peak(32)
c9 >> donk([1, var([_, [7, _, 7, (0, 4, 2)]]), 4, 1, 2], dur=1/2, mverb=0.5, scale=Scale.minor, valad=1000, valadr=0.5, valadd=0.5, valadt=0, oct=(var([2, 3, 2]), var([8,5,6, 7])), amp=2, beef=2).unison(2).sometimes("shuffle")

#@break(32)
a0.lpf=1600
a0.gdel=0
a0.oct=5

#@drop(32)
a0.lpf=1600
a0.gdel=0
a0.oct=5

#@outro(16)
a0 >> dbass([1, var([1, [7, 2, 7, (0, 4, 2)]]), 4, 1, 2], lpf=linvar([400, 3200], 128), dur=[1/2, 1/2, 1/4, 1/4],scale=Scale.minor, vakorg=2400, vakorgr=0.5, vakorgd=0.2,oct=(5, var([3,4,6, 5])), sus=[1, 1/2, 1/2]).unison(4).every(4, "shuffle")

#@part7(8)
~a0 >> dbass([1, var([1, [7, 2, 7, (0, 4, 2)]]), 4, 1, 2], lpf=linvar([400, 3200], 128), dur=[1/2, 1/2, 1/4, 1/4],scale=Scale.minor, vakorg=2400, vakorgr=0.5, vakorgd=0.2,oct=(5, var([3,4,6, 5])), sus=[1, 1/2, 1/2]).unison(4).every(4, "shuffle")

#@part8(32)
a1 >> organ([1, var([_, [7, _, 7, (0, 4, 2)]]), 4, 1, 2], mverb=0.8, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0,dur=1/2, leg=4, scale=Scale.minor, shape=0, oct=(var([5, 4, 6]), var([8,5,6, 7]))).unison(2).sometimes("shuffle")

#@part9(16)
a0.lpf=1600
a0.gdel=0
a0.oct=5

#@part10(8)
a0.oct=4

#@part11(16)
a0.hpf=400

#@part12(4)
a8 >> play("p.", dur=1/2, lpf=3400, amp=var([0, 1], [24, 8]), room2=0.2, damp2=1, sample=0, revus=8, shape=0.1, echo=[0.05, 0.25], echotime=x3.dur).sometimes("stutter", 2, rate=2, amp=1, dur=1/4)

#@part13(8)
a0.hpf=400

#@part14(4)
a0.hpf=0

#@part15(4)
a8 >> play("p.", dur=1/2, lpf=3400, amp=var([0, 1], [24, 8]), room2=0.2, damp2=1, sample=0, revus=8, shape=0.1, echo=[0.05, 0.25], echotime=x3.dur).sometimes("stutter", 2, rate=2, amp=1, dur=1/4)

#@part16(4)
a1.oct=4

#@part17(16)
drop()

#@part18(32)
a4 >> loop("nsbreak16", sample=PRand(8), dur=16, amp=2)

#@part19(16)
a4 >> loop("nsbreak16", sample=PRand(8), dur=16, amp=2).lclip(1)

#@part20(16)
a4 >> loop("nsbreak16", sample=PRand(8), dur=16, amp=2).lclip(4)

#@part21(16)
a4 >> loop("nsbreak16", sample=PRand(8), dur=16, amp=2).lclip(2)

#@part22(8)
a4 >> loop("nsbreak16", sample=PRand(8), dur=16, amp=2).lclip(0.25)

#@part23(32)
a4 >> loop("nsbreak16", sample=PRand(8), dur=16, amp=2).lclip(5)
