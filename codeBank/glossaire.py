# glossaire
# tutorial

####### Glossaire FoxDot #######

#### General #####
p1 >> pluck() ## joue pluck
p1.stop() ### stop p1
p_all.stop() ### stop tous les p
p1.solo() ### solo p1
p1.solo(0) ### solo off
p1.only() ###arrete les autres players
p1.follow(b1) ### suit b1
p1.accompany(b1)
p1.reset() ### reset attributs
p_all.stop() # arrête tous les p
g1 = Group(p1,p2,p3) #groupe
Clock.clear() ### Stop tous = Ctrl + .
Clock.bpm = 144 # tempo
Clock.connect("IP")
Clock.meter = (3,4) ## passe en 3/4
Scale.default.set("major") #defini la gamme
print(Scale.names()) #affiche les gammes
Root.default.set("C#") #defini la tonique
Root.default=var((PIndex()*4)%7,32) #circle of fifth
FoxDot.reload()

Master().hpf=0
Clock.bpm=linvar([120,180],[36,inf], start=now)

#### Sample ######
print(BufferManager()) #affiche les samples
bd >> play("|x2||y3|") #kick2 et percu3
() # altern
[] #simultané dans l'espace d'1 temps
{} #choisi au hasard
# <> #joue un pattern en même temps <X >< ->
P["x-o-"].amen() #melange les rythmes
P["x-o-"].bubble(PRand(8)) #autre melange
"x-o-x".replace("x", "v")

#### Effets #######
print(FxList)
# <Fx 'vibrato' -- args: vib, vibdepth>
# <Fx 'slideTo' -- args: slide, sus, slidedelay>
# <Fx 'slideFrom' -- args: slidefrom, sus, slidedelay>
# <Fx 'pitchBend' -- args: bend, sus, benddelay>
# <Fx 'coarse' -- args: coarse, sus>
# <Fx 'striate' -- args: striate, sus, buf, rate>
# <Fx 'pitchShift' -- args: pshift>
# <Fx 'highPassFilter' -- args: hpf, hpr>
# <Fx 'lowPassFilter' -- args: lpf, lpr>
# <Fx 'filterSwell' -- args: swell, sus, hpr>
# <Fx 'bandPassFilter' -- args: bpf, bpr, bpnoise, sus>
# <Fx 'chop' -- args: chop, sus>
# <Fx 'tremolo' -- args: tremolo, beat_dur>
# <Fx 'combDelay' -- args: echo, beat_dur, decay>
# <Fx 'spinPan' -- args: spin, sus>
# <Fx 'trimLength' -- args: cut, sus>
# <Fx 'reverb' -- args: room, mix>
# <Fx 'formantFilter' -- args: formant>
# <Fx 'wavesShapeDistortion' -- args: shape>
# <Fx 'overdriveDistortion' -- args: drive>
delay=[0,0.1] # decale de ..
# [broken in source] echo=0.5, decay=0.5

#### Synth #######
print(Player.get_attributes()) #les parametres des players
print(SynthDefs) #les Synths
p1 >> pluck([0,2,4], dur=[1/4,1/2,3/4]) # durée
[1,[2,4],3] # altern =1,2,3,1,4,3
(0,2,4) # accord
p1 >> pluck(dur=1/2, amp=(p1.degree>1)).follow(b1) #suit b1, joue les note > 1
dur=[1,1,1,rest(4)] # silence de 4

### Evenements ###
p1.every(4, "reverse") ### inverse p1 tous les 4 temps
p1.never("reverse") ### arrete le reverse
p1.sometimes("rate.offmul", 1.5, 0.75) ### ajoute un rate à 1.5 offbeat 0.75
"mirror"
"offadd", 7, 0.75 ### ajoute 7 en contre temps de 0.75
"offmul", 7 ### multiplie par 7 en contre
"splice" ### ???
"sample.offadd", 2, 0.75 #### ajoute le sample 2 en offbeat 0.75
n, "alt", P[4,5,6] ### altern au bout de n avec le Pattern

