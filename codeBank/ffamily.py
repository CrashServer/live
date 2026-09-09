# f-family #120
# documentation
  
  # === F-FAMILY — Raccourcis pour patterns et timevars ===                                                                               
  # Signature unifiée: f?(n=16, a=0, b=1)                                                                                               
  # n = durée en beats (timevars) ou longueur (patterns)                                                                                  
  # a = valeur min, b = valeur max                                                                                                        
  # Sans args: valeurs par défaut (16, 0, 1)                                                                                              
                                                                                                                                          
  # fi — fade in: monte de a vers b, puis reste (linvar)                                                                                  
p1 >> sinepad([0,4,7], dur=4, amp=fi())  # amp monte de 0 à 1 sur 16 beats                                                              
p1 >> sinepad([0,4,7], dur=4, lpf=fi(32, 200, 8000))  # filtre s'ouvre de 200 à 8000 sur 32 beats                                       
                                                                                                                                          
  # fo — fade out: descend de b vers a, puis reste (linvar inversé)
p1.amp = fo(8)  # fade out sur 8 beats, de 1 à 0
p1.lpf = fo(48, 400, 4000)  # filtre se ferme de 4000 à 400 sur 48 beats

# fb — fade bounce: oscille entre a et b en boucle (linvar cyclique)
b1 >> dbass([0,3,5], dur=1/2, lpf=fb(16, 400, 3000))  # filtre wah-wah entre 400 et 3000
b1.dist2 = fb(8, 0, 0.6)  # distortion qui respire entre 0 et 0.6

# fe — fade exponentiel: monte de a vers b avec courbe exponentielle (expvar)
p1.amp = fe(32)  # fade in lent au début, rapide à la fin
b1.lpf = fe(16, 200, 6000)  # ouverture de filtre exponentielle

  # fs — fade sinusoïdal: oscille doucement entre a et b (sinvar)
j1 >> blip(pan = fs(8, -1, 1))  # auto-pan sinusoïdal gauche/droite sur 8 beats
p1.amp = fs(32, 0.3, 0.7)  # volume qui pulse doucement

# fr — random: valeurs aléatoires entre a et b (PWhite) - répétés comme un [:8]
d1 >> play("-", dur=1/4, amp=fr(8, 0.2, 0.8))  # 8 amplitudes aléatoires entre 0.2 et 0.8
j1.pan = fr(16, -1, 1)  # panoramique aléatoire, cycle de 16

# fw — walk: marche aléatoire bornée (PWalk)
j1 >> plaitsX(fw(12, 1, 7), dur=1/4)  # mélodie en marche aléatoire, step de 1, max 7, répétion 12 foix
  b1.degree = fw(8, 1, 4)  # basse qui se promène doucement

 # fg — gaussien: distribution gaussienne (PGauss)
j1.fmod = fg(8, 0, 0.2)  # modulation FM gaussienne, centrée sur 0, écart 0.2, répétition 8 x

# ft — triangulaire: distribution triangulaire (PTrir)
j1 >> cs80(ft(8, 0, 12), dur=PDur(3,8))  # mélodie en distribution triangulaire 0-12

# fc — coin flip: pile ou face entre a et b (PCoin)
d1.amp = fc(8, 0, 1)  # chaque step est soit 0 soit 1 (gate aléatoire)
j1.oct = 4 + fc(8, 0, 1)  # alterne aléatoirement entre octave 4 et 5

# fq — onde sinusoïdale: un cycle de sinus mappé sur a-b (PSine)
p1.lpf = fq(32, 200, 8000)  # filtre qui suit une courbe sinusoïdale complète
d2.amp = fq(16, 0.2, 0.8)  # amplitude en forme de vague

# fz — dent de scie: un cycle de sawtooth mappé sur a-b (PSaw)
b1.lpf = fz(16, 400, 4000)  # filtre en dent de scie (montée linéaire, chute)

  # === Combinaisons ===
  # Multiplication: fi() * 4 → rampe de 0 à 4
b1 >> lbass([0,5], dur=1, amp=fi()*0.8, lpf=fb(16, 200, 2000)*fr(8, 1, 3))

  # Tableaux dans n: durées asymétriques (timevars seulement)
c1.lpf = fb([8,4], 400, 3000)  # monte sur 8 beats, redescend sur 4
c1.cutoff = fi([16,8,16], 200, 5000)  # rythme irrégulier de sweep

# Addition: fi() + 3 → rampe de 3 à 4
j1.oct = fw(16, 1, 3) + 4  # marche aléatoire autour d'octave 4-7
