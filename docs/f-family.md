# F-Family — Raccourcis de modulation pour le live coding

Chaque fonction `f_` génère un pattern ou une variable temporelle en 0 à 3 arguments.
Format unifié : `f_(n, a, b)` — `n` = durée/longueur, `a`/`b` = bornes.

---

## 1. FADES — Variables temporelles (valeur continue qui évolue dans le temps)

### `fi` — Fade In (linéaire, one-shot)
Monte de `a` vers `b` sur `n` beats, puis reste à `b`.

```python
# Simple — amp de 0 à 1 sur 16 beats
d1 >> dbass(dur=1, amp=fi())
# → beat 0: 0.0 → beat 4: 0.25 → beat 8: 0.5 → beat 12: 0.75 → beat 16: 1.0

# Durée custom — ouverture de filtre sur 8 beats
d1 >> dbass(dur=1, lpf=fi(8))
# → beat 0: 0.0 → beat 2: 0.25 → beat 4: 0.5 → beat 6: 0.75 → beat 8: 1.0

# Bornes custom — filtre de 200 à 8000 Hz sur 32 beats
d1 >> dbass(dur=1, lpf=fi(32, 200, 8000))
# → beat 0: 200 → beat 8: 2150 → beat 16: 4100 → beat 24: 6050 → beat 32: 8000

# Musique : intro progressive, le son apparaît doucement
d1 >> dbass([0,2,4,5], dur=PDur(5,8), amp=fi(16), lpf=fi(32, 200, 6000))
```

### `fo` — Fade Out (linéaire, one-shot)
Descend de `b` vers `a` sur `n` beats, puis reste à `a`.

```python
# Simple — disparition sur 16 beats
d1 >> dbass(dur=1, amp=fo())
# → beat 0: 1.0 → beat 8: 0.5 → beat 16: 0.0

# Fermeture de filtre lente
d1 >> dbass(dur=1, lpf=fo(32, 200, 8000))
# → beat 0: 8000 → beat 16: 4100 → beat 32: 200

# Musique : outro, le son s'efface
d1 >> dbass([0,2,4], dur=1, amp=fo(16), lpf=fo(32, 4000, 200))
```

### `fb` — Fade Bounce (linéaire, boucle infinie)
Monte de `a` à `b` sur `n` beats, puis redescend de `b` à `a` sur `n` beats. En boucle.

```python
# Simple — pulsation d'amplitude
d1 >> dbass(dur=1, amp=fb(4))
# → beat 0: 0 → beat 2: 0.5 → beat 4: 1 → beat 6: 0.5 → beat 8: 0 → ...

# Sweep de filtre — respiration
d1 >> dbass(dur=1, lpf=fb(8, 400, 4000))
# → beat 0: 400 → beat 4: 2200 → beat 8: 4000 → beat 12: 2200 → beat 16: 400 → ...

# Musique : pad qui respire avec le filtre
p1 >> keys([0,2,4,7], dur=4, sus=4, lpf=fb(16, 800, 6000), amp=0.4)
```

### `fe` — Fade Exponentiel (one-shot)
Comme `fi` mais la courbe est exponentielle — démarre très lentement puis accélère en fin.

```python
# Ouverture de filtre qui explose en fin
d1 >> dbass(dur=1, lpf=fe(16, 200, 8000))
# → beat 0: 200 → beat 4: ~350 → beat 8: ~700 → beat 12: ~2800 → beat 16: 8000

# Musique : buildup qui accélère — la tension monte de plus en plus vite
d1 >> dbass([0,0,3,5], dur=PDur(3,8), lpf=fe(32, 200, 8000), amp=fe(16, 0.2, 0.8))
```

### `fs` — Fade Sinusoïdal (boucle infinie)
Oscillation douce en forme de sinus entre `a` et `b`. Plus lisse que `fb`.

```python
# Pan stéréo doux
d1 >> dbass(dur=1, pan=fs(16, -1, 1))
# → mouvement fluide gauche↔droite, 16 beats par demi-cycle

# Wobble de filtre
d1 >> dbass(dur=0.5, lpf=fs(8, 400, 4000))
# → beat 0: 400 → beat 2: ~1300 → beat 4: 2200 → beat 6: ~3100 → beat 8: 4000 → ...
# (courbe douce, pas anguleuse comme fb)

# Musique : basse avec filtre qui ondule naturellement
d1 >> dbass([0,0,3,5,3], dur=PDur(5,8), lpf=fs(8, 600, 3000), amp=0.7)
```

