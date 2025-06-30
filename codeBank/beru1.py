# beru1
Clock.bpm=102
Scale.default="minor"
n3 >> loop("elephant16", dur=16, sample=0, chop=0, chopwave=5, chopi=.2).lclip(0)
w0 >> lbass(0, dur=8, oct=5, cutoff=4700, tanh=.5, amp=.7).unison(2)

x1 >> loop("xbass8", dur=8, sample=0, idist=1.0, noiz=0, noizr=0.3, noizt=0, vadiod=670, vadiodr=0.6, vadiodd=21.8, vadiodc=0.1).lclip(0)

n9 >> loop("xdrum8", dur=8, sample=PRand(808), drcomp=0.5, tanh=.5)

i7 >> play("<X.>", amp=3.0, lpf=0, lpr=0.7).sometimes("stutter")
i2 >> noloop("beru4", dur=8, sample=1, mverb=0.3, amp=PZero(4), tanh=1, looping=0, trig=0, fx=0)
