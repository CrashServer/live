#  darkChill  92
# interlude

Clock.bpm=92
Scale.default="minor"

d6 >> play("8..(8.)", dur=1, wshape=5, wgain=1, wmix=0.5, stereowidth=1, swfreq=100, swnarrow=1.5, swwide=1.5)

u9 >> play(".(.{..u})u.", sample=6, dur=1, rate=[1.43,-.4], mverb=.5, hpf=400, fbdelay=[0.5], fbtime=0.25, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1).human(20, 10,5)
t0 >> play("d", dur=1/2, amp=[1, PFr(0.2,1)], rate=PWhite(1,3), pan=PWhite(-1,1), mverb=.2).human(50,0, 15).often("stutter", PRand(16))

m0 >> cbass(var([0, -2, -4], [32]), dur=8, cutoff=PRand(180,415), rq=0.9, boost=1.5, detune=0.01, follow=2, slide=PWhite(0,3), slidedelay=0.5, hpf=60).unison(2)

o9 >> viola([6,3,P*[4,2,5]], dur=[P*[2,4,8], P*[2,4],P*[8,12]], beat_dur=1, rate=1, mverb=0.8, a=0.75, blur=2, lpf=PRand(1200,3000), hpf=300, amp=0.6).unison(2) + (-7,PStep(5, 7,0))

r3 >> loop("breakcore160_16", dur=8, sample=var(PRand(66), [64, 64]),sbrk=P*[0.5,1,1.5], sbrkdur=P*[0.5,1,4], sbrkmix=.5, hpf=200, high=2, vol=0.8, drcomp=.5)

f8 >> play(P["xx...x..[.x]x...x.."].replace("x", "x"), dur=1/2, sample=9)
f9 >> play(P["..U[.U][.U]..U[.U].U[.U][.U]..U"], dur=1/2, sample=9, fbdelay=0.5, fbtime=0.125, fbfeed=0.7, fbcutoff=3000, fbspread=0.02, beat_dur=1).sometimes("stutter", PRand(4,16), fbfeed=PWhite(.7, .9))

j1 >> tb305(P[1, 9, 8, 11, 11, 8, 0, 11, 8, 5, [9,_], 9, 7, 4, 8, 12],oct=var([5,6],[20,Prand(2,12)]), dur=1/4, cutoff=linvar([30,500], [88]), rq=PFr(0.2, .9), wave=linvar([0.1,0.9],[55]),beef=1, envmod=linvar([10,100], [64, 64]), eb=0.5, ebfeed=0.5, ebmix=0.3, ebmode=0, ebwow=0.1, ebflutter=0.15, ebsat=0.3)

e0 >> play("X", amp=2, transient=1.0, transattack=2, transsustain=.5, transtime=0.02).sometimes("stutter")

o9.stop()
j5 >> play("j", dur=16, sample=PRand(404), mverb=.1, wshape=3,rate=0.9, drcomp=.5, amp=2, hpf=300, high=2).unison(2,.125,40,.5 )