# R_Jazz
# R_

Clock.bpm=128
u7 >> loop("electrodrum32", dur=32, sample=2, mverb=0)
u4 >> loop("industia16", dur=16, sample=2)
c5 >> loop("jazzc8", dur=8, sample=7, comp=1)
j8 >> loop("jazzguitar8", dur=8, sample=4)
g0 >> noloop("fx4", dur=8, sample=1, rate=.1)
g8 >> play("<k(...[--])><-:><..*.>", sample=1, amp=1, bank=1, dur=1/2, rate=1, cut=1.2).sometimes("stutter")

w2 >> loop("mulholland8", dur=8, sample=1, fx2=0, fx1=0).lclip(8)
s5 >> plaitsX(preset=14, harm=PWhite(-1,1), morph=PWhite(-1,1), pan=PWhite(-1,1))
