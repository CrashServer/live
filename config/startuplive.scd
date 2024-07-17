"SC_JACK_DEFAULT_OUTPUTS".setenv("");
"SC_JACK_DEFAULT_INPUTS".setenv("");
FoxDot.start;
s.waitForBoot(
	{StageLimiter.activate(2)
	FoxDot.midi();
});
s.makeWindow;
