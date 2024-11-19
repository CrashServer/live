# organsav
Clock.bpm = 128
Root.default = "E"
Scale.default = Scale.minor

~r1 >> organ(P[var([0, -2, -3, -4], 8), 2, PStep(8, 5, 4), 2], dur=var([PDur(4, 8), PDur([5, 3, 6], 8)],
             [5, 7]), amp=1, crush=1, crush_=4, crush_d=2, bits=6, bits_=var([12, 16]), fmod=1, lpf=2800, lpr=0.4)

r2 >> organ(P[var([0, -2, -3, -4], 8), 2, PStep(8, 5, 4), 2], dur=var([4, PDur(4, 8)], [7, 5]), amp=0.8, crush=1, crush_=4,
            crush_d=2, fx2=0.2, bits=6, bits_=var([12, 8]), oct=(5, 7), fmod=1, lpf=2800, lpr=0.2).unison(2).every(4, "shuffle")

r3 >> bell(P[var([0, -2, -3, -4], 8), 4, PStep(4, 6, 8), 2], dur=var([4, PDur(4, 8)], [9, 3]), amp=0.6, crush=1, crush_=4, crush_d=2,
           mverb=0.2, bits=6, bits_=var([12, 8]), delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")

r4 >> bell(P*[var([0, -2, -3, -4], 8), 2, PStep(8, 5, 4), 2], dur=var([4, PDur(4, 8)], [11, 6]), amp=0.5, crush=1, crush_=4, crush_d=2,
           mverb=0.5, bits=6, bits_=var([12, 8]), r1=0.5, delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")

c2 >> cbass(var([0, -4, -2, -3], 8), dur=1/2, cutoff=40, follow=PFr(1, 4, 555)).unison(2) + (0, var([0, 7], [4, 1]))

r2 >> varsaw(oct=(3, PStep(4, 5, 6), 5), cut=4, cutmix=0.2, lpf=(800, linvar(
    [400, 12000], 128)), dur=[6, 2], sus=[4, 8], lpr=0.1, a=0.5).unison(3)

d1 >> play("x", sample=4, amp=PBin(344))
h3 >> play("s", valad=PFr(1000, 3000)).sometimes("stutter", PRand(16))
n2 >> play("..*.", echo=P*[0, PRand([0.125, 0.5, 0.75])], mverb=0.9, hpf=2000)

h3.hpf = 4000
h3.stop()


b8 >> lbass(var([0, -2, linvar([-2, 0], [8, 0])], [16, 8, 8]), dur=var([1/2, 1/4], [24, 8]),
            cutoff=PFr(4000, 12000), detune=0.9, tone=PFr(0.16, 0.9), dist2=0, oct=var([5, lininf(5, 6, 8)], [24, 8]))

r1 >> dab([-2, PWalk(8, 1, 1), -3, _, _, [0, 0, 3]], leg=4,
          echo=0.25, dur=1/4, oct=PStep(4, [5, 6], [5, 7]))
s1 >> klank(dur=8, oct=(3, 4, 6)).unison(3)  # progressif


s2 >> klank(oct=linvar([5, 6], 128), dur=PDur(3, 8) * 2).slider()
r1 >> dbass()
r2 >> donk()
r3 >> donk()

r4.oct = 7
r4 >> lbass()
q1 >> play("[--]", sample=5)
x1 >> play("x.", sample=var([5, 2], [24, 8]), amp=4, lpf=0)
x2 >> play("u ", sample=3, dur=4, amp=2)

p1 >> play("<E ><p >", sample=0, dur=PDur([3, 5], 8), amp=PWhite(
    2, 1), hpf=220, chop=1/2, leg=PWhite(15), pan=PWhite(-1, 1), fx2=1)

p1.stop()
r_all.dur = 2
r_all.oct = 3

r4 >> dab(dur=PDur(var([4, [5, 3, 8]], [6, 2]), 8), leg=(
    [0, 5]), cutoff=400, dist2=0.4, hpf=1000, hpr=0.1)

s3 >> klank(oct=linvar([5, 6], 128), dur=PDur(3, 5) *
            2, drive=linvar([0.02, 0.04], 32)).stop()
k4 >> lapin(([-4, -3], 4), oct=(3, 4), shape=0.4, fdistfreq=4000, dur=8, lpf=4000,
            fdist=1, hpf=200, bpf=0, lofi=1, amp=PCoin(0.2, 0, 0.25)).unison(2).slider().solo(0)

x4 >> play("..o.")

r2.degree = r4.degree

r3 >> varsaw()
r1 >> varsaw(mverb=0, dur=PDur(var([4, [5, 3, 8]], [6, 2]), 8), oct=3)
r2 >> donk(mverb=0, dur=PDur(var([4, [5, 3, 8]], [6, 2]), 8), oct=4)

r4 >> dbass(dur=var([1/2, 1/4, 2]), amp=2, shape=[0.2, 0.5])

r1 >> dbass(dafilter=PWhite(0.1, 0.1)[:32], lpf=var([400, linvar([400, 3200], 64)], [16, 8]), lpr=0.1, dur=var(
    [1/2, 1/4], [6, 2]), oct=var([6, 7, (3, 4, 5), (3, 4, 6), (4, 5, 6, 7), 3]), mpf=linvar([200, 3200], PRand(8)))

r2 >> donk()
r3 >> donk()

j1 >> bell(P[var([0, -2, -3, -4], 8), 2, PStep(8, 5, 4), 2],
           dur=4, amp=1, feed=0.5, oct=(3, 4), mverb=0.5)

j2 >> lbass(P[var([0, -2, -3, -4], 8), 2, PStep(8, 5, 4), 2],
            dur=2, amp=1, feed=0.5, oct=(3, 4, 5), mverb=0.8)

j1.oct = 2
