# lowhigh 168
# interlude

Clock.bpm = 168
l3 >> loop("techfx4", dur=16, sample=PRand(8), chop=4, chopmix=0.5, chopwave=2, lpf=PRand([400, 3200]), lpr=0.1)
l6 >> loop("rytm64", dur=64, amp=4, sample=PRand(4))
l2 >> play("{hipP}",dur=(4, 3, PRand([1, 4])), rate=(4, -3, PRand(-4, 4)), feed=0.0, dubd=0.0, sample=(0,[2, 0, 3], PRand(8))).unison(4)
l4 >> loop("wa8", dur=32, sample=PRand(8), formant=2, amp=PBin(8), lpf=3200)
l7 >> loop("techfx4", dur=16, sample=PRand(8), amp=1.0, hpf=200, leg=8)
l1 >> loop("techfx4", dur=16, sample=2, hpf=1200)
l0 >> loop("bass8", dur=16, leg=0, hpf=1200, spin=1, sample=6, shape=0.0)
n1 >> loop("ragedrum32", dur=32, hpf=400, sample=PRand(8))
q1 >> loop("nssynth16", dur=32, chop=8, chowave=4, echo=1, leg=1, amp=1, sample=PRand(8), mid=4)
n1 >> loop("xccongas32", dur=64, amp=4)
l5 >> loop("xccongas32", dur=64, amp=4, sample=1)
l3 >> loop("ragedrum32", dur=32)
k5 >> loop("nrhodes16", dur=16, hpf=1200, hpr=0.1).unison(4)
n1 >> play("{T}", dur=PDur(5, 8), amp=2, rate=PRand([16, 8]), leg=4)
n2 >> play("..C.", dur=1)
l0 >> loop("nshits16", dur=16, leg=0, hpf=1200, spin=1, sample=PRand(8), shape=0.0)
masterAll("sample", PRand(8))
n1 >> play("{Tptmp}", sample=PRand(8))
masterAll("cut", 1/2)
k4 >> play("kw ", sample=8, leg=32)
l1 >> loop("perc8", dur=8)
l6 >> loop("pad16", dur=16, sample=2, amp=1, a=1, lpf=1800, mverb=0.5).unison(2)

