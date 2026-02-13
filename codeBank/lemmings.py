# Lemmings 160 
# gaming


Scale.default = Scale.chromatic
Clock.bpm = 160


melody_notes = [18, 18, -60, 18, 18, -60, 16, 14, 18, 18, -60, 18, 18, -60, 18, 16, 18]
melody_durs = [1, 2/3, 0.0, 1/3, 2/3, 0.0, 1/3, 1.0, 1.0, 2/3, 0.0, 1/3, 1/3, 1/3, 1/3, 1.0, 0]
melody_amps = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]

d3 >> faim(melody_notes, dur=melody_durs, amp=melody_amps, oct=PStep(8, (4.01, 4), 4), sus=d3.dur + PWhite(1, 2), pan=PWhite(-0.5, 0.5)).human(80)

harmony_notes = [11, 11, -60, 11, 11, -60, 13, 14, 13, 13, -60, 13, 13, -60, 14, 16, 21]
harmony_durs = [1, 2/3, 0.0, 1/3, 2/3, 0.0, 1/3, 1.0, 1.0, 2/3, 0.0, 1/3, 2/3, 0.0, 1/3, 1.0, 0]

d8 >> faim(harmony_notes, dur=harmony_durs, amp=melody_amps, beef=var([1, 2]), oct=PRand([3, 4, [5, 2]]), sus=var([6 - d8.oct, 6 - d8.oct - 1])).human(5)



d3 >> faim([18, 18, -60, 18, 18, -60, 19, 21, 13, 11], dur=[1, 2/3, 0.0, 1/3, 2/3, 0.0, 1/3, 1.0, 4.0, 0], amp=[1, 1, 0, 1, 1, 0, 1, 1, 1, 1], dist2=0.4)


bass_pattern_1 = P[(-25, -13), (-25, -13), (-25, -13), (-25, -13), (-30, -18), (-30, -18), (-30, -18), (-30, -18)].stutter(8)
bass_pattern_2 = P[(-22, -10), (-22, -10), (-22, -10), (-22, -10), (-27, -15), (-27, -15), (-27, -15), (-27, -15)].stutter(2)
bass_pattern_3 = P[(-29, -17), (-29, -17), (-29, -17), (-29, -17), (-27, -15), (-27, -15), (-27, -15), (-27, -15)].stutter(2)

d4 >> lbass(bass_pattern_1 | bass_pattern_2 | bass_pattern_3 | bass_pattern_3, oct=6, dur=1, amp=1, cutoff=linvar([4000, 8000], [4, 2]), leg=4)


bell_notes = [-18, -60, -18, -60, -18, -60, -18, -60, ([-18, -1], -1)]
bell_durs = P[0.5, 4.0].stutter([8, 1])
bell_amps = var([[1, 0, 1, 0, 1, 0, 1, 0, 1], PRand([0, 0.2])], [4, 12])

d5 >> bell(bell_notes, lpf=4000, lpr=0.04, dur=bell_durs, amp=bell_amps, vol=0.5).unison(4)
d6 >> bell([-1, -18, -60, -18, -60, -18, -60, -18, -60], dur=P[4.0, 0.5].stutter([1, 8]), amp=[1, 1, 0, 1, 0, 1, 0, 1, 0])

# Karp Arpeggio
karp_pattern_1 = P[(2, 6, 9, 14), (4, 1, -3, 9)].loop(4)
karp_pattern_2 = P[(-1, 2, 6, 11), (-6, -3, 1, 6)].loop(3)
karp_pattern_3 = P[(-5, -1, 2, 7), (4, 1, -3, 9)].loop(1)

d0 >> karp(karp_pattern_1 | karp_pattern_2 | karp_pattern_3, dur=[4], amp=[1, 1], oct=5, cutoff=3200, lpf=4000, hpf=200, vol=0.3, echo=0.5).unison(2) + var(0, 12)

d3 >> faim([18, 18, -60, 18, -60, 14, 18, 18, -60, 18, -60, 19, 18, 16, 18], dur=[1, 2/3, 1/3, 2/3, 1/3, 1.0, 1.0, 2/3, 1/3, 1/3, 0.0, 1/3, 1/3, 1.0, 0], amp=[1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1])

donk_notes_1 = P[-60, 14, -60, 9, 14, -60, 14, -60, 14, -60, 9, -60, 4, 9, -60, 9, -60, 4, 9, -60]
donk_notes_2 = P[-60, 11, -60, 11, -60, 11, 11, -60, 11, -60, 6, -60, 6, -60, 6, 6, -60, 6, -60]
donk_notes_3 = P[-60, 7, -60, 2, 7, -60, 7, -60, 2, 7, -60, 9, -60, 4, 9, -60, 9, -60, 4, 9, -60]
donk_notes_4 = P[-60, 11, -60, 6, 11, -60, 11, -60, 6, 11, -60, 6, -60, 1, 6, -60, 6, -60, 1, 6, -60]

