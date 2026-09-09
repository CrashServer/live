# B3 96
Clock.bpm = 96;
b7 >> organ([1, var([_, [7, _, 7, (0, 4, 2)]]), 4, 1, 2], mverb=0.8, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0,dur=1/2, leg=0, scale=Scale.minor, oct=(var([5, 4, 6]), var([8,5,6, 7]))).unison(2).sometimes("shuffle")
b8 >> donk([1, var([_, [7, _, 7, (0, 4, 2)]]), 4, 1, 2], dur=1/2, mverb=0.5, scale=Scale.minor, valad=1000, valadr=0.5, valadd=0.5, valadt=0, oct=(var([2, 3, 2]), var([8,5,6, 7])), beef=2).unison(2).sometimes("shuffle")
b6 >> dbass([1, var([1, [7, 2, 7, (0, 4, 2)]]), 4, 1, 2], lpf=400, dur=[1/2, 1/2, 1/4, 1/4],scale=Scale.minor, vakorg=8400, vakorgr=0.5, vakorgd=0.1, vakorgt=4, oct=(5, var([3,4,6, 5])), sus=[1, 1/2, 1/2]).unison(4).every(4, "shuffle")
b7 >> faim(dur=1/2, amp=PBin(16), mverb=0.5, echo=0.5, sus=1)
