# Tie fight

o1 >> 

\          /
  \oo/
  /oo\
/          \

<<!oo!>>

# m8 >> blip(PTime(), dur=1/4, valad=500, valadr=0.3, valadd=5, valadt=0, valadc=0.2, detune=0.01, tone=1.0, beef=0.9, fdecay=1, mod=0.8, fx2=1, fx1=1, scale=Scale.chromatic, vol=var([0,1],[PRand(32)], 4))

# m8 >> guit(PTime(), dur=1, valad=3000, valadr=0.3, valadd=5, valadt=0, valadc=0.2, detune=0.01, tone=1.0, drift=0.5, rgate=1.5, beef=0.9, fdecay=1, mod=0.8, fx2=1, fx1=1, scale=Scale.chromatic, amp=var([0,1],[PRand(16), 4]))


# d3 >> eeri(rate=-4, glitch=1.4, glitchrate=1, glitchdepth=4, glitchcrush=5.0, glitchchance=0.9, beat_dur=1, tape=1, tapedrive=2.1, tapewarm=0.5, tapewobble=2.8, dur=4, sbrk=0.4, valad=500, valadr=0.3, valadd=5, valadt=4, valadc=0.2, hpf=300, fshift=2, fphase=0, fmix=0.5, xbitrot=0.5, rotbits=8, rotrate=0.5, rotjitter=0.1)
# l4 >> play('X ', amp=2)
# g3 >> play(PRand("Xx.G.xGg.xx.G[gg]x.x"), sample=10, tape=0.5, tapedrive=1.5, tapewarm=0.5, tapewobble=0.1, freeze=[0, 0, 1, 0])
# l3 >> loop("drumglitch32", pos=0, cut=0, dur=32, sample=12)
# u7 >> loop("ragedrum32",PRand(33), dur=32, sample=4, drcomp=.5, tape=0.5, tapedrive=1.5, tapewarm=0.5, tapewobble=121, amp=PFr(0,1)*4, ring=1.3, ringl=500, ringh=3500).lclip(2)
j1 >> play("UU", rate=[-2,1], eb=0.5, ebfeed=0.5, ebmix=0.3, ebmode=2, ebwow=0.1, ebflutter=0.15, ebsat=0.3, amp=4, dur=4, mverb=0.8, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=1, echo=P*[0.5,.25, .125], echomix=0.5, beat_dur=1, echotime=1)
o6 >> play("3", rate=0.4, dur=8,fx1=1)
lo.stop(32)
u7.stop(32)
m8 >> guit(PTime(), dur=1/4, valad=500, valadr=0.3, valadd=5, valadt=0, valadc=0.2, detune=0.01, tone=1.0, beef=0.9, fdecay=1, mod=0.8, fx2=1, fx1=1, scale=Scale.chromatic, vol=var([0,1],[PRand(32), 4]))
