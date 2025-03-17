# antenna

Clock.bpm = 122/2;
Scale.default = Scale.minor
Root.default = "F#"

e0 >> plaits(melody(),dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), drive=0, mverb=0.1, oct=3, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))
e0 >> plaits(melody(),dur=(1/2, 1/4), engine=(1, 4), drive=0, mverb=0.8, oct=5)
e1 >> bass(melody()[:8],dur=var([1/4, 2],[13, 3]), a=PWhite(0, 1), drive=0, amp=0.7, mverb=0.8).unison(2).every(13, "offmul", 2)
e0.every(4, "shuffle")

e1 >> bass(melody(),dur=1/4, oct=5, drive=0, mverb=0.8).unison(0)
e1 >> bass(melody(),dur=1/4, drive=linvar([0, 0.02], 32), mverb=0.8).unison(0)
g2 >> bass(melody() + var([7, 3, [4, 0]]),dur=var([1/4, 1/2]), drive=0, vol=0.5, mverb=0.1).unison(0)

Root.default = "E"
Scale.default = Scale.minor

# Melodic Foundation - Smoother Organ Layers
~r1 >> organ(
    P[var([0,-2,-3,-4],16), 2, PStep(8,5,4), 2],  # Wider variation
    dur=PDur(6,8),  # More breathing room
    amp=0.7, 
    crush=0.5,  # Less aggressive bitcrushing
    bits=8,  # Higher bit depth
    fmod=0.5,  # Gentler frequency modulation
    lpf=2000,  # Lower filter cutoff for warmth
    lpr=0.3,  # Softer resonance
    reverb=0.2  # Added subtle reverb
).spread(2)  # Wider stereo field

f0 >> organ(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([PDur(4,8),PDur([5,3,6],8)]), amp=1, crush=1, crush_=4, crush_d=2, bits=6, bits_=var([12, 16]), fmod=1, lpf=2800, lpr=0.4).solo(0)
r2 >> organ(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.8, crush=1, crush_=4, crush_d=2, fx2=0.2, bits=6, bits_=var([12, 8]), oct=(5, 7), fmod=1, lpf=2800, lpr=0.2).unison(2).every(4, "shuffle")

e_all.stop()




# Complementary Bell Texture
~r3 >> bell(
    P[var([0,-2,-3,-4],16), 4, PStep(4,6,8), 2],
    dur=PDur(5,8),  # Slightly irregular rhythm
    amp=0.5, 
    crush=0.3,  # Even less aggressive
    mverb=0.3,  # Moderate verb
    delay=0.25,  # Subtle echo
    oct=(5, 6, 7),  # Higher register for airiness
    lpf=2800,  # Brighter top end
    fmod=0.3
).every(4, "rotate")  # Subtle pattern rotation

e1 >> plaits(melody(),dur=var([1/2, (1/2, 2)]), drive=0, mverb=0.8, engine=var([11, 5], [3, 1]), oct=5).unison(0)

