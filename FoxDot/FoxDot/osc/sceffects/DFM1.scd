SynthDef.new(\DFM1,
{|bus, dfm, dfmr, dfmd, dfm_, dfm_d, dfmlfo, dfmlfomul, dfmlfoadd, dfmr_, dfmr_d, dfmrlfo, dfmrlfomul, dfmrlfoadd, dfmd_, dfmd_d, dfmdlfo, dfmdlfomul, dfmdlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
dfm = if(dfm_<=0, dfm, Line.kr(dfm, dfm_, sus*dfm_d));
dfm = if(dfmlfo<=0, dfm, dfm * SinOsc.kr(dfmlfo, 0, dfmlfomul, dfmlfoadd));
dfmr = if(dfmr_<=0, dfmr, Line.kr(dfmr, dfmr_, sus*dfmr_d));
dfmr = if(dfmrlfo<=0, dfmr, dfmr * SinOsc.kr(dfmrlfo, 0, dfmrlfomul, dfmrlfoadd));
dfmd = if(dfmd_<=0, dfmd, Line.kr(dfmd, dfmd_, sus*dfmd_d));
dfmd = if(dfmdlfo<=0, dfmd, dfmd * SinOsc.kr(dfmdlfo, 0, dfmdlfomul, dfmdlfoadd));
osc = DFM1.ar(osc, dfm, dfmr, dfmd,0.0);
ReplaceOut.ar(bus, osc)}).add;