---

## 2. FADES "NOW" — Démarrent à l'instant de l'évaluation

Le problème des fades normaux : `fi(8)` commence à beat 0. Si tu l'évalues au beat 47, tu es déjà au milieu. Les versions "now" résolvent ça.

### `fn` — Fade In Now
```python
# Évalué au beat 47 → fade de beat 47 à beat 55
d1 >> dbass(dur=1, amp=fn(8))
# → beat 47: 0.0 → beat 51: 0.5 → beat 55: 1.0

# Filtre qui s'ouvre maintenant
d1 >> dbass(dur=1, lpf=fn(16, 200, 6000))
```

### `fon` — Fade Out Now
```python
# Disparition immédiate sur 8 beats
d1 >> dbass(dur=1, amp=fon(8))
```

### `fbn` — Bounce Now
```python
# Oscillation qui démarre maintenant
d1 >> dbass(dur=1, lpf=fbn(8, 400, 4000))
```

### `fen` — Exponentiel Now
```python
# Buildup exponentiel qui démarre maintenant
d1 >> dbass(dur=1, lpf=fen(16, 200, 8000))
```

### `fsn` — Sine Now
```python
# Wobble sinusoïdal qui démarre maintenant
d1 >> dbass(dur=1, pan=fsn(8, -1, 1))
```

---

## 3. PATTERNS — Séquences discrètes (valeurs fixes en boucle)

### `fr` — Random (PWhite)
Valeurs aléatoires uniformes dans une plage.

```python
# 16 valeurs aléatoires entre 0 et 1
d1 >> dbass(dur=1, amp=fr())
# → P[0.72, 0.31, 0.89, 0.14, 0.55, 0.43, 0.97, 0.22, 0.66, 0.08, 0.81, 0.39, 0.53, 0.74, 0.19, 0.61]

# 8 degrés aléatoires entre 0 et 7
d1 >> dbass(degree=fr(8, 0, 7), dur=0.5)
# → P[5, 1, 6, 3, 0, 7, 2, 4]

# Listes : 4 notes graves + 8 notes aigues
d1 >> dbass(degree=fr([4, 8], [0, 4], [3, 7]), dur=0.5)
# → P[2, 0, 1, 3,  5, 7, 4, 6, 5, 7, 4, 6]
#    └─4 de 0-3─┘  └────8 de 4-7────────────┘

# Musique : mélodie aléatoire avec variation de vélocité
d1 >> dbass(degree=fr(8, 0, 7), dur=PDur(5,8), amp=fr(8, 0.3, 0.8))
```

### `fw` — Walk (marche aléatoire bornée)
Chaque valeur = précédente ± step. Borné entre -max et +max.

```python
# Marche de 16 pas, step=1, borné à ±7
d1 >> dbass(degree=fw(), dur=0.5)
# → P[0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3]  (évolue par pas de 1)

# 8 pas, step=2, borné à ±12
d1 >> dbass(degree=fw(8, 2, 12), dur=0.5)
# → P[0, 2, 4, 2, 0, -2, 0, 2]  (sauts plus grands, plage plus large)

# Musique : mélodie qui évolue progressivement — pas de sauts brusques
d1 >> pluck(degree=fw(16, 1, 7), dur=PDur(5,8), oct=5, sus=0.5)
```

### `fd` — Drunk (marche douce, brownienne)
Comme `fw` mais avec un pas par défaut de 0.5 → mouvement très fluide.

```python
# Drift lent sur 16 pas
d1 >> dbass(degree=fd(), dur=1)
# → P[0, 0.5, 0, -0.5, 0, 0.5, 1.0, 0.5, 1.0, 1.5, 1.0, 0.5, 0, 0.5, 0, -0.5]

# Dérive subtile de filtre
d1 >> dbass(dur=0.5, lpf=fd(16, 100, 4000))
# → P[0, 100, 200, 100, 200, 300, 200, ...]  (changements très doux)

# Musique : basse dont le filtre dérive doucement
d1 >> dbass([0,0,3,5], dur=PDur(5,8), lpf=fd(32, 100, 4000)+2000)
```

