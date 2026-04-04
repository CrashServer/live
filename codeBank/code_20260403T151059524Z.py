variation = Variation(32,4)

s7 >> play("..i.", bank=2, sample=4, rate=(0.75, 1), vol=.9, csweep=fc(16, 0, .6), cswfreq=f160, cswdepth=0.3, cswrate=0.5, cswdecay=0.5).sometimes("stutter", PRand(8))

x9 >> swiss(var([0, -2], [6,2]), oct=PStep(8, P*[5,4], 3), r=linvar([0.7, 1, 0.8], 0.5), dur=var([1/2, .75/PRand([2,3, 1])], [14,2]), rate=sinvar([1, 0], 0.5), rq=0.2, cutoff=linvar([600, 7800], 64), saw=linvar([1,3], [64, 64]), pulse=2, sin=linvar([.2, 5], 14), pw=linvar([0.136, 0.8], 26)).unison(0)

# a1 >> omi(fmamp=linvar([0.7, 1.1, 1], 1), dur=linvar([6, 10], 1)/2, echo=[1, ((1, 2))], fmrate=linvar([200, 1700], 16), fb=linvar([1, 4, 2], 0.5), xfb=0.1, cutoff=linvar([4900, 3900], 3), rq=0.9, fm_sin=0, fm_sin_i=0.91, r=linvar([.1, 2], [54, 54]))
b7.stop()
                                              
b7 >> play("X[-]", dur=1, gdel=0.0, gdeltime=0.1, gdelsize=0.1, gdelsprd=0.1, gdelfb=0.1, spring=0, sprdecay=1.5, sprdamp=0.5, sprtens=0.9, bitrot=linvar([0.8, 1.2, 0.9], 1), rotbits=8, rotrate=linvar([0.6, 1], 1), rotjitter=linvar([1, 1.3, 1.2], [1, 0.25])).sometimes("stutter", 2, mverb=0, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0)

d0 >> play("..{[--]c}.", amp=0.4,csweep=linvar([0.2, 0.3, 0.4], 1), lpf=linvar([1500, 1900], 1), rate=0.5, cswfreq=linvar([300, 1300], 3), cswdepth=0.2, cswrate=0.2, bitrot=linvar([0.4, 0.7], 1), rotbits=8, rotrate=0.2, rotjitter=0.1, cswdecay=0.2)
