FoxDot
{

	classvar server;
	classvar midiout;
	classvar stemGroup;    // dedicated Group holding all stem synths — freeAll kills them in one shot
	classvar stemBufs;     // Dictionary mapping bus -> Buffer (DiskOut sink, needs explicit close)

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

		stemGroup = nil;
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
		// spawns \stemDiskOut + \stemTap synth pair per bus into a dedicated
		// stem Group placed AFTER server.defaultGroup. Group runs after every
		// player group (which live INSIDE defaultGroup) so \stemDiskOut reads
		// bus N after \output FX has written to it.
		OSCFunc(
			{
				arg msg, time, addr, port;
				var i, bus, path, buf;
				// Fresh start: kill any leftover stem group from a previous session
				if (stemGroup.notNil) {
					"[stems] freeing leftover stem group".postln;
					stemGroup.free;
				};
				if (stemBufs.notNil) {
					stemBufs.do({ | b | AppClock.sched(0.5, { b.close; b.free; nil; }); });
				};
				stemGroup = Group.after(server.defaultGroup);
				stemBufs = Dictionary.new;
				("[stems] starting" + ((msg.size - 1) / 2) + "stem recordings, group" + stemGroup.nodeID).postln;
				i = 1;
				while ({ i < msg.size }, {
					bus = msg[i].asInteger;
					path = msg[i + 1].asString;
					buf = Buffer.alloc(server, 65536, 2);
					buf.write(path, "wav", "int16", 0, 0, true);
					stemBufs[bus] = buf;
					Synth.tail(stemGroup, \stemDiskOut, [\bus, bus, \buf, buf.bufnum]);
					Synth.tail(stemGroup, \stemTap, [\bus, bus]);
					("[stems]  bus" + bus + "->" + path).postln;
					i = i + 2;
				});
			},
			'/foxdot_stems_start'
		);

		// OSC: /foxdot_stems_stop  -- free stem Group (kills all children),
		// then close buffers after a flush delay
		OSCFunc(
			{
				arg msg, time, addr, port;
				if (stemGroup.notNil) {
					("[stems] stopping — freeing group" + stemGroup.nodeID).postln;
					stemGroup.free;
					stemGroup = nil;
				} {
					"[stems] stop received but stemGroup was nil!".postln;
				};
				if (stemBufs.notNil) {
					stemBufs.do({ | buf |
						AppClock.sched(0.5, { buf.close; buf.free; nil; });
					});
					stemBufs = Dictionary.new;
				};
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
