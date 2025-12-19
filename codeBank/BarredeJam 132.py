# BarredeJam 132
# mud

Clock.bpm = 132
w9 >> loop("ragegtr16", dur=16, lpf=3900, sample=PRand(8), mverb=0.0, chop=2, formant=0.0, dafilter=1300, dastart=1220, amp=PBin()).lclip([1, 2, 4]).slider()
c3 >> loop("electrodrum16", dur=16, sample=4, drcomp=0.8)

z7 >> loop("break160_16", dur=16, sample=var(PRand(404), 32))

n5 >> superbass(PTime()[:8], dur=1/2, cutoff=PFr(1400,9000),rq=0.6,oct=[5,6], wshape=5, sus=1/6, echo=.75).unison(3)

o4 >> play("..C.", sample=3).sometimes("stutter", PRand(15))
yw >> play("<x......x..x.....><...B........B...>", dur=0.25, dist2=0.0, sample=59, rate=1, echo=0.25)
yz >> play("<x......x..x.....><...B........B...>", dur=0.5, sample=59, rate=4, echo=0.5)
y8 >> play("<................><...B........B...>", dur=0.5, sample=59, rate=1, echo=[0.5, 0])

q4 >> play("-{:n}", rate=PFr(1, 8),dur=PDur(7,8), pan=PWhite(-1,1),wshape=5).unison(3).sometimes("stutter")