# explosion 142
# mud

Clock.bpm=142
Scale.default = "minor"
Root.default = 2

j1 >> play("j", sample=PRand(16), room=1, mix=0.5, amp=1, rate=(PSine(16)/100,-0.25), echo=1, echotime=4, drive=PWhite(0,0.1), chop=PWhite(0,4), dur=16, spf=1900, spfslide=4, spfend=4000).spread()
k5 >> play(PEuclid2(3,8,"X","|=2|"), sample=1,rate=var([1,0.7],[16,2]),lpf=linvar([800,5800],[24,0]), triode=PRand(16), lpr=linvar([1,0.05],[24,0])).often("stutter", Cycle([2,3,12]), amp=1, hpf=1800).sometimes("amen")
k6 >> play("X(---=)", amp=2, sample=var([1, 2], [4, 4]))
k7 >> play("<V(-[VX])V-><--(pu)->", sample=3, amp=var([0, 1], [3, 5]), hpf=45).every(7, "stutter", Cycle([2, 3, 1, 2, 3, 4]))
b5 >> dirt(dur=PDur(3,var([4,8],[4,5])), amp=1, formant=PRand(8), formantmix=0.2, slidefrom=PWhite(-0.5,0.5), lpf=linvar([900,2500],[8,0])).spread().rarely("offadd", 1, 0.75).degrade(0.2).every(8, 'stutter', Cycle([4,8,6]),dur=1)
k8 >> play("<((X )(V )V )(( c)(C ))><  |A3| ><  H @>", amplify=var([1, 0], [8, 4]), mpf=6000, crush=1, hpf=PRand([2000,1000,4000]), slide=var([0, -1], [4]), bpm=var([128, 64, 256], [3, 1, 1]), sample=((4, 2), 3)).sometimes("shuffle")

w7 >> play("$[$$]$[$$$]", amp=1, dur=1/1, sample=PRand(4), triode=4, rate=(0.5,1,2)).every(3, "stutter")

w1 >> saw(dur=PDur(3, 8), oct=PStep(7, 4, 3), octafuz=100, lpf=linvar([200, 4000],32), lpfend=PRand([800])  +1, lpfslide=1, drive=linvar([4, 400], 64), shape=linvar([1,5], 128), mpf=20000)
w2 >> saw(dur=PDur([3, 5], [8, 16, 32]), amp=1, oct=7, chop=0, coarse=4, drive=linvar([4, 400], 64), shape=linvar([1,5], 128), mpf=17000)
w3 >> jbass(sus=[8, 6,4, 8], dur=[8, 1/4, 1/4, 1/4, 1/4, 8, 1/4, 7.75, 1/4, 1/2, 1/4, 1/2], delay=(0, 4), lpf=10, amp=1, lpfslide=(0.2, 1, 0.5), lpfend=(PWhite(200, 480), PWhite(200, 480)))
w4 >> saw(dur=PDur([3, 5], [8, 16, 32]), amp=1, oct=4, chop=128, coarse=4, drive=linvar([4, 400], 64), shape=linvar([1,5], 128), mpf=8000)