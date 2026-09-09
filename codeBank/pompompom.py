# pompompom 132
# live2026_aube

Clock.bpm = 132
variation = 0
x9 >> swiss(var([0, -2], [6,2]), oct=PStep(8, P*[5,4], 3), r=linvar([0.7, 1, 0.8], 0.5), dur=var([1/2, .75/PRand([2,3, 1])], [14,2]), rate=sinvar([1, 0], 0.5), rq=0.2, cutoff=linvar([600, 7800], 64), saw=linvar([1,3], [64, 64]), pulse=2, sin=linvar([.2, 5], 14), pw=linvar([0.136, 0.8], 26)).unison(0)
b7 >> play("X[-]", dur=1, gdel=0.0, gdeltime=0.1, gdelsize=0.1, gdelsprd=0.1, gdelfb=0.1, spring=0, sprdecay=1.5, sprdamp=0.5, sprtens=0.9, bitrot=linvar([0.8, 1.2, 0.9], 16), rotbits=8, rotrate=linvar([0.6, 1], 16), rotjitter=linvar([1, 1.3, 1.2], [1, 0.25])).sometimes("stutter", 2, mverb=0, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0)
d0 >> play("..{[--]c}.", amp=0.4,csweep=linvar([0.2, 0.3, 0.4], 16), lpf=linvar([1500, 1900], 16), rate=0.5, cswfreq=linvar([300, 1300], 32), cswdepth=0.2, cswrate=0.2, bitrot=linvar([0.4, 0.7], 16), rotbits=8, rotrate=0.2, rotjitter=0.1, cswdecay=0.2)
x4 >> arpymod(x9.degree,rate=1, tone=4.72, body=4.35, dur=PRhythm([1, (3, 8)]), decimate=2, decbits=12, decrate=4000, decsmooth=0, fshift=0, fphase=0, fmix=0.5).unison(3)
s5 >> play(":", dur=8, delay=1.75, rate=4, echo=0.5, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, decimate=0.5, decbits=4, decrate=4000, decsmooth=0)
x5 >> arpymod(x9.degree,rate=1, oct=4, tone=4.72, body=4.35, dur=PRhythm([1, (5, 8)]), decimate=1, decbits=12, decrate=4000, decsmooth=0, fshift=4, fphase=0, fmix=0.5)
x4.stop()
x4 >> arpymod(x9.degree,rate=1, tone=4.72, body=4.35, dur=PRhythm([1, (3, 8)]), decimate=2, decbits=12, decrate=4000, decsmooth=0, fshift=0, fphase=0, fmix=0.5).unison(3) + var([0, 3, 0], bitrot=4, rotbits=8, rotrate=0.5, rotjitter=0.1, low=4)
b7 >> play("X[-]", dur=1, gdel=0.0, gdeltime=0.1, gdelsize=0.1, gdelsprd=0.1, gdelfb=0.1, spring=0, sprdecay=1.5, sprdamp=0.5, sprtens=0.9, bitrot=linvar([0.8, 1.2, 0.9], 16), rotbits=8, rotrate=linvar([0.6, 1], 16), rotjitter=linvar([1, 1.3, 1.2], [1, 0.25])).sometimes("stutter", 2, mverb=0, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0, bitrot=4, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, rotbits=8, rotrate=0.5, rotjitter=0.1)
x4 >> arpymod(x9.degree,rate=1, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tone=4.72, body=4.35, dur=PRhythm([1, (3, 8)]), decimate=1, decbits=7, decrate=4000, decsmooth=0, fshift=0, fphase=0, fmix=0.5).unison(3)
x5 >> arpymod(x9.degree,rate=1, oct=4, tone=4.72, body=4.35, dur=PRhythm([1, (5, 8)]), decimate=1, decbits=12, decrate=4000, decsmooth=0, fshift=4, fphase=0, fmix=0.5)

attack("pompompom")

##### attack@pompompom.slk:~$ #####

variation = Variation(32,4)

s7 >> play("..i.", bank=2, sample=4, rate=(0.75, 1), vol=.9, csweep=fc(16, 0, .6), cswfreq=160, cswdepth=0.3, cswrate=0.5, cswdecay=0.5).sometimes("stutter", PRand(8))

x9 >> swiss(var([0, -2], [6,2]), oct=PStep(8, P*[5,4], 3), r=linvar([0.7, 1, 0.8], 0.5), dur=var([1/2, .75/PRand([2,3, 1])], [14,2]), rate=sinvar([1, 0], 0.5), rq=0.2, cutoff=linvar([600, 7800], 64), saw=linvar([1,3], [64, 64]), pulse=2, sin=linvar([.2, 5], 14), pw=linvar([0.136, 0.8], 26)).unison(0)

# a1 >> omi(fmamp=linvar([0.7, 1.1, 1], 1), dur=linvar([6, 10], 1)/2, echo=[1, ((1, 2))], fmrate=linvar([200, 1700], 16), fb=linvar([1, 4, 2], 0.5), xfb=0.1, cutoff=linvar([4900, 3900], 3), rq=0.9, fm_sin=0, fm_sin_i=0.91, r=linvar([.1, 2], [54, 54]))
b7.stop()

