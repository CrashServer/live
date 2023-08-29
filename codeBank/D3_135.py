Clock.bpm = 135;
d1 >> dbass(PDur([3, 5, 7], 11), dur=PDur([3, 7, 5], 11), shift=(var([0, 0.5, 1, 1]), 0), leg=128, fmod=0, spr=0.1,spf=(10, (2500, 12)), spfslide=(0.1, 1), spfend=(10000, (10, 12500)), echo=var([0.25, 0.5, 0.75, 1]), hpf=(200, 1200)).unison(4)
d1.hpf=0
d1.mverb=0.5
d1.dist2=0.2

d1.mverb=0
d1.often("shuffle")
d1.sus=1
d1.oct=5
d1.lpf=400
d1.lpr=0.2

d1.dur=4
d1.dist2=0
d1.sus=4

d2 >> play("X ")
d3 >> dbass(PDur([3, 5, 7], 11), dur=PDur([3, 7, 5], 11), shift=(var([0, 4, 1, 1]), 0), leg=0, fmod=0, spr=0.1,spf=(10, (2500, 12)), spfslide=(0.1, 1), spfend=(100, (10, 1250)), echo=var([0.25, 0.5, 0.75, 1]), hpf=(2000, 1200), dist2=1).unison(4)
