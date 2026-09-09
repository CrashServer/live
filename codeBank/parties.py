# parties 170
# acid

#G1 - 170
Clock.bpm = 170
g1 >> lbass( var([ (4, [-4, 0]), [0,P*[7,8,10,[12,_]]]]), cut=(0.1, 1), dist2=0.5 ,r=PGauss(1, 0.2), cutoff=(200, 1600), dur=PRand([1/4, 1/2, 1/2, 1, 1/4]), submix=1, scale=Scale.minorPentatonic).unison(3).sometimes("stutter", oct=6)
g2 >> lbass(dur=1/2, dist2=4, a=0.24, amp=1, hpf=P*[1200, 1888, 3000])
g1.amp=var([1, 0], [16, 8, 8])
g3 >> lbass(dur=2, submix=linvar([0, 1], 32), cut=PRand([0.5, 0.25, 1, 2]))
g4 >> lbass([ [2, 4, 5], 4, [-4, 2, 4, 5]], amp=1-(g1.amp), dur=P*[4, 1/2], sus=g4.dur, r=4, hpf=400, chop=PRand([1, 2, 4, 8]), chopmix=P*[0, 0.5], cutoff=PWhite(1000, 8000), oct=(7, 6), scale=Scale.minorPentatonic).unison(2)
g3.amp=PWhite(0.1, 1)
g5 >> lbass([12, 4, 5], dur=2, sus=P*[g5.dur, g4.dur], r=[4, 0.1], chop=PRand([1, 2, 4, 8]), oct=var([4, 5, 6, 7, 8]), scale=Scale.minorPentatonic)
g6 >> tb303(melody(),dur=1/8, lpf=1200, oct=7, top=linvar([400, 16000]), shift=1, cutoff=400, scale=Scale.minorPentatonic).unison(2)
# [truncated in source] g1 >> lbass((4, [-4, 0]), dist2=var([0.5, 0.1]),r=PGauss(1, 0.2), amp=var([1, 0], [2, 6]), cutoff=(200, linvar([1200, 6400], 8)), dur=var( [ PRand([1/4, 1/

Clock.bpm = 98

Master().lpf=var([0, 4000, 6000, 15000], [24, 4, 2, 2])
Master().hpf=var([0, 20, 30, linvar([3200, 6400], 32)], [24, 4, 2, 2])
Master().cut=var([0, 1, 1/2, linvar([1/4, 1], 32)], [24, 4, 2, 2])

i0 >> loop("choir8", dur=16, mverb=1, amp=[0.3, 0.5, 0.4, 0.7], shift=(0.5, (1, 1.5)), dubd=0.5, chop=4, dublen=0.5)
i1 >> brown(lpf=400, a=PWhite(1, 2), dur=8, echo=0.5, delay=2, echotime=8, chop=4, lpr=0.1, hpf=0)
i2 >> pink(lpf=1200, dur=1, echo=P*[0.5, 1, 2, 4], delay=0.5, pan=PWhite(-1, 1), shift=(2, 1), echotime=2, chop=var([PWalk(8, 1, 1), 4]), lpr=PWhite(0.02, 0.1), hpf=linvar([2000, 4000]))
i3 >> loop("intro8", shift=PWhite(4, 2), dur=8, delay=4, vol=P*[0, 0.2, 0], dist2=0, revsus=0, sample=3, mverb=0, mverbdiff=PRand(5), amp=P*[0.2, 0.5, 0, 1,0])
i4 >> loop("intro8", shift=PWhite(0.5, 1.5), dur=[(16, 8), 4], dist2=1, revsus=0, sample=2, mverb=0.5, mverbdiff=PRand(5), amp=P*[0, 4, 1, 0, 0, 1])
i5 >> loop("psych32", dur=32, sample=3, amp=[0.5, 0.5,0.5, 1], feed=0.5, shift=1, krush=4, bits=2)

#################
Clock.bpm = 98;
i0 >> loop("dub8", dur=16 , formant=0, sample=2, amp=[0, 1, 0, 0 ], cut=2, high=12, low=0, hpf=15000, leg=40).brk(1)
i1 >> loop("cyber8", dur=8, sample=5, amp=P*[0, 1, 0, 1 ], cut=2, high=24, low=0, med=8, hpf=2000, leg=40).brk(1)
i2 >> loop("cyber8", dur=8, sample=2, amp=P*[0, 0, 1, 1 ], shift=2, dist2=0, cut=0, high=12, low=0, hpf=400, mverb=1).brk(2)
i3 >> loop("hiphop8", dur=(8, 4), sample=3, echo=0, mverb=0, spf=4000, spfend=600, spfslide=4, leg=0, amp=[1, 1, 0.4, 1, 0, 0.2], shift=(1, 2), dist2=0.1, hpf=800).unison(2)
i4 >> loop("nshits16", dur=16, sample=4, amp=[1, 0.3, 1, 1, 1.2], shift=[0, 1], hpf=1000, hpr=0.9).unison(2)
i5 >> loop("nsbass8", dur=16, sample=2, amp=[1, 0.3, 1, 1, 1.2], shift=0, hpf=1000, lpf=2000, hpr=0.9, mverb=0.2).unison(2)
i0 >> loop("nsbreak16", dur=16, sample=2, amp=[1, 0.5, 1, 0.4, 1], shift=[0, 1], low=4, hpf=100, hpr=0.9).unison(2)
i6 >> loop("techfx4", dur=8, shape=1,sample=2, amp=P*[0, 1], rate=4, cut=2, high=0, med=4, low=4).brk(1)
i7 >> loop("impulse32", dur=16, sample=0, amp=[1, 0, 2, 0.2])
i8 >> loop("ragedrum16", dur=16, dist2=0.5, sample=6, amp=[0, 1, 0.5, 1, 1], shift=[0, 1], hpf=100, hpr=0.9).unison(2)

x7 >> play("(...(.p)).((p.)c(p.).)((p.).(p.).)", dur=1/4, sample=4)
x8 >> play("x(x.).(x[.x])", dur=1, sample=3)
x9 >> play("(.......p).(pcp..c..)(p.p.....)", dur=1/4)
x0 >> play("(t.)..(.t.(T.))", dur=1/2)
