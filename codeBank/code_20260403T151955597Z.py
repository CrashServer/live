
b6 >> play("X.", amp=3, sample=8)
s0 >> svdk([0,0,3,0, 5,5,3,0], dur=0.25, sus=0.15, oct=4, grit=1,          cutoff=1200, res=0.4, body=0.6, harm=0.6, noise=0.7, lofi=0)

z8 >> play("x.", sample=8, amp=3, hpf=60, lpr=.2).sometimes("stutter", PRand(4))

# Server.addFx(dafilter=1200, dastart=250, darel=0.2, darq=0.5, datype=0)
           
i5 >> play()  
  
drop()

s_all.r=0


y2 >> play(pbuild("industrial", kick="X   [Xx] X X   X   "), rate=1)
# y0 >> play(pbuild("breaks", fill=4), lpf=3800)

y1 >> play(pbuild("techno"), lpf=0, sample=7, wshape=0.8, wgain=1, wmix=0.5, amp=2.1)




s4 >> svdk([3,2,5,3, 3,0,3,8], dur=0.25, sus=0.17, oct=5, grit=sinvar([3, 7], 8), cutoff=0,  res=0.6, body=1.0, harm=1.0, noise=1.0, lofi=0)

n2 >> play("i", sample=1, bank=2, dur=var([.5, .75/2, .25], [12, 4]), pan=PWhite(-1,1), )
n3 >> play("..i.", sample=5, bank=2, dur=.5, pan=PWhite(-1,1), wshape=8, wgain=1, wmix=0.5, drcomp=.5, bell=0.5, bellf=3500, bellq=0.9).sometimes("stutter")


~s1 >> svdk([0,1,3,0, 5,5,4,1], dur=0.25, sus=0.15, oct=(5, 5.07), grit=1,          cutoff=1200, res=0.4, body=0.6, harm=0.6, noise=0.2)

s1 >> svdk([0,0,3,0, 5,5,3,0], dur=0.25, sus=0.21, lpf=1200, leg=0, oct=4, grit=1, cutoff=linvar([1300, 2500, 3500, 1500], [2, 6, 8]), res=linvar([0.4, 0.7, 0.1, 1.1, 0.6, 1.3, 0.9], [1, 3, 4, 3, 4, 3]), gdel=0.3, gdeltime=0.5, gdelsize=0.1, gdelsprd=0.5, gdelfb=linvar([0.4, 1.4, 1], [4, 2]), body=linvar([0.3, 1.6, 1.8, 2], [2, 6, 3]), harm=sinvar([0.3, 5.3], 16), noise=linvar([0.3, 1.3, 0.8, 0.3], [4, 3, 4]), csweep=linvar([0.2, 0.3, 0.2, 0.5, 0.1, 0.2], [3, 2, 3, 4, 2]), cswfreq=sinvar([200, 250], 12), cswdepth=linvar([0.4, 0.7, 0.2], 1.5), cswrate=linvar([0.6, 1, 0.1, 0.6], [1.5, 4, 2]), cswdecay=0.5).unison(5)

# s2 >> svdk([0], dur=4, sus=4, grit=1.2, low=2, glide=0, noise=0, oct=4, res=0.9, cutoff=1200, body=1, drift=0.1, harm=1.2, slide=0.4)

g2 >> play("[--]", amp=2)
s1.oct=4
s5 >> play("..C.", amp=2)
s4.oct=4
s1 >> svdk([0,0,3,0, 5,5,3,0], dur=0.25, sus=0.21, lpf=1200, leg=0, oct=4, grit=1, cutoff=linvar([1300, 2500, 3500, 1500], [2, 6, 8]), res=linvar([0.4, 0.7, 0.1, 1.1, 0.6, 1.3, 0.9], [1, 3, 4, 3, 4, 3]), gdel=0.3, gdeltime=0.5, gdelsize=0.1, gdelsprd=0.5, gdelfb=linvar([0.4, 1.4, 1], [4, 2]), body=linvar([0.3, 1.6, 1.8, 2], [2, 6, 3]), harm=sinvar([0.3, 5.3], 16), noise=linvar([0.3, 1.3, 0.8, 0.3], [4, 3, 4]), csweep=linvar([0.2, 0.3, 0.2, 0.5, 0.1, 0.2], [3, 2, 3, 4, 2]), cswfreq=sinvar([200, 250], 12), cswdepth=linvar([0.4, 0.7, 0.2], 1.5), cswrate=linvar([0.6, 1, 0.1, 0.6], [1.5, 4, 2]), cswdecay=0.5).unison(5)
