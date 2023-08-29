# B2_96A
Clock.bpm = 96;
######################### ################ #####################
Scale.default = "chromatic"
b1 >> bass(-4, oct=6, dur=1/4, lpr=0.01, lpf=4000).human(40, 0, 0).unison(4).every(1, "offadd", PWhite(0, 1)).sometimes("offadd", PWhite(0.2, 1)).often("stutter", 1, fold=1).sometimes("offadd", 4)
b2 >> bass(8, oct=[5, 5], dur=PDur(3, 8), echo=0.5, hpf=2000, hpr=0.3).slider().sometimes("offadd", 4)
b3 >> feel([-4, 8, 18], oct=(4, 3), dur=PDur(3, 12), sus=4, amp=PWhite(0, 1), pan=PWhite(-1, 1)).unison(2).slider()
superbass = SynthDef("superbass")
b4 >> superbass((15, 20), dur=var([1, 1/8, 1/4, 1/8, 1, 1/8, 1/4, 1/2], [2, 1/4]), amp=0.25)
b5 >> feel(33, dur=PDur(11, 15), amp=[0, 0.4], hpf=PWhite(200, 2000))
b4 >> tb303([-4, 8], dur=1/4, oct=(3, 4, 2), leg=0, delay=0.5)
b5.oct=2
b5 >> play(": ")
b7 >> play("-oCc").sometimes("stutter", rate=(0.5, 2))
