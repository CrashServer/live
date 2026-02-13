# thehumblepath 132
# todo
b3 >> prodrums([0, 3, 7, 10, 12, 7], voice=4, dur=PDur(3, 8), layer1_amp=0.6, layer2_amp=0.7, layer3_amp=0.4, body_tone=var([3500, 3000, 4200], [6, 1, 1]), harmonic=1.5, fm_amount=1.7, fm_ratio=12.5, echo=0.5, tube=0.1, waveform=var([1, 6], 12), texture=11, decay=var([0.4, 0.2], 8), attack=0.1, mid_sat=0.8, high_sat=1.0, amp=0.55, scale=Scale.minor, oct=6, pan=PSine(8) * 0.3)
b1 >> prodrums([0, 3, 5], voice=4, dur=0.5, layer1_amp=0.9, layer2_amp=1.0, layer3_amp=1.0, body_tone=1901, harmonic=0.9, fm_amount=PFr(0, 4, 32, 16), waveform=0, decay=0.4,low_gain=0.4,  low_sat=1.2,    mid_gain=0.5,  amp=0.8, fm_ratio=var([1, 2, 4, 8, 16], PRand(8)),  scale=Scale.minor, oct=PStep(12, 4, 5))
b3 >> prodrums([0, 3, 7, 10, 12, var([7, 12, 13], [12, 1, 1])], voice=4, dur=PDur(3, 8), layer1_amp=0.5, layer2_amp=0.4, layer3_amp=0.4, body_tone=var([3500, 3000, 4200], [6, 1, 1]), harmonic=1.7, fm_amount=3, fm_ratio=0.5, waveform=var([1, 6], 12), texture=0,  decay=var([0.4, 0.2], 8), attack=0.1, echo=0.5, mid_sat=0.8, high_sat=1.0, amp=0.55, scale=Scale.minor, oct=(6, 5), pan=PSine(8) * 0.3)
b3 >> prodrums([0, 3, 7, 10, 12, var([7, 12, 13], [12, 1, 1])], voice=4, dur=PDur(3, 8), layer1_amp=0.5, layer2_amp=0.4, layer3_amp=0.4, body_tone=var([3500, 3000, 4200], [6, 1, 1]), harmonic=1.7, fm_amount=var([3,24], [7, 3]), fm_ratio=0.5, waveform=var([1, 6], 12), texture=17,  decay=var([0.4, 0.2], 8), attack=0.1, echo=0.5, mid_sat=0.8, high_sat=1.0, amp=0.55, scale=Scale.minor, oct=(6, 5), pan=PSine(8) * 0.3)
b5 >> prodrums([12, 10, 7, 5], voice=4, dur=var([0.25, 0.5], [3, 1]), layer1_amp=1, layer2_amp=1.1, layer3_amp=0.56, body_tone=var([3100, 2800, 200], 4), harmonic=1.8, fm_amount=1.35, waveform=8, texture=var([2, 0], 8), decay=0.25, attack=0.01, mid_gain=0.65,  high_gain=1, amp=0.5, scale=Scale.minor, oct=6).every(8, 'reverse')
p4 >> arpy([12, 15, 17, 19], dur=0.25, amp=0.1745, oct=6, sus=0.2, lpf=linvar([3000, 5000], 16), room=0.3, pan=PSine(12) * 0.5, scale=Scale.minor)
b3 >> prodrums([0, [3, 7,12], 7, 10, 12, var([7, 12, 13], [12, 1, 1])], voice=4, dur=PDur(3, 8), layer1_amp=0.5, layer2_amp=0.4, layer3_amp=0.4, body_tone=var([3500, 3000, 4200], [6, 1, 1]), harmonic=1.7, fm_amount=var([3,24], [7, 3]), fm_ratio=2, waveform=var([1, 6], 12), texture=6, leg=1,  decay=var([0.4, 0.2], 8), attack=0.1, echo=0.25, mid_sat=0.8, high_sat=1.0, amp=0.8, scale=Scale.minor, oct=(6, 5), pan=PSine(8) * 0.3)
p3 >> dbass([0, 3, 5, 7], dur=PDur(5, 8), amp=0.9, oct=5, decay=0.3, hpf=200, hpr=0.5, room=0.1, tape=1, tapedrive=1, dist2=0.3,scale=Scale.minor).every(8, 'reverse')
b6 >> prodrums([0, 3, 7, 5, PWalk(8, 1, 1)], voice=(4), dur=0.25, layer1_amp=1, layer2_amp=0.5, layer3_amp=0.3, body_tone=linvar([500, 900, 1400], 16), harmonic=2, fm_amount=1.2, hpf=200, fm_ratio=var([2, 2.5, 3], 4), waveform=6, texture=lininf(0, 42, 128), decay=0.2, mid_sat=var([0.6, 2.5], [16, 4]), amp=0.75,  scale=Scale.minor, oct=4, fshift=0, leg=0)
b7 >> cbass(b6.degree, dur=0.25, follow=4, lpf=1200, leg=4, hpf=1000)
p3 >> cbass([0, 3, 5, 7], dur=PDur(5, 8), amp=0.9, oct=5, decay=0.3, hpf=200, hpr=0.5, follow=4, room=0.2, dist2=0.2,scale=Scale.minor).every(8, 'reverse')
p8 >> pianovel([0, 13, 7, [10, 12, 9]], dur=4, amp=0.8, oct=(5, 4), sus=3, room=0.4, verb=0.5, scale=Scale.minor)
Root.default=var([0, 4, 0, [5, 4]], [24,8])
p4.stop()
b3.lpf=400
p4.hpf=1600
Root.default=0
p8 >> pianovel(var([[0,3,7,[10,12]],[3,7,10,[14,15]],[-2,2,5,[10,12]],[0,5,7,[12,15]],[5,7,10,[14,17]],[-3,0,3,[7,10]]],[8,8,4,8,4,4]), dur=var([4,2,8],[16,8,8]), amp=var([0.6,0.75,0.5],[12,4,16]), oct=var([(5,4),(4,3),(5,3)],[16,8,8]), sus=var([3,5,2],[12,8,12]), amplify=1.5, room=linvar([0.3,0.6],32), verb=linvar([0.4,0.7],48), scale=Scale.minor)
p9 >> pianovel(var([P[0,2,3,5,7,5,3,2],P[7,10,12,10,7,5,3,0],P[3,5,7,10,12,10,7,5],P[0,3,7,12,10,7,3,0],P[5,7,10,14,12,10,7,5]],[8,8,8,4,4]), dur=var([0.5,0.25,1],[12,4,16]), amp=var([0.5,0.65,0.4],[8,4,20]), oct=var([6,5,7],[16,8,8]), sus=0.4, room=0.4, verb=0.5, pan=sinvar([-0.4,0.4],16), amplify=1.5, scale=Scale.minor).every(16,'reverse')
p5 >> marimba([7, 5, 3, 0], dur=var([0.5, 1], [3, 1]), amp=0.6, oct=6, decay=0.4, room=0.25, pan=var([-0.3, 0.3], 2), scale=Scale.minor).every(16, 'stutter', 4)
p5 >> marimba(var([P[7,5,3,0],P[10,7,5,3,0],P[12,10,7,5],P[0,3,5,7,10],P[5,3,0,-2,0,3],P[7,10,12,10,7,5,3]],[8,4,4,8,4,4]), dur=var([0.5,1,0.25],[3,1,0.5]), amp=var([0.5,0.65,0.4],[12,4,16]), oct=var([5,6,4],[16,8,8]), decay=linvar([0.3,0.6],24), room=linvar([0.2,0.45],32), pan=var([-0.4,0.4,0,-0.2,0.2],[2,2,4,2,2]), scale=Scale.minor).every(16,'stutter',4).every(24,'reverse')
Root.default=var([0, 4, 3, [5, 4]], [24,8])
b6.dur=8
s0 >> loop("perc8", dur=16, hpf=300, amp=1, sample=4, shift=0, leg=1, dist2=0.4).lclip(4)

