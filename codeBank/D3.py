# nucleose
a1 >> play("<X[--]><..O.>", amp=4, room=0.7, mix=PRand([0,.4,0])).sometimes("stutter", PRand(8))
s1 >> saw((0,1), oct=(3,[4,5]), lpf=PRand(8800), lpr=PWhite(0.1,0.9), amp=[0,0.4,0], dur=var([4,1/4,2],16), chop=8, drive=0.2, slide=(PWhite(-2,2),PWhite(-1,1))).unison(16, analog=40)
b1 >> dbass(PArp([0,2,-2], 13), dur=1/4, lpf=8000).unison(3)
