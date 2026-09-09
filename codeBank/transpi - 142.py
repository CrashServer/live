# transpi - 142
Clock.bpm=142
Scale.default="minor"
Root.default=0

t1 >> play("l(...o)", bank=1, cut=0.2, fbdelay=0.5, fbtime=0.25, fbfeed=0.6, fbcutoff=3000, fbspread=0.02, beat_dur=1, amp=.8, hpf=90, pan=PWhite(-1,1))

l9 >> play("x.", lpf=0, amp=1.2, sample=9)
s9 >> play("..C.", sample=(0,3), room2=0.3, mix2=0.2, damp2=0.8, revatk=0.4, revsus=1, hpf=400).sometimes("stutter")
c5 >> play("-").often("stutter", PRand(8), pan=PWhite(-1,1))

# q5 >> loop("rock32", dur=32, sample=2, sbrk=0.5, t_reset=0, sbrkdur=0.125, sbrkmix=1.0, drcomp=.2)
v1 >> lbass(var([4, 12, 9, 8, 7], [8,8,8,4,4]), dur=1/2, oct=4, rq=0.6, cutoff = PFr(2250,3250), tone=0.16, tape=0.3, tapedrive=0.9, tapewarm=0.7, tapewobble=0.1)

e8 >> a_daftlead(P[4,4, [19, 19, 18,18, 16,16, 15,14], 4,4, [19, 19, 18,18, 16,16, 15,14], 4, [19,19, 18,18, 16,16, 15,14]],  dur=P[1/2], oct=(4,5), rate=0.4, r=[0.7, 0.7, 1.2, 0.7, PWhite(1,2)], cutoff=2400, resonance=0.2, filterEnv=0.3, drive=0.6, mverb=0.4, glide=0, glidedur=0.05, eb=0.5, ebfeed=0.5, ebmix=0.3, ebmode=2, ebwow=0.1, ebflutter=0.15, ebsat=0.3) # + (0, -2)


