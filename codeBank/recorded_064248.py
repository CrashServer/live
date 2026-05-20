# recorded_064248
# recorded

#@intro(32)
attack("blackorchid 88")

#@build(16)
x2 >> vati([11, 10, 9, 8, 7, 4, 3, 0], dur=0.25, oct=6, cutoff=linvar([800, 4000], 8), amp=var([0, 0.8], [24, 8]), leg=0)

#@peak(16)
p1 >> darkpad([0, 1, 6, 7], dur=var([rest(28), 4], [28, 4]), oct=3, amp=linvar([0.5, 0], 32), dark=0.9)

#@break(8)
attack("R_toto")

#@drop(16)
f8 >> loop("beats8", dur=8, sample=5)

#@outro(8)
attack("for my people 88")

#@part7(16)
p1 >> pianovel([4, 5, _, 7, 5, 4, _, 2], dur=[2, 1, 1, 2, 1, 0.5, 0.5, 2], oct=4, velocity=PRand(55, 80), hard=PWhite(0.5,0.8),velhard=PWhite(0.4, 0.6), lofi=0.7, lofiwow=0.5, lofiamp=0.5, cheapverb=0.2, cvdecay=1)

#@part8(8)
p2 >> pianovel(var([(2,4,7), (2,4,7), (1,3,7), (1,3,6.5), (0,2,5), (0,2,5), (1,3,7), (2,4,7)], [4]), dur=1, amp=0.8, hard=PWhite(0.2, 0.7), velhard=0.6, oct=4, velocity=[PRand(40, 60), PRand(20, 43)], lofi=0.6, lofiwow=0.25, lofiamp=0.5, lpf=sinvar([2000, 5000], 32))

#@part9(4)
p2 >> pianovel(var([(2,4,7),(2,4,7), (1,3,7),(1,3,6.5)], [4]),dur=1, amp=1, hard=PWhite(0.2,0.8), velhard=0.6, oct=4, velocity=[PRand(40, 60), PRand(20,43)], lofi=linvar([0.6, 1, 0.4], 1), lofiwow=0.25, lofiamp=0.2)

#@part10(16)
q9 >> loop("hiphop16", dur=16, room=0.1, sample=0)

#@part11(8)
f8.hpf=2400

#@part12(8)
d3 >> play("v.....(...{v[vv].}).", sample=8, delay=0.5, hpf=400, amp=var([0, 1], [28, 4]))
d4 >> play("(...(.p)).((p.).(p.).)((p.).(p.).)", dur=1/4, sample=4, crush=8,bits=8)

#@part13(8)
q9 >> loop("hiphop16", dur=16, room=0.1, sample=0, tape=0.4, tapedrive=1, tapewarm=0.5)

#@part14(8)
e6 >> play("+", dur=1/8, amp=PWhite(0.02, 0.08), pan=PWhite(-1, 1), sample=PRand(0, 3), hpf=2000)

#@part15(16)
x2.stop()

#@part16(32)
attack("trap")
d0 >> play(".{...u}..u...", sample=5, hpf=var(PRand(4000)+10), rate=(.5,2)).sometimes("stutter")
d1 >> play(".{...c}..c...", sample=5, mverb=0, flanger=0, chorus=var(PWhite(0, 1)), amp=P*[0, 1], rate=(P*[.5,.5,.5,-1],2))
d2 >> play("v.....(...{v.})(...{.v}))", cut=2, sample=8, hpf=50, drive=(0,var(PWhite(0,0.2)))).sometimes("stutter")
d3 >> play("v.....(...{v[vv].}).", sample=8, delay=0.5, hpf=400, amp=var([0, 1], [28, 4]))
d4 >> play("(...(.p)).((p.).(p.).)((p.).(p.).)", dur=1/4, sample=4, crush=8,bits=8)
d5 >> play("-{-[--]}-.-{[---][--]}(-.)(-[----])", sample=2, amp=PCoin(PWhite(0, 1),0,0.5), hpf=6000, pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble").sometimes("stutter", PRand(16), rate=PWhite(-1,5))
d6 >> play("---.-{[---][--]}(-.)(-[----])", hpf=5000, sample=10, amp=PCoin(PWhite(0, 1), 0, 0.5), pan=PWhite(-1,1)).sometimes("amen").sometimes("bubble")
d7 >> play("---.-{[---][--]}(-.)(-[----])", pan=PWhite(-1, 1), hpf=4000, amp=PCoin(PWhite(0, 1), 0, 0.5), sample=8).sometimes("amen").sometimes("bubble").every(4, "shuffle")

#@part17(16)
v5 >> loop("hiphop8", dur=8)

#@part18(8)
attack("spacesounds  120")
attack("spacesounds  120")
attack("spacesounds  120")

#@part19(16)
p1 >> sinepad(dur=PDur(3,8), degree=[0, 2, 4], oct=6, amp=linvar([0.5, 1], 16), sus=var([0.5, 1, 1], 8), atk=0.2, lpf=linvar([800, 3000], 64), mverb=0.2, hpf=1800).unison(3)

#@part20(8)
p2.stop()

#@part21(16)
x3 >> loop("aurora16", dur=16, amp=0.35, cheapverb=0.5).unison(4)

#@part22(16)
attack("noise")
a1 >> play("mow b", dur=P*[1/2, 2, 1/2], rate=(PWhite(-1, 1),PWhite(-1, 1)) * 2, sample=PRand(8)[:4], leg=2, shape=PWhite(0, 1))

#@part23(4)
p1.stop()

#@part24(4)
f8.stop()

#@part25(8)
q9.stop()

#@part26(16)
x3.only()
Clock.clear()
soff()
Server.clearFx()

#@part27(16)
rec_stop()

#@endfade(16)
