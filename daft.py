# daft 105
# todo

### ===== DAFT PUNK — Harder Better Faster Stronger =====
Clock.bpm = 105
Scale.default = Scale.major
Root.default = "C#"
d1 >> a_daft([1,1,5,4,1,1,4,3,3,3,2,1,3,3,5,4,1,3,4,3,1,3,4,3,5,4,3,3,1,0,1,3,1,1,3,1,3,5,3,1,3,0,0,3,0,4,3,2,3,6,6,1,6,4,3,1,6,5,5,1,3,1,1,1,1], dur=1/4, sus=1/2, rate=12, cutoff=var([800, 1200, 1300, 4000, 1600, 3200], 8), resonance=0.1, punch=2, oct=PStutter([5,6,5,6,5,6,5,6,5,6,5,7,5,6,4],[2,6,2,4,6,13,2,6,2,6,2,6,2,2,4]), shapemix=1).unison(3).every(16,"stutter",4)
v0 >> compkick(tone=4.0, noise=3.0, comp=1, drive=0.2, ring=1, metal=3.5, body=0.4, bend=1.3, dur=1/4)


### ===== DAFT PUNK — Around the World =====
Clock.bpm = 123
Scale.default = Scale.mixolydian
Root.default = "D"

d2 >> a_daft([4,4,4,4,5,6,6,6,6,0,1,1,1,1,2,1,0,5,5,4,3], cutoff=linvar([2000, 6000], 32), fbdelay=0.5, fbtime=0.25, fbfeed=0.7,  fbcutoff=3000, fbspread=0.02, beat_dur=1, dur=PStutter([1,1/2,1/4,3/2,1,1/2,1/4,3/2,1,1/2,1],[3,1,1,1,2,1,1,1,3,6,1]), sus=PStutter([1/2,1/4,1/2,1/4,1/2,1/4,1],[4,1,4,1,4,6,1]), oct=PStutter([5,6,6],[5,12,4]), mverb=0.1).unison(4)
d2 >> a_daft([4,4,4,4,5,6,6,6,6,0,1,1,1,1,2,1,0,5,5,4,3], cutoff=linvar([2000, 6000], 32), fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, dur=PStutter([1,1/2,1/4,3/2,1,1/2,1/4,3/2,1,1/2,1],[3,1,1,1,2,1,1,1,3,6,1]), sus=PStutter([1/2,1/4,1/2,1/4,1/2,1/4,1],[4,1,4,1,4,6,1]), shape=sinvar([0,0.4],16), oct=PStutter([5,6,6],[5,12,4]), mverb=0.1).unison(4)
d3>> varsaw([3,2,3,3,4,3,2,3,5,3], dur=PDur(10,16)*2, vocod=2, voccarr=0.5, vocbw=0.7, vowel=1, vowelf=5, vowelq=3) 


### ===== DAFT PUNK — Da Funk =====
Clock.bpm = 111
Scale.default = Scale.dorian
Root.default = "C"
d4 >> a_daft([4,3,4,6,1,0,1,3,6,5,6,1,4,5,6], dur=PStutter([2,1/2,3,1/2,3,1/2,3,1],[1,3,1,3,1,3,1,2]), sus=PStutter([3/2,1/4,2,1/4,2,1/4,2,3/4],[1,3,1,3,1,3,1,2]), oct=PStutter([5,4,5,4],[8,3,1,3]), mverb=0.2, sgate=0.5, sgthresh=1, sgmode=0, rgate=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, rgaterate=4, rgatewave=0).unison(3)
d5 >> a_daft([4,3,4,6,1,0,1,3,6,5,6,1,4,5,6], dur=PStutter([2,1/2,3,1/2,3,1/2,3,1],[1,3,1,3,1,3,1,2]), sus=PStutter([3/2,1/4,2,1/4,2,1/4,2,3/4],[1,3,1,3,1,3,1,2]), oct=PStutter([6,5,6,5],[8,3,1,3]), cutoff=4000)
b1 >> play("x", sample=4, dur=[1/2,3/4,3/4,1,1], sus=1/2, dist=0.0).unison(3)
d4 >> a_daft([4,3,4,6,1,0,1,3,6,5,6,1,4,5,6], dur=PStutter([2,1/2,3,1/2,3,1/2,3,1],[1,3,1,3,1,3,1,2]), sus=PStutter([3/2,1/4,2,1/4,2,1/4,2,3/4],[1,3,1,3,1,3,1,2]), oct=PStutter([5,4,5,4],[8,3,1,3]), mverb=0.2, sgate=0.5, sgthresh=1, sgmode=0, rgate=0.5, fbdelay=0.5, lpf=var([800,4000,800,2000],[16,8,8,16]), fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, rgaterate=4, rgatewave=0).unison(3)
p2>>faim(4, dur=1/2, sus=1, oct=3, tanh=0.4, tanhmix=0.5) 


