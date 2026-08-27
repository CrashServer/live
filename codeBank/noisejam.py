# noise jam 132
# noise

Clock.bpm=132

print(f2.valad)

f2 >> viola(dur=4, fmod=[2, 4, 6, 8], shape=1, oct=(3, 4, 5), pan=PWhite(-1, 1), chop=[16, 8, 4], blur=(2, PWhite(1,3)), valad=PGauss(500,200), hpf=[1200, 400, 3200, 200], valadr=PFr(0.3,.5), lpf=[2000, 4000, 6000], valadd=5, valadt=0, valadc=0.4, fx2=1, mverb=1).unison(4,.25)

x4 >> twang(oct=(2,3,4), dur=8, valad=450, valadr=0.2, valadd=25, valadt=0, valadc=0.3, fx1=1).unison(3, .5)

masterAll("fx2", [0.24, 0.5,0.6, 0.4, 1, 1])

f2.amp=lininf(1, 0, 16)
f2.stop()

q9 >> brown(dur=4, delay=2, vadiod=PFr(500,2200), vadiod_=6000, vadiod_d=PFr(.2,.8), vadiodr=0.7, vadiodd=5, vadiodc=0.3, valad=500, valad_=8000, valadr=0.6, valadd=15, valadt=0, valadc=0.3, fx2=1, fx1=1, fx=1).unison(3)

w6 >> blip(oct=4, dur=8, shape=0, rate=.2, fx1=1, fx2=1, fmod=1)

u7 >> ikea(hhat=PFr(4,8), amp=2, dist2=4, sn=PFr(0.1,.9), harm=PWhite(1,2), dur=1/2, pshift=(0,7), oct=(5, 6, 7), vadiod=1500, vadiodr=0.5, vadiodd=0.6, vadiodc=0.3).slider(.3)

u8

psynth()

soloRnd()

# [broken in source] a3 >> eeri(cutoff=400, valad=500, oct=(2, 3), valadr=0.3, valadd=50, shaope valadt=0, valadc=0.3, mverb=0.5).unison(2)

p3 >> angst(dur=4, lpf=PFr(10, 500, 8), lpf_=PFr(20,1200, 8), oct=6, comp=0.5, comp_down=1, comp_up=0.8, dubd=0.5, dublen=0.1, dubwidth=0.5, dubfeed=0.8).unison(2)
p4 >> angst(dur=6, delay=2, fx2=0.5, lpf=PFr(10, 500, 8), lpf_=PFr(20,1200, 8), oct=4, comp=0.5, comp_down=1, comp_up=0.4, dubd=0.5, dublen=0.1, dubwidth=0.12, dubfeed=0.8, pan=PWhite(-1, 1)).unison(4)

p5 >> abass(spread=0.8, cutoff=2800, rq=0.8, dur=1/2, lpf=PFr(10, 3200, 8), lpf_=PFr(20,3600, 8), oct=5, comp=0.7, comp_down=1, comp_up=0.8, dubd=0.5, dublen=0.2, dubwidth=0.5, dubfeed=0.8).unison(2)

p6 >> cluster(para1=PFr(10, 128), oct=6, dur=16, vakorg=1200, vakorgr=0.5, vakorgd=0.5, vakorgt=0, vakorgc=0.3, chop=8)
