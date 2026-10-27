// CrashFoxDot — headless sclang startup (no GUI window)
// Used by start.sh when scide refuses to display.
// Equivalent to startuplive.scd minus s.makeWindow.

"SC_JACK_DEFAULT_OUTPUTS".setenv("");
"SC_JACK_DEFAULT_INPUTS".setenv("");

FoxDot.start;

s.waitForBoot({
    2.wait;
    StageLimiter.activate(2);
    "[CrashFoxDot] SuperCollider ready — StageLimiter active".postln;
});

// sclang stays alive via FoxDot's OSCFunc listeners (no preventProcessExit needed)
