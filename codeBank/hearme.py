#HEAR ME 
p1 >> plaitsX([4, 0, var([4, 12])], dur=1/4, lpf=linvar([1200, 14000], [24, 8]), bright=linvar([0.5, 0.1], [16, 8]), rq=linvar([0.5, 0.1], [16, 18]), cutoff=4000, porta=linvar([0.5, 0.1], [8, 8]), morph=linvar([0.5, 0.1], [16, 8]), oct=var([2, 3], 16), timbre=linvar([0.1, 0.01], 32), harm=0.1, fdecay=2).unison(4, 0.125)
p2 >> plaitsX([12, 0, 1, 11], dur=1/4, lpf=linvar([1200, 4000], [24, 8]), bright=linvar([0.5, 0.1], [16, 8]), rq=linvar([0.5, 0.1], [16, 18]), cutoff=4000, porta=linvar([4, 0.1], [8, 8]), morph=linvar([0.5, 0.1], [16, 8]), oct=var([3, 4]), timbre=linvar([0.5, 0.9], [16, 18]), harm=var([0.5, 0.3, 0.1], [24, 8, 8]), fdecay=2, leg=32).unison(2).slider()
p3 >> plaitsX([(12, 4), 0, 1, 11, 21], dur=1/4, lpf=linvar([12000, 4000], [24, 8]), bright=linvar([1, 0.1], [16, 8]), rq=linvar([0.5, 0.1], [16, 18]), cutoff=12000, porta=linvar([0.5, 0.1], [8, 8]), morph=linvar([0.5, 1], [16, 8]), oct=var([3, 4]), timbre=linvar([0.5, 0.9], [16, 18]), harm=var([0.5, 0.3, 0.1], [24, 8, 8]), fdecay=2, leg=0).unison(2)