p8.dur=4
p8.amp=0.6
p8.oct=4
p8.echo=0.5

b7 >> prodrums(P[0, 0, 0, 0, PRand([5, 7, 10])], voice=4, dur=var([0.5, 0.25], [3, 1]), layer1_amp=2.5, layer2_amp=2.0, layer3_amp=1.0, body_tone=var([800, 400, 1200], 2), harmonic=0.5, fm_amount=1.3, fm_ratio=var([1, 0.5], 1), waveform=1, decay=0.2, attack=0.001,  low_sat=0.6, mid_sat=0.3, low_gain=1.5, mid_gain=0.8, texture=22, high_gain=1.0, amp=1.0, scale=Scale.minor)
Root.default = 0
b_all.dur=2

b3 >> prodrums(PWalk(8), voice=4, dur=0.125, layer1_amp=0.5, hpf=400, hpr=0.7, layer2_amp=0.7, layer3_amp=0.4, body_tone=var([3000, 2500], 4), harmonic=1.2, fm_amount=0.4, waveform=var([1, 6], 8), texture=var([0, 3], 4), decay=0.15, mid_sat=0.7, amp=1.0, scale=Scale.minor, oct=6)
b7 >> prodrums(P[0, 0, 0, 0, PRand([5, 7, 10])], voice=4, dur=var([0.5, 0.25], [3, 1]), layer1_amp=0.5, layer2_amp=1.0, layer3_amp=1.0, body_tone=var([800, 400, 1200], 2), harmonic=1, fm_amount=4.3, fm_ratio=var([1, 0.5], 1), waveform=1, decay=0.2, attack=0.001,  low_sat=2.0, mid_sat=0.8, low_gain=1.5, mid_gain=0.8, texture=0, high_gain=1.2, amp=1.0, scale=Scale.minor, oct=6)


