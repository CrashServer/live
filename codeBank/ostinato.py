# ostinato — foundation for free-jazz improvisation
# freejazz

Clock.bpm = 68
Scale.default = "dorian"
Root.default = "D"

#@bed
b1 >> subbass([0, 0, 0, 4, 0, 0, -3, 0], dur=PWhite(6, 16), sus=PWhite(8, 24), oct=4, amp=1.3, lpf=260, lpr=0.3, hpf=35, tape=0.4, tapedrive=1.2, pan=0)
p1 >> industrialdrone([0, 4, 0, -3, 0], dur=PWhite(12, 32), sus=PWhite(16, 40), oct=4, amp=0.5, cutoff=linvar([320, 1800], 96), res=0.5, detune=0.4, noise=0.3, sub=0.4, feedback=0.35, cheapverb=0.75, cvdecay=4, miVerb=0.5, mverbfreeze=sinvar([0, 0.7], 48), stereowidth=0.85, hpf=90)
m1 >> pad2([(0, 2, 4), (0, 4, 7), (0, 2, 7), (0, 3, 6)], dur=PWhite(16, 40), sus=PWhite(20, 48), oct=5, amp=0.35, cutoff=linvar([800, 3200], 120), cheapverb=0.7, cvdecay=3, jpverb=0.4, jpsize=0.95, jpdamp=0.3, hpf=220, stereowidth=0.82)
r1 >> bell(PRand([0, 4, 7, 11, 2, 9]), dur=PWhite(6, 20), sus=PWhite(4, 12), oct=6, amp=0.18, cheapverb=0.75, cvdecay=4, jpverb=0.6, jpsize=0.98, jpdamp=0.25, hpf=600, pan=PRand([-0.75, -0.35, 0.35, 0.75]))

#@shift
Root.default = "Eb"
b1 >> subbass([0, 0, 0, 4, 0, 0, -3, 0], dur=PWhite(6, 16), sus=PWhite(8, 24), oct=4, amp=1.3, lpf=240, lpr=0.3, hpf=35, tape=0.45, tapedrive=1.3, pan=0)
p1 >> industrialdrone([0, 4, 0, -3, 0], dur=PWhite(12, 32), sus=PWhite(16, 40), oct=4, amp=0.55, cutoff=linvar([240, 1400], 80), res=0.55, detune=0.45, noise=0.35, sub=0.45, feedback=0.4, cheapverb=0.8, cvdecay=4.5, miVerb=0.55, mverbfreeze=sinvar([0, 0.8], 40), stereowidth=0.88, hpf=100)
m1 >> pad2([(0, 1, 4), (0, 3, 6), (0, 1, 7), (-1, 2, 5)], dur=PWhite(16, 40), sus=PWhite(20, 48), oct=5, amp=0.42, cutoff=linvar([600, 2400], 96), cheapverb=0.8, cvdecay=3.5, jpverb=0.5, jpsize=0.95, jpdamp=0.3, hpf=240, stereowidth=0.82)
r1 >> bell(PRand([0, 3, 6, 10, 1, 8]), dur=PWhite(6, 20), sus=PWhite(4, 12), oct=6, amp=0.2, cheapverb=0.8, cvdecay=4, jpverb=0.65, jpsize=0.98, jpdamp=0.25, hpf=600, pan=PRand([-0.75, -0.35, 0.35, 0.75]))

#@open
b1 >> subbass([0, 0, 0, 4, 0, 0, -3, 0], dur=PWhite(6, 16), sus=PWhite(8, 24), oct=4, amp=1.2, lpf=500, lpr=0.25, hpf=35, tape=0.35, tapedrive=1.2, pan=0)
p1 >> industrialdrone([0, 4, 0, -3, 0], dur=PWhite(12, 32), sus=PWhite(16, 40), oct=4, amp=0.55, cutoff=linvar([1200, 5200], 64), res=0.4, detune=0.4, noise=0.3, sub=0.35, feedback=0.3, cheapverb=0.7, cvdecay=3.5, miVerb=0.45, mverbfreeze=sinvar([0, 0.5], 48), stereowidth=0.9, hpf=120)
m1 >> pad2([(0, 2, 4), (0, 4, 7), (0, 2, 7), (0, 3, 6)], dur=PWhite(16, 40), sus=PWhite(20, 48), oct=5, amp=0.4, cutoff=linvar([1500, 5500], 48), cheapverb=0.65, cvdecay=2.8, jpverb=0.35, jpsize=0.92, jpdamp=0.35, hpf=220, stereowidth=0.85)
r1 >> bell(PRand([0, 4, 7, 11, 2, 9]), dur=PWhite(5, 16), sus=PWhite(4, 12), oct=6, amp=0.3, cheapverb=0.7, cvdecay=4, jpverb=0.6, jpsize=0.98, jpdamp=0.2, hpf=600, pan=PRand([-0.8, -0.35, 0.35, 0.8]))

