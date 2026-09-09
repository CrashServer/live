# ultimate partition 48
# ambient

Scale.default = Scale.yu;
Root.default = "G"
Clock.bpm = 48;

a1 >> play("b", dur=4, shape=0, sample=12, mverb=0, valad=400, valadd=4, feed=0.5, amp=0.8)
a2 >> play("V ", dur=2, sample=12, shape=0, mverb=0, valad=400, valadd=4, feed=0.5, amp=0.2).unison(2)
a1 >> play("b", dur=var([1/6, 1/2], [12, 4]), sample=4, amp=var([0.1, P[PWalk(10, 1, 1)]/4]), shape=0.1, mverb=0, valad=1200, delay=1/3, shift=0, leg=4, valadd=4)
a3 >> play("//o.", dur=2, sample=PwRand([12, 10, 6, 8], [1, 8, 3, 2]), shape=0, mverb=0, valad=400, valadd=4, feed=0.5, amp=0.3).unison(2)
a2 >> rsin(dur=2, lpf=3400, hpf=2400, hpr=0.9, chop=4, sus=2, amp=linvar([0.1, 0.5]), shape=0.2, rate=0.5, mverb=0, dist2=0.2)
y1 >> varsaw(P*[  P*[Scale.yu, Scale.minorPentatonic][:4], Scale.egyptian ][:16], dur=P*[1/2, 1/2, (4, 1/2), 1/2, 1/2, 4], chop=0, oct=PwRand([3, 4, 5, 5.012, 3.1], [2, 3, 5, 6, 2]), echomix=PWhite(0, 1), echo=(0.5, 1.25, 2, 0.25, linvar([0.25, 0.1], 32)), echotime=4, delay=(( P[1.25, 0.25], PRand([0.25, 6, 0.75, 1, 1.25]))), mverb=0.5, shift=0.5, low=21, room2=1, glide=(0.5, 4, 0.75), sus=y1.dur+4, amp=PBin()/2, lpf=linvar([200, 4000], PRand(32))).sometimes(4, "shuffle").unison(0).slider()

y1 >> bass(P*[Scale.yu, Scale.minorPentatonic][:8],amp=PBin()/4, mverb=0.3, dur=P*[2, 1/2, (4, 1/2), 4, 1/2], rate=1,  oct=PwRand([3, 4, 3, 4, 3], [2, 3, 4, 3, 2]), echo=((1, 2, 4), (0.5, 0.25, 0.75)), echotime=8, delay=(( P[0.5, 2], PRand([0.25, 0.5, 0.75, 1, 1.25]))), fdist=1, sus=y2.dur+PWhite(0, 1)).every(4, "shuffle").slider()
y1 >> bass(P*[Scale.yu][:2],amp=PBin()/4, dur=P*[2, 1/2, (4, 1/2), 4, 1/2], phaser=0.25, shift=0.5, tanh=0.2,  oct=PwRand([3, 4], [2, 3, 4, 3, 2]), echo=(0.5, 0.25), feed=0.5, echotime=8, delay=(( P[0.5, 2], PRand([0.125, 0.125, 0.25, 1, 1.25]))), sus=y3.dur+PWhite(0, 1), dist2=0, mverb=0.5, shape=0.3, formant=0.2).every(6, "shuffle").unison(0).slider()

c1 >> cluster(dur=4, delay=(0, 2), leg=0, fmod=0, rate=1, oct=4, mverb=0.5, amp=1.4)
a_all.stop()
y_all.only()
y_all.shift=2
c1.stop()
y_all.chop=8
y_all.leg=4

y_all.lpr=0.05
y_all.lpf=2000

k1 >> play(".[--][Kk]k", rate=0.5, mverb=0.9, dur=7/3, amp=2, echo=0.25, sample=4)

# THE ULTIMATE PARTITION

# PART FRICA _____________

# --->DEBUT TROP REMPLI

