# B2_96
Clock.bpm = 96;

setseed(42)
b1 >> dbass([(0, 4, 2), V], dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), scale=Scale.minor, oct=var([5, 7]), valadd=0.2, valad=400, valadr=0.7)

b3 >> lbass((0, 4, 2) + var([2, 4]), dur=var([1/2, PDur(3, 8)]), scale=Scale.minor)
e4 >> bass(melody(),dur=4, leg=4, oct=5, hpf=4000).unison(4).slider()

b5 >> varsaw(melody(),dur=2, lpf=200, formant=0.0,mveb=0.6, oct=(5, 4, 6), hpf=4000).unison(4)
b3 >> bass([1, var([1, [7, 2, 7, (0, 4, 2)]]), 4, 1, 2], dur=1/2, scale=Scale.minor, echo=1, oct=(5, var([8,5,6, 7]))).unison(2)
~b3 >> lbass((var([0, 4, 2, 0, 4, 7, 6], [2, 1, 2]), 4, 2) + var([2, 4]), dur=var([1/2, PDur(3, 8)]), scale=Scale.minor).unison(4)
a