### `fg` — Gaussian (distribution normale)
Valeurs concentrées autour de la moyenne `a`, avec un écart-type `b`.

```python
# 16 valeurs autour de 0, spread 1
d1 >> dbass(degree=fg(), dur=0.5)
# → P[-0.2, 0.8, -0.5, 0.1, 1.3, -0.1, 0.3, 0.6, -0.9, 0.2, -0.3, 0.4, 0.0, -0.7, 0.5, 0.1]

# 8 valeurs centrées sur 4, spread 1 — degrés qui restent proches de 4
d1 >> dbass(degree=fg(8, 4, 1), dur=0.5)
# → P[3.8, 4.3, 3.5, 4.1, 5.0, 3.9, 4.7, 3.6]

# Deux groupes : 4 notes autour de 0, 8 notes autour de 5
d1 >> dbass(degree=fg([4, 8], [0, 5], [0.5, 1]), dur=0.5)
# → P[0.2, -0.1, 0.4, -0.3,  4.8, 5.3, 4.6, 5.1, 5.7, 4.9, 5.2, 4.5]
#    └──autour de 0──────┘   └──────autour de 5──────────────────────┘

# Musique : mélodie qui gravite autour d'une note pivot
d1 >> pluck(degree=fg(16, 3, 1.5), dur=PDur(5,8), oct=5)
```

### `ft` — Triangulaire (distribution en triangle)
Comme gaussien mais borné — les valeurs ne dépassent jamais [a, b].

```python
# 16 valeurs entre 0 et 8, concentrées au milieu
d1 >> dbass(degree=ft(), dur=0.5)
# → P[4, 3, 5, 2, 6, 3, 4, 5, 3, 4, 6, 2, 5, 4, 3, 5]  (peu de 0 ou 8, beaucoup de 3-5)

# 8 valeurs entre 0 et 12
d1 >> dbass(degree=ft(8, 0, 12), dur=0.5)
# → P[5, 7, 4, 8, 6, 3, 7, 5]  (concentrées autour de 6)

# Musique : mélodie "naturelle" — peu d'extrêmes, beaucoup de milieu
d1 >> pluck(degree=ft(16, 0, 7), dur=PDur(3,8), oct=5, sus=0.3)
```

### `fc` — Coin (pile ou face)
Chaque valeur est soit `a` soit `b`, probabilité 50/50.

```python
# Stutters aléatoires — son ou silence
d1 >> dbass(dur=1, amp=fc())
# → P[0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0]

# 8 flips entre 0 et 0.8 — groove aléatoire
d1 >> dbass(dur=0.25, amp=fc(8, 0, 0.8))
# → P[0, 0.8, 0.8, 0, 0, 0.8, 0, 0.8]

# Musique : hi-hat aléatoire qui alterne fort/faible
b1 >> play("x", dur=0.25, amp=fc(16, 0.2, 0.8))
```

### `fq` — Sine Wave (onde sinusoïdale discrète)
Un cycle de sinus découpé en `n` pas.

```python
# 16 pas d'un cycle sinus entre 0 et 1
d1 >> dbass(dur=0.5, amp=fq())
# → P[0.0, 0.38, 0.71, 0.92, 1.0, 0.92, 0.71, 0.38, 0.0, -0.38, -0.71, -0.92, -1.0, -0.92, -0.71, -0.38]

# Filtre qui fait un sweep sinusoïdal
d1 >> dbass(dur=0.5, lpf=fq(16, 200, 8000))
# → P[200, 1700, 3100, 4200, 4600, 4200, 3100, 1700, 200, ...]

# 2 cycles concaténés : 8 pas court + 16 pas long
d1 >> dbass(dur=0.25, lpf=fq([8, 16], 200, 8000))
# → P[200..8000..200 (8 pas), 200..8000..200 (16 pas, plus lent)]

# Musique : mélodie ondulante
d1 >> pluck(degree=fq(8, 0, 7), dur=0.5, oct=5)
```

### `fz` — Sawtooth (dent de scie discrète)
Rampe linéaire de 0 à 1 (ou a à b) sur `n` pas, puis repart à 0.

