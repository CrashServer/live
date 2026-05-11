FoxDot
{

	classvar server;
	classvar midiout;
	classvar stemSynths;   // Dictionary mapping bus -> [diskOutSynth, tapSynth]
	classvar stemBufs;     // Dictionary mapping bus -> Buffer (DiskOut sink)

	*start
	{ | remote = false |

		server = Server.default;

		server.options.memSize = 8192 * 16 * 8; // increase this if you get "alloc failed" messages
		server.options.maxNodes = 1024 * 32; // increase this if you are getting drop outs and the message "too many nodes"
		server.options.numOutputBusChannels = 16; // set this to your hardware output channel size, if necessary
		server.options.numInputBusChannels = 2; // set this to your hardware output channel size, if necessary

		if (remote, {
			server.options.bindAddress = "0.0.0.0"; // allow connections from any address
		});

		stemSynths = Dictionary.new;
		stemBufs = Dictionary.new;

		server.boot();

		OSCFunc(
			{
				arg msg, time, addr, port;
				var fn;

				// Get local filename

				fn = msg[1].asString;

				// Print a message to the user

				("Loading SynthDef from" + fn).postln;

				// Add SynthDef to file

				fn = File(fn, "r");
				fn.readAllString.interpret;
				fn.close;

			},
			'foxdot'
		);

		StageLimiter.activate(2);

		// === STEM RECORDING (video_game branch) ===
		// Per-player audio capture to disk for adaptive game-audio stems.
		// Each player routes its synth output to a private bus via output=N.
		// stemTap mirrors bus -> master (0,1) so the user still hears the mix.
		// stemDiskOut writes the bus signal to a .wav file.

		Server.default.waitForBoot({
			SynthDef(\stemDiskOut, { | bus = 16, buf = 0 |
				DiskOut.ar(buf, In.ar(bus, 2));
			}).add;

			SynthDef(\stemTap, { | bus = 16, gain = 1.0 |
				Out.ar(0, In.ar(bus, 2) * gain);
			}).add;

			"[stems] SynthDefs registered (\\stemDiskOut, \\stemTap)".postln;
		});

		// OSC: /foxdot_stems_start [bus1, path1, bus2, path2, ...]
		// Allocates a Buffer per bus, opens file for DiskOut streaming,
		// spawns \stemDiskOut + \stemTap synth pair for each bus.
		//
		// Node placement: spawned AFTER server.default.defaultGroup, so they
		// run in the root group AFTER every player group's per-note chain
		// (which lives INSIDE defaultGroup). If we put them inside defaultGroup
		// via Synth.tail(nil, ...) they'd land at the front of the group's
		// child list and new player groups would be appended after them on
		// every note — \stemDiskOut would read bus N BEFORE \output writes
		// to it, capturing silence.
		OSCFunc(
			{
				arg msg, time, addr, port;
				var i, bus, path, buf;
				("[stems] starting" + ((msg.size - 1) / 2) + "stem recordings").postln;
				i = 1;
				while ({ i < msg.size }, {
					bus = msg[i].asInteger;
					path = msg[i + 1].asString;
					buf = Buffer.alloc(server, 65536, 2);
					buf.write(path, "wav", "int16", 0, 0, true);
					stemBufs[bus] = buf;
					stemSynths[bus] = [
						Synth.after(server.defaultGroup, \stemDiskOut, [\bus, bus, \buf, buf.bufnum]),
						Synth.after(server.defaultGroup, \stemTap, [\bus, bus])
					];
					("[stems]  bus" + bus + "->" + path).postln;
					i = i + 2;
				});
			},
			'/foxdot_stems_start'
		);

		// OSC: /foxdot_stems_stop  -- free all stem synths + close buffers
		OSCFunc(
			{
				arg msg, time, addr, port;
				("[stems] stopping" + stemSynths.size + "stems").postln;
				stemSynths.do({ | pair | pair[0].free; pair[1].free; });
				stemBufs.do({ | buf |
					AppClock.sched(0.25, { buf.close; buf.free; nil; });
				});
				stemSynths = Dictionary.new;
				stemBufs = Dictionary.new;
				"[stems] done".postln;
			},
			'/foxdot_stems_stop'
		);

		"Listening for messages from FoxDot".postln;
	}

	*startRemote
	{
		this.start(true);
	}

	*midi
	{
		arg port=0;

		MIDIClient.init;

		midiout = MIDIOut(port);

		OSCFunc(
			{
				arg msg, time, addr, port;
				var note, vel, sus, channel, nudge, cc, value;

				// listen for specific MIDI trigger messages from FoxDot

				note    = msg[2];
				vel     = msg[3];
				sus     = msg[4];
				channel = msg[5];
				nudge   = msg[6];
				cc      = msg[7];
				value   = msg[8];

				if ( cc==0, {
				SystemClock.schedAbs(time + nudge, {midiout.noteOn(channel, note, vel)});
					SystemClock.schedAbs(time + nudge + sus, {midiout.noteOff(channel, note, vel)});},{
					SystemClock.schedAbs(time + nudge, {midiout.control(channel, cc, value)});} // crash mod
				)
				},
			'foxdot_midi'

		);

		("Sending FoxDot MIDI messages to" + MIDIClient.destinations[port].name).postln;

	}
}
