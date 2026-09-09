# toHappy 132
# banger, todo

Clock.bpm=132

l1 >> loop("atmo8", dur=8, sample=3, mverb=1)
b3 >> plaitsX((var([0,3,2],[16]),var([3,2,5,2],8)), preset=13 ,dur=1/4, fdecay=[2,PFr(1,2,808)], drive=PFr(0.02,0.4)).gtr((5,6)).human(20,-4) + (0,var([0,P*[-1,5]],[7,1]))
b4 >> lbass(var([3, [0,0,0,[5,8]]], 8), dur=1/2, fmod=0).gtr(1)

d2 >> play("<x.><..o.><---(-:)><..*.><|X1|.>", sample=7, comp=.5)
u7 >> play("X.")