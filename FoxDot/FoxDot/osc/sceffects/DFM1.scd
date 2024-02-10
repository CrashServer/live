SynthDef.new(\DFM1,
{|bus, dfm, dfmr, dfmd, dfm_, dfm_d, dfmr_, dfmr_d, dfmd_, dfmd_d, sus|
var osc;
osc = In.ar(bus, 2);
dfm = if(dfm_<=0, dfm, Line.kr(dfm, dfm_, sus*dfm_d));
dfmr = if(dfmr_<=0, dfmr, Line.kr(dfmr, dfmr_, sus*dfmr_d));
dfmd = if(dfmd_<=0, dfmd, Line.kr(dfmd, dfmd_, sus*dfmd_d));
osc = DFM1.ar(osc, dfm, dfmr, dfmd,0.0);
ReplaceOut.ar(bus, osc)}).add;