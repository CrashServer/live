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
