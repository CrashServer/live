# war 114
k4 >> cbass(dur=4, lofi=0.1, echo=PWhite(0.025, 0.029), mverb=0.2, follow=4)
k5 >> noise(dur=4, cut=1/9, hpf=1400, lofi=0.1, echo=PWhite(0.25, 0.029), mverb=0.2, follow=4)
k6 >> cbass(-4, dur=var([1, 1/6, 1/3, 1/2, 1/6], [12, 4]), follow=4, dist2=0.5, mverb=0.5).unison(2)
k7 >> alva()
k9 >> loop("ragedrone16", dur=16)
p4 >> rsin(dur=8,oct=2, lpf=1200)