#@close
b1 >> subbass([0, 0, 0, 4, 0, 0, -3, 0], dur=PWhite(6, 16), sus=PWhite(8, 24), oct=4, amp=1.35, lpf=160, lpr=0.35, hpf=35, tape=0.5, tapedrive=1.4, pan=0)
p1 >> industrialdrone([0, 4, 0, -3, 0], dur=PWhite(12, 32), sus=PWhite(16, 40), oct=4, amp=0.48, cutoff=linvar([160, 780], 80), res=0.6, detune=0.4, noise=0.3, sub=0.55, feedback=0.4, cheapverb=0.85, cvdecay=4.5, miVerb=0.6, mverbfreeze=sinvar([0.2, 0.85], 40), stereowidth=0.82, hpf=85)
m1 >> pad2([(0, 2, 4), (0, 4, 7), (0, 2, 7), (0, 3, 6)], dur=PWhite(16, 40), sus=PWhite(20, 48), oct=5, amp=0.32, cutoff=linvar([380, 1200], 60), cheapverb=0.8, cvdecay=3.5, jpverb=0.55, jpsize=0.96, jpdamp=0.45, hpf=200, stereowidth=0.8)
r1 >> bell(PRand([0, 4, 7, 11, 2, 9]), dur=PWhite(8, 24), sus=PWhite(4, 12), oct=6, amp=0.08, cheapverb=0.85, cvdecay=5, jpverb=0.7, jpsize=0.98, jpdamp=0.3, hpf=600, pan=PRand([-0.75, -0.35, 0.35, 0.75]))

#@sparse
m1.stop()
r1 >> bell(PRand([0, 4, 7, 11, 2, 9]), dur=PWhite(10, 28), sus=PWhite(4, 12), oct=6, amp=0.05, cheapverb=0.85, cvdecay=5, jpverb=0.7, jpsize=0.98, jpdamp=0.25, hpf=600, pan=PRand([-0.75, -0.35, 0.35, 0.75]))
p1 >> industrialdrone([0, 4, 0, -3, 0], dur=PWhite(12, 32), sus=PWhite(16, 40), oct=4, amp=linvar([0.5, 0.22], 12), cutoff=linvar([280, 1400], 80), res=0.55, detune=0.4, noise=0.3, sub=0.45, feedback=0.35, cheapverb=0.8, cvdecay=4, miVerb=0.55, mverbfreeze=sinvar([0.2, 0.7], 40), stereowidth=0.85, hpf=90)

#@dense
b1 >> subbass([0, 0, 0, 4, 0, 0, -3, 0], dur=PWhite(6, 16), sus=PWhite(8, 24), oct=4, amp=1.4, lpf=320, lpr=0.3, hpf=35, tape=0.45, tapedrive=1.3, pan=0)
p1 >> industrialdrone([0, 4, 0, -3, 0], dur=PWhite(12, 32), sus=PWhite(16, 40), oct=4, amp=0.7, cutoff=linvar([400, 2600], 72), res=0.55, detune=0.45, noise=0.4, sub=0.5, feedback=0.4, cheapverb=0.75, cvdecay=4, miVerb=0.5, mverbfreeze=sinvar([0.1, 0.8], 40), stereowidth=0.9, hpf=95)
m1 >> pad2([(0, 2, 4), (0, 4, 7), (0, 2, 7), (0, 3, 6)], dur=PWhite(16, 40), sus=PWhite(20, 48), oct=5, amp=0.48, cutoff=linvar([900, 3600], 80), cheapverb=0.7, cvdecay=3, jpverb=0.45, jpsize=0.95, jpdamp=0.3, hpf=220, stereowidth=0.88)
r1 >> bell(PRand([0, 4, 7, 11, 2, 9]), dur=PWhite(4, 14), sus=PWhite(4, 12), oct=6, amp=0.3, cheapverb=0.7, cvdecay=4, jpverb=0.6, jpsize=0.98, jpdamp=0.25, hpf=600, pan=PRand([-0.8, -0.35, 0.35, 0.8]))
f1 >> sinepad([(0, 4, 7, 11), (0, 3, 7, 10), (-2, 2, 5, 9)], dur=PWhite(24, 56), sus=PWhite(28, 64), oct=6, amp=0.22, spectralfreeze=sinvar([0.3, 0.7], 40), freezerand=0.3, jpverb=0.7, jpsize=0.98, jpdamp=0.2, hpf=420, stereowidth=0.9)
g1 >> gong(PRand([0, 4, 7, 11]), dur=PWhite(18, 48), sus=PWhite(12, 30), oct=5, amp=0.25, cheapverb=0.8, cvdecay=5, jpverb=0.65, jpsize=0.98, jpdamp=0.25, hpf=300, pan=PRand([-0.6, 0.6]))