### ===== DR. DRE — Still D.R.E. =====
Clock.bpm = 96
Scale.default = Scale.major
Root.default = "C"
d1 >> dbass(Pvar([(0,5),P[(0,5),(6,4)],(6,4)],[5,1,2]), dur=1/2, rate=0.5, oct=PStutter([5,4],[11,5])).unison(3)
d2 >> dbass([4,5,6,2], dur=[1,3], sus=[1,3/4], oct=[6,6,6,7])
d3 >> plaitsX(Pvar([(0,5),P[(0,5),(6,4)],(6,4)],[5,1,2]), dur=1/2, oct=PStutter([6,4],[11,5]))
d1 >> cs80(Pvar([(0,5),P[(0,5),(6,4)],(6,4)],[5,1,2]), tape=var([0,0.3],32), dur=1/2, oct=PStutter([5,4],[11,5])).unison(2,0.01)
~v4 >> compkick(dur=PDur(3,8), comp=1, body=0.6)
Root.default=var([0,-2,5],16)


### ===== METALLICA — Enter Sandman =====
Clock.bpm = 110
Scale.default = Scale.chromatic
Root.default = "C"
d2 >> faim([2,2,4,5,5,2], dur=[1,1/2,1/2,1/2,1,1/2], oct=[4,5,5,4,4,5], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=0.5, tapedrive=1.5, tube=0.4, tubegain=1.5, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,3,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,3,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, resonbank=0.8, rbfreq=var([300, 400, 500, 600, 650, 700, 800], 8), rbdecay=0.5, rbspread=1.0, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,3,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=3.1, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400, (400, 550)], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=3.1, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400, 800], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=var([0.1, 0.2, 0.5, 0.8, 1, 2]), tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=1.1, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=1.1, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400, 800, 600, 700], P*[1, 2, 4, 8]), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=var([1.1, 2, 4, 8, 16], 8), tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=16, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400, 600], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=1200, subhgain=1, leg=8, vadiodc=0.5, tape=1.6, tapedrive=32, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=6, tapewarm=1.8, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
~d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[5,6,5,5,6,5], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=0.1, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400, 600], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=var([0.1, 0.2, 0.5, 0.8, 1, 2]), tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)

