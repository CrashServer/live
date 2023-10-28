# A2
Scale.default="minor"
a1 >> bass([(0, 4, 2), [V, III, II, III, II]], amp=0.5, dur=4, a=2, oct=var([5, 7, [5,4, 5]]))
a2 >> lbass((0, 4, 2) + var([2, 4]), amp=0.5, dur=var([1/2, PDur(3, 8)]), a=var([0.5, 1, 0], [8, 4, 2]))
a3 >> varsaw(dur=8, lpf=1000,mverb=0.6, a=2, oct=(5, 6, 7), hpf=200).unison(4)
