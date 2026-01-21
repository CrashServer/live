#  insaneOnSixtyFour 172
# banger, chaosBits

Clock.bpm=172
Scale.default="minor"
Root.default="D"
cyH = 64
cyL = 64

l1 >> loop("wardrum16", dur=16,sample=var(PRand([18,23]), [cyH]),drcomp=.5, amp=var([0.5, 1], [cyH, cyL]), hpf=120)
~l2 >> loop("rockriff_16", dur=16, sample=2, low=1, chop=var([0,P*[2,4,8]], [cyH, cyL]), chopi=var(PRand([0, .25, .5, .75]), [32]), mid=1.2, hpf=0)

l3 >> loop("gscreechvar16", dur=16, sample=PRand(55), hpf=var([0, 7000], [cyH, cyL]), mverb=.3)
d1 >> play("X", amp=Pvar([P[1,0],PTimebin()], [cyH, cyL]), mid=2).sometimes("stutter")
d2 >> play("{---=}", rate=PFr(1.0,3.0), pan=PWhite(-1,1)).sometimes("stutter", PRand(15))

d3 >> play("..o.", sample=6, high=1, amp=1.5).sometimes("stutter", 4)

l2.filename="metalgtr16"
l2.sample=5;
l2.room=0.7
l2.dafilter=var(PRand(400, 1200),16)

# optionnal 
l4 >> loop("jungleboy16", dur=16,sample=var(PRand(404), [cyH]), hpf=500, drcomp=var([0, .5],[cyH, cyL]))
s1 >> rave(Pvar([var([14,18],[15,1]), PSaw(cyH*2)*14], [cyH, cyL]), dur=var([1/2,1],[15,1]), glide=PWhite(0.0,2.0), oct=(5,4,5), eb=0.25, ebfeed=0.5, ebmix=0.3, ebmode=1, ebwow=.56, ebflutter=125, ebsat=0.6, hpf=500, high=2).unison(3)

# Server.addFx(dafilter=1200, dastart=50, darel=1, darq=0.5, datype=0, sus=1) ## trigger once cause sus

## Voice
h7 >>loop("oldies8", dur=8, drcomp=.5, drive=0, wshape=0,  wgain=1, wmix=0.5, sample=14, rate=0.8, eb=0.75, ebfeed=0.5, ebmix=0.3, ebmode=1, ebwow=15, ebflutter=150, ebsat=0.3, amp=PZero(8,7)*2)
m3 >> loop("ragegrowl16", dur=16, sample=(PRand(44),PRand(66)), amp=Pvar([P[1,0],P[0]], [cyH, cyL]), eb=0.25, ebfeed=0.5, ebmix=0.3, ebmode=1, ebwow=.15, ebflutter=150, ebsat=0.3, mverb=.2, high=2, hpf=120)
