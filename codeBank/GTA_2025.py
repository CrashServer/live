# GTA_2025 164
# Cover

Root.default = "C"
Clock.bpm=164
Scale.default="dorian"

t1 >> mpluck([[0, 1, 2, 1, 0, 1 ,0, -1],-3], mverb=lininf(0,0.8,32), amp=0.70, oct=(PStep(8, 5, 6), 5, 7), pan=PWhite(-1,1), cut=1/2, dur=2, delay=0, hpf=400, fx2=1).unison(4)
t2 >> tb304([[0, 1, 2, 1, 0, 1 ,0, -1],-3], dur=1/2,hpf=503, hpr=0.2, amp=PGauss(0.4, 0.1), oct=PStep(7,6,5), rate=linvar([0.1,1.8],24), sus=PWhite(0.2,0.3), mverb=0.5).unison(3).sometimes("stutter", oct=[6, 8], mverb=0, rq=0.2)

t3 >> tb304(t2.degree + 5, oct=PStep(4, 5, [6, 7]), hpf=1609, delay=var([0,(0.125, 0)], [5, 3]), amp=linvar([0.4, 0.8], [16]), rq=0.6, mverb=0.5).accompany(t2).unison(4).human().slider()

t5 >> ssaw([0,2,P+(3,4),P+(6,7,8,14)], oct=(5.01, 3.99, 7), sawtype=P*[0,1], sawmix=0.5,  lpr=0.5, amp=(0.7, 0.6, 0.4), lpf=7700, dur=8, fx2=1).unison(4)
t6 >> ssaw([0,2,3,(4.5,7)], oct=(4,5), dur=8, lpf=800, slide=0.2, slidedelay=0.8, hpf=90, fx2=1).unison(3)

t7 >> dbass([0,0,-1,7,7,-1], dur=[1/2,1/2,[rest(3)]], amp=1, oct=5, echo=0.25, sus=1.5)
t8 >> jbass(4, dur=1/2, amplify=var([0,1],[3.5,0.5]), amp=1, echo=0.5, oct=4)

t9 >> dbass(P[3, 4, 4.5, [4, 3]].stutter(2), dur=1/4, oct=(5,6), amplify=var([0, 1], [6, 2]))
t0 >> tb304([(0, [7, 3]), (0, [4, -1])], dist2=0.5, oct=P(3, [4, [5, 6]]), dur=[1/2, 1/2, [rest(1)]], sus=1, mverb=0.5).unison(2)

t4 >> superbass([[0, 1, 2, 1, 0, 1 ,0, -1],-3], amp=0.7, hpf=linvar([200, 400]), hpr=0.39, dur=1/2, phase=0, sus=linvar([0.6, 1], 16), fx1=0.5).unison(2)

d0 >> play(".{...u}..u...", sample=5, hpf=var(PRand(4000)+10), rate=(.5,2)).sometimes("stutter")
d1 >> play(".{...c}..c...", sample=5, chorus=var(PWhite(0, 1)), amp=P*[0, 1], rate=(P*[.5,.5,.5,-1],2))
d2 >> play("v.....(...{v.})(...{.v}))", cut=2, sample=8, hpf=50, drive=(0,var(PWhite(0,0.2)))).sometimes("stutter")
d3 >> play("v.....(...{v[vv].}).", sample=8, delay=0.5, hpf=400, amp=var([0, 1], [28, 4]))
d4 >> play("(...(.p)).((p.).(p.).)((p.).(p.).)", dur=1/4, sample=4, crush=8,bits=8)
d5 >> play("-{-[--]}-.-{[---][--]}(-.)(-[----])", sample=2, amp=PCoin(PWhite(0, 1),0,0.5), hpf=6000, pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble").sometimes("stutter", PRand(16), rate=PWhite(-1,5))
d6 >> play("---.-{[---][--]}(-.)(-[----])", hpf=5000, sample=10, amp=PCoin(PWhite(0, 1), 0, 0.5), pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble")
d7 >> play("---.-{[---][--]}(-.)(-[----])", pan=PWhite(-1, 1), hpf=4000, amp=PCoin(PWhite(0, 1), 0, 0.5), sample=8).sometimes("amen").sometimes("bubble").every(4, "shuffle")

b8 >> play("X.", bank=0, lpf=400)

h2 >> loop("junglebouncy16", dur=16)
