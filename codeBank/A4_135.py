Clock.bpm = 135;
Scale.default = Scale.minorPentatonic
Root.default = "G"
a1 >> dafbass([0, 1, 7, 7, 5, 4, 5, 5], dur=PDur(4,8), oct=[4, 5, 5], shape=0, fmod=2, lpf=linvar([200, 8000], [24, 8]), sus=[1, 1/2, 1/2, 1]).rarely("offadd", var([4, 9])).unison(4)