p_all.stop()
b6 >> prodrums([0, 3, 7, 5, PWalk(8, 1, 1)], voice=(4), dur=0.25, layer1_amp=1, layer2_amp=1.2,layer3_amp=0.8,  body_tone=linvar([500, 900, 140], 16), harmonic=0.7, fm_amount=3.1,  fm_ratio=var([2, 2.5, 3], 4),     waveform=6,  texture=10, decay=0.3,  mid_sat=1.6, amp=0.75,     scale=Scale.minor, oct=4)
b1 >> prodrums([0, 3, 5, var([7, 10], 8)], voice=4, dur=0.5, layer1_amp=1.1, layer2_amp=1.0, layer3_amp=1.0, body_tone=1901, harmonic=2.0, texture=12, fm_amount=0.5, waveform=1, decay=0.4, low_gain=0.4, low_sat=1.2, mid_gain=0.5, lpf=linvar([400, 3000], 16), lpr=0.3, amp=0.8, scale=Scale.minor, oct=(4))
b6 >> prodrums([0, 3, 7, 5], voice=4, dur=0.5, layer1_amp=1.1, layer2_amp=0.7, layer3_amp=0.5, body_tone=linvar([500, 900, 140], 16), harmonic=0.7, fm_amount=1.5, fm_ratio=var([2, 2.5], 4), waveform=6, texture=5, decay=0.5, lpf=linvar([300, 2000], 16), lpr=0.5,  mid_sat=1.2, amp=0.6, scale=Scale.minor, oct=4)
b_all.only()
p6 >> glass([10, 12, 15], dur=2, amp=0.4, oct=6, sus=2, verb=0.8, mix=0.5, lpf=5000, room=0.7, scale=Scale.minor)
b7 >> prodrums(P[0, 0, 0, PRand([5, 7, 10, 12])], voice=4, dur=var([0.5, 0.25, 1.0], [3, 1, 0.5]), layer1_amp=linvar([2.5, 3.5], 8), layer2_amp=var([2.0, 3.0], 2), layer3_amp=1.0, body_tone=var([800, 400, 1200, 600], [2, 1, 1, 0.5]), harmonic=var([0.5, 0.3], 4), fm_amount=linvar([1.3, 1.0, 2.5], 8), fm_ratio=var([1, 12, 1.5], [2, 1, 1]), waveform=var([2, 0], 4), decay=var([0.2, 0.1, 0.4], [4, 1, 1]), attack=0.001, low_sat=var([1.0, 1.5], 2), mid_sat=1.3, oct=4, low_gain=0.5, mid_gain=0.8, texture=var([0, 2], 8), high_gain=0.2,  amp=1.0, scale=Scale.minor).every(16, 'stutter', 4)
Root.default = "C"
d7 >> play("t", dur=0.5, sample=PChain({0:[0,1,2], 1:[2,3], 2:[1,0], 3:[3,0]}), amp=var([0.8, 1.2], 1), pan=var([-0.6, -0.2, 0.2, 0.6], 0.5), room=0.25)

b3.dur=4
d7.stop()
b3.stop()
b5.stop()
b7.stop()
p3.stop()
p5.stop()

