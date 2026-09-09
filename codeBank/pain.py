# pain 132
# todo
Clock.bpm = 132
e5 >> play("b", sample=var([7, 8, 10], [12, 4, 8]), a=PWhite(0, 0.01), dur=1/4, rate=[2, 1, 1, 2, 1, 2]*4, hpf=100, vakorg=2400, vakorgr=0.1, vakorgd=0.5, vakorgt=3, vakorgc=0.3, slide=0.0, hpr=0.1, chorus=0.0, tanh=0.2, amp=var([1, 0.4, 0.7], [7, 3, 2, 4, 2, 5])).sometimes("stutter", 2, rate=4, echo=0.5, echotime=4, slide=4)
p7 >> bbass(dur=16, oct=6, shape=3, a=0.04, r=0.3, spin=PRand([0, 8]),mverb=0.5).unison(4)
e6 >> play("X", sample=var([6, 5], [12, 4]), a=PWhite(0, 0.01), dur=1/2, autopan=1, rate=[4, 1, 4, 4, 1, 2], hpf=100, vakorg=2400, vakorgr=0.1, vakorgd=0.5, vakorgt=3, vakorgc=0.3, hpr=0.1, chorus=0.1, resonz=0.4).sometimes("stutter", 2)
e8 >> play("b", sample=var([7, 8], [12, 4]), a=PWhite(0, 0.01), dur=1/4, rate=[7, 7, 7, 6, 6, 6,7, 8,8, 6], hpf=100, vakorg=11120, mverb=0, vakorgr=0.1, vakorgd=0.5, vakorgt=3, vakorgc=0.3, hpr=0.1, chorus=0.0, lpf=linvar([2000, 12000], 128), lpr=0.1, leg=2).unison(2)
y8 >> four(linvar([0,2],64), a=0.36, fx2=0, tremolo=P*[2,4,8], amp=0.8, mverb=0.5, oct=6, shape=.3, pan=PWhite(-1, 1))
e5.lpf=400
e7 >> play("-", sample=var([7, 8], [12, 4]), a=PWhite(0, 0.01), dur=1/2, rate=[4, 3, 3, 3, 3, 2], hpf=100, vakorg=2400, vakorgr=0.1, vakorgd=0.5, vakorgt=3, vakorgc=1.0, slide=0.0, hpr=0.1, chorus=0.0, tanh=0.2, amp=var([1, 0.4, 0.7], [7, 3, 2, 4, 2, 5]))
p7.shape=0
e5.dur=PDur(5, 8)
e6.dur=PDur(3, 8)
y8 >> four(linvar([0, var([2, 3, 1], 32)], 64), fx2=linvar([0, 0.3], 48), tremolo=var([P*[2,4,8], P*[4,8,16], P*[2,8,4], P*[8,4,2]], [16, 8, 4, 4]), amp=linvar([1.5, 2.2], 32), mverb=linvar([0.4, 0.7], 48), oct=var([6, 5, 7], [24, 4, 4]), shape=linvar([0.2, 0.5], 32), pan=PWhite(-1, 1), lpf=var([1200, 2400, 800, 1600], [16, 8, 4, 4]), a=linvar([2, 5], 64))
e8.rate=1

e7.leg=0
e5.leg=4
e5 >> play("b", sample=var([7, 8], [12, 4]), a=PWhite(0, 0.01), dur=1/4, rate=[2, 1, 1, 2, 1, 2], hpf=100, vakorg=2400, vakorgr=0.1, vakorgd=0.5, vakorgt=3, vakorgc=0.3, hpr=0.1, chorus=0.0).sometimes("stutter", 2)
e4 >> play("h", sample=var([7, 8], [12, 4]), a=PWhite(0, 0.01), dur=1/4, rate=[7, 7, 7, 6, 6, 6,7, 8,8, 6], hpf=100, vakorg=11200, vakorgr=0.1, vakorgd=0.5, vakorgt=3, amp=0.3, vakorgc=0.3, hpr=0.1, chorus=0.0, lpf=linvar([2000, 12000], 128), lpr=0.1, leg=4).unison(2)
p7.stop()
y8.stop()
j3 >> play("T..h hh4. Tbbb mbbb", sample=4, cut=1/4)

