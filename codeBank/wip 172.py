# wip 172

r3 >> blip(oct=(3,P*[4,5,6]), dur=[P*[8,3],P*[0,1]], fm_saw=PWhite(), fm_saw_=PWhite(), fm_saw_i=PWhite(), fm_saw_i_=PWhite(0,1), valad=PFr(2500,6000), valadr=0.1, valadd=5, valadt=0, valadc=0.2, vol=.8, lofi=0, wshape=0, wgain=1, wmix=0.5).unison(5, .25)

# z1 >> lbass(dur=PDur([3,5],8), lpf=0, rate=1.2, wshape=2, wgain=1, wmix=0.5, fm_pulse=0, fm_pulse_i=0.9, tone=.5, hpf=200, vol=0.8).unison(3)

v3 >> supersaw(lpf=2400, dur=ù5, oct=(3,4), r=0.8, fm_pulse=0.4, fm_pulse_i=0.4)

Clock.bpm=172
        
w2 >> play("x.", sample=1, mverb=0.3, lpf=1310, combres=0, combfreq=200, combdecay=0.3, combspread=0.01).sometimes("stutter")
g1 >> play("-", lpf=0, sample=7, rate=2, pan=PWhite(-1,1)).sometimes("stutter")


w2 >> play("x.",sample=1, mverb=PWhite(.1, 0.5), lpf=PFr(200,4350),cut=1,  combres=0.5, combfreq=50, combdecay=0.3, combspread=0.1)

y2 >> play("..o.", lpf=0, sample=9, fm_sin=0.6, fm_sin_i=.1).sometimes("stutter")

# a1 >> play("l.(...l)[ll]", bank=1, sample=1, cut=3, mverb=.2, lpf=4400, hpf=0)

# g2 >> play("..g.", bank=1, cut=0, sample=var([0,1], [12, 4]), hpf=400)

l1 >> plaitsX(PTime(), rate=0.5, oct=5,dur=1/2, fm_sin=0.3, fm_sin_i=0.5, mverb=0.3).unison(3)

e4 >> play("k...", bank=1, mverb=0.3, lpf=1500)

# j7 >> loop("acid4", dur=4, sample=5, lofi=0)

i7 >> loop("break16", var([0, PRand(4)], [3, 1]), dur=16,sample=8, drcomp=.5, wide=0).lclip(var(P*[4,2,1, 1/2,1/4], [PRand(4)])).sometimes("stutter", PRand(8), shift=PWhite(.2, 2), shiftsize=0.1)