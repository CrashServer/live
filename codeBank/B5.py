# B5
Clock.bpm = 120;
h1 >> play("h", dur=PDur(var([7,8,4],[8,2,2]),8)/var([1,[2,0.5]],16), sample=PStep(8,1,3), rate=PWhite(1,4), amp=PWhite(0.0, 0.5), pan=PWhite(-1,1)).degrade(0.2)
h2 >> play("<(x.)(.x).(..x)><(k.)(.M).(..O)>", delay=0, sample=(2, 4), rate=(1, 0.5), hpf=30, dur=var([2,1/4], 8), spf=P*[14000,60,300], spfslide=PSine(64)*0.35, spfend=P*[500,1700,200])
h3 >> play("(.v)(.V|w0|).(.v.)", sample=3, hpf=50, dur=var([4,1],16), crush=1, echo=P*[0.5,0.25], echomix=linvar([0,1],[19,0]), lpf=4800)
h4 >> play("e", amp=var([0,0.5], [3,1]), crush=8, sample=PRand(8), rate=linvar([8,PRand(16)*-1],[8,0]), leg=PRand(25), dur=1/4, echotime=1, echo=1, pan=PWhite(-0.5,0.5))
h5 >> play("p[PP]", sample=PRand(8), crush=4, amp=h1.rate>=0, amplify=PWhite(0.1, 1), leg=PWhite(10, 25), room=1, mix=0.3, dur=1/8, echotime=1, echo=1, pan=[-1,1])