donk_durs_1 = P[1.0, 1/3, 0.0, 1/3, 1.0, 1/3, 1/3, 1/3, 1/3, 1.0, 1/3, 0.0, 1/3, 1.0, 1/3, 1/3, 0.0, 1/3, 1/3, 0]
donk_durs_2 = P[1, 1/3, 1/3, 1.0, 0.0, 1/3, 1/3, 1/3, 1/3, 1.0, 1/3, 1/3, 1.0, 0.0, 1/3, 1/3, 1/3, 1/3, 0]
donk_durs_3 = P[1, 1/3, 0.0, 1/3, 1.0, 1/3, 1/3, 0.0, 1/3, 1/3, 1.0, 1/3, 0.0, 1/3, 1.0, 1/3, 1/3, 0.0, 1/3, 1/3, 0]

donk_amps_1 = P[0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
donk_amps_2 = P[0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
donk_amps_3 = P[0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]

d2 >> donk(donk_notes_1 | donk_notes_2 | donk_notes_3 | donk_notes_4, dur=donk_durs_1 | donk_durs_2 | donk_durs_3 | donk_durs_3, amp=donk_amps_1 | donk_amps_2 | donk_amps_3 | donk_amps_3, lpr=1, vol=1, lpf=4000, dist2=[0.2, 0.5]).unison(4)

d6.stop()
# d9 >> play("O", rate=-0.25, amp=0.25, sample=3, dur=16)
d5.stop()
d0.stop()

d3 >> faim([(18,), (18,), (-60,), (18,), (-60,), (14,), (18,), (18,), (-60,), (18,), (-60,), (19,), (18,), (16,), (18,)], dur=[1.0, 2/3, 1/3, 2/3, 1/3, 1.0, 1.0, 2/3, 1/3, 1/3, 0.0, 1/3, 1/3, 1.0, 0], amp=[1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], sus=2)

d4 >> faim([(11,), (11,), (-60,), (11,), (-60,), (14,), (13,), (13,), (-60,), (13,), (-60,), (16,), (21,)], oct=6, dur=[1.0, 2/3, 1/3, 2/3, 1/3, 1.0, 1.0, 2/3, 1/3, 2/3, 1/3, 1.0, 0], amp=[1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1], sus=2).only()

d7.stop()
d7 >> faim([(26,), (-60,)], dur=[4.0, 4.0], amp=[1, 0])

d5 >> pluck([-18, -60], dur=var([1/2, 1/4], [12, 4]), amp=[1, 0], dist2=linvar([1, 2], 32), a=0.8, vol=linvar([0.2, 0.6], [16, 8])).unison(4)

d5 >> bell([-18, -60, -18, -60, -18, -60, -18, -60, ([-18, -1], -1)], dur=P[0.5, 4.0].stutter([8, 1]), amp=[1, 0, 1, 0, 1, 0, 1, 0, 1]).unison(4)

d6 >> bell([-1, -18, -60, -18, -60, -18, -60, -18, -60], dur=P[4.0, 0.5].stutter([1, 8]), amp=[1, 1, 0, 1, 0, 1, 0, 1, 0])


d7 >> faim([-60, 9, 16, 14, 9, 14], dur=[1.0, 1.5, 1.5, 1.5, 1.5, 1.0], amp=[0, 1, 1, 1, 1, 1])
d7 >> faim([-60, 18, 26, 26, 25, 23, 25], dur=[1.0, 1.5, 1.5, 1.0, 1.0, 1.0, 1.0], amp=[0, 1, 1, 1, 1, 1, 1])

d4.stop()
d6.stop()
d5.stop()
d0.stop()
d3.stop()
d8.stop()

d7 >> varicelle([-60, 9, 16, 14, 9, 14], dur=[1.0, 1.5, 1.5, 1.5, 1.5, 1.0], amp=[0, 1, 1, 1, 1, 1])
d7 >> pluck([-60, 18, 26, 26, 25, 23, 25], dur=[1.0, 1.5, 1.5, 1.0, 1.0, 1.0, 1.0], amp=[0, 1, 1, 1, 1, 1, 1])
e7 >> lbass([18, 18, -60, 18, -60, 21, 13, 11], oct=3, dur=[1, 2/3, 1/3, 2/3, 1/3, 1.0, 4.0, 0], amp=[1, 1, 0, 1, 0, 1, 1, 1])



d3 >> faim([18, 21, 23, 26, 28, 30], dur=0.5, amp=1, oct=PStep(16, [4, 5, 6]), sus=linvar([0.5, 2], 8), dist2=linvar([0.4, 1.2], 16), pan=PSine(8)).human(50)
Clock.bpm = 170
e2 >> loop("hiphop8", dur=16, sample=1, dist2=2)

d8 >> faim([11, 14, 16, 18, 21, 23], dur=0.5, amp=0.8, oct=PRand([4, 5, 6]), beef=linvar([1, 3], 8), sus=2, lpf=linvar([2000, 8000], 12)).human(20).unison(3)

d4 >> lbass(P[(-25, -13), (-30, -18), (-22, -10), (-27, -15)].stutter(4), oct=var([5, 6], [16, 8]), dur=0.5, amp=0.3, cutoff=linvar([6000, 12000], 8), leg=8, dist2=1.5, room=0.3)

d2 >> donk(P[14, 16, 18, 21, 23, 26, -60].shuffle(), dur=P[1/4, 1/3, 1/6].shuffle(), amp=PRand([0.8, 1, 1.2]), lpf=linvar([3000, 10000], 8), dist2=var([0.5, 1.5], 4), rate=PWhite(0.8, 1.2)).unison(6)

# d5 >> bell(P[-18, -15, -13, -10, -8, -6, -3, -1], dur=0.125, amp=linvar([0.5, 1.2], 16), lpf=8000, lpr=0.02, room=0.5, mix=0.3).unison(2)

# d6 >> bell(P[([-18, -6], [-15, -3], [-13, -1])], dur=var([2, 1, 0.5], [8, 4, 4]), amp=1, verb=0.8, dist2=0.6).unison(2)

d0 >> karp(P[(2, 6, 9, 14, 18), (4, 7, 11, 16, 21), (-1, 3, 7, 12, 16)].shuffle(), dur=0.25, amp=1, oct=var([5, 6, 7], [8, 4, 4]), cutoff=linvar([4000, 10000], 12), hpf=400, echo=var([0.25, 0.5, 0.75], 8), vol=0.8).unison(3)

d9 >> play("O-XO-X--", rate=linvar([1, 2], 16), amp=var([0.5, 0.8, 1.2], [4, 4, 8]), sample=var([3, 4, 5], 8), dur=0.5, room=0.2)

e2 >> loop("hiphop8", dur=8, sample=var([1, 2], 16), dist2=linvar([2, 4], 8), rate=1.2, amp=1.2)



# Varicelle texture
d7 >> varicelle([9, 14, 16, 18, 21, 23, 26], dur=var([0.25, 0.5, 1], [8, 8, 4]), amp=linvar([0.6, 1], 12), oct=PRand([4, 5, 6]), room=0.7, mix=0.4, dist2=0.8)


Clock.bpm = 180

d3 >> faim([18, 23, 26, 30, 33, 35], dur=0.125, amp=1.5, oct=7, sus=0.1, dist2=2, pan=PSine(16), lpf=12000).human(30).unison(8).only()

d8 >> faim(P[11, 14, 18, 21, 25, 28, 32].rotate(), dur=0.0625, amp=1.2, oct=6, beef=4, sus=3, room=0.8).human(10).unison(6)

d4 >> lbass(P[(-25, -13, 0), (-30, -18, -6)].stutter(2), oct=6, dur=0.25, amp=1.5, cutoff=15000, leg=12, dist2=2.5, room=0.5, hpf=50)

d2 >> donk(P[14, 18, 23, 26, 30, -60].shuffle(), dur=P[1/8, 1/6, 1/4].shuffle(), amp=1.5, lpf=12000, dist2=2, rate=PWhite(1, 1.5)).unison(8)



Clock.bpm = 160


d3.stop()
d8.stop()
d2.stop()
d0.stop()
d9.stop()

d7 >> faim([26, 25, 23, 21, 18, 16, 14, 11, 9, 6], dur=2, amp=linvar([1, 0.3], 20), oct=5, sus=4, room=0.9, mix=0.7, lpf=linvar([8000, 2000], 20))

e7 >> lbass([18, 13, 11, 6, 2, -1], oct=3, dur=4, amp=linvar([1, 0.5], 24), cutoff=linvar([4000, 1000], 24), sus=8, room=0.8)

d5 >> bell([-18, -13, -10, -6, -3, -1], dur=var([4, 8], [12, 12]), amp=linvar([0.8, 0.2], 24), lpf=linvar([6000, 2000], 24), room=1, mix=0.9).unison(2)

Clock.bpm = 140

d7 >> varicelle([9, 11, 14, 18], dur=8, amp=linvar([0.6, 0.1], 32), oct=4, room=1, mix=1, sus=16)

d6 >> bell([(-18, -6, 6)], dur=16, amp=linvar([0.5, 0], 16), room=1, mix=1).unison(3)

e7 >> lbass([18, 14, 11, 6], oct=2, dur=16, amp=linvar([0.8, 0], 64), cutoff=linvar([2000, 500], 64), sus=32)

d4 >> pluck([-18, -15, -13, -10], dur=var([8, 16], [16, 16]), amp=linvar([0.3, 0], 64), a=1, dist2=0.2, room=1, mix=1).unison(2)

e2 >> loop("hiphop8", dur=32, sample=1, dist2=linvar([1, 0], 32), rate=linvar([1, 0.5], 32), amp=linvar([0.5, 0], 32))
