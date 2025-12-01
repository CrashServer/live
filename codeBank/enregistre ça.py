# enregistre ça
k4 >> play("x ", feed=1.3, dur=0.5, dubd=0.1, rate=1, dudlen=0.6, echo=P*[0, 0.5, 1, 2], feedfreq=10, feedlfo=P*[1600, 122, 112, 400, 1200, 1600, 2400, 4000], feedlfomul=8, hpf=101, feedlfoadd=0.9)
k5 >> play("b..", feed=0.1, feed_=PRand(14), feedfreq=PRand(22,5000), rate=[-1,1], feedlfo=PRand(8000), wshape=7, feedlfomul=4, mverb=0.8, feedlfoadd=0.9, pan=PWhite(-1,1), valad=PFr(20, 2500), valadr=PFr(.1, 0.9), valadd=5, valadt=0, valadc=0.06, vol=0.4).unison(3)
