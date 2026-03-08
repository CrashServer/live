# HEAR ME

p1 >> plaitsX([4, 0, var([4, 12])], dur=1/4, lpf=linvar([1200, 14000], [24, 8]), bright=linvar([0.5, 0.1], [16, 8]), rq=linvar([0.5, 0.1], [16, 18]), cutoff=4000, porta=linvar([0.5, 0.1], [8, 8]), morph=linvar([0.5, 0.1], [16, 8]), oct=var([2, 3], 16), timbre=linvar([0.1, 0.01], 32), harm=0.1, fdecay=2).unison(4, 0.125)
p2 >> plaitsX([12, 0, 1, 11], dur=1/4, lpf=linvar([1200, 4000], [24, 8]), bright=linvar([0.5, 0.1], [16, 8]), rq=linvar([0.5, 0.1], [16, 18]), cutoff=4000, porta=linvar([4, 0.1], [8, 8]), morph=linvar([0.5, 0.1], [16, 8]), oct=var([3, 4]), timbre=linvar([0.5, 0.9], [16, 18]), harm=var([0.5, 0.3, 0.1], [24, 8, 8]), fdecay=2, leg=32).unison(2).slider()
p3 >> plaitsX([(12, 4), 0, 1, 11, 21], dur=1/4, lpf=linvar([12000, 4000], [24, 8]), bright=linvar([1, 0.1], [16, 8]), rq=linvar([0.5, 0.1], [16, 18]), cutoff=12000, porta=linvar([0.5, 0.1], [8, 8]), morph=linvar([0.5, 1], [16, 8]), oct=var([3, 4]), timbre=linvar([0.5, 0.9], [16, 18]), harm=var([0.5, 0.3, 0.1], [24, 8, 8]), fdecay=2, leg=0).unison(2)

# --- part 2: voices separate, p2 finds its cry ---
p1.morph = linvar([0.1, 0.7], 16)
p1.harm = var([0.1, 0.5], [12, 4])
p1.timbre = linvar([0.01, 0.4], 16)
p2.porta = linvar([0.1, 8], [4, 12])
p2.leg = var([32, 4, 32], [8, 4, 4])
p2.bright = linvar([0.1, 0.8], 16)
p2.oct = var([3, 4, 5], [8, 4, 4])
p3.dur = var([1/4, 1/8], [12, 4])
p3.morph = linvar([0.5, 1], 8)
p3.amp = var([0.7, 1.2], [8, 8])

# --- part 3: pulse appears underneath, p1 shifts engine ---
d1 >> play("x.......x..x....", dur=1/4, amp=var([0, 0.6], [24, 8]), shape=0.5, hpf=80)
p1.preset = var([0, 9], [12, 4])
p1.degree = [4, 0, 4, 12, 0, 12]
p1.oct = var([2, 3, 2], [8, 4, 4])
p1.lpf = linvar([4000, 18000], 16)
p1.fdecay = var([2, 0.5], [12, 4])

# --- part 4: p2 becomes the voice, others make room ---
p2.degree = var([[12, 0, 1, 11], [0, 11, 12, 1]], [8, 8])
p2.porta = linvar([8, 0.01], 8)
p2.timbre = linvar([0.9, 0.1], [4, 12])
p2.morph = linvar([0.1, 0.9], 8)
p2.oct = var([4, 5, 4, 3], [4, 4, 4, 4])
p2.leg = var([32, 0, 32], [8, 4, 4])
p2.amp = 1.2
p3.amp = var([1.2, 0.4], [4, 12])
p3.leg = var([0, 8], [8, 8])
p1.amp = var([0.8, 0.4], [4, 12])

# --- part 5: collision — all voices in same register, fighting ---
p1.oct = (3, 4)
p1.preset = var([0, 1, 9], [4, 4, 8])
p1.dur = var([1/4, 1/8], [8, 8])
p1.amp = 1
p2.leg = 0
p2.dur = 1/8
p2.preset = var([0, 3], [8, 8])
p2.oct = (4, 5)
p3.degree = [(12, 4), 0, 1, 11, 21, (0, 7)]
p3.oct = (4, 5)
p3.bright = linvar([0.1, 1], 4)
p3.amp = 1
d1.amp = 0.8
d2 >> play("..o...o.", dur=1/4, sample=3, amp=var([0, 0.5], [8, 8]))

# --- part 6: HEAR ME — peak, everything wide open ---
p1.lpf = 18000
p1.bright = 1
p1.morph = 1
p1.porta = linvar([0.1, 4], 4)
p1.unison(6, 0.2)
p2.lpf = 14000
p2.bright = 1
p2.porta = linvar([0.01, 12, 0.01], [2, 2, 12])
p2.cutoff = 12000
p2.unison(4)
p3.lpf = 18000
p3.cutoff = 18000
p3.dur = 1/8
p3.unison(4, 0.15)

# --- part 7: aftermath — FM dissolves into shimmer ---
p1.porta = linvar([4, 0], 32)
p1.lpf = linvar([18000, 200], 64)
p1.bright = linvar([1, 0], 48)
p1.amp = linvar([1, 0], 64)
p2.porta = linvar([12, 0], 48)
p2.lpf = linvar([14000, 300], 48)
p2.leg = linvar([0, 64], 32)
p2.amp = linvar([1.2, 0], 48)
p3.lpf = linvar([18000, 200], 32)
p3.bright = linvar([1, 0], 24)
p3.amp = linvar([1, 0], 32)
d1.amp = linvar([0.8, 0], 32)
d2.amp = linvar([0.5, 0], 32)
