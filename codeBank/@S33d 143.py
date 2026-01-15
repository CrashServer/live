# @S33d 143
# banger
Clock.bpm=143
Root.default="C#"
Scale.default="zhi"

l1 >> loop("wardrum16", dur=16, amp=1, sample=var(PRand(99), [32, 32]), drcomp=0, hpf=120)

s1 >> tb305(PTime(), oct=6, eb=0.5, ebfeed=0.5, ebmix=0.3, ebmode=1, ebwow=0.1, ebflutter=0.15, ebsat=0.3, dur=1/2, cutoff=linvar([200,900],[33,44]), rq=0.9, wave=linvar([-1.4, 1.4], [55, 55]), beef=2, envmod=90, glide=0, bits=8, crush=0)#.solo(-32)

b1 >> swiss(var([0,-2, 2, 5], [16]), dur=1/2, oct=3, rate=1.4, rq=0.1, cutoff=3000, saw=2, pulse=1, sin=2, pw=0.52, hpf=[120, 0]) + var([0, PGauss()], [7, 1])

b2 >>  lbass(PStep(8,P[1:16],var([0,-2, 2, 5], [16])), glide=0.3, eb=0.5, ebfeed=0.5, ebmix=0.3, ebmode=2, ebwow=0.1, ebflutter=0.15, ebsat=0.3, dur=1/2,cutoff=2610, tone=0.7, rq=0.9, detune=0.3, amp=0.8, hpf=120).unison(3)

s2 >> soprano(PTime(), dur=PRy(), rate=1, eb=0.5, ebfeed=0.5, ebmix=0.3, ebmode=0, ebwow=0.1, ebflutter=0.15, ebsat=0.3)

d1 >> play("<x..><..o.>", sample=9, drcomp=.5, high=2)
l2 >> loop("drumglitch32", dur=32, hpf=400, chop=4, chopi=.5, sample=PRand(808))
d2 >> play("X.", amp=2).sometimes("stutter")