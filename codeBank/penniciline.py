# penniciline 130
# techno

Clock.bpm = 130

k1 >> cs80(dur=P[1,1,0.5,0.5,1,0.25,0.25,0.25,0.25], gate=0.8, fbdelay=0.7, fbtime=0.2, glide=var([0, 0.2, 8],[8, 4, 2]), fbfeed=0.7, fbcutoff=PRand([400, 20000]), oct=3, fbspread=0.5, beat_dur=1, mverb=1, mverbmix=lininf(0, 0.5, 128), mverbdamp=0.4, mverbdiff=0.225, mverbfreeze=0, multicrush=4, mclowdrive=4, mcmiddrive=1, apan=0.2, shimmer=1, shimsize=0.8, shimpitch=var([0, 0.5, 4, 8, 32], [32, 8]), shimmix=1, awidth=1, apwave=0, mchighdrive=linvar([0.1,4],[132, 4, 8]), mclofreq=12000, mchifreq=linvar([1000, 12000], 8))
s1 >> play("x ",dur=PStep([8],[2,1,0.5,0.25]), dist2=0.5, combres=0, combfreq=400, combdecay=0.5, combmix=0.5, combspread=0.06, amp=2.0, gate=0.4, fbdelay=0.2, fbtime=0.1, fbfeed=0.9, fbcutoff=1000, fbspread=0.03, beat_dur=1, leg=4)
h5 >> a_hhat(dur=0.25, amp=P[0.3,0.2,0.25,0.15]*PRand([1,1,1,0]))
h4 >> a_hhat(dur=P[0.25,0.125,0.125,0.25,0.25], decay=P[0.02,0.03,0.02,0.05,0.03], dist=0.2, amp=0.5)
h5 >> play("U.u.", amp=1, dur=4, dist2=0.9, sample=4, fbdelay=1, fbtime=0.8, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1)
k1.hpf=400
k7 >> dbass(dur=P[1,1,0.5,0.5,1,0.25,0.25,0.25,0.25], gate=0.9, drift=4, fbdelay=0.7, fbtime=0.5, glide=var([0, 0.4, 8],[8, 4, 2]), fbfeed=0.7, fbcutoff=3000, fbspread=1.45,oct=7, beat_dur=1, mverb=1, mverbmix=lininf(0, 0.5, 128), mverbdamp=0.4, mverbdiff=0.225, mverbfreeze=0, multicrush=linvar([1, 400], 32), mclowdrive=1, mcmiddrive=12, mchighdrive=1.8, mclofreq=12000, mchifreq=linvar([1000, 12000], 8))
k1.hpf=50
k4 >> play("X ", amp=2, sample=6)
k3 >> dbass(dur=k1.dur, dist2=1, rate=4, shape=0, gate=0.5, oct=(5, 6, P[7, 6])).unison(4)
k9 >> cs80(k1.dur, oct=6,  mverb=0.5, gate=0.6).unison(4)
k2 >> play("-", dur=k1.dur/2.0, fbdelay=-0.5, fbtime=0.3, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1)
k3 >> dbass()
k1 >> dbass()
k9.oct=2
l4 >> loop("bsbass4", dur=4, amp=2)
s1.stop()
k3.lpf=400
k1.oct=2
k7.oct=3
k1.oct=3
k3.oct=5
k1.oct=3
k1.oct=2
k1 >> blip()
k1.hpf=1200

k1.degree=-1
# k1.dur=4.slider()   # broken in source
# k4 >> play(".X", amp=1)

k1.degree=-1

# k7 >>play("X ", amp=4)
s1.stop()

# k1 >> abass(lpf=1200)
# k8 >> dbass(dur=1/2, dist2=0.3, shape=2, tanh=0.2)

k4 >> play("")
