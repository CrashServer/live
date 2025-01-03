SynthDef.new(\dcomp,
{|bus, dcomp, dcomp_, dcomp_d, sus|
var osc;
osc = In.ar(bus, 2);
dcomp = if(dcomp_<=0, dcomp, Line.kr(dcomp, dcomp_, sus*dcomp_d));
osc = DCompressor.ar(osc, ratio: dcomp);
ReplaceOut.ar(bus, osc)}).add;