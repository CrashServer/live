SynthDef.new(\octafuz,
{|bus, octafuz, octamix, octafuz_, octafuz_d, octafuzlfo, octamix_, octamix_d, octamixlfo, sus|
var osc,dis,osc_base;
osc = In.ar(bus, 2);
octafuz = if(octafuz_<=0, octafuz, Line.kr(octafuz, octafuz_, sus*octafuz_d));
octafuz = if(octafuzlfo<=0, octafuz, octafuz * SinOsc.kr(octafuzlfo, 0, 1, 1));
octamix = if(octamix_<=0, octamix, Line.kr(octamix, octamix_, sus*octamix_d));
octamix = if(octamixlfo<=0, octamix, octamix * SinOsc.kr(octamixlfo, 0, 1, 1));
osc_base = osc;
dis = [1,1.01,2,2.02,4.5,6.01,7.501];
dis = dis ++ (dis*6);
osc = ((osc * dis*octafuz).sum.distort);
osc = (osc * 1/6)!2;
osc = SelectX.ar(octamix, [osc_base, osc]);
ReplaceOut.ar(bus, osc)}).add;