```python
# 16 pas de rampe 0→1
d1 >> dbass(dur=0.5, amp=fz())
# → P[0.0, 0.067, 0.133, 0.2, 0.267, 0.333, 0.4, 0.467, 0.533, 0.6, 0.667, 0.733, 0.8, 0.867, 0.933, 1.0]

# Rampe de filtre 200→8000 sur 8 pas
d1 >> dbass(dur=0.5, lpf=fz(8, 200, 8000))
# → P[200, 1314, 2429, 3543, 4657, 5771, 6886, 8000]

# Musique : arpège ascendant mécanique
d1 >> pluck(degree=fz(8, 0, 7), dur=0.25, oct=5)
# → P[0, 1, 2, 3, 4, 5, 6, 7]  (montée linéaire)
```

### `ff` — Fractal (PFrac)
Séquence fractale — motifs auto-similaires basés sur `(a*i + b) % 1`.

```python
# 16 valeurs fractales entre 0 et 1
d1 >> dbass(dur=0.5, amp=ff())
# → P[0.0, 0.63, 0.26, 0.89, 0.52, 0.15, 0.78, 0.41, 0.04, 0.67, 0.30, 0.93, 0.56, 0.19, 0.82, 0.45]
# (motif quasi-régulier mais pas répétitif — intéressant rythmiquement)

# Degrés fractals entre 0 et 7
d1 >> dbass(degree=ff(16, 0, 7), dur=0.5)
# → P[0, 4, 1, 6, 3, 1, 5, 2, 0, 4, 2, 6, 3, 1, 5, 3]

# Musique : mélodie avec structure cachée
d1 >> pluck(degree=ff(16, 0, 7), dur=PDur(5,8), oct=5, sus=0.5)
```

### `fxr` — Exclusive Random (PxRand — jamais deux fois la même)
Comme `fr` mais ne répète jamais la même valeur deux fois de suite. Évite les notes "collées".

```python
# 16 degrés aléatoires 0-7, jamais de répétition
d1 >> dbass(degree=fxr(), dur=0.5)
# → P[3, 5, 2, 6, 0, 4, 1, 7, 3, 6, 2, 5, 0, 4, 7, 1]
# (contrairement à fr qui pourrait donner P[3, 3, 5, 5, ...])

# 8 valeurs entre 0 et 12
d1 >> pluck(degree=fxr(8, 0, 12), dur=0.5, oct=5)
# → P[7, 3, 10, 1, 8, 4, 11, 2]  (toujours du mouvement, jamais statique)

# Comparaison avec fr :
# fr(8, 0, 4)  → P[2, 2, 3, 1, 1, 4, 0, 3]  (les 2,2 et 1,1 sont ennuyeux)
# fxr(8, 0, 4) → P[2, 4, 1, 3, 0, 2, 4, 1]  (toujours un changement)

# Musique : mélodie qui bouge toujours — pas de notes "collées"
d1 >> pluck(degree=fxr(16, 0, 7), dur=PDur(5,8), oct=5, sus=0.5,
    lpf=fb(16, 800, 4000))
```

### `fperlin` — Bruit de Perlin (mouvement organique)
Bruit de Perlin 1D — le standard de l'animation/graphisme pour le mouvement naturel.
Plus lisse que `fd` (drunk), avec une structure multi-échelle.
`n` = longueur, `a` = min, `b` = max. 4e arg optionnel : octaves (1-6, défaut 3).

```python
# 16 valeurs organiques entre 0 et 1
d1 >> dbass(dur=0.5, amp=fperlin())
# → P[0.52, 0.55, 0.61, 0.68, 0.72, 0.71, 0.65, 0.58, 0.53, 0.51, 0.54, 0.60, 0.63, 0.59, 0.53, 0.50]
# (très lisse — les valeurs voisines sont toujours proches)

# 32 valeurs de filtre
d1 >> dbass(dur=0.25, lpf=fperlin(32, 200, 8000))
# → P[2100, 2400, 2900, 3500, 4200, 4800, 5100, 4900, 4400, 3800, 3200, 2800, ...]
# (comme une colline douce — pas de sauts brusques)

# Comparaison avec fd (drunk) :
# fd(16, 100, 4000)    → P[0, 100, 200, 100, 0, 100, ...]  (marche aléatoire, peut rester coincé)
# fperlin(16, 0, 4000) → P[2100, 2400, 2900, ...]  (mouvement fluide avec structure)

# 1 octave = très lisse, collines larges
d1 >> dbass(dur=0.5, lpf=fperlin(32, 200, 8000, 1))
# → P[2100, 2300, 2600, 3000, 3500, 4100, 4700, 5200, 5600, 5800, 5700, 5400, ...]

# 6 octaves = détaillé, rugueux mais encore cohérent
d1 >> dbass(dur=0.5, lpf=fperlin(32, 200, 8000, 6))
# → P[2100, 2800, 2400, 3100, 3900, 3600, 4500, 5100, 4800, 5300, 5100, 4600, ...]

# Musique : pad avec filtre qui dérive organiquement
p1 >> keys([0,2,4,7], dur=4, sus=4,
    lpf=fperlin(32, 800, 6000), amp=fperlin(32, 0.2, 0.6), oct=5)

# Mélodie Perlin — contour mélodique naturel
d1 >> pluck(degree=fperlin(16, 0, 7), dur=PDur(5,8), oct=5,
    lpf=fperlin(32, 400, 4000, 1))  # filtre très lisse (1 octave)

# Accords Perlin — deux voix organiques parallèles
d1 >> keys(degree=fperlin(16, (0, 0), (5, 9)), dur=1, sus=2, oct=5)
```

