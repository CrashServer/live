

rec()


attack("R_Psy")
##### attack@R_Psy.fwk:~$ #####

Clock.bpm=168

c9 >> loop("synth4", dur=(4, 8), amp=PBin(16)*0.5, sample=6, mverb=1, echo=0.5, a=0.2, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, pan=linvar([-1, 1], 8))

sb >> hardstab([([0, 0, 0, 4, 1],4,7)], dur=4, fbdelay=PWhite(0.1, 0.9), fbtime=0.75, fbfeed=0.3, fbcutoff=2000, amp=0.3, gate=0.6)

c9 >> loop("synth4", dur=(4, 8), amp=PBin(16)*0.5, sample=7, mverb=1, echo=0.5, a=0.2, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, pan=linvar([-1, 1], 8))

c9 >> loop("synth4", dur=(4, 8), amp=PBin(16)*0.5, sample=6, mverb=1, echo=0.5, a=0.2, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1, pan=linvar([-1, 1], 8))

y9 >> four(linvar([0,2],64), fx2=0, tremolo=P*[2,4,8], amp=.8, mverb=0.5, oct=5, shape=.3, rgate=0.5, pan=PWhite(-1, 1))

px >> plaitsX(var([P[0,2,4],P[4,5,7],P[7,9,11]],[8,8,8]), dur=0.5, preset=var([9,10,11],[8,8,8]), oct=(4,5), chopmix=linvar([0,0.5],16), chopwave=(2,3), mverb=0.4, amp=0.8)
n7 >> prof(rate=linvar( [.01, .7], 128), oct=3, dur=8, valad=700, valadr=0.3, valadd=5, valadt=0, valadc=0.2, fx2=.4, eb=0.5, ebfeed=0.25, ebmix=0.3, ebmode=2, ebwow=0.1, ebflutter=0.15, ebsat=0.3, fx1=.1).after(16, "stop")
dp >> darkpad([(0,4,7),(0,3,7)], dur=var([8,8],[8,8]), dark=0.6, movement=linvar([0.2,0.6],32), cutoff=linvar([600,1500],16), pumper=0.4, pumprate=1, amp=0.4)
dl >> darklead(P[0,2,4,7,9,7,4,2], dur=0.25, cutoff=linvar([1500,5000],8), detune=0.01, drive=1.5, sub=0.2, fbdelay=0.3, fbtime=0.5, fbfeed=0.35, oct=4, amp=0.125).sometimes("degree.add", 7)
dp.stop()
sb.stop()

hv >> hoover([(0,4,7)], dur=32, porta=1.5, portadur=0.3, tubedrive=0.5, tubewarm=0.4, amp=0.5, sus=6)


# i0 >> loop("psybass32", dur=32,pos=0, amp=1, room=0.0, sample=24, beat_stretch=1, looping=1.0, drcomp=0.1, mverb=0.0)
# gz >> prof([(0,4,7)], dur=8, wave=linvar([0,60],64), cutoff=linvar([500,3000],32), res1=0.4, lfo1=1, rate1=0.25, depth1=2, oct=5, mverb=0.5, amp=0.5)
e9 >> loop("seq16", dur=16, sample=0, comp=0, hpf=1200, mverb=0.0).lclip(var([PRand([1,2,4,8])],32))
c9.lpf=800
y8 >> four(linvar([0,2],64), fx2=0, tremolo=P*[2,4,8], amp=.8, mverb=0.5, oct=5, shape=.3, pan=PWhite(-1, 1))
y9 >> four(linvar([0,2],64), fx2=0, tremolo=P*[2,4,8], amp=.8, mverb=0.5, oct=5, shape=.3, rgate=0.5, pan=PWhite(-1, 1))
z4 >> loop("psych32", dur=32, sample=PRand(111), fx1=0, fx=0, hpf=200, mverb=0.2)

