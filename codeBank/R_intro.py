# R_intro
# R_

Clock.bpm=102
Scale.default="minor"
n3 >> loop("elephant16", dur=16, sample=0, chop=0, chopwave=5, chopi=.2).lclip(0)
x1 >> loop("xbass8", dur=8, sample=0, idist=1.0, noiz=0, noizr=0.4, noizt=0, vadiod=670, vadiodr=0.6, vadiodd=21.8, vadiodc=0.1).lclip(0)
z8 >> tb304([0,2,4,5], dur=1/4, oct=3, cutoff=220, rq=0.9, top=1500, fAtk=0.001, fDec=0.15, fSus=0.0, fRel=0.2, wave=0).end(8, 2)
n9 >> loop("xdrum8", dur=8, sample=PRand(808), drcomp=0.5, tanh=.5)
i7 >> play("<X.>", amp=3.0, lpf=0, lpr=0.7).sometimes("stutter")
i2 >> noloop("beru4", dur=8, sample=1, mverb=0.3, amp=PZero(4), tanh=1, looping=0, trig=0, fx=0)
