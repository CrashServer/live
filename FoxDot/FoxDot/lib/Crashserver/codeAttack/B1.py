# B1
b1 >> loop("cosmic16", dur=16, echotime=8, echo=4, sample=3, hpf=40, amp=0.5).unison(4)
b2 >> loop("sweep16", dur=32, echotime=8, echo=4, spf=200, spfend=8000, spfslide=8, sample=0, hpf=40, amp=0.2).unison(4)
b3 >> loop("cosmic16", dur=16, sample=3, amp=0.5, echotime=4, echo=2, shift=PStep(4, 1, 0.5), hpf=400).unison(4)
b4 >> loop("hiphop8", dur=16, sample=4)
b5 >> loop("atmo8", dur=8, sample=1, amp=[0, 0, 0.7, 0.5] * 2) #
b6 >> play("Pp", dur=PDur(3, 8), sample=2, hpf=PWhite(2000, 4000))
b7 >> loop("atmo32", dur=32, sample=2).unison(2)
b8 >> loop("atmo32", dur=32, sample=1, delay=8, hpf=4000).unison(2)
b9 >> loop("nszap8", sample=1, dur=16)
b0 >> loop("nsbreak16", sample=2, dur=16)