y8.a=4
s1 >> bbass(var([0, 0, -2, 0, 3], [4, 4, 4, 2, 2]), dur=var([4, 2, 8], [16, 8, 8]), oct=7, shape=linvar([2, 6], 48), a=0.01, r=linvar([0.2, 0.4], 32), lpf=linvar([200, 500], 64), amp=linvar([1.5, 2.2], 32))
n1 >> play(var(["s", "ss", "s.", ".s"], [16, 8, 4, 4]), sample=PRand([0,2,4,6,8]), dur=var([1/4, 1/8, 1/2], [16, 8, 8]), hpf=linvar([4000, 8000], 32), lpf=linvar([10000, 16000], 48), amp=var([0.4, 0.6, 0.3], [12, 4, 16]), pan=PWhite(-0.8, 0.8), room=linvar([0.1, 0.4], 64))
e8 >> play("b", sample=var([7, 8], [12, 4]), a=PWhite(0, 0.01), dur=1/4, rate=[7, 7, 7, 6, 6, 6,7, 8,8, 6]*1, hpf=100, vakorg=11200, vakorgr=0.1, vakorgd=0.5, vakorgt=3, vakorgc=0.3, hpr=0.3, gate=0.4, chorus=linvar([0, 0.5],32), lpf=linvar([2000, 12000], 128), amp=0.1, lpr=0.2, leg=0).unison(2)
p7 >> bbass(var([0, -2, 3, 0, 5], [16, 8, 8, 16, 16]), dur=var([16, 8, 32], [32, 16, 16]), oct=var([5, 4, 6], [32, 16, 16]), shape=linvar([4, 8], 64), a=linvar([0.15, 0.35], 48), r=linvar([0.25, 0.5], 32), spin=var([PRand([0,8]), PRand([4,12]), PRand([0,4,8])], [16, 8, 8]), mverb=linvar([0.4, 0.7], 48), lpf=expvar([1500, 4000], 64), lpr=linvar([0.2, 0.4], 32)).unison(var([4, 6, 2], [24, 4, 4]))
p7.amp=2
o5 >> play("X ", amp=2)
e9 >> play("..O.", fbdelay=0.3)
e6 >> play("X", sample=7, a=PWhite(0,0.005), dur=var([1,2,4],[16,16,32]), autopan=0.3, rate=[2,1,2,1], hpf=linvar([100,250],48), vakorg=linvar([2000,1000],64), vakorgd=0.7, vakorgt=2, hpr=0.05, resonz=linvar([0.3,0.15],48), amp=linvar([0.6,0.2],64), mverb=linvar([0.4,0.9],48))
e8 >> play("b", sample=7, a=PWhite(0,0.005), dur=var([1/2,1,2],[24,16,24]), rate=var([[6,6,7,7],[7,6,7,6]],[24,24]), hpf=linvar([100,300],48), vakorg=linvar([8000,4000],64), vakorgd=0.6, vakorgt=2, hpr=0.15, chorus=linvar([0.2,0.6],48), lpf=linvar([8000,2000],64), lpr=0.08, leg=linvar([2,8],64), amp=linvar([0.6,0.15],64), mverb=linvar([0.3,0.8],48)).unison(2)
y8 >> four(linvar([2,0],64), fx2=linvar([0.2,0],48), tremolo=P*[4,8,16], amp=linvar([1.5,0.4],64), mverb=linvar([0.6,0.95],48), oct=var([6,7],[32,32]), shape=linvar([0.4,0.1],48), pan=PWhite(-0.5,0.5), lpf=linvar([1800,600],64), a=linvar([4,8],64))
p7 >> bbass(var([0,0,3],[32,16,16]), dur=var([32,64],[32,32]), oct=5, shape=linvar([6,2],64), a=linvar([0.3,0.6],48), r=linvar([0.4,0.9],48), spin=0, mverb=linvar([0.5,0.95],48), lpf=linvar([2500,800],64), lpr=0.2, amp=linvar([1.6,0.3],64)).unison(2)

n1 >> play("s", sample=PRand([0,2,4]), dur=var([1,2,4],[24,24,16]), hpf=linvar([5000,8000],48), lpf=linvar([14000,8000],64), amp=linvar([0.4,0.1],64), pan=PWhite(-0.4,0.4), room=linvar([0.3,0.8],64), mverb=linvar([0.2,0.7],48))

o5 >> play("X", dur=var([4,8,16],[24,24,16]), amp=linvar([1.5,0.3],64), hpf=linvar([60,200],48), room=linvar([0.2,0.7],64), mverb=linvar([0.1,0.6],48))

e9 >> play("..O.", dur=var([2,4,8],[24,24,16]), fbdelay=linvar([0.3,0.6],48), fbtime=linvar([0.5,0.9],48), fbfeed=linvar([0.3,0.6],48), amp=linvar([0.7,0.2],64), mverb=linvar([0.3,0.8],48))

j3.stop()
e10.stop()
m1.stop()
