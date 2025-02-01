# for my people
Clock.bpm = 88
Scale.default="minor"
Root.default="E"

# [2,4,7,] [1,3,7,] [1,3,6.5,] [0.5, 3, 6.5,] [0.5,3,6]

# p2 >> pianovel(var([(2,4,7),(2,4,7), (1,3,7),(1,3,6.5), (0.5,3,6.5),(0.5,3,6),(0.5,2.5,6)], [4,4, 4,4, 4,2,2 , 4,2,2]),dur=1,amp=1, oct=4, velocity=PRand(40,60))

p2 >> pianovel(var([(2,4,7),(2,4,7), (1,3,7),(1,3,6.5)], [4]),dur=1, amp=1, hard=PWhite(0.6,0.8), velhard=0.6, oct=4, velocity=[60 | PRand(40,53)[:7]], lofi=0.6, lofiwow=0.25, lofiamp=0.5)
p1 >> pianovel([4,5], dur=P[6,2], oct=5, velocity=PRand(60,80), hard=PWhite(0.6,0.8), velhard=PWhite(0.4, 0.6), lofi=0.7, lofiwow=0.5, lofiamp=0.5)

q9 >> loop("hiphop16", dur=16, room=0.1, sample=0)

e4 >> play("-")

d4 >> play("<[vv]...|U1|...>")
e4 >> play("...(...z)", sample=2)