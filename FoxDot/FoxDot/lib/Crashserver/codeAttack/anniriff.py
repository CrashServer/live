# anniriff
n1 >> zap(0, dur=8, hpf=40, drive=[PWhite(0.1,0.4),0.2], oct=(3, PStep(9,5,[4, (5, 6)])), chop=4, chopmix=0.25, spf=10, spfend=8000, spfslide=(0.1, PRand(4,8)), octer=1, octersubsub=var([2, PRand(1,15)], [13]), fx1=0, hpfx1=80, amp=P[0.3,0, 0.1, 0, 0.1, 0], vol=0.7).unison(4)
n2 >> sawbass(0, dur=8, sus=[8], echo=1/2, amp=(n1.amp==0), mid=2, echotime=PRand(0,12), oct=(5,4,5), drive=(0.01,0,0.01), vol=0.6).unison(3,var(PWhite(0.25,0.30)),var(PRand(99),8))
n1.synthdef="lazer"
n2.synthdef="zap"
n3 >> brown(chop=PRand(8), chopwave=PWhite(0,8), dur=PWhite(0.1,4), amp=var([0, expvar([0,2],[6,0])], [14, 2]), pan=PWhite(-1,1), spf=40, spfend=PRand(400,9800), spfslide=n3.dur/2, drive=1, hpf=linvar([3200, 200], [PRand(4,32), 0]), fx2=1, fx1=1, hpr=PWhite(0.1,0.9))
n4 >> ebass([1,0,0,0,0], dur=[1/2,1/2,1,1], oct=(4), pick=0.2, cutoff=linvar([850, 1250],32), decay=1.2, rel=n4.dur*0.5, amp=1, fold=(0, 0.3), vol=0.5).penta()
n5 >> ebass([1,0,0,0], dur=[1/2,1/2,1,1], oct=(3, 4, 5), pick=(0.2,0.5,0.7), cutoff=linvar([250, 1250],32), decay=1.2, rel=n4.dur*0.1, amp=1, fold=(0,0.3,0.2), vol=0.4).penta()
n6 >> click(PWhite(-0.1, 0.1),dur=b8.dur, hpf=var([200, 3200], [4, 4]), oct=(3, 4), hpr=0.2, shape=(1,0.5), amp=n4.degree == 0).unison(0)
n4.shape=0
n4.pick=[0.8, 0.2, 0.2]
n7 >> play("b...", sample=4, vol=0.7, cut=2)
n6 >> play("(K...)(K...)..", dur=1/2, sample=(0,9), cut=PWhite(0.5,5), vol=0.8, fx1=1)
n8 >> play("(O...)(O...)..", dur=1/2, sample=(8), cut=PWhite(0.5,5), vol=0.7)
n9 >> lapin((0,4), amp=var([0, 1], [PRand(8,16),PRand(1,8)]), dur=PDur(var([4,P*[6,5,7]],[6,2]),8), sus=1/8, oct=(5,6), rate=0.8, shape=0.2, fx1=0, fx2=1, drive=0.8, tanh=0).unison(3,0.25,90)
n0 >> ebass([1,0,0,0,0], dur=[1/2,1/2,1,1], oct=(4), lofi=var([0, 0.01], 8), pick=0.2, cutoff=linvar([850, 1250],32), decay=0.6, rel=n4.dur*0.5, amp=1, fold=(0, 0.14), smooth=0.1, lofiwow=1, vol=0.3, tanh=0.2).penta()