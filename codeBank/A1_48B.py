Clock.bpm = 48;
a0 >> plaits(melody() + PWalk(8, 1, 1),dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), mverb=0.5, oct=PStep(4, 4, 5), amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))
a1 >> loop("rvoice16", dur=16, sample=1, spf=(100, PWhite(2000, 500)), spfend=(PWhite(200, 5000), 500), chop=4, shift=(P*[1, 2, 0.5], P*[1, 2, 0.5]), chopmix=(0.5, 0.25, 2), feed=0.5, delay=(0, 4, 8), spfslide=16, hpf=800, mverb=0).unison(2)
a3 >> loop("rbot4", dur=16, sample=3, shift=1, hpf=1000, mverb=0.5).unison(2)
a1 >> loop("rvoice16", dur=16, sample=1, spf=(100, PWhite(2000, 500)), spfend=(PWhite(200, 5000), 500), chop=4, shift=(P*[1, 2, 0.5], P*[1, 2, 0.5]), chopmix=(0.5, 0.25, 2), feed=0.5, delay=(0, 4, 8), spfslide=16, hpf=1200, formant=var([0, (0.5, 0)])).unison(2)

a2 >> plaitsX([PSine(PWalk(8, 6, PWalk(8, 1, 1)))], oct=4, tanh=var([0, 0.2], P*[2, 4, 8, 16]), dur=P[1/2, [1/1, 1/2, 1/2]], sus=1/2, lpr=linvar([0.05, 4], P*[1, 2, 4, 8, 16]), preset=(3, 8), lpf=linvar([400, 4000], [24, 8]), amp=0.1, pan=(linvar([-1, 1], 32), PWhite(-1, 1))).sometimes("stutter", echo=2, oct=4, sus=1)
a0 >> plaits(melody(),dur=(1/2, 1/4), engine=Pvar([3, 4]), drive=var([0, 0.1, 0.2, 0]), mverb=0.8, oct=4, dist2=0.4)

a0 >> bass(melody(),dur=var([1/4, 2],[13, 3]), drive=0, mverb=0.8).unison(2).every(13, "offmul", 2)
a3 >> loop("rbot4", dur=4, sample=1, shift=0, hpf=1000, mverb=0.5).unison(2) #dur>
a9 >> loop("techfx4", dur=16, delay=8, sample=4, amp=2, shift=0, hpf=2000, mverb=0.5, shape=0.0).unison(2)
