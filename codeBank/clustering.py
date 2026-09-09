# Clustering 96
Clock.bpm = 96
b2 >> donk()
b1 >> cluster(hpf=400, hpr=0.1, dur=2.5, oct=4, mverb=0.5)
b3 >> cluster(dur=4, oct=3)
b4 >> play("xxox", sample=(3, (é4*P[6:12]) + 4))
b1.dur=5
b3 >> dbass()
b2 >> dbass(dur=1/2, rate=P[è8/4, à/10]).unison(4)
b1 >> fbass((1/4, 1/2, 0), sus=(4, 8), dur=[4, 2], hpr=0.1, mverb=0.5, hpf=100, hpr_=0.5)
b2 >> dab((1/4, 1/2, 0), sus=(4, 8), dur=[1/2, 1], hpr=0.1, mverb=0.5, hpf=ù5 * 400, hpr_=0.3, lpf=(é8 + 1) * PWhite(0, 800), chop=4, lpr=(è/4) + 0.2, vol=0.4)
b1 >> ews(dur=4, oct=(3, 4, 5))
b4 >> play("x:k%", sample=var([4, 3, 2]), dur=1/4)
b1.stop()
