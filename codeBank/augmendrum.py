# augmendrum
h1 >> play("h", dur=PDur(var([7,8,4],[8,2,2]),8)/var([1,[2,4]],16), sample=PStep(8,1,3), rate=PWhite(1,4), amp=PWhite(0.0, 0.5), pan=PWhite(-1,1)).degrade(0.2)

d1 >> play("(x.)(.x).(..x)", sample=(4,2), hpf=30, dur=var([2,1/4], 8), spf=[14000,60,300], spfslide=PSine(64)*0.35, spfend=P*[500,1700,200])
d2 >> play("(.v)(.V|w0|).(.v.)", sample=3, hpf=50, dur=var([4,1],16), crush=1, echo=P*[0.5,0.25], echomix=linvar([0,1],[19,0]), lpf=4800)
p1 >> play("j", amp=var([0,0.5], [3,1]), crush=8, sample=PRand(8), rate=linvar([8,PRand(16)*-1],[8,0]), leg=25, dur=1/4, echotime=1, echo=1)
p2 >> play("p", sample=PRand(8), crush=4, amp=p1.rate>=0, amplify=PWhite(0.1, 1), leg=PWhite(10, 25), room=1, mix=0.3, dur=1/8, echotime=1, echo=1, pan=[-1,1])
h2 >> play("[--]", sample=PRand(8), rate=var([0.7, linvar([1,4],8)]), leg=1, dur=1/4, amp=var([0,0.5], [3,4]), hpf=5600).spread()

p3 >> play("(XP)", sample=PRand(8), rate=[0.7,1.1], leg=PRand([16,64,32]), dur=1/4, amp=var([0,p2.amp==1],[8,16]), mpf=6500)
s1 >> play("(yL) ", sample=(PRand(8), PRand(8)), dur=2, rate=(0.4, -2), delay=(0, 1), slide=(4, 1), bpf=(800,4800), bpr=(0.2,0.8))
d3 >> play("K", dur=var([32,1/4], [1,[4,8]]), rate=linvar([2,1], 4), echo=var([0.75,0.5,0.25,0.125], P*[0.25,1,0.5,0.125]), cut=0.9)

a1 >> play("I ",rate=(0.25,PWhite(0.15,0.3)), triode=PRand(9), dur=4, spin=0.25, amp=0.5, room=1, mix=(0,0.6), hpf=350).after(4, "stop")

a2 >> play("(kc){.@}(..)P", amp=1, rate=4).sometimes("trim",3).every(13, "stutter", Cycle([4,13,2]), hpf=4000, pan=[-1,1])
a3 >> play("(+.)(.+)", room=0.5, mix=0.2, sample=5, amplify=P*[0,1], rate=[-0.5,1], delay=[PWhite(0,0.12),0])