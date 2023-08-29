# A1_48A
Clock.bpm = 48;
a1 >> bass([(0, 4, 2), [V, III, II, III, II]], dur=4, scale=Scale.minor, a=2, oct=var([5, 7, [5,4, 3]]))
a2 >> lbass((0, 4, 2) + var([2, 4]), dur=var([1/2, PDur(3, 8)]), scale=Scale.minor, a=var([0.5, 1, 0], [8, 4, 2]))
a4 >> varicelle(dur=4, oct=4, hpf=4000).unison(4)
a5 >> varsaw(dur=2, lpf=200, formant=0.0,mveb=0.6, oct=(5, 4, 6), hpf=4000).unison(4)
a5 >> bass([1, var([1, [7, 2, 7, (0, 4, 2)]]), 4, 1, 2], dur=1/2, scale=Scale.minor, oct=(5, var([8,5,6, 7]))).unison(2)
