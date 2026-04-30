# twoheadedstate 68
# ambient
Clock.bpm = 68
Scale.default = "dorian"
Root.default = "D"


m1 >> pad2([(0, 2, 4), (0, 4, 7), (0, 2, 7), (0, 3, 6)], dur=PWhite(16, 40), sus=PWhite(20, 48), oct=5, amp=0.8, cutoff=linvar([800, 3200], 120), cheapverb=0.7, cvdecay=3, jpverb=0.4, jpsize=0.95, hpf=220, stereowidth=0.82)
r1 >> bell(PRand([0, 4, 7, 11, 2, 9]), dur=PWhite(6, 20), sus=PWhite(4, 12), oct=5, amp=0.4, cheapverb=0.75, cvdecay=4, jpverb=0.6, jpsize=0.98, jpdamp=0.25, hpf=600, pan=PRand([-0.75, -0.35, 0.35, 0.75]))
g1 >> gong(PRand([0, 4, 7, 11]), dur=PWhite(18, 48), sus=PWhite(12, 30), oct=5, amp=0.125, cheapverb=0.8, cvdecay=5, jpverb=0.65, jpsize=0.98, hpf=300, pan=PRand([-0.6, 0.6]))
m3 >> pad2([(0, 2, 4), (0, 4, 7), (0, 2, 7), (0, 3, 6)], dur=PWhite(16, 40), sus=PWhite(20, 48), oct=5, amp=0.35, cutoff=linvar([800, 3200], 120), cheapverb=0.7, cvdecay=3, jpverb=0.4, jpsize=0.95, jpdamp=0.3, hpf=220, stereowidth=0.82)
m2 >> pad2([(0, 1, 4), (0, 3, 6), (0, 1, 7), (-1, 2, 5)], dur=PWhite(16, 40), sus=PWhite(20, 48), oct=5, amp=0.42, cutoff=linvar([600, 2400], 96), cheapverb=0.8, cvdecay=3.5, jpverb=0.5, jpsize=0.95, hpf=240, stereowidth=0.82)
b1 >> subbass([0, 0, 0, 4, 0, 0, -3, 0], dur=PWhite(6, 16), sus=PWhite(8, 24), oct=4, amp=1.3, lpf=260, lpr=0.3, hpf=35, tape=0.4, tapedrive=1.2, pan=0)




