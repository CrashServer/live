OSCFunc(
    {
        arg msg, time, addr, port;
        addr.sendMsg("/foxdot/cpu",
            Server.default.peakCPU,
        );
    }, '/foxdot/cpu'
);