Group(p1,p2).amplify = var([1,0],[28,4])

#### Transfo ####
().offbeat()
().penta() ## pentatonique
().slider() ## slide effect
().spread() ##
().alt_dur()
().reverse()
().degrade() ##

### Variables ###
var([0,4000],[4,4]) ## 0 pour 4 beats, 4000 pour 4beats
linvar([0,4000],[4,4]) ## chgt lineaire de 0 à 4000 puis 0 en 4*2 4beats
linvar([0,4000],[4,0]) ## chgt lineaire de 0 à 4000 en 4 beats puis retour 0
expvar([])
sinvar([])

#### Pattern #####
help(Patterns.Sequences)

# [broken in source] [1,2,3]*2 = [1,2,3,1,2,3]
# [broken in source] P[1,2,3]*2 = [2,4,6]
P[:8] = [0,1,2,3,4,5,6,7]
P[2:10:2] #debut fin pas : 2,4,6,8
P[5:8] = [5,6,7] # liste de l'un à l'autre
# [broken in source] Prange(4,10,2)= P[4,6,8] #liste avec step
P[PRand([1,2,3,4])[:4], 6, 7] # [1,2,3,4] aleatoire sur 4beats + 6 , 7
PwRand([1,2,3,4],[10,5,2,1]) # Random avec probabilités
PStep(8,1,-0.5) ### repete -0.5 7* + 1 +1*
PWalk()
PZ12([2,7]) ## random alternance entre 2 et 7
PZip([0,1,2],[3,4]) ## = P[(0, 3), (1, 4), (2, 3), (0, 4), (1, 3), (2, 4)]
PShuf([1,2,3]) #version mélangée du Pattern
PAlt([1,2,3],[4,5]) # alterne les valeurs de 2 Patterns
# [broken in source] PPairs([0,4,2,6], λ n: n*2) # melange en transformant avec fonction
PStretch([0,2,4,6], 13) # etire le pattern pour faire 13 pas
PZip([0,1,2], [3,4]) # P[(0, 3), (1, 4), (2, 3), (0, 4), (1, 3), (2, 4)]`
PStutter([0,1,2], 2) # répette chaque valeurs
# [broken in source] PEuclid2([7,4],8,"X", "--[--]"), sample=3) #génére un rythm eucli avec sample
P10(8) # random 0 1 sur 8 pas
# [broken in source] P*(0,2,4), dur=1/2 # spread les notes sur la durée
P*[1,2,3] # random
# P/ # spread mais joue l'accord
# p+ #spread sur le sus
P^(0,2,4,0.5) # spread de la durée de la derniere valeur (0.5)

# [broken in source] P%(1,2,3)|

#Pattern method ex : P[:8].shuffle()
# [broken in source] .shuffle() # melange
# [broken in source] .palindrome() #rajoute l'inverse à la fin abccba
# [broken in source] .rotate(n) #decale de n
# [broken in source] .stretch(n) #repete le patern jusqu'à qu'il fasse n
# [broken in source] .reverse() #inverse le Pattern
# [broken in source] .loop(n) #repete le pattern n fois
# [broken in source] .offadd(n) #intercale une valeur +n entre
# [broken in source] .offmul(n) #intercale une valeur *n entre
# [broken in source] .stutter(n) #repete chaque valeur n fois
# [broken in source] .penta() # joue la pentatonique
# [broken in source] .mirror()
# [broken in source] .shufflets(3) # accord dans le desordre
# [broken in source] .limit(sum, 7) # creer un pattern dont la somme = 7, len ou sum
# [broken in source] .layer("reverse")

###Fonction python
# abs : nombre que positif

# [broken in source] amp: (b1.char="o")*2 ## amp=2 quand b1 = "o"

# @nextBar
# [broken in source] def change():
Scale.default="major"
Root.default=+2

#SonicPi
from FoxDot.lib.Extensions.SonicPi import LoadSonicPiSynths, pisynth
LoadSonicPiSynths()
a1 >> pisynth.tb303(note=50, amp=.7, dur=1, attack=0, cutoff=70)
