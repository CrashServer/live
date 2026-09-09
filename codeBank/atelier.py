# atelier foxdot
# tutorial

### LES BASES

# Évaluer une ligne de code avec Ctrl + Enter
p1 >> pluck()

# arrêter/stopper une ligne
p1 >> pluck().stop()

# p1 ici correspond au nom du "player", on peut le voir aussi comme le nom de la piste audio.
# On peut utiliser n'importe quelle association de chiffres et lettres sur 2 caractères.
# Ex : aa, k1, sn, bd, e8, ...

# Ensuite, la première instruction que l'on va lui donner est le nom de l'instrument (pluck dans l'exemple précédent).
# On retrouve la liste des instruments disponibles avec :
print(SynthDefs)

bi >> blip()

# On stoppe tous les sons avec Ctrl + .

### LES NOTES

# sans instructions entre les parenthèses, le 'player' va jouer en continu la première note de la gamme par défaut : do Majeur
# ajoutons quelques notes, rappel en programmation on commence toujours par le 0.

bi >> blip([0,2,4])

# Gamme CMaj (do Majeur):
# C - 0 - do
# D - 1 - re
# E - 2 - mi
# F - 3 - fa
# G - 4 - sol
# A - 5 - la
# B - 6 - si

# en utilisant les [] on joue les notes [0,2,4] à la suite et en boucle
# si on utilise des () on joue les notes en même temps, comme un accord

bi >> blip((0,2,4))

# on peut également créer des variations ainsi :

bi >> blip([0,2,4]) + [0,0,0,1]

bi >> blip([0,1,2]) + (0,2,4)

### LE RYTHME

# On change la rythmique du 'player' avec 'dur' (comme durée/duration).

bi >> blip([0,2,4], dur=1/2)

bi >> blip([0,1,3], dur=[1,1/2,1/2])

# Ici la note 0 dure 1 beat, et la note 1 et 3 durent 1/2 beat.

### LES SAMPLES

# FoxDot peut jouer aussi des samples, comme des percussions, en utilisant le synthé 'play'
# Au lieu d'utiliser une liste de nombres, on va utiliser des caractères où à chacun correspond un son

d1 >> play("x-o-")

# ici     x est la grosse caisse / kick
#         - est le charley / hi hat
#        o est la caisse claire / snare

# mettre des caractères entre () va les alterner
d1 >> play("x(-x)o-")

# mettre entre [] va les jouer plus vite
d1 >> play("x[--]o-")

# mettre entre {} va les choisir aléatoirement
d1 >> play("x-o{-ox}")

d1 >> play("(x[--])xo{-[--][-x]}")

# liste des samples disponibles
print(Samples)

# On peut également changer la banque de samples
d1 >> play("x-o-", sample=2)

d1 >> play("x-o-", sample=[0,1,2])

#On peut changer la vitesse de lecture d'un sample

d1 >> play("x", dur=4, rate=0.25)

## LES VARIATIONS DANS LE TEMPS

# on peut changer facilement un paramètre dans le temps à l'aide de var
# var([1er valeur, 2eme valeur], [durée 1er temps, durée 2eme temps])

p1 >> pluck(var([0,2],[6,2]))
# ici on va jouer 0 pendant 6 beats et 2 pendant 2

# on peut également changer la valeur linéairement
p1 >> pluck(linvar([0,2],[5,3]))
# la note va monter linéairement de 0 à 2 pendant 5 beats puis descendre de 2 à 0 pendant 3 beats

p1 >> pluck(var([0,2,6],[6,2]))

### LES ATTRIBUTS

# On a déjà vu certains attributs comme 'degree' (note) ou 'dur' mais il en existe plein d'autres.

print(Player.get_attributes())

p1 >> pluck([0, 1, 2, 3], dur=1/2, sus=2, pan=[-1,1])

# octave
bi >> blip(oct=[3,5,4])

# dur
p1 >> pluck([0, 1, 2, 3], dur=[1, 1, 0]) # ignorer toutes les 3eme note

p1 >> pluck([0, 1, 2, 3], dur=[1, 1, rest(2)]) # silence toute les 3 notes pendant 2 beat

# Scale

# changer la gamme
print(Scale.names())

p1 >> pluck([0, 2, 4, 6, 7], scale=Scale.minor)

Scale.default = "locrian"

# Amplification et volume
p1 >> pluck([0, 1, 2], dur=[1, 1/2, 1/2], amp=[1, 0.5, 1/3])

## LES FX

# Comme dans d'autres logiciels de musique, on peut rajouter des effets.

print(FxList)

# le premier paramètre est obligatoire et active l'effet, les suivants sont des paramètres supplémentaire de l'effet

p1 >> pluck(dur=4, slide=1, slidedelay=0) # slide effet

p1 >> pluck(dur=4, slide=1, slidedelay=0.5) # slide effet avec un délai d'effet de 0.5

p1 >> pluck(dur=4, slide=0, slidedelay=0.5) # slide est coupé

# RESSOURCES
# ----------
# https://foxdot.org/
# https://github.com/Qirky/Troop
# Groupe telegram FoxDot (anglophone)
# supercollider : https://supercollider.github.io

# CONTACTS
# --------
# GROUPE FACEBOOK LIVE CODING STRASBOURG
# https://www.facebook.com/livecodingstrasbourg/
#
# SVDK : svdkwast@gmail.com
# ZBDM : lagouttedo@gmail.com
# contact@crashserver.fr

# CRASH SERVER
# http://crashserver.fr
# https://mamot.fr/@crashserver
# https://www.youtube.com/crashserver/
# https://www.facebook.com/crashserverlive
# https://www.instagram.com/crashserver
# https://twitter.com/crashserver2