### `fl` — Life (automate cellulaire)
PLife — séquence générée par des règles de Wolfram. `a` = chaos (0.0-1.0).

```python
# 16 valeurs, chaos moyen, borné 0-7
d1 >> dbass(degree=fl(), dur=0.5)
# → P[3, 5, 2, 6, 1, 4, 7, 3, 5, 0, 6, 2, 4, 7, 1, 5]
# (le chaos contrôle la complexité du motif)

# Chaos 0 (linéaire, très ordonné)
d1 >> dbass(degree=fl(16, 0.0, 7), dur=0.5)
# → P[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  (tout à zéro, règle 0)

# Chaos 0.5 (structures complexes, règle 110)
d1 >> dbass(degree=fl(16, 0.5, 7), dur=0.5)
# → P[3, 5, 6, 3, 1, 5, 7, 2, 4, 6, 3, 5, 1, 4, 7, 2]  (motifs avec structure)

# Chaos 1.0 (maximum, règle 30)
d1 >> dbass(degree=fl(16, 1.0, 7), dur=0.5)
# → P[4, 1, 7, 2, 6, 0, 5, 3, 7, 1, 4, 6, 2, 5, 0, 3]  (chaotique mais déterministe)

# Musique : évolution organique
d1 >> pluck(degree=fl(32, 0.7, 7), dur=PDur(5,8), oct=5, lpf=fb(16, 800, 4000))
```

---

## 4. STEP/HOLD — Valeurs qui changent par paliers

### `fh` — Hold (var() raccourci)
Change de valeur tous les `n` beats. Pas d'interpolation — saute directement.

```python
# Alterne entre 0 et 1 tous les 4 beats
d1 >> dbass(dur=1, amp=fh())
# → beat 0-3: 0 → beat 4-7: 1 → beat 8-11: 0 → beat 12-15: 1 → ...

# Alterne vite (2 beats chacun)
d1 >> dbass(dur=1, amp=fh(2))
# → beat 0-1: 0 → beat 2-3: 1 → beat 4-5: 0 → ...

# Deux octaves qui alternent
d1 >> dbass(dur=1, oct=fh(8, 4, 5))
# → beat 0-7: oct 4 → beat 8-15: oct 5 → beat 16-23: oct 4 → ...

# Liste de valeurs — cycle complet
d1 >> dbass(dur=1, lpf=fh(4, [200, 800, 2000, 4000]))
# → beat 0-3: 200 → beat 4-7: 800 → beat 8-11: 2000 → beat 12-15: 4000 → ...

# Durées différentes par valeur
d1 >> dbass(dur=1, lpf=fh([8, 4], [200, 4000]))
# → beat 0-7: 200 → beat 8-11: 4000 → beat 12-19: 200 → ...
# (8 beats à 200, puis 4 beats à 4000)

# Musique : structure de section — verse/chorus par le filtre
d1 >> dbass([0,2,4,5], dur=PDur(5,8),
    lpf=fh(16, [800, 2000, 4000, 6000]),
    amp=fh(8, [0.4, 0.7]))
```

---

## 5. EXPANSION DE LISTES ET PGROUPS (ACCORDS)