k0 >> loop("frica8", dur=8, sample=2, dist2=0, echo=2, echotime=4)
j1 >> loop("frica8", dur=16, sample=3, dist2=0, echo=2, echotime=4)
k1 >> loop("perc8", dur=8, sample=1, dist2=var([0, 1]))
k0 >> play("TtPm")
k2 >> loop("nblstutter170", dur=32, sample=0, dist2=0, spf=3200, spfslide=16, spfend=200, mverb=0.5, hpf=400, hpr=1)
k3 >> loop("xhop16", dur=16, sample=2, dist2=0.2, hpf=2000, hpr=0.1)
k4 >> play("k", sample=2, amp=[1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], dist2=0.5)
k5 >> loop("hihat16", dur=16, shift=0.5, echo=0.5, sample=4, dist2=0)

k6 >> play("+", dur=PDur(3, 16))
k7 >> play("+", sample=9, dur=PDur(7, 16))
k8 >> play("p", dur=1, sample=4, delay=0.5, hpf=400, hpr=0.1)
k9 >> loop("dnbfx16", dur=16, shift=0, sample=2, dist2=0)

k0 >> play("k", sample=2, delay=var([0.5, (0.5, 1)]), amp=[1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])
k1 >> loop("fx8", dur=8, sample=2, dist2=0)
k2 >> play("k", dur=1/4, sample=var([7, 8, 2]), delay=var([0.5, (0.5, 1)]), amp=[1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], dist2=2)

k3 >> loop("rhythm8", dur=8, sample=1, dist2=0)
k5 >> loop("xtbass16", dur=16, amp=1, sample=0, dist2=0)
k6 >> loop("xtech8", dur=8, amp=1, sample=0, dist2=0)

t1 >> fbass(dur=[2, 1/2, 1/2, 1/4, 1/4, 1/4, 1/4], dist2=0).unison(0)
t2 >> dbass(dur=P[2, 1/2, 1/2, 1/4, 1/4, 1/4, 1/4]/2, oct=5, dist2=0, leg=4, high=4).unison(4)

# PART ________________________________ DIAMANT

Clock.bpm = 122;

e0 >> tb303(0, dur=1/4, cut=1/2, amp=PBin(), cutoff=var([200, 3200, 4000, 8000], [8, 12, 4, 8]), top=PRand(1200)[:8], rq=0.01, dec=var([0.1, 0.2, 0.5, 12], [4]))

e1 >> tb303(0, dur=var([1/2, 1/4], [4, 8]), cut=1/2, amp=1, oct=var([4, 5], [24, 8]), dist2=1, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:16], rq=[0.01, 0.001, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))

e2 >> tb303(dur=var([1/4, 1/2], [4, 8]), cut=1, amp=1, oct=var([3, 7], [24, 8]), dist2=1, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:8], rq=[0.01, 0.001, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))

e3 >> tb303(dur=1/2, cut=1/2, delay=0.125, amp=1, oct=var([6, 7], [24, 8]), dist2=1, cutoff=var([2000, 3200, 400, 800], [32]), top=PRand(1200)[:8], rq=[0.01, 0.001, 0.2, 0.5, 1], dec=var([0.1, 0.2, 0.5, 12], [4]))

e4 >> varicelle([0, -4], dur=4, dist2=1, mverb=0.5, oct=3, disto=1, dist=1, tanh=1).unison(4)

e3.stop()
e5 >> tb303(dur=var([1/4, 1/2], [4, 8]), cut=1, amp=1, oct=var([3, 7], [24, 8]), dist2=1, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:8], rq=[0.01, 0.001, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))

e0 >> fbass()
e1 >> fbass()
e2 >> ebass()
d1 >> play("x ", sample=6)
d2 >> play("--=-", sample=[2, 2, 1, 1], dur=1/4, delay=PWhite(-0.01, 0.01))
d3 >> play("+", sample=6, delay=PRand([-1/4, 1/4, 0]))
d4 >> play("c", sample=6, amp=var([0, 1], [12, 4]), amplify=PBin())
d5 >> play("C", sample=0, amp=var([0, 1], [12, 4]), amplify=PBin())
e1 >> play("X ")

