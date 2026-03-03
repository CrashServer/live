# biases_are_bells 124
# trance

Clock.bpm = 122;
d1 >> play("x", amp=Pacc(3, 8), sample=5, dur=1/4, resonbank=0.2, rbfreq=[47, 50, 50, 57, 50, 62, 69], rbdecay=[0.6, 0.2, 0.6, 0.6, 0.6, 0.7, 0.2], pong=0, rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, dfdec=0.1, dftone=2, lpf=0, lpr=0.1).unison(4)
                  
d1 >> play("x", amp=Pacc(5, 8), sample=5, dur=1/4, resonbank=0.2, rbfreq=[47, 50, 50, 47, 50, 62, 69], rbdecay=[0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.2], rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, dfdec=0.6, high=1, dftone=2, lpf=0, lpr=0.1).unison(4)   

# dfdec >> 0.2 > 0.7                  
d1 >> play("x", amp=Pacc(4, 8), sample=5, dur=1/4, resonbank=0.2, rbfreq=[47, 50, 50, 47, 50, 62, 69], rbdecay=[0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.2], rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, dfdec=0.7, dftone=2, lpf=linvar([2000, 4000], [32,0]), lpr=0.1).unison(4)                   
               
d1 >> play("x", amp=Pacc(4, 8), sample=5, dur=1/4, resonbank=0.2, rbfreq=[47, 50, 50, 47, 50, 62, 69], rbdecay=[0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.2], rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, dfdec=0.7, dftone=2, lpf=0, lpr=0.1).unison(4)   
                  
d4 >> play("x", dur=0.5, mverb=1, rate=2, mverbmix=0.5, mverbdamp=0.8, mverbdiff=0.625, mverbfreeze=0, cheapverb=PBin(8), cvdecay=1.5, cvdamp=0.5, amp=Pacc(6, 4), amplify=PLife(0.5), hpf=3200, echo=0.25, sample=6, resonbank=0.1, rbfreq=36, rbdecay=0.5, rbspread=1, glitch=0.5, glitchrate=8, glitchdepth=0.5, glitchcrush=0.3, glitchchance=0.5, beat_dur=1)    
                  
d8 >> play(".-u-", dur=0.25, amp=Pacc(4))
d6 >> play("..U:", rfreq=8000, resonz=0.4, fbdelay=0.5, fbtime=0.25, fbfeed=0.5, fbcutoff=3000, fbspread=0.11, rgate=0.5, rgaterate=4, rgatewave=0, beat_dur=1)
                                   
d1 >> play("x", amp=Pacc(3, 8), sample=5, dur=1/4, resonbank=0.8, rbfreq=[47, 50, 50, 47, 50, 62, 69], rbdecay=[0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.2], rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, dfdec=0.7, dftone=3, lpf=linvar([2000, 4000], [32,0]), lpr=0.1).unison(4)

d3 >> play("s", dur=0.5, sample=2, amp=0.56, amplify=PFDur((3,8),(5,16)), octclean=0.4, ocsub=0.7, ocup=0, hpf=100, lpf=4000, delay=PSwing(0.06))

d5 >> play("-", dur=0.25, sample=2, amp=0.9, amplify=PEuclid(7,16), hpf=6000, cheapverb=0.7, cvdecay=3, cvdamp=0.3, pan=0.3)

d1 >> play("x", amp=Pacc(3, 8), sample=5, dur=1/4, resonbank=0.8, rbfreq=[47, 50, 50, 47, 50, 62, 69], rbdecay=[0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.2], rbspread=(1, var([1, 2, 3], [12, 2, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, rate=1, dfdec=0.7, dftone=3, lpf=linvar([2000, 4000], [32,0]), lpr=0.1).unison(3)

d1 >> play("x", amp=Pacc(3, 8), sample=5, dur=1/4, resonbank=0.8, rbfreq=[47, 50, 50, 47, 50, 62, 69], rbdecay=[0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.2], rbspread=(1, var([12, 2, 6], [12, 12, 2])), dynfuzz=0.1, dfgain=1, dfatk=0.015, dfdec=0.7, dftone=3, lpf=linvar([2000, 4000], [32,0]), lpr=0.1).unison(3)
                                   
d7 >> a_hhat(tone=8000, metallic=1, distortion=2, open=1)               
                  
Server.addFx(hpf=0)

k4 >> play("K ", sample=7, amp=2)
                  
d1.dur=8
