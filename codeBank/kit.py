# kit 132
# live2026_aube

kit = pkit("techno", seed=12)
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=185, fbdelay=0.1, fbtime=0.25, fbfeed=0.7, fbcutoff=10300, fbspread=0.4, beat_dur=1, spring=1, sprdecay=1.1, sprdamp=0.6, sprtens=0, gdel=0, gdeltime=0.01,gdelsize=0.01, gdelsprd=0.1, gdelfb=.1).unison(3)
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=85, fbdelay=0.1, fbtime=0.25, fbfeed=0.7, fbcutoff=300, fbspread=0.4, beat_dur=1, spring=4, sprdecay=2, sprdamp=0.6, sprtens=0.5, gdel=0, gdeltime=0.01,gdelsize=0.01, gdelsprd=0.1, gdelfb=.1).unison(3)
kit = pkit("techno", seed=19)
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=850, fbdelay=0.2, fbtime=0.25, fbfeed=0.7, fbcutoff=1300, fbspread=0.2, beat_dur=1, spring=4, sprdecay=1.5, sprdamp=0.1, sprtens=1, gdel=0.1, gdeltime=0.01,gdelsize=0.01, gdelsprd=0.1, gdelfb=.1).unison(3)

kit = pkit("techno", seed=14)
d1 >> play(kit.kick, dur=0.25, low=0, mid=linvar([4, 8], 32), lowfreq=85, leg=0, fbdelay=0.25, fbtime=0.25, fbfeed=0.7, fbcutoff=1300, fbspread=0.4, beat_dur=1, spring=0.7, sprdecay=1.8, sprdamp=0.6, sprtens=1, gdel=0, gdeltime=0.01,gdelsize=0.01, gdelsprd=1, echo=0.5,shape=4, gdelfb=.1).unison(3)

kit = pkit("techno", seed=4)
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=185, fbdelay=0.14, rate=1, rgate=0.5, rgaterate=4, rgatewave=0, fbtime=0.119, fbfeed=1.0, fbcutoff=4100, fbspread=4, beat_dur=1, spring=4.7, sprdecay=1.8, sprdamp=0.3, sprtens=1.0, gdel=0.1, gdeltime=0.10,gdelsize=0.10, gdelsprd=0.2, echo=0.0, gdelfb=1.2).unison(3)

kit = pkit("techno", seed=19)
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=185, fbdelay=0.025, fbtime=0.79, fbfeed=1.0, fbcutoff=4100, fbspread=0.4, beat_dur=1, spring=0.7, sprdecay=1.8, sprdamp=0.3, sprtens=1.4, gdel=0.1, gdeltime=0.10,gdelsize=0.10, gdelsprd=0.1, echo=0.0, gdelfb=0.6).unison(3)
d1 >> play(kit.kick, dur=0.25, low=0, mid=0, high=1, mverb=0.05, lowfreq=85, leg=0, fbdelay=0.25, fbtime=0.25, fbfeed=0.7, fbcutoff=1300, fbspread=0.4, beat_dur=1, spring=0.7, sprdecay=1.8, sprdamp=0.6, sprtens=1, gdel=0, gdeltime=0.01,gdelsize=0.01, gdelsprd=1, echo=1,shape=4, gdelfb=.1).unison(3)

~d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=185, fbdelay=0.14, rate=1, rgate=0.5, rgaterate=4, rgatewave=0, fbtime=0.119, fbfeed=1.0, fbcutoff=4100, fbspread=4, beat_dur=1, spring=4.7, sprdecay=1.1, sprdamp=0.9, sprtens=1.0, gdel=0.1, gdeltime=0.10,gdelsize=0.10, gdelsprd=0.2, echo=0.0, gdelfb=1.2).unison(3)

d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=185, fbdelay=0.025, fbtime=0.79, fbfeed=1.0, fbcutoff=4100, fbspread=0.4, beat_dur=1, spring=0.7, sprdecay=1.8, sprdamp=0.3, sprtens=1.4, gdel=0.1, gdeltime=0.10,gdelsize=0.10, gdelsprd=0.1, echo=0.0, gdelfb=0.6).unison(3)

d1.rate=var([8, 0.5, 0], [8, 2, 6])
kit = pkit("techno", seed=19)
d2 >> play(kit.hat, dur=0.25, sblur=0.1, sbluramt=2, hpf=8000, shimmer=0.0, shimsize=0.8, shimpitch=0.5, shimmix=0.4, gdel=0.2,gdeltime=0.01, gdelsize=0.01, gdelsprd=0.8, gdelfb=0.5).unison(2)

d2.dur=1/2

drop()
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=85, fbdelay=0.1, fbtime=0.25, fbfeed=0.7, fbcutoff=300, fbspread=0.4, beat_dur=1, spring=4, sprdecay=1.8, sprdamp=0.6, sprtens=1, gdel=0, gdeltime=0.01,gdelsize=0.01, dist2=0.0, gdelsprd=0.1, gdelfb=.1).unison(3)
d1.rate=1

kit = pkit("techno", seed=10)
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=4850, fbdelay=0.5, fbtime=0.5, fbfeed=1.0, fbcutoff=410, fbspread=0.4, beat_dur=1, spring=0.64, sprdecay=1.8, sprdamp=0.2, sprtens=1.3, lpf=0, lpr=0.3, gdel=0.1, gdeltime=0.10,gdelsize=0.10, gdelsprd=0.1, echo=0.0, gdelfb=0.6).unison(3)

