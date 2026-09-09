# Augmentation 98
# Reisub

Clock.bpm=98
Root.default = -4

g1 >> faim([2,3,[5,7]], dur=([[1,1,1/2],2,1/2,4,1/2]*PRand([2,3,1,4])), slide=var([0,[-4,4]], [7,1]), leg=PWhite(0,4), sus=g1.dur*PWhite(0.2,1.5), oct=(4,5), chop=P*[0,4,16], hpf=var([1000, 0], [PRand(2,11), PRand(12,19)]), fx1=1, fx2=1, fx1hpf=150, amp=0.5, room=1, mix=PWhite(0.2,0.5)).unison(3).sometimes("shuffle") + (0,[2,[4,6]])
b1 >> faim(var([-2,0],8), dur=P[1,1,1,0, 1,0,0,1]*1/2, amp=0.5,hpf=var([0, 1000], [PRand(4,16), PRand(4,9)]), oct=(3,4)).sometimes("stutter") + var([0,PGauss()],[6,2])

h1 >> play("h", dur=PDur(var([7,8,4],[8,2,2]),8)/var([1,[2,0.5]],16), sample=PStep(8,1,3), rate=PWhite(1,4), amp=PWhite(0.0, 0.5), pan=PWhite(-1,1)).degrade(0.2)
d1 >> play("<(x.)(.x).(..x)><(k.)(.M).(..O)>", delay=0, sample=(2, 4), rate=(1, 0.5), hpf=30, dur=var([2,1/4], 8), spf=P*[14000,60,300], spfslide=PSine(64)*0.35, spfend=P*[500,1700,200])
d2 >> play("(.v)(.V|w0|).(.v.)", sample=3, hpf=50, dur=var([4,1],16), crush=1, echo=P*[0.5,0.25], echomix=linvar([0,1],[19,0]), lpf=4800)
p1 >> play("j", amp=var([0,0.5], [3,1]), crush=8, sample=PRand(8), rate=linvar([8,PRand(16)*-1],[8,0]), leg=PRand(25), dur=1/4, echotime=1, echo=1, pan=PWhite(-0.5,0.5))
p2 >> play("p", sample=PRand(8), crush=4, amp=p1.rate>=0, amplify=PWhite(0.1, 1), leg=PWhite(10, 25), room=1, mix=0.3, dur=1/8, echotime=1, echo=1, pan=[-1,1])
h2 >> play("[--]", sample=PRand(8), rate=var([0.7, linvar([1,4],8)]), leg=1, dur=1/4, amp=var([0,0.5], [3,4]), hpf=5600).spread()

p3 >> play("(Xs)", sample=PRand(8), rate=[0.7,1.1], leg=PRand([16,64,32]), dur=1/4, amp=var([0,p2.amp==1],[8,16]), mpf=PRand(6500,14000))
s1 >> play("(yL) ", sample=(PRand(8), PRand(8)), dur=2, rate=(0.4, -2), delay=(0, 1), slide=(4, 1), bpf=(800,4800), bpr=(0.2,0.8))
d3 >> play("K", dur=var([32,1/4], [1,[4,8]]), rate=linvar([2,1], 4), echo=var([0.75,0.5,0.25,0.125], P*[0.25,1,0.5,0.125]), cut=0.9)