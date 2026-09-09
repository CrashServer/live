# unknownfate 138
# album_untitled


Clock.bpm = 138
Scale.default = "minor"
Root.default = "F#"

c1 >> play("-", sample=8, dur=1/4, amp=PWhite(0.06, 0.15), hpf=8000, hpr=0.3, pan=PWhite(-0.4, 0.4), bank=0).degrade(0.05)
p1 >> darkpad([0, 6, 0, 4], dur=16, sus=14, oct=4, amp=linvar([0, 0.4], 32), atk=8, dark=0.85, detune=0.04, cutoff=linvar([300, 1400], 64), room=0.95, mix=0.7, jpverb=0.6, jpsize=0.98, jpdamp=0.4, hpf=140)
e1 >> bell(PRand([0, 7, 11, 4]), dur=PWhite(8, 24), sus=PWhite(4, 12), oct=5, amp=linvar([0, 0.35], 24), cheapverb=0.85, cvdecay=5, jpverb=0.7, jpsize=0.98, jpdamp=0.25, hpf=600, pan=PRand([-0.7, -0.3, 0.3, 0.7]))
b1 >> subbass([0, 0, -5, 0], dur=8, sus=8, oct=4, amp=linvar([0, 1.4], 16), lpf=180, lpr=0.2, hpf=35, tape=0.5, tapedrive=1.4, lofi=0.3, lofiwow=1, smooth=0.1)
e1 >> bell(PRand([0, 7, 11, 4, 9]), dur=PWhite(6, 18), sus=PWhite(4, 10), oct=5, amp=0.4, cheapverb=0.85, cvdecay=5, jpverb=0.7, jpsize=0.98, jpdamp=0.25, hpf=600, pan=PRand([-0.7, -0.3, 0.3, 0.7]))
b1 >> subbass([0, 0, -5, 0], dur=8, sus=8, oct=4, amp=linvar([1.5, 0.7], 24), lpf=linvar([220, 100], 24), lpr=0.2, hpf=35, tape=0.6, tapedrive=1.4, lofi=0.4, lofiwow=1, smooth=0.1)
g1 >> gong(PRand([0, -5]), dur=PWhite(20, 40), sus=PWhite(24, 48), oct=4, amp=0.22, cheapverb=0.95, cvdecay=8, jpverb=0.85, jpsize=0.99, jpdamp=0.2, hpf=300, pan=PRand([-0.5, 0.5]))
h1 >> play("-(--)-(--)-(--)-(-=)", dur=1/4, sample=PStep(16, 1, 3), rate=PWhite(0.95, 1.08), amp=PWhite(0.15, 0.32), pan=PWhite(-0.5, 0.5), hpf=4400).degrade(0.25)
r1 >> pianovel([4, 7, 11, 9, 4, 2], dur=P[8, 4, 4, 8], echo=1, echotime=2, echomix=0.55, velocity=PRand(35, 55), oct=5, amp=0.38, mverb=0.9, jpverb=0.6, jpsize=0.96, jpdamp=0.3, hpf=300, lpf=3200)
b1 >> subbass([0, 0, -5, 0, -7, 0, -3, 0], dur=8, sus=8, oct=4, amp=1.5, lpf=220, lpr=0.2, hpf=35, tape=0.55, tapedrive=1.5, lofi=0.35, lofiwow=1, smooth=0.1)
m2 >> pad2([(0, 2, 4), (-2, 1, 5), (0, 4, 7), (-4, -1, 3), (0, 3, 7)], dur=PWhite(16, 32), sus=PWhite(20, 40), oct=5, amp=0.4, cutoff=linvar([400, 2400], 96), cheapverb=0.9, cvdecay=4.5, jpverb=0.65, jpsize=0.97, jpdamp=0.3, hpf=220, stereowidth=0.88)
y5 >> loop("hiphop16", dur=16)