q3 >> compkick(0, punch=0.5, comp=16, release=0.35, click=1.0,drive=0.4, sub=1, tape=1, tapedrive=2, body=0.2, echo=0, tone=0.0, oct=3,)
# q7 >> play("[--]", hpf=6500)

i0 >> loop("psybass32", dur=32,pos=0, amp=1, room=0.1, sample=, beat_stretch=1, looping=1.0, drcomp=0.1, mverb=0.0)

i5 >> loop("psydrum32", dur=32, sample=var(PRand(202),64))

y8.stop()
e7 >> loop("psydrum16", dur=16, sample=PRand(8)[:8])
z4.stop()






attack("Tio 132")
# cr >> creep(var([7,5],[4,4])+P[0,0,12,0], dur=2, rate=linvar([0.5,2],16), hpf=400, mverb=0.6, amp=0.25)
# p1 >> prof([0,2,4,5,7,5,4,2], dur=0.5, cutoff=linvar([2000,6000],16), rq=0.4, rate=0.5, phase=0.5, mverb=0.4, amp=0.33)

b3 >> loop("electrodrum8", dur=8, sbrk=PStep(4,0.25,0), t_reset=0, sbrkdur=0.5, sbrkmix=1.0, sample=2, drcomp=.5)

seq = var([P[0,0,3,0,5,0,0,3], P[0,2,5,2,7,5,2,0], P[-2,0,3,5,7,5,3,0], P[0,0,5,7,10,7,5,0]], [16, 16, 8, 24])
chd = var([(0,4,7), (0,3,7), (-2,2,5), (2,5,9)], [12, 12, 8, 32])
a1 >> acidline([0,0,3,0,5,0,0,3], dur=0.25, cutoff=linvar([400,2000],8), res=linvar([0.5,0.8],4), drive=2.5, accent=P[0,0,1,0]*0.5, tubedrive=0.4, amp=4.0)
a1 >> acidline(var([seq], [16, 8, 8]), dur=var([0.25, 0.125, 0.25], [24, 4, 4]), cutoff=expvar([300, var([2000, 4000], [16, 16])], 8), res=linvar([0.4, 0.9], 16), drive=linvar([1.5, 4], 32), accent=var([P[0,0,1,0]*0.5, P[1,0,0,1]*0.6, P[0,1,0,1]*0.4], [12, 8, 12]), tubedrive=linvar([0.2, 0.7], 48), amp=var([0.6, 0.8, 0.5], [12, 4, 16]))

d2 >> play("-", sample=5, dur=0.25, amp=P[0.4,0.15,0.3,0.15], hpf=4000)
d3 >> play("..C.", sample=2, dur=0.5, amp=0.55)


attack("R_toto")

##### attack@R_toto.off:~$ #####

Clock.bpm=168
f8 >> loop("beats8", dur=8, sample=5)
c1 >> loop("berlin8", dur=8, sample=4)

m0 >> loop("cinambi8", dur=8, sample=var([3,2],[24,8]), hpf=200,)

# v3 >> loop("circlebreak16", dur=16, sample=7, comp=1, sbrk=.5, sbrkdur=.5)
b4 >> loop("nbvarp16", dur=32, sample=6, hpf=120)
x4 >> loop("ragedrum16", dur=32, sample=5, amp=1, comp=1, fx=1)

r9 >> loop("electrodrum16", dur=16, sample=3, comp=1)
p6 >> play("<x.><.><..o.><k.>", sample=1, amp=1, bank=0).sometimes("stutter")
p6.bank=1
~x4 >> play("x ", sample=3, amp=9)

# e9 >> loop("housebass24", dur=32, chop=0, sample=7, amp=0.5, hpf=0, fx1=0, a=0, octer=0, shift=0, octersub=à, octersubsub=1).unison(4).lclip(var([PRand([1,2,4,8])],32))

h2 >> play(".(.U)..", rate=PWhite(-.5,-1), fx2=1)






x8 >> play("<k.><.>", hpf=0, amp=2, drcomp=0.6, sample=0)
