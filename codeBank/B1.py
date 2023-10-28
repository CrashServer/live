# B1
c1 >> loop("cosmic16", dur=16, sample=3, hpf=40, amp=0.5).unison(4)
c3 >> loop("cosmic16", dur=16, sample=3, amp=0.5, echotime=0, echo=0, shift=PStep(4, 1, 0.5), hpf=400).unison(4)
c4 >> loop("hiphop8", dur=16, sample=4)
c0 >> loop("nsbreak16", sample=3, dur=16)
c6 >> play("Pp", dur=PDur(3, 8), sample=2, hpf=PWhite(2000, 4000))
c7 >> loop("atmo32", dur=32, sample=2).unison(0)
c8 >> loop("atmo32", dur=32, sample=1, delay=8, hpf=4000).unison(0)
c9 >> loop("nszap8", sample=1, dur=16)
