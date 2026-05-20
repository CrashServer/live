# recorded_073119
# recorded

#@intro(64)
k8 >> radio(rate=1, dur=4, shimmer=1, shimsize=0.8, shimpitch=0.5, shimmix=0.5)

#@build(32)
q3 >> loop("quake8", dur=8)

#@peak(16)
k8 >> radio(rate=1, dur=4, shimmer=1, shimsize=0.8, shimpitch=4, shimmix=0.5)

#@break(16)
q3 >> loop("quake8", dur=2)

#@drop(32)
z6 >> loop("sundrone16", dur=16)

#@outro(32)
z6 >> loop("sundrone16", dur=16, wshape=0.4, wgain=1, wmix=0.5)

#@part7(8)
k8.dur=2

#@part8(16)
k8.hpf=800

#@part9(32)
q3.lclip(2)

#@part10(16)
b6 >> loop("exoplanet16", dur=16)

#@part11(16)
z6.chop=4

#@part12(32)
b6.mverb=0.5

#@part13(8)
s5 >> mpluck(linvar([0, -8], 32),filter=3, cutoff=2800, rq=0.8)

#@part14(8)
s5 >> mpluck(linvar([0, -8], 32),filter=3, dur=1/2, cutoff=2800, rq=0.8)

#@part15(8)
s5 >> mpluck(linvar([0, -8], 32),filter=3, dur=(1/2, 1/4), cutoff=2800, rq=0.8)

#@part16(32)
z6.dur=4

#@part17(16)
k8 >> ethpad(rate=1, attack=2.0, release=4.0)

#@part18(32)
q3 >> loop("aurora16", dur=16)

#@part19(32)
f8 >> arpymod(linvar([0, -32], 32),rate=0.5, cutoff=5000, rq=0.5)

#@part20(32)
k8 >> ethpad(rate=1, attack=2.0, release=4.0, sgate=1, sgthresh=1, sgmode=0)

#@part21(16)
q3 >> loop("aurora16", dur=16, sgate=1, sgthresh=1, sgmode=0)

#@part22(16)
z6 >> loop("sundrone16", dur=16, wshape=0.4, sgate=1, sgthresh=1, sgmode=0 wgain=1, wmix=0.5)

#@part23(16)
z6 >> loop("sundrone16", dur=16, wshape=0.4, sgate=1, sgthresh=1, sgmode=0 wgain=1, wmix=0.5)
z6 >> loop("sundrone16", dur=16, wshape=0.4, sgate=1, sgthresh=1, sgmode=0 wgain=1, wmix=0.5)

#@part24(8)
z6 >> loop("sundrone16", dur=16, wshape=0.4, sgate=1, sgthresh=1, sgmode=0 wgain=1, wmix=0.5)

#@part25(8)
z6 >> loop("sundrone16", dur=16, wshape=0.4, sgate=1, sgthresh=1, sgmode=0,wgain=1, wmix=0.5)

#@part26(16)
k8.stop()

#@part27(32)
g7 >> ebass(dur=2)

#@part28(4)
g7 >> ebass(fw(8, 1, 4),dur=2)

#@part29(8)
g7 >> ebass(fw(8, 1, 4),dur=1/4)

#@part30(16)
g7 >> ebass(fw(8, 1, 4),dur=1/4).unison(4)
g7 >> ebass(fw(8, 1, 4),dur=1/4).unison(14)

#@part31(8)
g7 >> ebass(fw(8, 1, 4),dur=1/4, shape=0.1, shapemix=0.5).unison(14)

#@part32(8)
f8.stop()
q3.stop()

#@part33(16)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, shapemix=0.5).unison(14)

#@part34(16)
z6.stop()
b6.stop()
s5.stop()

#@part35(16)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, shapemix=0.5).unison(4)

#@part36(16)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=0, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=0.4, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=0.5, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=0.6, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=0.7, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=0.8, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=0.9, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=1.0, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=1.1, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=1.2, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=1.3, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=1.4, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=1.5, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=1.6, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=1.7, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=1.8, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=1.9, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=2.0, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=2.1, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=2.2, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=2.3, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=2.4, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=2.5, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=2.6, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=2.7, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=2.8, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=2.9, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=3.0, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=3.1, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=3.2, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=3.3, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=3.4, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=3.5, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=3.6, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=3.7, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=3.8, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=3.9, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=4.0, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=4.1, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=4.2, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=4.3, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=4.4, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=4.5, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=4.6, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=4.7, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=4.8, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=4.9, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=5.0, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=5.1, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=5.2, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=5.3, sgthresh=1, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=5.3, sgthresh=2, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=5.3, sgthresh=3, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=5.3, sgthresh=4, sgmode=0, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=5.3, sgthresh=4, sgmode=1, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=5.3, sgthresh=4, sgmode=2, shapemix=0.5).unison(4)
g7 >> ebass(fw(32, 1, 4),dur=1/4, shape=0.1, sgate=5.3, sgthresh=4, sgmode=3, shapemix=0.5).unison(4)

#@part37(8)
Clock.clear()
soff()
Server.clearFx()

#@part38(16)
rec_stop()

#@endfade(16)
