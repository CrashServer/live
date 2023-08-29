Clock.bpm = 120;
b1 >> bass([(0, 4, 2), V], dur=var([PDur(var(PRand(2,7),PRand(2,8)),8),8],[24,8]), scale=Scale.minor, oct=var([5, var([PRand([4, 5, 6, 7])])]))
b1.slider()
b3 >> lbass((0, 4, 2) + var([2, 4]), dur=var([1/2, PDur(3, 8)]), scale=Scale.minor)
b3 >> bass([1, var([1, [7, 2, 7, (0, 4, 2)]]), 4, 1, 2], leg=4, dur=1/2, scale=Scale.minor, echo=1, oct=(5, var([8,5,6, 7]))).unison(2)


b1.dur=1/2