e9 >> faim(dur=1/4,dist2=0, shape=[0, 1]).unison(4)
e8 >> tb303(dur=PDur(5, 16), cutoff=400, rq=0.04, oct=3)

# PART --------------------------------------

b1 >> ssaw([7, 4, 4, 3, (8, -4), 8, ([-4, _], [-4, (_, (4, 4)), 8])], a=(0.1, linvar([0.1, 0.8], 32)), oct=(5, 6), r=0.4, dur=1/2, sus=(3/4, 1/2), scale=Scale.chromatic)
b2 >> ssaw([_, 4, _, 3, (_, -4), 8, ([-4, _], [-4, (_, (4, 4)), 8])], a=(0.1, linvar([0.1, 0.8], 32)), oct=(5, 4), r=0.1, dur=1/4, sus=(1/2, 1/4), scale=Scale.chromatic)

# ------------------------------------------------------------------------------------------------------------------

PART [120] # cute pad 

b2 >> sinepad([8,8,(8, 3), _], dur=var([ (1/2, 1/4, 1/2, 1), 1], [2, 8]),oct=var([ PArp([4, 5, 4]), 5]), lpf=1200, scale=Scale.chromatic).every(2, "stutter", degree=-60, mpf=1200, hpf=200, leg=32, dist2=2, echo=(2, 0.5, 3), echotime=8, mverb=0.5, shift=1, low=1, high=12, feed=0.5).every(1, "stutter", degree=var([12, 4, 8, 12], 8), leg=40, bpf=linvar([200, 4000], 32), bpr=0.85, dist2=0, echo=(2, 0.5, 3), echotime=8, mverb=0.5, shift=1, low=1, high=21, feed=0.5)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# [PART 96]

# [intro seule]

a3 >> plaitsX(var([ var([0, 2], [12, 4]), 6], [7, 1]),oct=var([3, (2, 3)]), cut=(2, P[0.5, 1]), sus=(1, 1/2), spfslide=(0.3, 0.1), dur=(2, 1, 1/4), delay=(0, (0.25, 0.5), 1, 0.01), spfend=(3200, (linvar([200, 3000], 32), 320)), shape=0, spf=(linvar([200, 4000], 32), linvar([2000, 12000], 8)), low=3, echo=2, high=21, mid=6).unison(4)

[PART170]

Clock.bpm = 170

d1 >> plaitsX(oct="3", dur=1/2, blur=1, sus=[0.6, 1, 0.7, 0.5])

d2 >> plaitsX(oct=var([3, 2, 4], [7, 3, 2]), preset=var([(P*[2, 6, 1, 2], 3), (3, 7), 7], [4, 2, 2]), dur=1/2, blur=1, sus=[0.6, 1, 0.7, 0.5]).unison(2)

d3 >> plaitsX(oct=var([3, 2, 4], [2, 3, 2]), cut=1/128, mverb=0.0, amp=1, preset=var([(P*[2, 6, 1, 2], 3), (3, 7), 7], [4, 2, 2]), dur=1/4, blur=1, sus=[0.6, 1, 0.7, 0.5]).unison(2)
d3.mverb=0

d3.cut=1/2
f3.amp=PBin()

d4 >> pianovel(0, engine=8,oct=5,dur=P*[(1, 1/2), P(1/2, 1, P*[1/2, 1, 1/4])], amp=PBin(), sus=[0.5, 1, 0.3, 0.2], vol=0.5).sometimes("offadd", P[-4, -3, 4])
d1 >> tb303(oct=(3, 4, 5),dur=P[(1, 1/2), P(1/2, 1, P*[1/2, 1, 1/4])], amp=PBin(), vol=0.7).sometimes("offadd", P[-4, -3, 4])
d3 >> donk(var([-4, 4, -4], 8),oct=4, cut=(2, P[0.5, 1]), sus=(1/4, 1/2), spfslide=(0.3, 0.1), dur=(4, 1, 1/4), delay=(0, (0.25, 0.5), 1, 0.01), spfend=(3200, (linvar([200, 3000], 32), 320)), shape=0, spf=(linvar([200, 4000], 32), linvar([2000, 12000], 8)), low=0, echo=1, amp=0.5, high=4, mid=12).unison(4)
d2 >> organ(var([-4, 4, -4], 8),oct=5, cut=(2, P[1/2, 1]), sus=(1/4, 1/2), spfslide=(0.3, 0.1), dur=(4, 1, 2), delay=(2, (0.25, 0.5), 1, 0.01), spfend=(3200, (linvar([200, 3000], 32), 320)), shape=0.1, spf=(linvar([200, 4000], 32), linvar([2000, 12000], 8)), low=0, echo=1, amp=0.5, high=4, mid=12).unison(4)