### Listes `[ ]` → concaténation
Les fonctions Pattern acceptent des listes dans n'importe quel argument.
Chaque élément génère un bloc, les blocs sont concaténés.

```python
# fr([4, 8], [0, 3], [3, 7])
# = fr(4, 0, 3) | fr(8, 3, 7)
# → P[2,0,1,3, 5,4,7,6,3,5,7,4]  (4 graves + 8 aigus)

# fq([8, 16], 200, 8000)
# = fq(8, 200, 8000) | fq(16, 200, 8000)
# → un cycle rapide de 8 pas, puis un cycle lent de 16 pas

# fw([4, 4], [1, 3], [4, 7])
# = fw(4, step=1, max=4) | fw(4, step=3, max=7)
# → P[0,1,2,1, 0,3,6,3]  (marche douce + marche agitée)
```

### Tuples `( )` → PGroups (accords/simultané)
Un tuple génère un pattern par élément du tuple, puis zip en PGroups.

```python
# ft(8, 0, (5, 12))
# = zip(PTrir(0, 5)[:8], PTrir(0, 12)[:8]) en PGroups
# → P[(2, 5), (3, 8), (1, 4), (4, 10), (2, 7), (3, 9), (1, 3), (4, 11)]
# Chaque note est un accord de 2 voix — une dans 0-5, l'autre dans 0-12

d1 >> pluck(degree=ft(8, 0, (5, 12)), dur=0.5, oct=5)
# Joue des accords de 2 notes, distribution triangulaire

# fr(8, (0, 3), (4, 7))
# = zip(PWhite(0, 4)[:8], PWhite(3, 7)[:8])
# → P[(2, 5), (0, 6), (3, 4), (1, 7), ...]
d1 >> pluck(degree=fr(8, (0, 3), (4, 7)), dur=0.5)
# Accords aléatoires : note grave 0-4, note aiguë 3-7

# fperlin(16, (0, 0), (7, 12))
# → P[(3.2, 7.8), (3.5, 8.1), (3.8, 8.6), ...]
# Deux voix Perlin parallèles, chacune dans sa plage
d1 >> keys(degree=fperlin(16, (0, 0), (7, 12)), dur=1, sus=2)
```

---

## 6. COMBINAISONS AVANCÉES

### Fade + Pattern
```python
# Mélodie fractale avec filtre qui ouvre exponentiellement
d1 >> pluck(degree=ff(16, 0, 7), dur=PDur(5,8),
    lpf=fe(32, 200, 8000), amp=fb(8, 0.3, 0.8), oct=5)

# Basse drunk avec wobble sinusoïdal
d1 >> dbass(degree=fd(8, 1, 7), dur=1,
    lpf=fs(8, 400, 3000), shape=fb(16, 0, 0.5))
```

### Pattern sur Pattern
```python
# Degrés = walk, filtre = sine pattern, amp = coin
d1 >> pluck(degree=fw(16, 1, 7), dur=0.5,
    lpf=fq(8, 400, 6000), amp=fc(16, 0.3, 0.8), oct=5)
```

### Now + Hold — changement de section en live
```python
# Tu es au milieu du set — transition immédiate
d1 >> dbass([0,3,5,7], dur=PDur(5,8),
    amp=fn(8),                         # fade in maintenant
    lpf=fen(16, 200, 6000),            # filtre expo qui ouvre maintenant
    oct=fh(16, [4, 5]))                # alterne octave toutes les 16 mesures
```

### Multi-couches expressives
```python
# Pad atmosphérique avec mouvement constant
p1 >> keys([0,2,4,7], dur=4, sus=4,
    amp=fs(32, 0.2, 0.6),             # respiration lente
    lpf=fb(16, 1000, 5000),           # filtre bounce
    pan=fs(24, -0.7, 0.7),            # pan sine lent (déphasé du filtre)
    shape=fh(8, [0, 0.1, 0.3, 0]))    # distortion par paliers

# Basse technique avec variation maximale
d1 >> dbass(degree=fw(8, 1, 7), dur=PDur(5,8),
    amp=ft(8, 0.3, 0.9),              # vélocité triangulaire
    lpf=fq(16, 400, 4000),            # filtre sine
    sus=ff(8, 0.1, 0.8),              # durée fractale
    shape=fc(8, 0, 0.4))              # distortion coin flip

# Drums avec humanisation
b1 >> play("X x [oo] {x-}", dur=0.5,
    amp=fg(16, 0.6, 0.15),            # vélocité gaussienne autour de 0.6
    pan=fd(16, 0.1, 0.3),             # léger drift stéréo
    lpf=fh(8, [4000, 6000, 3000, 8000]))  # filtre qui change par section
```

