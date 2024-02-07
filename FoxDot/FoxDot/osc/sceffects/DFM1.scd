SynthDef.new(\DFM1,
{|bus, dfm, dfmr, dfmd, dfm_, dfmr_, dfmd_, sus|
var osc;
osc = In.ar(bus, 2);
dfm = dfm+Line.kr(0, dfm_, sus);
dfmr = dfmr+Line.kr(0, dfmr_, sus);
dfmd = dfmd+Line.kr(0, dfmd_, sus);
osc = DFM1.ar(osc, dfm, dfmr, dfmd,0.0);
ReplaceOut.ar(bus, osc)}).add;