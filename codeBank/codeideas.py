# code ideas
# snippets

# CODE IDEAS
# ---------

# Plaits Voice effect
###################
p3 >> plaits(engine=7, a=PWhite(0,1), oct=PRand(4,7), dur=var([PRy()],64), harm=PWhite(0.1,1), amp=PWhite(0.3,0.8), morph=PWhite(0.1,1), fx2=1, cutoff=4000, rq=0.9, porta=0.1, timbre=PWhite(0.1,0.8), dist2=PStep(16,1,0))

# Mring effect
##################
b8 >> superbass(mring=1, oct=(2,1), rmodel=PStep(8,PRand(0,5),3), rstruct=linvar([0.1,0.19],64), rpos=PWhite(0,1), vol=0.5, rbright=0.8, rdamp=0.8)
x8 >> play("<x[--]><..o.>", sample=(4, 5), mring=x8.rmodel, rmodel=var([1,2, 5]), mverb=x8.rmodel/5,  rbright=1, rstruct=(0.2,0.1), dist2=1, rdamp=0.8)
s4  >> star(mring=1, dur=PDur(3, 8), oct=(0.5, 1), rstruct=4, poly=5, bright=1, regg=2, rmodel=5, mverb=0.5)
