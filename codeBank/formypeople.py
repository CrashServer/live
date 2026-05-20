# for my people 88
# Cover

Clock.bpm = 88
Scale.default="minor"
Root.default="E"

p2 >> pianovel(var([(2,4,7),(2,4,7), (1,3,7),(1,3,6.5)], [4]),dur=1, amp=1, hard=PWhite(0.2,0.8), velhard=0.6, oct=4, velocity=[PRand(40, 60), PRand(20,43)], lofi=0.6, lofiwow=0.25, lofiamp=0.5)
p1 >> pianovel([4,5], dur=P[6,2], oct=5, velocity=PRand(60,80), hard=PWhite(0.6,0.8), velhard=PWhite(0.4, 0.6), lofi=0.7, lofiwow=0.5, lofiamp=0.5)

q9 >> loop("hiphop16", dur=16, room=0.1, sample=0)

e4 >> play("-", dur=1/2, amp=PBin(1664), sample=2, pan=PWhite(-1,1)).sometimes("stutter", PRand(2, 16)).human(40, 10)
d4 >> play("<([vv].)...>")
e4 >> play("...(...z)", sample=2)


#@intro(32)
Clock.bpm = 88
Scale.default="minor"
Root.default="E"
p2 >> pianovel(var([(2,4,7),(2,4,7), (1,3,7),(1,3,6.5)], [4]),dur=1, amp=1, hard=PWhite(0.2,0.8), velhard=0.6, oct=4, velocity=[PRand(40, 60), PRand(20,43)], lofi=linvar([0.6, 1, 0.4], 1), lofiwow=0.25, lofiamp=0.2)

#@build(16)
p1 >> pianovel([4,5], dur=P[6,2], oct=5, velocity=PRand(60,80), hard=PWhite(0.6,0.8), velhard=PWhite(0.4, 0.6), lofi=0.7, lofiwow=0.5, lofiamp=0.5, mverb=0.5)

#@peak(16)
p2 >> pianovel(var([(2,4,7), (2,4,7), (1,3,7), (1,3,6.5), (0,2,5), (0,2,5), (1,3,7), (2,4,7)], [4]), dur=1, amp=0.8, hard=PWhite(0.2, 0.7), velhard=0.6, oct=4, velocity=[PRand(40, 60), PRand(20, 43)], lofi=0.6, lofiwow=0.25, lofiamp=0.5, lpf=sinvar([2000, 5000], 32))

#@break(16)
p1 >> pianovel([4, 5, _, 7, 5, 4, _, 2], dur=[2, 1, 1, 2, 1, 0.5, 0.5, 2], oct=4, velocity=PRand(55, 80), hard=PWhite(0.5,0.8),velhard=PWhite(0.4, 0.6), lofi=0.7, lofiwow=0.5, lofiamp=0.5, cheapverb=0.2, cvdecay=1)

#@drop(16)
p2 >> pianovel(var([(2,4,7), (2,4,7), (1,3,7), (1,3,6.5), (0,2,5), (0,2,5), (1,3,7), (2,4,7)], [4]), dur=(1, 0.5), amp=0.8, hard=PWhite(0.2, 0.7), velhard=0.8, oct=(4, 5), velocity=[PRand(40, 60), PRand(20, 43)], lofi=0.2, lofiwow=0.25, lofiamp=0.5, lpf=sinvar([2000, 5000], 32))

#@outro(16)
b1 >> dbass(var([2, 2, 1, 1, 0, 0, 1, 2], [4]), dur=4, oct=4, sus=3.5, amp=0.6, lpf=300, subenh=0.5, subhfreq=80)

#@part7(8)
b1 >> dbass(var([2, 2, 1, 1, 0, 0, 1, 2], [4]), dur=4, oct=4, sus=3.5, amp=0.6, lpf=300, subenh=0.5, subhfreq=80).unison(3)

#@part8(8)
d2 >> play("v.....(...{v.})(...{.v}))", cut=2, sample=8, hpf=50, drive=(0,var(PWhite(0,0.2)))).sometimes("stutter")

#@part9(4)
d3 >> play("v.....(...{v[vv].}).", sample=8, delay=0.5, hpf=400, amp=var([0, 1], [28, 4]))
d4 >> play("(...(.p)).((p.).(p.).)((p.).(p.).)", dur=1/4, sample=4, crush=8,bits=8)

#@part10(16)
m1 >> soft(melody(), dur=PDur(3,8), oct=6, sus=var([1,2,0.5], [4,4,8]), amp=sinvar([0.15, 0.35], 24), lpf=linvar([1200, 3500], 48),lofi=0.5, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, lofiwow=0.8, lofiamp=1.0, tape=0.2)

#@part11(16)
p1.lpf=1200
q9 >> loop("hiphop16", dur=16, room=0.1, sample=0, tape=0.4, tapedrive=1, tapewarm=0.5)

#@part12(16)
d4 >> play("(vV)..v...v...(vV)..", dur=0.5, amp=[0.9, 0.5, 0.7], sample=0)

#@part13(16)
e4 >> play("-", dur=1/2, amp=PBin(1664), sample=2, pan=PWhite(-0.5, 0.5)).sometimes("stutter", PRand(2, 8)).human(30, 8) 
e5 >> play("s", dur=1/4, amp=PWhite(0.05, 0.2), pan=PWhite(-1, 1), sample=1).human(40, 15)                                              
p2 >> dbass(dur=PDur(3, 8), resonbank=0.2, rbfreq=70, rbdecay=0.5, vocod=0.5, voccarr=0.5, vocbw=0.3, rbspread=1.0, tape=0.5, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1).unison(3)

#@part14(8)
e6 >> play("+", dur=1/8, amp=PWhite(0.02, 0.08), pan=PWhite(-1, 1), sample=PRand(0, 3), hpf=2000)

