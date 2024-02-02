# power
b8 >> blip(PArp([0,2,[4,[5,6]]],4), dur=1/2, mverb=0.8, pan=[-1,1], echo=0.25, rate=var([0,4],[16]), echotime=0.01, shape=(0,linvar([0,0.8],[32,0]))).unison(3)
b9 >> faim(var(P[-4:1:1],8), dur=ù, beef=(0,2), oct=5, dist2=0, vol=1)
