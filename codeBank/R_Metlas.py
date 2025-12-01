# R_Metlas
n3 >> loop("metalgtr8", dur=8)
p7 >> loop("metalgtr16", dur=16, sample=13, sbrk=0, mverb=0, room=0.2).lclip(4)
j5 >> loop("metaldrum16", dur=16, sample=8, drcomp=0.5, shape=0.2).lclip(2)
j8 >> loop("metalsynth16", dur=16, sample=1, fx1=1, fx2=0).lclip(4)
f8 >> play("<k.><~.><..|u4|.>", sample=0, amp=3, rate=linvar([1, 1, PRand(2)], [24,8,0]), dur=var([1/2,1/4,1/8], [24,4,4])).sometimes("stutter")
