# Crazy Train 144
# Cover

Clock.bpm=144
Scale.default="chromatic"
r0 >> faim([6, 6, _, [9, 14], [9,14], _, 4, 4, _], dur=[0.5, 0.5, [3,1,1]],amp=1, oct=3, dist2=1, vol=0.7, beef=2).chroma()
r1 >> faim([6,6,13,6,14,6,13,6,11,9,8,9,11,9,8,4],dur=1/2,amp=1, dist2=1, oct=4, vol=0.7, leg=0, beef=0).chroma()

d1 >> play("<xx.>", dur=[0.5, 0.5, [3,1,1]], comp=1, vol=4) 
d2 >> play("<..u.><->", dur=1/2 ,sample=0, comp=1)
w6 >> loop("circlebreak16", dur=16, sample=7, comp=0, vol=1, fx=1)
