# biniou style 110
Clock.bpm=110
Scale.default="dorian2"
Root.default=0

k7 >> swiss(PStep(12,[1,2],0),dur=[1/2,PDur([4,5],8)], oct=(3),rate=1, rq=0, cutoff=8000, saw=2, pulse=0.5, sin=0.2, pw=0.9,tape=.3, tapedrive=15, tapewarm=0.3, tapewobble=0.5, valad=1510, valadr=0.4, valadd=1.5, valadt=0, valadc=0.1, r=0.7, rc=4,hpf=120, high=3, vol=.8).unison(3, .1).every(0.5, "stutter", cycle=8, r=0.5, cut=1)

u6 >> play("<(k.)-><|x5|.>", sample=0, amp=2, drcomp=.5).sometimes("stutter")
s1 >> play("<..o.><..C.>", sample=(6,3), room2=0.1, mix2=0.6, damp2=0.8, revatk=0.3, revsus=0.4, wshape=5, wgain=1, wmix=0.5, hpf=200)

m0 >> play(".[.i]..", bank=2, sample=PRand(999), wshape=6, wgain=1, wmix=0.5, cut=1, hpf=200)

m8 >> tb305([0, 1, 2, 3, 4, 3, 2], dur=PStep(6, PDur([1,3],8), 1/4), cutoff=500, oct=6, rq=0.3, wave=0.5,beef=2, envmod=80, valad=290, valadr=0.8, valadd=25, valadt=4, valadc=0.2,eb=0.25, ebfeed=0.5, ebmix=0.3, ebmode=2, ebwow=0.1, ebflutter=0.15, ebsat=0.3, amp=PTimebin())

k5 >> loop("drum8", dur=8, sample=3, drcomp=.4)
