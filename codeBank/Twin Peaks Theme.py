# Twin Peaks Theme
Scale.default="chromatic"
Clock.bpm=72
s1 >> faim([[2,5], _, 0],dur=[3.0, 0.5, 0.5],amp=1, oct=(4,5), blur=1.2, tremolo=8, tremolomix=0.7, beef=2, mverb=0.2).unison(1)
s2 >> sinepad([_, -3, (4, 9, 5), 2, _, 0, (12, 9, 7), 5], dur=[0.5, 0.5, 2.0, 1.0], amp=1.2, rate=1, mverb=0.5, oct=5)
s3 >> sine([2, -7, 0, 5, 7, 9, 7, 5, 0],dur=[[4.0] + [0.5]*8],amp=1, oct=[4, 4] + [(4,5)]*7, rate=0.2, blur=1)
