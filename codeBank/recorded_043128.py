# recorded_043128
# recorded

#@intro(32)
l1 >> loop("atmo8", dur=8, sample=3, mverb=1)

#@build(8)
l2 >> loop("atmo8", dur=8, sample=3, mverb=1, tremolo=0.5, tremolomix=1)

#@peak(16)
b3 >> plaitsX((var([0,3,2],[16]),var([3,2,5,2],8)), preset=13 ,dur=1/4, fdecay=[2,PFr(1,2,808)], drive=PFr(0.02,0.4)).gtr((5,6)).human(20,-4) + (0,var([0,P*[-1,5]],[7,1]))

#@break(16)
Clock.clear()
soff()
Server.clearFx()

#@drop(16)
rec_stop()

#@endfade(16)
