chrono()

a1 >> play("-", fx2=0, rate=PFr(1,2.4), pan=PWhite(-1,1), dur=0.5, hpf=4000).human(40, 5,5)

x1 >> play("k.K.k..k[kk]", sample=0, valad=PFr(400,2000), valadr=PFr(0.7, 0.9)).sometimes("stutter", PRand(4))

f6 >> lbass((PWhite(-0.125, 0.125),PWhite(-0.125, 0.125)), oct=(2,3,4), fx1=1, dur=8, fx2=1) + PwRand([0,PRand(9)],[75,25])
x2 >> play("x.", sample=4, lpf=1400, amp=1)
f3.stop()
7 >> ebass((PWhite(-0.125, 0.125),PWhite(-0.125, 0.125)), oct=(3,5,4), fx1=1, dur=8, fx2=1, amp=0.4) + PwRand([0,PRand(9)],[75,25])


print(PRand(0,9)[:16])

x3 >> loop("vocalcrash8", hpf=PWhite(800, 1600), mverb=0.5, fx1=0.7, pos=PWhite(-1,1), sample=PRand(8),dur=16, a=PWhite(0, 1), fx2=0.5, amp=1, clouds=1, clouds_=PWhite(0, 1), csize=PWhite(0.1, 3), csize_=3, csize_d=4).unison(2)

x4 >> gsynth("vocalcrash8", size=0.5, mring=1.0, density=10, deg=4, amp=0, rmodel=2, rpoly=4, rpos=PWhite(0, 1))

g1 >> play("G", dur=PRand(32), crush=PRand(16), bits=PRand(4,16), sample=PRand(2020), amp=0.8, chop=PRand(4,16))

z1 >> total(b3.degree[0],dur=16, amp=[1,PWhite(0,0.5)], fmod=PRand([16, 32, 64, 128]), fx1=1, bpf=PRand(800,4000), bpr=0.1, bpr_=0.5, bpr_d=4, vib=PRand(16), spin=PWhite(-1,1)).slider()

print(Clock.bpm)

Clock.bpm = lininf([120, 140, 32)

psynth("gsynth")

pfx("mring")

m2 >> plaitsX([0,5,7,3], preset=12, dur=P*[3,rest(1)], oct=5, hpf=3500, mring=1, rstruct=PWhite(0.2,0.7), rmodel=2, fx2=1) 


l1 >> 


clouds_, clouds_d, cpos_, cpos_d, csize_, csize_d, cdens_, cdens_d, ctex_, ctex_d, cpitch_, cpitch_d, cgain_, cgain_d, cfb_, cfb_d, cmode_, cmode_d, sus|



pfx("clouds")