~d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,3,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
# p3 >> loop("metaldrum32", dur=16, amp=4, sample=PRand(8), sbrk=0.1, tube=0.5, tubegain=1.5, tubewarm=0.6, tubebias=0.1)
~d2 >> faim([2,2,4,5,5,2], dur=1/4, oct=[4,5,5,4,5,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
p3 >> loop("quake8", dur=8, amp=8, sample=PRand(8))
~d2 >> faim([2,2,4,7,5,2], dur=1/4, oct=[4,5,5,4,5,4], vadiod=4500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1, tapedrive=2, tube=0.8, tubegain=1.9, echo=0.25, fbdelay=0.5, fshift=4, fphase=0, fmix=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=1.7, tubebias=0.1, tapewarm=0.5, tapewobble=1.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d3 >> cbass([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[5,5,5,6,6,6], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=var([1.1, 2, 4, 8, 16], 8), tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)

x9 >> play("X-o-", dur=1/4, amp=4, rate=1, sample=18, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1)

~d2 >> faim([2,2,4,5,5,2], dur=1/1, oct=[4,5,5,4,5,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)

# d3 >> fbass([2,2,4,5,5,7], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[5,5,5,6,6,6], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=0, vadiodc=0.5, tape=1.6, tapedrive=var([1.1, 2, 4, 8, 16], 8), tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400, 800], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)

x9 >> play("[.].X.", dur=1/4, amp=4, rate=1, sample=18, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1)

d2 >> faim([2,2,4,5,5,2], dur=[1,1/2,1/2,1/2,1,1/2], oct=[4,5,5,4,4,5], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=0.5, tapedrive=1.5, tube=0.4, tubegain=1.5, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5).only()






#d3 >> vati(PRand([0,(7,2),(6,1),4,6,7,9,11]), dur=PRand([1,1/2]), oct=4, beef=1).unison(3)


### ===== JUSTICE — Shrine (Ultima VII) =====
Clock.bpm = 80
Scale.default = Scale.mixolydian
Root.default = "D"
d1 >> cbass([0,5,2,5,0,5,6,4,1,4,6,4], dur=1/2, oct=[6,5], amp=0.5).unison(3)
d2 >> cbass([(5,0,2),(4,6,1)], dur=3, sus=2, amp=0.5, follow=4)
d3 >> cbass([0,5,2,5,0,5,6,4,1,4,6,4], dur=1/2, oct=[5,6], amp=0.7)
d4 >> cbass([5,6,0,1,2,3,3], dur=PStutter([1/2,4,2],[5,1,1]), sus=[1/2,1/2,1/8,1/8,1/2,1/8,2], oct=[6,7,7,7,7,7,7], amp=0.5)
b1 >> cbass([2,2,4,1,1,3,5,6,0,1,2,4,5,6,0,1,2,2,3,1,1,4,5,6,0,1,2,3,4,5,4,3,2,0], dur=PStutter([2,1/2,2,1/2,1,1/2,1,2,1/2,2,1/2,1,1/2,1/4,2],[1,2,1,6,1,4,1,1,2,1,8,2,1,2,1]), sus=PStutter([1/2,1/8,1,1/2,1/8,1,1/2,1/8,1/2,1,1/2,1/8,2],[8,2,1,2,2,1,8,2,2,2,1,2,1]), oct=PStutter([7,5,6,5,6,7,5,6],[6,1,4,2,3,6,1,11]), amp=0.5)
b2 >> tb304([5,6,0,1,2,4,5,6,0,1,2,2,3,1,1,4,5,6,0,1,2,3,4,5,4,3,2,0], dur=PStutter([1/2,1,1/2,1,2,1/2,2,1/2,1,1/2,1/4,1/3,2],[4,1,4,1,1,2,1,8,2,1,1,1,1]), sus=PStutter([1/2,1/8,1,1/2,1/8,1,3/4,1/2,1/8,1/2,1,1/2,1/8,2],[2,2,1,2,2,1,6,2,2,2,2,1,2,1]), oct=PStutter([4,5,4,5,7,4,5,6],[1,4,2,3,6,1,10,1]), amp=0.5)
p1 >> pluck([0,0,2,6,6,1,0,0,1,6,6,1], dur=[2,1/2,1/2], sus=1/2, oct=6, amp=0.25)


### ===== JUSTICE — Valentine (Gesaffelstein vibe) =====
Clock.bpm = 105
Scale.default = Scale.major
Root.default = "C#"
d1 >> pluck(Pvar([P[(1,1,3),(1,3),(1,3),(1,3),(0,0,2),(0,2),(0,1),(0,1),(4,6,1),(6,1)],(6,1),P[(5,5,0),(5,0)],(5,0),P[(3,5,0),(5,0)],(5,0)],[5,3,1,3,1,11]), spring=0.2, sprdecay=1.5, sprdamp=0.5, sprtens=0.5, dur=1/2, sus=PStutter([2,1/4,2,1/4,4,1/4,4,1/4,4,1/4],[1,3,1,3,1,7,1,7,1,7]), oct=PStutter([4,5,4,5,3,5,3,4,3,4],[1,3,1,3,1,7,1,7,1,7])).unison(3)
d2 >> dbass([3,2,3,4,5,4,5,3,4,3,2,3,4,5,1,2,3,1,5,0,5,0,5,5,5,5,3,2], dur=[2,1/4,2,1/4,2,2,3/2,2,1/4,4,8,2,1/4,3/2,1/4,1/4,3/2,3,1/4,1/4,3/2,3/2,1/2,1/4,1/4,1,2,1/4], sus=1/4, oct=PStutter([5,4,5,6,5,6,5,6,5],[6,1,7,4,1,1,1,1,6])).unison(3)

### ===== JUSTICE — Phantom =====
Clock.bpm = 120
Scale.default = Scale.mixolydian
Root.default = "C"
d1 >> pianovel(PStutter([1,4,5,6,5,6],[8,1,3,1,5,1]), dur=[1,1,1,1,1,1,3/4,1/2,3/4,1,1,1/4,3/4,1,1,1,3/4,1/2,3/4], oct=4)
d2 >> pianovel(PStutter([1,4,5,6,5,6],[8,1,3,1,5,1]), dur=[1,1,1,1,1,1,3/4,1/2,3/4,1,1,1/4,3/4,1,1,1,3/4,1/2,3/4], oct=4)
d3 >> bbass([5,3,1,5,1,3,5,1,3,1,5,3,1,3,1,5,2,0,5,0,2,5,0,2,0,5,2,0,5,0,2,5,2,0,5,2,0,5,2,0,5,2,0,5,2,0,5,2,4,2,0,4,2,0,4,2,0,4,2,0,4,2,0,4], dur=1/4, oct=PStutter([6,5,6,7,6,5,6,5,6,7,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6],[3,1,3,3,5,1,2,1,3,3,3,1,2,1,2,1,2,1,2,1,2,1,2,1,17]))
d2 >> dbass(PStutter([1,4,5,6,5,6],[8,1,3,1,5,1]), dur=[1,1,1,1,1,1,3/4,1/2,3/4,1,1,1/4,3/4,1,1,1,3/4,1/2,3/4], oct=5, drive=0.1).unison(3)
d3 >> a_gesa([5,3,1,5,1,3,5,1,3,1,5,3,1,3,1,5,2,0,5,0,2,5,0,2,0,5,2,0,5,0,2,5,2,0,5,2,0,5,2,0,5,2,0,5,2,0,5,2,4,2,0,4,2,0,4,2,0,4,2,0,4,2,0,4], dur=1/4, oct=PStutter([6,5,6,7,6,5,6,5,6,7,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6],[3,1,3,3,5,1,2,1,3,3,3,1,2,1,2,1,2,1,2,1,2,1,2,1,17]))
d1 >> a_gesa(PStutter([1,4,5,6,5,6],[8,1,3,1,5,1]), dur=[1,1,1,1,1,1,3/4,1/2,3/4,1,1,1/4,3/4,1,1,1,3/4,1/2,3/4], oct=7)
~g2 >> a_xbass(PStutter([1,4,5,6,5,6],[8,1,3,1,5,1]), dur=[1,1,1,1,1,1,3/4,1/2,3/4,1,1,1/4,3/4,1,1,1,3/4,1/2,3/4], oct=5, drive=0.1).unison(3)

### ===== DEVO — Gut Feeling =====
Clock.bpm = 148
Scale.default = Scale.major
Root.default = "C"
d1 >> dbass([2,4,0,5,1], dur=4, oct=[4,4,5,4,5]).unison(3)
d2 >> tb304(PRand([0,1,2,3,4,5,6]), dur=PRand([1,1/2,3/2]), sus=3/2, oct=PRand([3,4,5]))
d3 >> tb305([2,4,0,5,1], dur=4, oct=4)
b1 >> faim([(2,4),(4,6),(4,0),(2,5),(5,1)], dur=4, oct=5)
b2 >> cs80([(2,6),(4,6),(4,0),(2,0),(5,1),(6,2),(6,1),(0,2),(0,2),(1,3),(2,4),(1,4),(2,4),(5,5),(1,5)], dur=4, oct=PStutter([5,6,5,6],[7,6,1,1]), fatk=0.75, fdec=0.5, fsus=0.4, frel=1.0, cutoff=200, detune=0.002, vibspeed=0.1, vibdepth=0.004, glide=0.8, glidedur=0.015)
p1 >> faim(Pvar([(1,1),P[(1,1),(0,0)],(0,0),(1,1)],[1.5,1,1.5,4]), dur=PStutter([1/2,1/4,1/2,1/4,1/2,1/4,1/2,1/4,1/2,1/4],[1,1,1,1,2,1,1,1,5,8]), sus=PStutter([1/2,1/4,1/2,1/4],[1,4,1,16]), oct=6)
p2 >> pluck(PwRand([(1,1),(0,0),(2,6)],[247,75,1]), dur=PRand([1/2,1/4]), sus=1/4, oct=[3,5])
d4 >> faim(Pvar([P[2,4,0,5,1,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,1,1,1],P[1,1,1,1,1,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,1,1,1]],[37.5,580]), dur=PStutter([4,1/2,1/4],[5,1199,1]), sus=PStutter([1/2,1/4],[5,1200]), oct=7)