d2.stop()
d1.shape=0

kit = pkit("techno", seed=21)
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=120, fbdelay=0.05, fbtime=0.3, fbfeed=0.4, fbcutoff=2000, fbspread=0.1, beat_dur=1, spring=0.6, sprdecay=1.2, sprdamp=0.7, sprtens=0.3, gdel=0, gdeltime=0.02, gdelsize=0.02, gdelsprd=0.2, gdelfb=0.1).unison(3)

d3 >> play(kit.kick, dur=0.25, low=0.4, lowfreq=90, fbdelay=0.08, fbtime=0.3, fbfeed=0.5, fbcutoff=1600, fbspread=0.15, beat_dur=1, spring=1.8, sprdecay=1.6, sprdamp=0.4, sprtens=0.6, gdel=0.15, gdeltime=0.03, gdelsize=0.03, gdelsprd=0.3, gdelfb=0.25).unison(3)

kit = pkit("techno", seed=33)
d3 >> play(kit.kick, dur=0.25, low=0.2, lowfreq=310, fbdelay=0.12, fbtime=0.45, fbfeed=0.6, fbcutoff=5200, fbspread=0.5, beat_dur=1, spring=2.6, sprdecay=1.9, sprdamp=0.25, sprtens=0.9, gdel=0.3, gdeltime=0.05, gdelsize=0.04, gdelsprd=0.5, gdelfb=0.4).unison(3)

d3 >> play(kit.kick, dur=0.25, low=0, mid=linvar([1, 5], 24), lowfreq=90, leg=0, fbdelay=0.2, fbtime=0.6, fbfeed=0.85, fbcutoff=3400, fbspread=1.2, beat_dur=1, spring=3.4, sprdecay=1.4, sprdamp=0.15, sprtens=1.2, gdel=0.5, gdeltime=0.07, gdelsize=0.06, gdelsprd=0.6, echo=0.4, shape=2, gdelfb=0.6).unison(3)

kit = pkit("techno", seed=45)
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=185, fbdelay=0.16, rate=1, rgate=0.6, rgaterate=8, rgatewave=1, fbtime=0.35, fbfeed=0.9, fbcutoff=6800, fbspread=2, beat_dur=1, spring=4.2, sprdecay=1.7, sprdamp=0.35, sprtens=1.1, gdel=0.4, gdeltime=0.09, gdelsize=0.08, gdelsprd=0.4, echo=0.2, bitrot=0.3, rotbits=10, rotrate=0.7, rotjitter=0.15, gdelfb=0.9).unison(3)

d2 >> play(kit.hat, dur=0.25, sblur=0.15, sbluramt=2, hpf=7500, shimmer=0.35, shimsize=0.75, shimpitch=0.6, shimmix=0.45, gdel=0.25, gdeltime=0.02, gdelsize=0.02, gdelsprd=0.7, gdelfb=0.45).unison(2)
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=185, fbdelay=0.1, rgate=0.4, rgaterate=6, rgatewave=0, fbtime=0.35, fbfeed=0.8, fbcutoff=4800, fbspread=1.5, beat_dur=1, spring=3.8, sprdecay=1.6, sprdamp=0.4, sprtens=1, gdel=0.45, gdeltime=0.08, gdelsize=0.07, gdelsprd=0.5, gdelfb=0.8).unison(3)
d1.shape=0
d2.amp=0.15
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=100, fbdelay=0, fbtime=0.25, fbfeed=0, spring=0.3, sprdecay=1, sprdamp=0.8, sprtens=0.2, gdel=0, gdeltime=0.01, gdelsize=0.01, gdelsprd=0.1, gdelfb=0).unison(3)

d2.amp=linvar([0.4, 0], 24)
d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=90, fbdelay=0.05, fbtime=0.3, fbfeed=0.3, fbcutoff=1500, spring=1, sprdecay=1.3, sprdamp=0.6, sprtens=0.3, gdel=0.1, gdeltime=0.02, gdelsize=0.02, gdelsprd=0.2, gdelfb=0.15, amp=linvar([1, 0], 24)).unison(3)

d3 >> play(kit.kick, dur=0.25, low=0, lowfreq=90, fbdelay=0.05, fbtime=0.3, fbfeed=0.3, fbcutoff=1500, spring=1, sprdecay=1.3, sprdamp=0.6, sprtens=0.3, gdel=0.1, gdeltime=0.02, gdelsize=0.02, gdelsprd=0.2, gdelfb=0.15, amp=linvar([1, 0], 24)).unison(3)
d2.stop()
d3.stop()
ld.stop()
pd.stop()

kit = pkit("techno", seed=3)
d1 >> play(kit.kick, dur=0.25, low=0, mid=0, high=1, mverb=0.05, lowfreq=85, leg=0, fbdelay=0.25, fbtime=0.25, fbfeed=0.7, fbcutoff=1300, fbspread=0.4, beat_dur=1, spring=0.7, sprdecay=1.8, sprdamp=0.6, sprtens=1, gdel=0, gdeltime=0.01,gdelsize=0.01, gdelsprd=1, echo=1,shape=4, gdelfb=.1).unison(3)

Clock.bpm = 144