b2 >> prodrums([7, 10, 12, 10, 7, 5], voice=4, dur=0.5, layer1_amp=1.2, layer2_amp=0.9, layer3_amp=1.0, body_tone=var([2400, 2800], 8), harmonic=1.0, fm_amount=0.8, fm_ratio=var([2, 3, 4], 4), waveform=1, decay=0.5, attack=0.05, mid_gain=0.7, high_gain=0.9, amp=0.75, scale=Scale.minor, oct=5)

b6 >> prodrums([0, 3, 7, 5, PWalk(8, 1, 1)], voice=4, dur=PDur(var([5, 7], 8), 8), layer1_amp=1.2, layer2_amp=1.5, layer3_amp=1.0, body_tone=expvar([500, 1400], 16), harmonic=0.8, fm_amount=2.5, fm_ratio=var([2, 2.5, 3, 1.5], 2), waveform=3, texture=var([0, 10, 5], [6,  1, 1]), decay=0.3, mid_sat=0.8, amp=0.8, scale=Scale.minor, oct=4)

b7 >> prodrums([0, 0, 0, PRand([3, 5, 7])], voice=4, dur=var([0.5, 0.25], [3, 1]), layer1_amp=1.5, layer2_amp=1.2, layer3_amp=0.8, body_tone=var([800, 600], 2), harmonic=0.6, fm_amount=1.5, fm_ratio=var([1, 1.5], 1), waveform=2, decay=0.25, low_sat=0.6, mid_sat=0.5,low_gain=1.2, amp=0.85, scale=Scale.minor)

b4 >> prodrums([12, 15, 17, 19, 17, 15], voice=4, dur=0.25, layer1_amp=1.5, layer2_amp=1.2, layer3_amp=1.0, body_tone=var([4000, 4500], 2), harmonic=1.8, fm_amount=2.0, fm_ratio=var([3, 4], 2), waveform=var([1, 2], 4), texture=3, decay=0.2, attack=0.001, high_sat=0.5, high_gain=1.2, amp=0.4, scale=Scale.minor, oct=5, pan=var([-0.5, 0.5], 1))
b7 >> prodrums([0, 0, 0, PRand([5, 7, 10, 12])], voice=4, dur=var([0.5, 0.25, 0.125], [3, 1, 0.5]), layer1_amp=linvar([2.5, 3.5], 4), layer2_amp=var([2.0, 3.2], 2), layer3_amp=1.5, body_tone=var([800, 400, 1200, 600], [2, 1, 1, 0.5]), harmonic=var([0.5, 0.3], 2), fm_amount=linvar([1.3, 3.5], 4), fm_ratio=var([1, 0.5, 1.5], 1), waveform=var([2, 0], 2), decay=var([0.2, 0.1], 4), low_sat=var([0.4, 1.5], 2), mid_sat=0.5, low_gain=0.8, texture=var([0, 5], 4), amp=1.1, scale=Scale.minor).every(8, 'stutter', 4)

masterAll("lpf", 0)
p1 >> pads([0, 3, 7, 10], dur=8, sus=8, amp=1.5, oct=4, chop=0, room=1.0, mix=0.4, lpf=2000, lpr=0.2, scale=Scale.minor)
p6 >> glass([7, 10, 12], dur=4, amp=0.5, oct=6, sus=4, verb=0.9, mix=0.6, room=0.8, pan=sinvar([-0.6, 0.6], 16), scale=Scale.minor)
           
b2 >> prodrums([0, 7, 5, 3], voice=4, dur=1, layer1_amp=1.2, layer2_amp=0.8, layer3_amp=1.5, body_tone=linvar([1500, 2200], 8), harmonic=0.7, fm_amount=0.8, waveform=1, decay=0.6, low_gain=0.5, mid_gain=0.6, amp=0.7, scale=Scale.minor, oct=5)

