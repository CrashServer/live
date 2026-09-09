# power
# banger

p0 >> blip(PArp([0,2,[4,[5,6]]],4), dur=1/2, mverb=(0.8, 0, 0.8), echo=0.25, rate=linvar([0,4],[55,0]), echotime=0.01, shape=(0,linvar([0,0.8],[32,0]))).unison(3)
p1 >> lbass(var(P[-4:1:1],8), dur=PDur([3,5],8), beef=(0,2), oct=5, cutoff=PFr(3400, 6000), tone=linvar([0.16,0.7],[64,0]),vol=1)
