(
// Audio Analyzer - SC-side analysis engine for audio-reactive patterns
// Sends amplitude and onset data back to Python via OSC

// Analysis SynthDef - runs on a specific bus
SynthDef(\foxdot_analyzer, {|bus=0, reply_id=0, rate=10|
	var sig, amp, onset, fftbuf;
	sig = In.ar(bus, 2);
	amp = Amplitude.kr(Mix(sig), 0.01, 0.1);
	fftbuf = LocalBuf(512);
	onset = Onsets.kr(FFT(fftbuf, Mix(sig)), 0.5);
	SendReply.kr(Impulse.kr(rate), '/foxdot/analysis', [amp, onset], reply_id);
}).add;

// OSCFunc to receive Python commands to start/stop analysis
OSCFunc({|msg, time, addr, port|
	var action, bus, replyId, rate, node;
	action = msg[1].asString;

	case
	{action == "start"} {
		bus = msg[2].asInteger;
		replyId = msg[3].asInteger;
		rate = msg[4] ? 10;
		node = msg[5].asInteger;
		("AudioAnalyzer: starting on bus" + bus + "reply_id" + replyId + "node" + node).postln;
		Synth(\foxdot_analyzer, [\bus, bus, \reply_id, replyId, \rate, rate], target: RootNode(Server.default), addAction: \addToTail);
	}
	{action == "stop"} {
		replyId = msg[2].asInteger;
		("AudioAnalyzer: stopping reply_id" + replyId).postln;
		// Free all analyzer synths (they auto-free when the monitored synth ends)
	};
}, '/foxdot/analyzer_ctl');

"AudioAnalyzer loaded".postln;
)
