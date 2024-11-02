#summer
Clock.bpm = 132
Scale.default = "chromatic"
b2 >> click([(-9, 6),6,6,6,6,4, 5, 6], oct=PStep(12, 3, 4), hpf=PRand(2000),  sus=b2.dur, dur=[1/4, 1/2, 1/2, 1/2, var([1/2, 1/4]),1/2, 1/4], mverb=0.0, shape=0.0,cut=linvar([[2, 4], 1/4], 128), echo=var([ 0.025, 0.05], 16), octer=1, leg=0,  octersub=2, octersubsub=var([2, PRand(15,2222)], [15, 1])).unison(4).sometimes("stutter", 9).slider() + var([0, 0.5])
b2 >> donk()
e2 >> abass(var([([7, 0], 0), [(12, 0), ([6, 0], 0), (0, [12, 7])]]),oct=(4, PStep(16, 3, 5)), dur=[4, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2], leg=linvar([0, 4], 32), scale=Scale.chromatic, drive=PWhite(0.0, 0.1), hpf=50, hpr=(0.1, 0.9))
b2 >> nylon()
b2 >> click()
b2.leg=5
e2 >> play("-")
