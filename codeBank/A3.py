# A3
a0 >> plaits(melody() + PWalk(8, 1, 1),dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), mverb=0.5, oct=PStep(4, 4, 5), amp=0.3, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))
a1 >> loop("rvoice16", dur=16, sample=1, spf=(100, PWhite(2000, 500)), spfend=(PWhite(200, 5000), 500), chop=4, shift=(P*[1, 2, 0.5], P*[1, 2, 0.5]), chopmix=(0.5, 0.25, 2), feed=0.5, delay=(0, 4, 8), spfslide=16, hpf=800).unison(2)
a3 >> loop("rbot4", dur=16, sample=3, shift=1, hpf=1000)