b7 >> play("X[-]", dur=1, gdel=0.0, gdeltime=0.1, gdelsize=0.1, gdelsprd=0.1, gdelfb=0.1, spring=0, sprdecay=1.5, sprdamp=0.5, sprtens=0.9, bitrot=linvar([0.8, 1.2, 0.9], 16), rotbits=8, rotrate=linvar([0.6, 1], 16), rotjitter=linvar([1, 1.3, 1.2], [1, 0.25])).sometimes("stutter", 2, mverb=0, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0)
d0 >> play("..{[--]c}.", amp=0.4,csweep=linvar([0.2, 0.3, 0.4], 16), lpf=linvar([1500, 1900], 16), rate=0.5, cswfreq=linvar([300, 1300], 32), cswdepth=0.2, cswrate=0.2, bitrot=linvar([0.4, 0.7], 16), rotbits=8, rotrate=0.2, rotjitter=0.1, cswdecay=0.2)

drop()

soloRnd()
x4 >> arpymod(x9.degree,rate=1, tone=4.72, body=4.35, dur=PRhythm([1, (3, 8)]), decimate=2, decbits=12, decrate=4000, decsmooth=0, fshift=0, fphase=0, fmix=0.5).unison(3) + var([0, 3, 0], bitrot=4, rotbits=8, rotrate=0.5, rotjitter=0.1, low=4)
x4 >> arpymod(x9.degree,rate=1, tone=4.72, body=4.35, dur=PRhythm([1, (3, 8)]), decimate=2, decbits=12, decrate=4000, decsmooth=0, fshift=0, fphase=0, fmix=0.5).unison(3) + var([0, 3, 0], bitrot=4, rotbits=8, rotrate=0.5, rotjitter=0.1, low=4)

x5 >> arpymod(x9.degree,rate=1, oct=4, tone=4.72, body=4.35, dur=PRhythm([1, (5, 8)]), decimate=0, decbits=12, decrate=4000, decsmooth=0, fshift=4, fphase=0, fmix=0.5, multicrush=1, mclowdrive=4, mcmiddrive=1, mchighdrive=1.8, mclofreq=200, mchifreq=3000)

b7 >> play("X[-]", dur=1, gdel=0.0, gdeltime=0.1, gdelsize=0.1, gdelsprd=0.1, gdelfb=0.1, spring=0, sprdecay=1.5, sprdamp=0.5, sprtens=0.9, bitrot=linvar([0.8, 1.2, 0.9], 16), rotbits=8, rotrate=linvar([0.6, 1], 16), rotjitter=linvar([1, 1.3, 1.2], [1, 0.25])).sometimes("stutter", 2, mverb=0, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0, bitrot=4, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, rotbits=8, rotrate=0.5, rotjitter=0.1)

x9 >> swiss(var([0, 4], [6,2]), oct=PStep(8, P*[5,4], 3), r=linvar([0.7, 1, 0.8], 0.5), dur=var([1/2, .75/PRand([2,3, 1])], [14,2]), rate=sinvar([1, 0], 0.5), rq=0.2, cutoff=linvar([600, 7800], 64), hpf=800, saw=linvar([1,3], [64, 64]), pulse=2, sin=linvar([.2, 5], 14), pw=linvar([0.136, 0.8], 26)).unison(0)
sc >> scratch([7,12,7,rest(0),5,rest(0)], oct=5, dur=PRand([0.5,0.25,1],4), sus=PRand([0.1,0.2,0.3],4), amp=sinvar([0,0.3],4), rate=sinvar([0.1,0.5],2), depth=sinvar([0.3,0.8],4), pitchShift=var([0,1,2,-1],4), dynfuzz=0.5)

x4.stop()
x5 >> arpymod(x9.degree,rate=1, oct=4, tone=4.72, body=4.35, dur=PRhythm([1, (5, 8)]), decimate=1, decbits=12, decrate=4000, decsmooth=0, fshift=4, fphase=0, fmix=0.5, multicrush=1, mclowdrive=2, mcmiddrive=1, mchighdrive=1.1, mclofreq=1200, mchifreq=300, mid=2)
x5 >> arpymod(x9.degree,rate=1, oct=(4, 5, 6), tone=4.72, body=4.35, dur=PRhythm([1, (5, 8)]), decimate=1, decbits=12, decrate=4000, decsmooth=0, fshift=4, fphase=0, fmix=0.5, multicrush=1, mclowdrive=2, mcmiddrive=1, mchighdrive=1.1, mclofreq=1200, mchifreq=300, mid=2)

o6 >> subbass(x9.degree, dur=4, amp=4, shape=0.1)
x5 >> donorgan(x9.degree,rate=1, oct=(4, 5), tone=0.72, body=4.35, dur=PRhythm([1, (7, 8)]), decimate=1, decbits=12, decrate=4000, decsmooth=0, fshift=8, fphase=0, fmix=0.5).follow(x9)
x4 >> arpymod(2,rate=1, tone=12, body=4.35, oct=6, dur=PRhythm([1, (3, 8)]), decimate=2, amp=0.5, decbits=12, decrate=4000, decsmooth=0, fshift=0, fphase=0, fmix=0.5).unison(3)
