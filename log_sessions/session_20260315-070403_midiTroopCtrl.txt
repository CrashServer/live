# SAINT 120
# interlude

Root.default='C'
Scale.default="minor"
Clock.bpm = lininf(120, 170, 128)

b1 >> lbass(var([0, -2, 0.5], 8), formant=var([0, 0.1], [24, 8]), formantmix=PWhite(0, 0.3), oct=(6, 5, [4, 3]) + var([0, 1], [14, 2]) + PwRand([0, 1, 1.25], [30, 1, 1]), rate=linvar([1.2, 0.3], [32]), fmod=linvar([0, 1], [128]), scale=Scale.chromatic, drive=var([0, (0.1, 0)], [12, 4]), dur=1/2, amp=0.5, mverb=0, mverbdamp=[0.2, 1], mverbdiff=[1, 0.4], hpf=linvar([100, 400], 8)).unison(4).every(8, "stutter", slide=0.01, lpf=linvar([4000, 8000], 16))
b3 >> soprano((b1.degree, 0), dur=PRand(1,8), blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(7,6,5)), drive=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), room=0.5, mix=0.5, amplify=0.5, spin=0).unison(2)
b1.rate=lininf(1, 0.1, 32)
b1.mverb=0.0
b1.lpr=lininf(1, 0.1, 64)
b1.slide=var([0, 1], [28, 4])
b1.degree=0.5
b1.chop=var([0, 1, 1/2], [12, 2, 2])
b4 >> play("(#....)..(...~)", rate=PWhite(-1,4)*0.25).unison(3, 1,99)
b5 >> play("@", sample=2, hpf=4000).fill(0)
b6 >> play("-", dur=1/2, amp=0.5, sample=(var([3, 4], [4, 4]), 3), glide=1,shift=var([0, 2], [24, 8]), pshift=0).slider()
b7 >> play(var(["-.--", "[--]"], 8), sample=1, rate=0.5, formant=0.4, hpf=7000)
b1.dur=lininf(1/2, 1/4, 16)
b8 >> dbass(var([0, -2, 0.5], 8), oct=(6, 5) + var([0, 1], [14, 2]), rate=linvar([1.2, 0.3], [64]), scale=Scale.chromatic, dur=1/2, amp=1, hpf=100).slider().unison(4).solo(0)
b1.lpf=linvar([3200, 1600], 128)
b1.amp=0.8
e1 >> play("# ", dur=4, rate=(-1, 2)).unison(2).after(4, "stop")
e2 >> play("# ", sample=(1,4), dur=4, rate=(-1, 1)).after(8, "stop")
e3 >> play("& ", sample=5, rate=-2, shift=4, dur=4).after(32, "stop")
e4 >> play("#k", sample=(1,4), dur=4, rate=(-1, 1), mverb=1, room2=0.5,  chop=0.25, chopmix=[0.5, 0], damp2=0.9, revsus=1).after(4, "stop")

