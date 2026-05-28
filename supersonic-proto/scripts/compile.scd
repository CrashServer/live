// Compile all SuperSonic SynthDefs
// Run via: sclang scripts/compile.scd
//
// ~outDir is shared across all loaded files via SC environment variables.

~outDir = "/home/svdk/live/supersonic-proto/synthdefs/compiled/";
("Writing to: " ++ ~outDir).postln;

// ── Synths ───────────────────────────────────────────────────────────────────
[
    "synthdefs/src/synths/dbass.scd",
    "synthdefs/src/synths/saw.scd",
    "synthdefs/src/synths/sine.scd",
    "synthdefs/src/synths/rsin.scd",
    "synthdefs/src/synths/donk.scd",
].do { |rel|
    ("/home/svdk/live/supersonic-proto/" ++ rel).load;
};

// ── FX ───────────────────────────────────────────────────────────────────────
[
    "synthdefs/src/fx/fx_chain.scd",
].do { |rel|
    ("/home/svdk/live/supersonic-proto/" ++ rel).load;
};

"All SynthDefs compiled.".postln;
0.exit;
