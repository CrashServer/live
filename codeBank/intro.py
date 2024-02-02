# intro
scene0
Clock.bpm=48
a1 >> play("{yYnNFlL}", sample=PRand(99), dur=PDur(3,8)*PRand([2,4,8,16]), pan=PWhite(-1,1), amp=linvar([0,0.5],[PRand(16,32),PRand(16,64)]), amplify=P*[0,1], rate=P*[1,PWhite(-1,4)], mverb=P*[0,PWhite(0.2,0.1)])
a2 >> eeri((melody()), oct=(3), dur=8, atk=0.05, blur=PWhite(1,2), rate=PRand(0,12), vib=PRand(12))
a3 >> glitcher(oct=PRand(8), rate=PWhite(1, 128), amp=0.6, dur=PWhite(0.2,4), len=PWhite(1, 16), henA=PWhite(0.01, 4), fmod=0, henB=PWhite(0.1, 0.2), t=P*[2, 4, 6, 8, 32], crush=PRand(16),bits=16, shape=0, mverb=0.6, revsus=a1.dur)
