# multiCore 172
# mud

Clock.bpm=172

d6 >> play("<x.><..o.><->", sample=9, hpf=(50,0, PRand(400, 9500)), hpr=(0.4,0.5,0.5), amp=1).often("stutter", PRand(6), hpf=400)

y7 >> loop("breakcore160_16", dur=16,sample=var(PRand(9009), [64, 64]), sbrk=0.5, sbrkdur=PWhite(-4, 30), sbrkmix=1.0,t_reset=PRand(9), decimate=0, decbits=PRand(0,6), decrate=4000, decsmooth=0, octclean=P*[0,PWhite()], ocsub=0.5, ocup=PWhite(0, 2))
y5 >> loop("breakcore155_16", dur=16,sample=var(PRand(9009), [64, 64]), sbrk=0.5, sbrkdur=PWhite(-4, 30), sbrkmix=1.0,t_reset=PRand(9), decimate=0, octclean=P*[0,PWhite()], ocsub=0.5, ocup=PWhite(0, 2))

h5 >> svdk(expvar([0, P[7,14]], [4,0]), dur=PDur([4,5],8), oct=PStep(8,4,3), sus=expvar([1/8, 1/4], [32,0]),track=4,  noise=expvar([0.3, 10], [64,0]), harm=.9, hpf=PFr(210,500), hpr=.2, amp=0.7)

s4 >> pbass(dur=var([1/2,P[1, 1/3,1/3,1/3]],[32,0]),  oct=4, valad=linvar([1500, 2500], [64,0]), hpf=75, hpr=.2, echo=0)

o5 >> space(PTime(-7,7), dur=P[P*[3,7,15],1], rate=1, rq=0.5, mverb=.3, hpf=400, amp=1, rgate=.8, rgaterate=2, rgatewave=3, beat_dur=1).unison(3, .5) + [0, PGauss()]

k3 >> pianovel(P[var([0, -2, -4, P+(-3,[6,7])], 8) ,0, 2, 3, 5, 3], dur=P[1, 1, 1/2, 1/2, 1/2 ,1/2],velocity=PTime(50, 70),  oct=4, dafilter=200, dastart=120, darel=0.2, darq=0.5, datype=0, vol=0.8)
