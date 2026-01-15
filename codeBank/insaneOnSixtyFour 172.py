#  insaneOnSixtyFour 172
# banger

Clock.bpm=172
Scale.default="minor"
Root.default="D"

l1 >> loop("wardrum16", dur=16,sample=var(PRand([18,23]), [32, 32]),drcomp=.5)
~l2 >> loop("rockriff_16", dur=16, sample=2, low=1, chop=var([0,P*[2,4,8]], [64, 64]), chopi=var(PRand([0, .25, .5, .75]), [32]), mid=1.2)
l3 >> loop("gscreechvar16", dur=16, sample=PRand(55), hpf=var([0, 7000], [64]), mverb=.3)
d1 >> play("X", amp=Pvar([P[1,0],PTimebin()], [64])).sometimes("stutter")
d2 >> play("{---=}", rate=PFr(1.0,3.0), pan=PWhite(-1,1)).sometimes("stutter", PRand(15))

d3 >> play("..o.", sample=6, high=1, amp=1.5).sometimes("stutter", 4)
l2.filename="metalgtr16"
l2.sample=5
l2.dafilter=var(PRand(400, 1200),16)

# optionnal 
# l3 >> loop("junglebouncy16", dur=16,sample=var(PRand(404), [64]), high=2)
# s1 >> rave([PSaw(128)*14], dur=1/2, glide=2, oct=(5,4,5), eb=0.25, ebfeed=0.5, ebmix=0.3, ebmode=1, ebwow=.56, ebflutter=125, ebsat=0.6, hpf=400, high=2).unison(3)
# Server.addFx(dafilter=1200, dastart=50, darel=1, darq=0.5, datype=0)
