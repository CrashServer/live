# scream
s1 >> jbass(1, oct=4, dur=var([1/2,1/4],[6,2]), amp=2, sus=s1.dur*0.7, hpf=40).sometimes("stutter") + var([0,[2,-1,6],[1,2,-1,3]],[6,1,1])
s2 >> play("..I.", drive=(0,0.1), dur=P*[0.5,1,2], sample=1, room2=linvar([0,1],24), mix2=linvar([0,0.9],37), rate=(PWhite(-0.5,1)), amp=1, pan=linvar([-1,1],24))