r4 >> bell(P[var([0,-2,-3,-4],8),4,PStep(4,6,8),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.6, crush=1, crush_=4, crush_d=2, mverb=0.2, bits=6, bits_=var([12, 8]), delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")
b5 >> bell(P*[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.5, crush=1, crush_=4, crush_d=2, mverb=0.5, bits=6, bits_=var([12, 8]), r1=0.5, delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")

e0.dur=var([2, 1/4, 1/4, 1/4, 1/4])
e3 >> bass(melody(),dur=1/4, drive=linvar([0, 0.05], 32), mverb=0.8, delay=var([0, 0.5]), oct=6)
e3 >> lbass(dur=1/2, oct=4, drive=1, amp=PBin(8))
e0 >> plaits(melody(),dur=(1/2, 1/4), engine=(1, 4), drive=0, mverb=0.8, oct=5)

r2 >> varsaw(oct=(3, PStep(4, 5, 6), 5), cut=4, cutmix=0.2, lpf=(800, linvar([400, 12000], 128)), dur=[6, 2], sus=[4, 8], lpr=0.1, a=0.5).unison(3)

e3.stop()
g1 >> dbass(delay=0.25,dur=1/4, dist2=0, lpf=120, cut=1/2, mverb=0.01, mpf=linvar([200, 2000], 128), vol=0.5, rate=(0.5, 1)).unison()

g3 >> lbass(dur=1/4, hpf=400, drive=0.0, lpf=1200, mpf=1600)
g_all.lpr=linvar([0.5, 0.1], [1, 4, 8])
e3.dist2=0.5

g_all.only()
Clock.bpm = 122;

# Breakbeat Drum Foundation
~h1 >> play("b(3,8)", 
    sample=var([0,1,2],8),  # Varied drum samples
    cut=0.1,  # Tighter cuts
    dur=PDur(3,8),  # Syncopated rhythm
    amp=0.8, 
    lpf=1200,  # Filtered for smoothness
    hpf=200,   # Low-end warmth
    pan=PWhite(-0.5,0.5)  # Subtle stereo movement
)

h3 >> play("s", valad=PFr(1000,3000)).sometimes("stutter", PRand(16))
n2 >> play("..*.", echo=P*[0,PRand([0.125, 0.5, 0.75])], mverb=0.9, hpf=2000)


g3.dur=lininf(1/2, 1/8, 32)
g3.dist=0.3
g3.mverb=0.5

g_all.stop()

p1 >> pluck(var([([7, 0], 0), [(12, 0), ([Scale.chromatic, 0], 0), (0, [12, 7])]]),oct=(3, PStep(16, 3, 4)), dur=PwRand([[4, 1, 1/2], P[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2]], [1, 30]), leg=linvar([0, 4], PRand(16)[:4]), pan=linvar([-1, 1], [32]), scale=Scale.chromatic, drive=var([PWhite(0.01, 0.1), [0, (0.01, 0.2)]]), hpf=PWhite(30, 60), hpr=(0.1, 0.9)).sometimes("stutter", 1, mverb=0.6, feed=0.2, rate=0.2, shape=0.2) + var([0, 3, 4], [PRand([24, 128]), 2, 2])
h3.stop()
e3 >> lbass(dur=1/4, oct=PRand([4, 5, 6])[:4], drive=0.3)
g2 >> dbass(dur=1/4, echo=var([1/3, 0]), lpf=0, cut=0, mverb=0.04, mpf=linvar([200, 12000], 128), vol=0.5, rate=(0.25, 0.5), oct=7, hpf=linvar([2000, 12000], 32), engine=(3,10)).unison(2)

b1 >> bass([0, 7, 5, 4], dur=1/2, amp=0.8, drive=1, lpf=800, mverb=0.2)
n2.stop()
s2 >> klank(oct=linvar([5, 6], 128), dur=PDur(3, 8)* 2).slider()

attack("filter")
##### attack@filter.znn:~$ #####
masterAll("lpf", var([0, 4000, 6000, 15000], [24, 4, 2, 2]))
masterAll("hpf", var([0, 20, 30, linvar([3200, 6400], 32)], [24, 4, 2, 2]))
masterAll("cut", var([0, 1, 1/2, linvar([1/4, 1], 32)], [24, 4, 2, 2]))
masterAll("reset")
r4.oct=7

r4 >> lbass()
q1 >> play("[--]", sample=5)
x1 >> play("x.", sample=var([5, 2], [24, 8]), amp=1, lpf=0)
x2 >> play("u ", sample=3, dur=4, amp=2)

b8 >> lbass(var([0, -2, linvar([-2,0],[8,0])], [16,8,8]), dur=var([1/2,1/4],[24,8]), cutoff=PFr(4000,12000), detune=0.9, amp=0.4, tone=PFr(0.16,0.9), dist2=0.9, oct=var([5,lininf(5,6,8)],[24,8])).stop()
 
