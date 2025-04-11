SynthDef.new(\DFM1,
{|bus, dfm, dfmr, dfmd, dfm_, dfm_d, dfmlfo, dfmr_, dfmr_d, dfmrlfo, dfmd_, dfmd_d, dfmdlfo, sus|
var osc;
osc = In.ar(bus, 2);
dfm = if(dfm_<=0, dfm, Line.kr(dfm, dfm_, sus*dfm_d));
dfm = if(dfmlfo<=0, dfm, dfm * SinOsc.kr(dfmlfo, 0, 1, 1));
dfmr = if(dfmr_<=0, dfmr, Line.kr(dfmr, dfmr_, sus*dfmr_d));
dfmr = if(dfmrlfo<=0, dfmr, dfmr * SinOsc.kr(dfmrlfo, 0, 1, 1));
dfmd = if(dfmd_<=0, dfmd, Line.kr(dfmd, dfmd_, sus*dfmd_d));
dfmd = if(dfmdlfo<=0, dfmd, dfmd * SinOsc.kr(dfmdlfo, 0, 1, 1));
osc = DFM1.ar(osc, dfm, dfmr, dfmd,0.0);
ReplaceOut.ar(bus, osc)}).add;