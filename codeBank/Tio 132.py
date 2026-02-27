# Tio 132
# chaosbits

q3 >> compkick(0, punch=0.5, comp=16, release=0.35, click=1.0,drive=0.4, sub=1, tape=1, tapedrive=2, body=0.2, echo=0, tone=0.0, oct=3,)

n7 >> prof(rate=linvar( [.01, .7], 128), oct=3, dur=8, valad=700, valadr=0.3, valadd=5, valadt=0, valadc=0.2, fx2=.4, eb=0.5, ebfeed=0.25, ebmix=0.3, ebmode=2, ebwow=0.1, ebflutter=0.15, ebsat=0.3, fx1=.1)

cr >> creep(var([7,5],[4,4])+P[0,0,12,0], dur=2, rate=linvar([0.5,2],16), hpf=400, mverb=0.6, amp=0.25)

p1 >> prof([0,2,4,5,7,5,4,2], dur=0.5, cutoff=linvar([2000,6000],16), rq=0.4, rate=0.5, phase=0.5, mverb=0.4, amp=0.33)

gz >> prof([(0,4,7)], dur=8, wave=linvar([0,60],64), cutoff=linvar([500,3000],32), res1=0.4, lfo1=1, rate1=0.25, depth1=2, oct=5, mverb=0.5, amp=0.5)

dl >> darklead(P[0,2,4,7,9,7,4,2], dur=0.25, cutoff=linvar([1500,5000],8), detune=0.01, drive=1.5, sub=0.2, fbdelay=0.3, fbtime=0.5, fbfeed=0.35, oct=4, amp=0.125).sometimes("degree.add", 7)

sb >> hardstab([([0, 0, 0, 4, 1],4,7)], dur=4, fbdelay=PWhite(0.1, 0.9), fbtime=0.75, fbfeed=0.3, fbcutoff=2000, amp=0.3, gate=0.6)

hv >> hoover([(0,4,7)], dur=32, porta=1.5, portadur=0.3, tubedrive=0.5, tubewarm=0.4, amp=0.4, sus=6)

b3 >> loop("electrodrum8", dur=8, sbrk=PStep(4,0.25,0), t_reset=0, sbrkdur=0.5, sbrkmix=1.0, sample=2, drcomp=.5)

seq = var([P[0,0,3,0,5,0,0,3], P[0,2,5,2,7,5,2,0], P[-2,0,3,5,7,5,3,0], P[0,0,5,7,10,7,5,0]], [16, 16, 8, 24])
chd = var([(0,4,7), (0,3,7), (-2,2,5), (2,5,9)], [12, 12, 8, 32])
a1 >> acidline([0,0,3,0,5,0,0,3], dur=0.25, cutoff=linvar([400,2000],8), res=linvar([0.5,0.8],4), drive=2.5, accent=P[0,0,1,0]*0.5, tubedrive=0.4, amp=4.0)
a1 >> acidline(var([seq], [16, 8, 8]), dur=var([0.25, 0.125, 0.25], [24, 4, 4]), cutoff=expvar([300, var([2000, 4000], [16, 16])], 8), res=linvar([0.4, 0.9], 16), drive=linvar([1.5, 4], 32), accent=var([P[0,0,1,0]*0.5, P[1,0,0,1]*0.6, P[0,1,0,1]*0.4], [12, 8, 12]), tubedrive=linvar([0.2, 0.7], 48), amp=var([0.6, 0.8, 0.5], [12, 4, 16]))

d2 >> play("-", sample=5, dur=0.25, amp=P[0.4,0.15,0.3,0.15], hpf=4000)
d3 >> play("..C.", sample=2, dur=0.5, amp=0.55)

dp >> darkpad([(0,4,7),(0,3,7)], dur=var([8,8],[8,8]), dark=0.6, movement=linvar([0.2,0.6],32), cutoff=linvar([600,1500],16), pumper=0.4, pumprate=1, amp=0.4)
px >> plaitsX(var([P[0,2,4],P[4,5,7],P[7,9,11]],[8,8,8]), dur=0.5, preset=var([9,10,11],[8,8,8]), oct=(4,5), chopmix=linvar([0,0.5],16), chopwave=(2,3), mverb=0.4, amp=0.55)
