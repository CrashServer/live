Clock.bpm = 110
Scale.default = Scale.chromatic
Root.default = "C"



d2 >> faim([2,2,4,5,5,2], dur=[1,1/2,1/2,1/2,1,1/2], oct=[4,5,5,4,4,5], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=0.5, tapedrive=1.5, tube=0.4, tubegain=1.5, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)


d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,3,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)


d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,3,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, resonbank=0.8, rbfreq=var([300, 400, 500, 600, 650, 700, 800, 820, 1200], 8), rbdecay=0.5, rbspread=1.0, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)

d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,3,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=3.1, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400, (400, 550)], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5, beef=2, leg=4)

~d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[5,6,5,5,6,5], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=0.1, tube=0.8, tubegain=1.9, echo=0.5, f=0.9, resonbank=0.8, rbfreq=var([300, 400, 600], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=var([0.1, 0.2, 0.5, 0.8, 1, 2]), tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)


#disto
# ~d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=3.1, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=var([0.1, 0.2, 0.5, 0.8, 1, 2]), tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2, beef=2, rate=2)
# d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=1.1, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5, beef=4)
d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=var([1.1, 2, 4, 8, 16], 8), tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
~d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,3,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=PWhite(0.1, 0.9), tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)


l2 >> dbass(d2.degree, dur=1/4, shape=0, amp=4, valad=1500, valadr=1, valadd=5, valadt=0, valadc=0.2)
~d2 >> faim([2,2,4,5,5,2], dur=1/4, oct=[4,5,5,4,5,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)

~d3 >> cbass([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[5,5,5,6,6,6], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=var([1.1, 2, 4, 8, 16], 8), tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)

ag.stop()
x9 >> play("x-o-", dur=1/4, amp=4, rate=1, sample=8, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1)

~d2 >> faim([2,2,4,5,5,2], dur=1/1, oct=[4,5,5,4,5,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
~d2 >> faim([2,2,4,5,5,2], dur=1/4, oct=[6,6,6,4,6,5], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
l2 >> dbass(d2.degree, dur=1/4, shape=0, amp=4, valad=1500, valadr=1, valadd=5, valadt=0, valadc=0.2, oct=6)

l2.oct=6
d3.oct=7
d2.oct=3


~d2 >> faim([2,2,4,5,5,2], dur=1/1, oct=[4,5,5,4,5,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)

d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=var([1.1, 2, 4, 8, 16], 8), tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)

d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=16, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
~d2 >> faim([2,2,4,5,5,2], dur=1/4, oct=[4,7,5,6,5,6], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d2 >> faim([2,2,4,5,5,2], dur=[1,1,2,2], oct=[5,5,4,5], vadiod=2500, vadiodr=0.6, vadiodd=2.4, subenh=1, subhfreq=120, subhgain=2, vadiodc=0.5, tape=0.4, tapedrive=0.6, tube=0.3, tubegain=1.2, cheapverb=0.8, cvdecay=0.85, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4]), amp=linvar([0.6,1.2],32)).every(8,"stutter",2,rate=0.5)

d3.stop()
x9.stop()
l2.oct=5
l2.fbdelay=0.5
l2.leg=4
l2.low=0
Root.default = "G"
d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.0, tapedrive=1.4, tube=0.6, tubegain=1.6, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=linvar([1500,5000],32), fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.7, tapewobble=0.2, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
l2 >> dbass(d2.degree, dur=1/4, shape=0, amp=4, valad=1500, valadr=1, valadd=5, valadt=0, valadc=0.2, oct=5)

d2 >> faim([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[4,5,4,4,5,4], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=var([1.1,2,4,8,16],8), tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300,400,600],8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
~d2 >> faim([2,2,4,5,5,2], dur=1/4, oct=[4,5,6,4,5,6], vadiod=1500, vadiodr=0.4, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=2, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.5, fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=0.1, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5, beef=0)

Scale.default = Scale.minorPentatonic
d3.stop()
~d2 >> faim([2,2,4,5,5,2], dur=1/4, oct=3, vadiod=1500, vadiodr=0.2, vadiodd=1.8, subenh=1, subhfreq=100, subhgain=1, vadiodc=0.5, tape=1.2, tapedrive=2.2, tube=5, tubegain=1.9, echo=0.5, fbdelay=1, fbtime=0.5, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=0.5, tapewobble=0.1, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5, beef=0)

~d3 >> cbass([2,2,4,5,5,2], dur=([1,1/2,1/2,1/2,1,1/2], 1/4), oct=[5,5,5,6,6,6], vadiod=45500, vadiodr=0.9, vadiodd=1.8, subenh=1, subhfreq=400, subhgain=1, vadiodc=0.5, tape=1.6, tapedrive=var([1.1, 2, 4, 8, 16], 8), tube=0.8, tubegain=1.9, echo=0.5, fbdelay=0.9, resonbank=0.8, rbfreq=var([300, 400], 8), rbdecay=0.8, rbspread=1.0, fbtime=0.5, fbfeed=0.7, fbcutoff=6000, fbspread=0.22, beat_dur=1, tubewarm=0.6, tubebias=4, tapewarm=1.4, tapewobble=0.6, shape=var([0,0.1],[28,4])).every(8,"stutter",2,rate=0.5)
d2.oct=4