[EVOLUTION]

d4 >> play("x ").sometimes("stutter", delay=0.25, rate=2)
d3.dur=4
d2.shape=0.2
d5 >> play("..u.", sample=var([2, 4], [5, 4]), echo=5)
d6 >> play("X ", sample=3)
d7 >> play("xK..")
d3 >> play("[-[-]].[-]-", dist2=4, rate=2, cut=1/4, sample=8, echo=0.5,lpf=2120)
k2 >> play("..-.", delay=(1.5,(0.5, 1.25)), sample=(0, 2), leg=3, mverb=(0, 0.2))
k4 >> play(".(.[:S]).",  sample=4, pan=-1, mverb=0.8, a=0.3)
b_all.dur=1
j1 >> play("..c.")
d_all.oct=var([(3, 4), (5, 5)])

# [NEWBEAT 133]

[GLAUCK]

b2 >> sinepad([8,8,(8, 3), _], vol=0.2, dur=var([ (1/2, 1/4, 1/2, 1), 1], [2, 8]),oct=var([ PArp([4, 5, 4]), 5]), lpf=1200, scale=Scale.chromatic).every(2, "stutter", degree=-60, mpf=1200, hpf=200, leg=32, dist2=2, echo=(2, 0.5, 3), echotime=8, mverb=0.0, shift=1, low=1, high=12, feed=0.5).every(1, "stutter", degree=var([12, 4, 8, 12], 8), leg=40, bpf=linvar([200, 4000], 32), bpr=0.85, dist2=0, echo=(2, 0.5, 3), echotime=8, mverb=0.0, shift=1, low=1, high=2, feed=0.5)

b3 >> sinepad([8,8,([3, -4, 3], 12), (_, -4)], vol=0.1, dur=var([(2, 4, 4, 1), 1], [2, 8]),oct=var([ PArp([4, 5, 4]), P[6, 4]]), lpf=linvar([400, 4000], 32), scale=Scale.chromatic).every(2, "stutter", degree=-60, mpf=1200, hpf=200, leg=32, dist2=0, echo=(2, 0.5, 3), echotime=8, mverb=0, shift=1, low=1, high=12, feed=0.5).every(1, "stutter", degree=var([12, 4, 8, 12], 8), leg=4, bpf=linvar([200, 4000], 32), bpr=0.85, dist2=0, echo=(2, 0.5, 3), echotime=8, mverb=0.5, shift=1, low=1, high=4, feed=0.5)

b2 >> bell()
k3 >> play("Z", dur=1/2, sample=[PWalk(8, 1, 1), 9, 8], hpr=0.9, hpf=120,delay=(1.0,(0.5, 2)), a=0.5, rate=0.1, cut=1/2)
k2 >> play("..-.", delay=(1.5,(0.5, 1.25)), sample=(0, 2), leg=3, mverb=(0, 0.2))
k4 >> play(".(.[:S]).",  sample=4, pan=-1, mverb=0.8, a=0.3)
b_all.dur=1

b3 >> lbass()
b2.oct=3

# [INTRO CRADE]

Clock.bpm = 120;

