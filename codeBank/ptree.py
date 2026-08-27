# Ptree
# bass

Scale.default = Scale.chromatic
o3 >> dbass((PTree(4)[:4],6), oct=(4, 5), tanh=1, multicrush=1, mclowdrive=8, mcmiddrive=1, mchighdrive=0, mclofreq=2000, lpf=12000, lpr=0.1, mchifreq=(3000, 1200), tanhmix=0.5, dur=P[1/4, 1/2, 1/4, 1/2, 1/4, 1/2].exp(P[2, 2.5, 2, 2])).chroma().unison(3)

o3 >> dbass((PTree(4)[:4],6), oct=(4, 5), tanh=0, multicrush=1, mclowdrive=32, mcmiddrive=4, mchighdrive=0, mclofreq=200, lpf=16700, lpr=0.1, mchifreq=(3000, 1200), tanhmix=0.5, dur=P[1/4, 1/2, 1/4, 1/2, 1/4, 1/2].exp(P[2, 2.5, 2, 2])).chroma().unison(3)

o3 >> dbass((PTree(4)[:4],6), oct=(4, (5, 5.02)), tanh=0, multicrush=1, mclowdrive=32, mcmiddrive=12, mchighdrive=1, mclofreq=400, lpf=16700, lpr=0.1, mchifreq=(3202, 1000), tanhmix=0.7, dur=P[1/4, 1/2, 1/4, 1/2, 1/4, 1/2].exp(P[2, 2.5, 2, [2, 2.5]])).chroma().unison(3)

o3 >> dbass((PTree(4)[:4],6), oct=(4, 5), tanh=0, multicrush=1, mclowdrive=64, mcmiddrive=256, mchighdrive=0, mclofreq=400, lpf=16700, lpr=0.1, mchifreq=(13000, 4500), tanhmix=0.7, dur=P[1/4, 1/2, 1/4, 1/2, 1/4, 1/2].exp(P[2, 2.5, 2, 2])).chroma().unison(3)

o3 >> dbass((PTree(4)[:4],6), oct=(4, 5), tanh=0, multicrush=1, mclowdrive=16, mcmiddrive=5, fbdelay=1, fbtime=0.25, fbfeed=0.7, fbcutoff=3400, fbspread=0.12, beat_dur=1, mchighdrive=3, mclofreq=4600, lpf=16700, lpr=0.1, mchifreq=(13000, 4500), tanhmix=0, dur=P[1/4, 1/4, 1/4, 1/2, 1/4, 1/2].exp(P[2, 2, 1])).chroma().unison(3)

o3 >> dbass((PTree(4)[:4],6), oct=(4, 5), tanh=0, multicrush=1, mclowdrive=16, mcmiddrive=5, fbdelay=1, fbtime=0.25, fbfeed=0.9, fbcutoff=3400, fbspread=0.12, beat_dur=1, mchighdrive=3, mclofreq=4600, lpf=16700, lpr=0.1, mchifreq=(1300, 400), resonbank=0.5, rbfreq=200, rbdecay=0.5, rbspread=1.0, tanhmix=0, dur=P[1/4, 1/4, 1/4, 1/2, 1/4, 1/2].exp(P[2, 2, 1])).chroma().unison(3)