#@home
Root.default = "D"
b1 >> subbass([0, 0, 0, 4, 0, 0, -3, 0], dur=PWhite(6, 16), sus=PWhite(8, 24), oct=4, amp=1.3, lpf=260, lpr=0.3, hpf=35, tape=0.4, tapedrive=1.2, pan=0)
p1 >> industrialdrone([0, 4, 0, -3, 0], dur=PWhite(12, 32), sus=PWhite(16, 40), oct=4, amp=0.5, cutoff=linvar([320, 1800], 96), res=0.5, detune=0.4, noise=0.3, sub=0.4, feedback=0.35, cheapverb=0.75, cvdecay=4, miVerb=0.5, mverbfreeze=sinvar([0, 0.7], 48), stereowidth=0.85, hpf=90)
m1 >> pad2([(0, 2, 4), (0, 4, 7), (0, 2, 7), (0, 3, 6)], dur=PWhite(16, 40), sus=PWhite(20, 48), oct=5, amp=0.35, cutoff=linvar([800, 3200], 120), cheapverb=0.7, cvdecay=3, jpverb=0.4, jpsize=0.95, jpdamp=0.3, hpf=220, stereowidth=0.82)
r1 >> bell(PRand([0, 4, 7, 11, 2, 9]), dur=PWhite(6, 20), sus=PWhite(4, 12), oct=6, amp=0.18, cheapverb=0.75, cvdecay=4, jpverb=0.6, jpsize=0.98, jpdamp=0.25, hpf=600, pan=PRand([-0.75, -0.35, 0.35, 0.75]))

#@fade(48)
b1 >> subbass([0, 0, 0, 4, 0, 0, -3, 0], dur=PWhite(6, 16), sus=PWhite(8, 24), oct=4, amp=linvar([1.3, 0], 48), lpf=260, lpr=0.3, hpf=35, tape=0.4, tapedrive=1.2, pan=0)
p1 >> industrialdrone([0, 4, 0, -3, 0], dur=PWhite(12, 32), sus=PWhite(16, 40), oct=4, amp=linvar([0.5, 0], 48), cutoff=linvar([320, 1800], 96), res=0.5, detune=0.4, noise=0.3, sub=0.4, feedback=0.35, cheapverb=0.75, cvdecay=4, miVerb=0.5, mverbfreeze=sinvar([0, 0.7], 48), stereowidth=0.85, hpf=90)
m1 >> pad2([(0, 2, 4), (0, 4, 7), (0, 2, 7), (0, 3, 6)], dur=PWhite(16, 40), sus=PWhite(20, 48), oct=5, amp=linvar([0.35, 0], 48), cutoff=linvar([800, 3200], 120), cheapverb=0.7, cvdecay=3, jpverb=0.4, jpsize=0.95, jpdamp=0.3, hpf=220, stereowidth=0.82)
r1 >> bell(PRand([0, 4, 7, 11, 2, 9]), dur=PWhite(6, 20), sus=PWhite(4, 12), oct=6, amp=linvar([0.18, 0], 36), cheapverb=0.75, cvdecay=4, jpverb=0.6, jpsize=0.98, jpdamp=0.25, hpf=600, pan=PRand([-0.75, -0.35, 0.35, 0.75]))