a1 >> donk(oct=1, hpf=100,  bits=1, crush=12, echo=(0.5, 4, 8,12), echotime=12, krush=4, chop=4, fmod=(0, 12), dist2=0.4,  dur=16, sus=8, spf=(3200, 40), delay=(0, 0.25, 0.5, 0.75, 2, 4, 8), dubd=0.5, feed=0.4, shift=(4, 1, 0), dublen=0.1, mverb=0.5, spfslide=(4,PWhite(0, 4)), spfend=(PWhite(2000, 10000),PWhite(2000, 10000))).unison(6)
a2 >> play("k.", dist2=1, sample=4, delay=0, valadd=1, leg=0, valad=20, mverb=(0.5, 0), mverbdamp=0.2).every(2, "stutter", rate=2, dist2=0, sample=2, leg=4).sometimes("stutter", rate=4, echo=0.25)
c1 >> play("%", dur=8, mverb=0.5, sample=4, rate=1, leg=4, amp=4)

d3 >> play("k.", dist2=0, sample=4, delay=0, valadd=0, valad=0, mverb=(0.5, 0), mverbdamp=0.2).every(4, "stutter", rate=2).sometimes("stutter", rate=4, echo=0.25)
a2 >> play("K.", dur=2, dist2=0, sample=var([3, 4]), mverb=(0.5, 0), mverbdamp=0.2).every(4, "stutter", rate=2)

a1 >> play("T ", amp=4, dur=4, dist2=0)

a3 >> play("ko", dist2=2, sample=4, mverb=0, mverbdamp=0.2).every(5, "stutter", rate=2)
a5 >> play("n.", dist2=1, sample=2, mverb=(0.5, 0), mverbdamp=0.2).every(4, "stutter", rate=2)

a1 >> bass(rate=0.2, leg=128, cut=1, tanh=8).every(4, "stutter").every(4, "shuffle").every(7, "stutter", rate=4, echo=0.25, dist2=2, hpf=1200, tanh=4, bits=1, crusher=4).unison(4)

d1 >> dbass(P[-65, -65, -65, -65, 11, 12].stutter(2), dur=1/2, dist2=1, shape=0, revsus=1, mverb=0.5, amp=2, oct=(6, 5))

133 > NEWBEAT
Clock.bpm = 133;
Root.default = "D#"
d1 >> dbass([3, 4, 4, 8, 4, 7,  4, 4], scale=Scale.chromatic, dur=1/2, hpf=linvar([4000, 400], 32)).unison(2)
d2 >> dbass([3, 4, 4, 8, 4, 7, 4, 4], oct=P[5, 6], scale=Scale.chromatic, dur=1/2, echo=0.25)
d3 >> ssaw(P*[3, 4, 4, 8, 4, 7, 4, 4], scale=Scale.chromatic, dur=1/2, amp=PWhite(0, 1), oct=6)
d4 >> zap([3, 4, 4, 8, 4, 7, 4, 4], scale=Scale.chromatic, dur=1/4, oct=PWalk(4, 1, 1) + 2, dist2=1).unison(2)
d5 >> play("x ", sample=4, hpf=40, amp=0.8, lpf=4000, mverb=(0, 0.1), hpr=[0.1, 0.5])
d6 >> play("pM", lpf=1200, hpf=1200, dur=var([2, PDur(3, 8)]), lpr=linvar([0.1, 0.8], [8, 16]), rate=(1, 0.5, 0.25), delay=(0, 0.25, 1), amp=1)
d1 >> ebass([0, 0, 0.1, 0, 2], dur=1/2, hpr=0.1, oct=6, hpf=400, mverb=0.01).slider().unison(4) + var([0, 14], [15, 1])
d2.dur=1/2
d2.dist2=0.3
d2.mverb=0.5
d3 >> play("p", amp=P[1, 1, 1, 1, 0.1, 0.1].stutter(2), sample=5, shape=var([0, 0.5, 1]), vol=2)
d4 >> play("+", amp=P[1, 1, 1, 1, 0.1, 1].stutter(2), dur=PDur([3, 3, 5, 8], 8) * 4, sample=d3.dur, shape=0, rate=P*[1, 2, -1, 1, 1, 2, 4])