#@part15(16)
p1 >> dbass()
p2 >> dbass(dynfuzz=0.3,dfgain=1, dfatk=0.015, dfdec=0.2, dftone=1.3, tanh=0.8).unison(3)

#@part16(16)
p3 >> a_stress(var([(2,4,7), (2,4,7), (1,3,7), (1,3,6.5), (0,2,5), (0,2,5), (1,3,7), (2,4,7)], [4]), follow=2, dur=1/4, amp=0.8, hard=PWhite(0.2,  0.7), velhard=var([0.4, 0.6, 0.5, 0.7], 8), oct=8, velocity=[PRand(35, 65), PRand(15, 40)], lofi=0.6, lofiwow=fs(16, 0.15, 0.4),lofiamp=0.5, lpf=sinvar([1800, 6000], 32), tape=0.25, tapewarm=0.4, shape=0.1, vowel=0.2, vowelf=0, vowelq=1).unison(3)

#@part17(16)
p2 >> dbass(p1.degree, dur=1/4)
q9 >> loop("hiphop16", dur=16, room=0.1, sample=0)
p3 >> play(":.o.",sample=8)

#@part18(16)
e4 >> play("-", dur=1/2, amp=PBin(1664), sample=2, pan=PWhite(-1,1)).sometimes("stutter", PRand(2, 16)).human(40, 10)
d4 >> play("<([vv].)...>")
e4 >> play("...(...z)", sample=2)

#@part19(4)
~p2 >> saw(var([(2,4,7),(2,4,7), (1,3,7),(1,3,6.5)], [4]),dur=1, amp=1, hard=PWhite(0.2,0.8), velhard=0.6, oct=4, velocity=[PRand(40, 60), PRand(20,43)], lofi=0.6, lofiwow=0.25, lofiamp=0.2, csweep=0.1, cswfreq=200, cswdepth=0.3, cswrate=0.5, cswdecay=0.5)

#@part20(16)
p2 >> dbass(var([(2,4,7), (2,4,7), (1,3,7), (1,3,6.5)], [4]), dur=1, amp=1, hard=PWhite(0.2,0.8), velhard=0.6, oct=4,         
velocity=[PRand(40,60), PRand(20,43)], lofi=0.6, lofiwow=0.25, lofiamp=0.5)

#@part21(8)
p1 >> pianovel([4,5], dur=P[6,2], oct=5, velocity=PRand(60,80), hard=PWhite(0.6,0.8), velhard=PWhite(0.4,0.6), lofi=0.7,lofiwow=0.5, lofiamp=0.5)

#@part22(8)
b1 >> subbass(p2.degree, dur=4, sus=3.5, amp=0.4, oct=3, lpf=200)

#@part23(8)
a1 >> ethpad(var([(0,2,4), (0,2,4), (0,1,4), (0,1,3)], [8]), dur=4, sus=linvar([3,5],32), amp=sinvar([0.15, 0.3], 16), oct=4,lpf=linvar([600, 2200], 64), tape=0.3, tapedrive=0.4)
a1 >> ethpad(var([(0,2,4), (0,2,4), (0,1,4), (0,1,3)], [8]), dur=4, sus=linvar([3,5],32), amp=sinvar([0.15, 0.3], 16), oct=4,lpf=linvar([600, 2200], 64), tape=0.3, tapedrive=0.4)

#@part24(16)
b5 >> loop("hiphop16", dur=16)

#@part25(16)
rec_stop()

#@endfade(16)

Clock.bpm = 88
Scale.default = "minor"
Root.default = "E"
p1 >> pianovel([4, 5, 7, 5, 4, 2, 0, -3], dur=[2, 1, 1, 2, 1, 0.5, 0.5, 2], oct=4, velocity=PRand(45, 65), hard=PWhite(0.4, 0.7), velhard=PWhite(0.3, 0.5), lofi=0.7, lofiwow=0.5, lofiamp=0.5, cheapverb=0.4, cvdecay=2.5, hpf=200, amp=linvar([0, 0.5], 16))
a1 >> a_stress(var([(2, 4, 7), (-3, 0, 4), (-2, 1, 4), (0, 2, 4)], 4), follow=2, dur=1/4, oct=8, velhard=var([0.4, 0.6, 0.5, 0.7], 8), lofiwow=fs(16, 0.15, 0.4), tape=0.3, tapewarm=0.4, shape=0.1, vowel=0.2, vowelf=0, vowelq=1, hpf=240, amp=linvar([0, 0.4], 16)).unison(3)
p1 >> pianovel([4, 5, 7, 5, 4, 2, 0, -3, 7, 5, 4, 2], dur=[2, 1, 1, 2, 1, 0.5, 0.5, 2, 1, 1, 2, 2], oct=4, velocity=PRand(50, 70), hard=PWhite(0.4, 0.7), velhard=PWhite(0.3, 0.5), lofi=0.7, lofiwow=0.5, lofiamp=0.5, cheapverb=0.4, cvdecay=2.5, hpf=200, amp=0.5)
b1 >> dbass(var([2, 2, 1, 1, 0, 0, 1, 2], 4), dur=4, oct=4, sus=3.5, lpf=300, subenh=0.5, subhfreq=80, subhgain=1.2, tape=0.4, tapedrive=1.2, hpf=35, amp=linvar([0, 0.7], 16)).unison(3)
m1 >> soft(melody(), dur=PDur(3, 8), oct=6, sus=var([1, 2, 0.5], [4, 4, 8]), lpf=linvar([1200, 3500], 48), lofi=0.5, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, lofiwow=0.8, tape=0.2, hpf=400, amp=linvar([0, 0.35], 24))
