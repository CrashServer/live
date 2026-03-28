# svdkdirty # trance
# 134

b6 >> play("X ", amp=3, sample=8)
s3 >> svdk([0,0,3,0, 5,5,3,0], dur=0.25, sus=0.15, oct=4, grit=1,          cutoff=1200, res=0.4, body=0.6, harm=0.6, noise=0.2)
s4 >> svdk([0,0,3,0, 5,5,3,0], dur=0.25, sus=0.15, oct=5, grit=1,          cutoff=1200, res=0.4, body=0.6, harm=0.6, noise=0.2)
~s1 >> svdk([0,0,3,0, 5,5,3,0], dur=0.25, sus=0.15, oct=5, grit=1,          cutoff=1200, res=0.4, body=0.6, harm=0.6, noise=0.2)
s1 >> svdk([0,0,3,0, 5,5,3,0], dur=0.25, sus=0.21, lpf=1200, leg=0, oct=4, grit=1, cutoff=linvar([1300, 2500, 3500, 1500], [2, 6, 8]), res=linvar([0.4, 0.7, 0.1, 1.1, 0.6, 1.3, 0.9], [1, 3, 4, 3, 4, 3]), gdel=0.3, gdeltime=0.5, gdelsize=0.1, gdelsprd=0.5, gdelfb=linvar([0.4, 1.4, 1], [4, 2]), body=linvar([0.3, 1.6, 1.8, 2], [2, 6, 3]), harm=sinvar([0.3, 5.3], 16), noise=linvar([0.3, 1.3, 0.8, 0.3], [4, 3, 4]), csweep=linvar([0.2, 0.3, 0.2, 0.5, 0.1, 0.2], [3, 2, 3, 4, 2]), cswfreq=sinvar([200, 250], 12), cswdepth=linvar([0.4, 0.7, 0.2], 1.5), cswrate=linvar([0.6, 1, 0.1, 0.6], [1.5, 4, 2]), cswdecay=0.5).unison(5)

s2 >> svdk([0], dur=4, sus=4, grit=1.2, low=2, glide=0, noise=0, oct=4, res=0.9, cutoff=1200, body=1, drift=0.1, harm=1.2, slide=0.4)
g2 >> play("[--]", amp=2)
s1.oct=4
s5 >> play("..C.", amp=2)
s4.oct=4
s1 >> svdk([0,0,3,0, 5,5,3,0], dur=0.25, sus=0.21, lpf=1200, leg=0, oct=4, grit=1, cutoff=linvar([1300, 2500, 3500, 1500], [2, 6, 8]), res=linvar([0.4, 0.7, 0.1, 1.1, 0.6, 1.3, 0.9], [1, 3, 4, 3, 4, 3]), gdel=0.3, gdeltime=0.5, gdelsize=0.1, gdelsprd=0.5, gdelfb=linvar([0.4, 1.4, 1], [4, 2]), body=linvar([0.3, 1.6, 1.8, 2], [2, 6, 3]), harm=sinvar([0.3, 5.3], 16), noise=linvar([0.3, 1.3, 0.8, 0.3], [4, 3, 4]), csweep=linvar([0.2, 0.3, 0.2, 0.5, 0.1, 0.2], [3, 2, 3, 4, 2]), cswfreq=sinvar([200, 250], 12), cswdepth=linvar([0.4, 0.7, 0.2], 1.5), cswrate=linvar([0.6, 1, 0.1, 0.6], [1.5, 4, 2]), cswdecay=0.5).unison(5)