---

## 7. TABLEAU RÉCAPITULATIF

### Variables temporelles (continues)

| Fn | Type | Forme | Par défaut | Boucle ? |
|----|------|-------|------------|----------|
| `fi` | linvar | ╱ rampe up | n=16 a=0 b=1 | non |
| `fo` | linvar | ╲ rampe down | n=16 a=0 b=1 | non |
| `fb` | linvar | ╱╲ triangle | n=16 a=0 b=1 | oui |
| `fe` | expvar | ⌒ expo up | n=16 a=0 b=1 | non |
| `fs` | sinvar | ∿ sinus | n=16 a=0 b=1 | oui |
| `fh` | var | ▄▀▄ paliers | n=4 a=0 b=1 | oui |
| `fn` | linvar | ╱ (from now) | n=16 a=0 b=1 | non |
| `fon` | linvar | ╲ (from now) | n=16 a=0 b=1 | non |
| `fbn` | linvar | ╱╲ (from now) | n=16 a=0 b=1 | oui |
| `fen` | expvar | ⌒ (from now) | n=16 a=0 b=1 | non |
| `fsn` | sinvar | ∿ (from now) | n=16 a=0 b=1 | oui |

### Patterns (séquences discrètes)

| Fn | Source | Distribution | Par défaut |
|----|--------|-------------|------------|
| `fr` | PWhite | uniforme | n=16 a=0 b=1 |
| `fxr` | PxRand | uniforme sans répétition | n=16 a=0 b=7 |
| `fw` | PWalk | marche step=a max=b | n=16 a=1 b=7 |
| `fd` | PWalk | marche douce step=0.5 | n=16 a=0.5 b=7 |
| `fg` | PGauss | gaussienne mean=a dev=b | n=16 a=0 b=1 |
| `ft` | PTrir | triangulaire [a,b] | n=16 a=0 b=8 |
| `fc` | PCoin | binaire a ou b | n=16 a=0 b=1 |
| `fq` | PSine | sinus discret | n=16 a=0 b=1 |
| `fz` | PSaw | dent de scie | n=16 a=0 b=1 |
| `ff` | PFrac | fractale | n=16 a=0 b=1 |
| `fl` | PLife | automate cellulaire chaos=a | n=16 a=0.5 b=7 |
| `fperlin` | Perlin 1D | bruit organique multi-octave | n=16 a=0 b=1 (oct=3) |

---

## 8. IDÉES D'AJOUTS POSSIBLES

### Générateurs FoxDot sans raccourci f-

| Idée | Source | Usage |
|------|--------|-------|
| `fwr` | PwRand | random pondéré — certaines notes plus probables |
| `flog` | PLog | lognormale — valeurs rares mais extrêmes |
| `fm` | melody() | Markov — mélodie basée sur les transitions |

### Générateurs extérieurs à FoxDot

| Idée | Concept | Usage musical |
|------|---------|---------------|
| `florentz` | Attracteur de Lorenz | Chaos déterministe — séquences "papillon". Trois dimensions → degree + lpf + amp simultanés |
| `fhenon` | Attracteur de Hénon | Chaos simple à 2 paramètres. Plus prévisible que Lorenz |
| `fmorph` | Interpolation temporelle entre patterns | `fmorph(P[0,2,4], P[7,5,3], 16)` → en 16 beats passe graduellement du premier pattern au second |
| `flerp` | Interpolation entre patterns | `flerp(pat_a, pat_b, 0.3)` → 70% pat_a + 30% pat_b. Morphing entre deux mélodies |
| `fenv` | Enveloppe ADSR pattern | `fenv(a=2, d=2, s=0.7, r=4)` → forme d'enveloppe sur N beats. Pour structurer des sections |
| `fquant` | Quantification | `fquant(fr(16, 0, 7), [0,2,4,5,7])` → force les valeurs sur une liste. Tout pattern → gamme |
| `frot` | Rotation progressive | `frot(P[0,2,4,7], 4)` → chaque 4 beats le pattern tourne d'un cran |