b3 >> prodrums([0, 3, 7, 10, 12, 7], voice=4, dur=PDur(3, 8), layer1_amp=0.8, layer2_amp=0.7, layer3_amp=1.0, body_tone=var([3500, 3000, 4200], [6, 1, 1]), harmonic=2.5, fm_amount=1, fm_ratio=4, waveform=var([3, 6], 12), texture=4, decay=var([0.4, 0.2], 8), attack=0.1, mid_sat=0.8, high_sat=1.6, amp=0.55, scale=Scale.minor, oct=6, pan=PSine(8) * 0.3)
b5 >> prodrums([12, 10, 7, 5], voice=4, dur=var([0.25, 0.5], [3, 1]), layer1_amp=0.86, layer2_amp=1.3, layer3_amp=0.45, body_tone=var([3100, 2800], 4), harmonic=3.9, fm_amount=4, waveform=3, texture=var([2, 0], 8), decay=0.57, attack=0.04, mid_gain=0.65,  high_gain=0.75, amp=0.3, scale=Scale.minor, oct=5).every(8, 'reverse')
b3 >> prodrums([0, 3, 7, 10, 12, var([7, 12, 13], [12, 1, 1])], voice=4, dur=PDur(3, 8), layer1_amp=0.5, layer2_amp=0.4, layer3_amp=0.4, body_tone=var([3500, 3000, 4200], [6, 1, 1]), harmonic=1.7, fm_amount=6, fm_ratio=2.0, waveform=var([1, 6], 12), texture=0, decay=var([0.4, 0.2], 8), attack=0.1, echo=0.5, mid_sat=0.8, high_sat=1.4, amp=0.55, scale=Scale.minor, oct=(6, 5), pan=PSine(8) * 0.3)
p4 >> arpy([12, 15, 17, 19], dur=0.25, amp=0.2, oct=6, sus=0.2, lpf=linvar([3000, 5000], 16), room=0.3, pan=PSine(12) * 0.5, scale=Scale.minor)
p3 >> bass([0, 3, 5, 7], dur=PDur(5, 8), amp=0.9, oct=5, tape=0.5, decay=0.3, hpf=200, hpr=0.5, room=0.2, dist2=0.4,scale=Scale.minor).every(8, 'reverse')
b1 >> prodrums(var([P[0,3,5],P[0,3,7],P[0,5,7],P[0,3,5,7],P[-2,0,3],P[0,3,5,10]],[8,8,4,8,4,4]), voice=4, dur=var([0.5,0.25,1],[12,4,16]), layer1_amp=linvar([0.8,1.1],16), layer2_amp=linvar([0.9,1.2],24), layer3_amp=var([1.0,0.8,1.2],[8,4,4]), body_tone=linvar([1700,2200],32), harmonic=linvar([0.8,1.0],24), fm_amount=linvar([0.4,0.7],16), waveform=var([1,2,0],[12,4,8]), decay=linvar([0.35,0.5],24), low_gain=linvar([0.35,0.5],32), low_sat=linvar([1.0,1.5],16), mid_gain=linvar([0.4,0.65],24), amp=var([0.75,0.9,0.65],[12,4,16]), fm_ratio=var([1,1.5,0.5],[16,8,8]), scale=Scale.minor, oct=var([4,(4,3),(4,5)],[16,8,8]))
b5 >> prodrums(var([P[12,10,7,5],P[14,12,10,7],P[10,7,5,3],P[15,12,10,7,5],P[12,10,7,5,3,0],P[17,14,12,10]],[8,4,4,8,4,4]), voice=4, dur=var([0.25,0.5,0.125],[3,1,0.5]), layer1_amp=linvar([0.8,1.0],16), layer2_amp=linvar([0.35,0.55],24), layer3_amp=linvar([0.4,0.55],32), body_tone=var([3100,2800,3400,2600],[4,4,2,2]), harmonic=linvar([2.4,2.9],24), fm_amount=linvar([1.2,1.6],16), waveform=var([6,3,1],[8,4,4]), texture=var([2,0,4,1],[8,4,2,2]), decay=linvar([0.5,0.7],24), attack=linvar([0.03,0.06],32), mid_gain=linvar([0.6,0.75],24), high_gain=linvar([0.7,0.85],32), amp=var([0.28,0.35,0.22],[12,4,16]), scale=Scale.minor, oct=var([5,6,4],[16,8,8]), pan=sinvar([-0.3,0.3],12)).every(8,'reverse').every(16,'stutter',4)
p3 >> cbass([0, 3, 5, 7], dur=PDur(5, 8), amp=0.9, oct=6, decay=0.3, hpf=200, hpr=0.7, follow=4, room=0.2, dist2=0.1,scale=Scale.minor).every(8, 'reverse')
p1.dur=4
b3.dur=4
p8 >> pianovel([0, 3, 7, [10, 12, 9]], dur=4, amp=0.8, oct=(5, 4), sus=3, room=0.4, verb=0.5, scale=Scale.minor)
d9 >> play("d", dur=PDur(3, 8), sample=var([0, 1, 2], 4), rate=P[1, 1.5, 2, 1.25], amp=0.7, room=0.5, formant=var([0, 1], 8), scale=Scale.minor)
p8.dur=16
p8.amp=0.6
p8.oct=3
p5 >> marimba([7, 5, 3, 0], dur=var([0.5, 1], [3, 1]), amp=0.55, oct=5, decay=0.4, room=0.25, pan=var([-0.3, 0.3], 2), scale=Scale.minor).every(16, 'stutter', 4)
b7 >> prodrums(P[0, 0, 0, 0, PRand([5, 7, 10])], voice=4, dur=var([0.5, 0.25], [3, 1]), layer1_amp=2.5, layer2_amp=2.0, layer3_amp=1.0, body_tone=var([800, 400, 1200], 2), harmonic=0.5, fm_amount=1.3, fm_ratio=var([1, 0.5], 1), waveform=2, decay=0.2, attack=0.001,  low_sat=0.6, mid_sat=0.3, low_gain=1.5, mid_gain=0.8, texture=22, high_gain=1.0, amp=1.0, scale=Scale.minor)
l8 >> loop("electrodrum16", dur=16, amp=1)
b7 >> prodrums(P[0, 0, 0, 0, PRand([5, 7, 10])], voice=4, dur=var([0.5, 0.25], [3, 1]), layer1_amp=0.5, layer2_amp=1.0, layer3_amp=1.0, body_tone=var([800, 400, 1200], 2), harmonic=1, fm_amount=4.3, fm_ratio=var([1, 0.5], 1), waveform=1, decay=0.2, attack=0.001,  low_sat=2.0, mid_sat=0.8, low_gain=1.5, mid_gain=0.8, texture=0, high_gain=1.2, amp=1.0, scale=Scale.minor, oct=6)
b6 >> prodrums([0, 3, 7, 5, PWalk(8, 1, 1)], voice=(4), dur=0.25, layer1_amp=1, layer2_amp=1.2,layer3_amp=0.8,  body_tone=linvar([500, 900, 140], 16), harmonic=0.7, fm_amount=3.1,  fm_ratio=var([2, 2.5, 3], 4),     waveform=6,  texture=10, decay=0.3,  mid_sat=1.6, amp=0.75,     scale=Scale.minor, oct=4)
b1 >> prodrums([0, 3, 5, var([7, 10], 8)], voice=4, dur=0.5, layer1_amp=0.9, layer2_amp=1.0, layer3_amp=1.0, body_tone=1901, harmonic=0.9, fm_amount=0.5, waveform=1, decay=0.4, low_gain=0.4, low_sat=1.2, mid_gain=0.5, lpf=linvar([400, 3000], 16), lpr=0.4, amp=0.8, scale=Scale.minor, oct=(4))
b6 >> prodrums([0, 3, 7, 5], voice=4, dur=0.5, layer1_amp=0.6, layer2_amp=0.7, layer3_amp=0.5, body_tone=linvar([500, 900, 140], 16), harmonic=0.7, fm_amount=1.5, fm_ratio=var([2, 2.5], 4), waveform=6, texture=5, decay=0.5, lpf=linvar([300, 2000], 16), lpr=0.5,  mid_sat=1.2, amp=0.6, scale=Scale.minor, oct=4)
p6 >> glass([10, 12, 15], dur=2, amp=0.4, oct=6, sus=2, verb=0.8, mix=0.5, lpf=5000, room=0.7, scale=Scale.minor)
b3 >> prodrums()
b7 >> prodrums(P[0, 0, 0, PRand([5, 7, 10, 12])], voice=4, dur=var([0.5, 0.25, 1.0], [3, 1, 0.5]), layer1_amp=linvar([2.5, 3.5], 8), layer2_amp=var([2.0, 3.0], 2), layer3_amp=1.0, body_tone=var([800, 400, 1200, 600], [2, 1, 1, 0.5]), harmonic=var([0.5, 0.3], 4), fm_amount=linvar([4.3, 6.0, 2.5], 8), fm_ratio=var([1, 12, 1.5], [2, 1, 1]), waveform=var([2, 0], 4), decay=var([0.2, 0.1, 0.4], [4, 1, 1]), attack=0.001, low_sat=var([2.0, 3.5], 2), mid_sat=1.3, oct=4, low_gain=0.5, mid_gain=0.8, texture=var([0, 2], 8), high_gain=0.2,  amp=1.0, scale=Scale.minor).every(16, 'stutter', 4)
d7 >> play("t", dur=0.5, sample=PChain({0:[0,1,2], 1:[2,3], 2:[1,0], 3:[3,0]}), amp=var([0.8, 1.2], 1), pan=var([-0.6, -0.2, 0.2, 0.6], 0.5), room=0.25)
b3.dur=4
d7.stop()
b3.stop()
b5.stop()
b7.stop()
p3.stop()
p5.stop()

