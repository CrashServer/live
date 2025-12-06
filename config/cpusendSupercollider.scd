// CPU peak osc send every 10s
b = NetAddr.new("192.168.1.42", 2887);    // create the NetAddr


(
r = Routine {
	loop {
		b.sendMsg("/CPU", round(s.peakCPU,0.01));
	1.yield;
	};
}.play();
)
;
// Stop the osc send
r.stop()