b2 >> prodrums([7, 10, 12, 10, 7, 5], voice=4, dur=0.5, layer1_amp=1.2, layer2_amp=0.9, layer3_amp=1.0, body_tone=var([2400, 2800], 8), harmonic=1.0, fm_amount=0.8, fm_ratio=var([2, 3, 4], 4), waveform=1, decay=0.5, attack=0.05, mid_gain=0.7, high_gain=0.9, amp=0.75, scale=Scale.minor, oct=5)
b6 >> prodrums([0, 3, 7, 5, PWalk(8, 1, 1)], voice=4, dur=PDur(var([5, 7], 8), 8), layer1_amp=1.2, layer2_amp=1.5, layer3_amp=1.0, body_tone=expvar([500, 1400], 16), harmonic=0.8, fm_amount=2.5, fm_ratio=var([2, 2.5, 3, 1.5], 2), waveform=6, texture=var([0, 10, 5], [6,  1, 1]), decay=0.3, mid_sat=1.8, amp=0.8, scale=Scale.minor, oct=4)
b7 >> prodrums([0, 0, 0, PRand([3, 5, 7])], voice=4, dur=var([0.5, 0.25], [3, 1]), layer1_amp=1.5, layer2_amp=1.2, layer3_amp=0.8, body_tone=var([800, 600], 2), harmonic=0.6, fm_amount=1.5, fm_ratio=var([1, 1.5], 1), waveform=2, decay=0.25, low_sat=0.6, mid_sat=0.5,low_gain=1.2, amp=0.85, scale=Scale.minor)
b4 >> prodrums([12, 15, 17, 19, 17, 15], voice=4, dur=0.25, layer1_amp=1.5, layer2_amp=1.2, layer3_amp=1.0, body_tone=var([4000, 4500], 2), harmonic=1.8, fm_amount=2.0, fm_ratio=var([3, 4], 2), waveform=var([1, 2], 4), texture=3, decay=0.2, attack=0.001, high_sat=0.5, high_gain=1.2, amp=0.4, scale=Scale.minor, oct=5, pan=var([-0.5, 0.5], 1))
p1 >> pads([0, 3, 7, 10], dur=8, sus=8, amp=0.6, oct=4, chop=0, room=0.7, mix=0.4, lpf=2000, lpr=0.2, scale=Scale.minor)
x5 >> play("k ", sample=4)
p6 >> glass([7, 10, 12], dur=4, amp=0.5, oct=6, sus=4, verb=0.9, mix=0.6, room=0.8, pan=sinvar([-0.6, 0.6], 16), scale=Scale.minor)
a3 >> a_gesa([12, 15, 17, 19], dur=0.25, cutoff=expvar([2000, 8000], 8), rq=var([0.2, 0.05], 2), dist2=linvar([0.0, 0.5], 16), crush=var([0, 8], 8), unison=8, wide=1.2, detune=var([0.02, 0.05], 4), amp=0.7, oct=6, pan=var([-0.7, 0.7], 0.5), scale=Scale.minor).every(4, 'stutter', 8, dur=0.0625)
a4 >> a_stab([0, 3, 7, 10], dur=var([2, 1, 0.5], [3, 2, 1]), cutoff=var([800, 1500, 400], [4, 2, 2]), dist2=var([1.0, 1.8], 2), rq=0.15, unison=6, wide=0.8, amp=linvar([0.2, 0.4], 8), oct=4, scale=Scale.minor).every(8, 'offadd', 2)
a8 >> a_hhat(0, dur=var([0.125, 0.0625, 0.25], [4, 2, 2]), hpf=2100, sample=7, cutoff=200, bpf=1200)
