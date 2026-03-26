import { playersList } from "./functionUtils";

export const foxdotAutocomplete = {
    synths: [
        {text: 'abass()', displayText: 'abass'},
        {text: 'acidbass()', displayText: 'acidbass'},
        {text: 'alva()', displayText: 'alva'},
        {text: 'ambi()', displayText: 'ambi'},
        {text: 'angst()', displayText: 'angst'},
        {text: 'arpy()', displayText: 'arpy'},
        {text: 'arpymod()', displayText: 'arpymod'},
        {text: 'audioin()', displayText: 'audioin'},
        {text: 'bass()', displayText: 'bass'},
        {text: 'bbass()', displayText: 'bbass'},
        {text: 'bell()', displayText: 'bell'},
        {text: 'bellmod()', displayText: 'bellmod'},
        {text: 'blip()', displayText: 'blip'},
        {text: 'bnoise()', displayText: 'bnoise'},
        {text: 'bounce()', displayText: 'bounce'},
        {text: 'braids()', displayText: 'braids'},
        {text: 'breakcore()', displayText: 'breakcore'},
        {text: 'brown()', displayText: 'brown'},
        {text: 'bug()', displayText: 'bug'},
        {text: 'cbass()', displayText: 'cbass'},
        {text: 'charm()', displayText: 'charm'},
        {text: 'click()', displayText: 'click'},
        {text: 'cluster()', displayText: 'cluster'},
        {text: 'combs()', displayText: 'combs'},
        {text: 'crackle()', displayText: 'crackle'},
        {text: 'creep()', displayText: 'creep'},
        {text: 'cringe()', displayText: 'cringe'},
        {text: 'crunch()', displayText: 'crunch'},
        {text: 'cs80()', displayText: 'cs80'},
        {text: 'dab()', displayText: 'dab'},
        {text: 'dafbass()', displayText: 'dafbass'},
        {text: 'dbass()', displayText: 'dbass'},
        {text: 'dblbass()', displayText: 'dblbass'},
        {text: 'dirt()', displayText: 'dirt'},
        {text: 'donk()', displayText: 'donk'},
        {text: 'donorgan()', displayText: 'donorgan'},
        {text: 'dopple()', displayText: 'dopple'},
        {text: 'dub()', displayText: 'dub'},
        {text: 'dustV()', displayText: 'dustV'},
        {text: 'ebass()', displayText: 'ebass'},
        {text: 'eeri()', displayText: 'eeri'},
        {text: 'elmbass()', displayText: 'elmbass'},
        {text: 'ews()', displayText: 'ews'},
        {text: 'faim()', displayText: 'faim'},
        {text: 'fbass()', displayText: 'fbass'},
        {text: 'feel()', displayText: 'feel'},
        {text: 'four()', displayText: 'four'},
        {text: 'fuzz()', displayText: 'fuzz'},
        {text: 'glass()', displayText: 'glass'},
        {text: 'glitchbass()', displayText: 'glitchbass'},
        {text: 'glitcher()', displayText: 'glitcher'},
        {text: 'gong()', displayText: 'gong'},
        {text: 'grat()', displayText: 'grat'},
        {text: 'guit()', displayText: 'guit'},
        {text: 'gray()', displayText: 'gray'},
        {text: 'growl()', displayText: 'growl'},
        {text: 'gsynth()', displayText: 'gsynth'},
        {text: 'hnoise()', displayText: 'hnoise'},
        {text: 'ikea()', displayText: 'ikea'},
        {text: 'jbass()', displayText: 'jbass'},
        {text: 'karp()', displayText: 'karp'},
        {text: 'keys()', displayText: 'keys'},
        {text: 'klank()', displayText: 'klank'},
        {text: 'lapin()', displayText: 'lapin'},
        {text: 'latoo()', displayText: 'latoo'},
        {text: 'lazer()', displayText: 'lazer'},
        {text: 'lbass()', displayText: 'lbass'},
        {text: 'lfnoise()', displayText: 'lfnoise'},
        {text: 'loop()', displayText: 'loop'},
        {text: 'marimba()', displayText: 'marimba'},
        {text: 'mpluck()', displayText: 'mpluck'},
        {text: 'noise()', displayText: 'noise'},
        {text: 'noloop()', displayText: 'noloop'},
        {text: 'nylon()', displayText: 'nylon'},
        {text: 'onset()', displayText: 'onset'},
        {text: 'organ()', displayText: 'organ'},
        {text: 'orient()', displayText: 'orient'},
        {text: 'orientmod()', displayText: 'orientmod'},
        {text: 'pad2()', displayText: 'pad2'},
        {text: 'pads()', displayText: 'pads'},
        {text: 'pasha()', displayText: 'pasha'},
        {text: 'pbass()', displayText: 'pbass'},
        {text: 'piano()', displayText: 'piano'},
        {text: 'pianovel()', displayText: 'pianovel'},
        {text: 'pink()', displayText: 'pink'},
        {text: 'plaits()', displayText: 'plaits'},
        {text: 'plaitsX()', displayText: 'plaitsX'},
        {text: 'play()', displayText: 'play'},
        {text: 'pluck()', displayText: 'pluck'},
        {text: 'pluck2()', displayText: 'pluck2'},
        {text: 'prof()', displayText: 'prof'},
        {text: 'prophet()', displayText: 'prophet'},
        {text: 'pulse()', displayText: 'pulse'},
        {text: 'quin()', displayText: 'quin'},
        {text: 'radio()', displayText: 'radio'},
        {text: 'rave()', displayText: 'rave'},
        {text: 'razz()', displayText: 'razz'},
        {text: 'rhodes()', displayText: 'rhodes'},
        {text: 'ripple()', displayText: 'ripple'},
        {text: 'rsin()', displayText: 'rsin'},
        {text: 'saw()', displayText: 'saw'},
        {text: 'sawbass()', displayText: 'sawbass'},
        {text: 'scatter()', displayText: 'scatter'},
        {text: 'scratch()', displayText: 'scratch'},
        {text: 'sine()', displayText: 'sine'},
        {text: 'sinepad()', displayText: 'sinepad'},
        {text: 'sitar()', displayText: 'sitar'},
        {text: 'snick()', displayText: 'snick'},
        {text: 'soft()', displayText: 'soft'},
        {text: 'soprano()', displayText: 'soprano'},
        {text: 'sos()', displayText: 'sos'},
        {text: 'space()', displayText: 'space'},
        {text: 'spark()', displayText: 'spark'},
        {text: 'splaffer()', displayText: 'splaffer'},
        {text: 'splitter()', displayText: 'splitter'},
        {text: 'squish()', displayText: 'squish'},
        {text: 'ssaw()', displayText: 'ssaw'},
        {text: 'star()', displayText: 'star'},
        {text: 'stretch()', displayText: 'stretch'},
        {text: 'subbass()', displayText: 'subbass'},
        {text: 'superbass()', displayText: 'superbass'},
        {text: 'supersaw()', displayText: 'supersaw'},
        {text: 'swell()', displayText: 'swell'},
        {text: 'swiss()', displayText: 'swiss'},
        {text: 'tb303()', displayText: 'tb303'},
        {text: 'total()', displayText: 'total'},
        {text: 'tritri()', displayText: 'tritri'},
        {text: 'twang()', displayText: 'twang'},
        {text: 'varicelle()', displayText: 'varicelle'},
        {text: 'varsaw()', displayText: 'varsaw'},
        {text: 'vati()', displayText: 'vati'},
        {text: 'video()', displayText: 'video'},
        {text: 'viola()', displayText: 'viola'},
        {text: 'virus()', displayText: 'virus'},
        {text: 'waves()', displayText: 'waves'},
        {text: 'tekno()', displayText: 'tekno'},
        {text: 'wobble()', displayText: 'wobble'},
        {text: 'zap()', displayText: 'zap'}
    ],
    foxKeyword: [
        { text: 'linvar([],[])', displayText: 'linvar' },
        { text: 'var([],[])', displayText: 'var' },
        { text: 'expvar([],[])', displayText: 'expvar' },
        { text: 'sinvar([],[])', displayText: 'sinvar' },
        { text: 'Pvar([],[])', displayText: 'Pvar' },
        { text: 'PSine()', displayText: 'PSine' },
        { text: 'PMorse()', displayText: 'PMorse' },
        { text: 'genArp()', displayText: 'genArp' },
        { text: 'PBin()', displayText: 'PBin' },
        { text: 'PHex("")', displayText: 'PHex' },
        { text: 'PSaw()', displayText: 'PSaw' },
        { text: 'PTime()', displayText: 'PTime' },
        { text: 'PFrac()', displayText: 'PFrac' },
        { text: 'PFr()', displayText: 'PFr' },
        { text: 'lininf()', displayText: 'lininf' },
        { text: 'expinf()', displayText: 'expinf' },
        { text: 'PTimebin()', displayText: 'PTimebin' },
        { text: 'linmod()', displayText: 'linmod' },
        { text: 'PDrum()', displayText: 'PDrum' },
        { text: 'gen("techno", "bass")', displayText: 'gen - melody pattern' },
        { text: 'gp("tb1")', displayText: 'gp - named melody' },
        { text: 'PChords()', displayText: 'PChords' },
        { text: 'PGauss()', displayText: 'PGauss' },
        { text: 'PLog()', displayText: 'PLog' },
        { text: 'PTrir()', displayText: 'PTrir' },
        { text: 'PCoin()', displayText: 'PCoin' },
        { text: 'PChar()', displayText: 'PChar' },
        { text: 'PMarkov()', displayText: 'PMarkov' },
        { text: 'PZero()', displayText: 'PZero' },
        { text: 'PBool()', displayText: 'PBool' },
        { text: 'melody()', displayText: 'melody' },
        { text: 'PRy()', displayText: 'PRy' },
        { text: 'norm()', displayText: 'norm' },
        { text: 'clamp()', displayText: 'clamp' },
        { text: 'lmap()', displayText: 'lmap' },
        { text: 'PRand()', displayText: 'PRand' },
        { text: 'PTuple()', displayText: 'PTuple' },
        { text: 'PWhite(0,1)', displayText: 'PWhite' },
        { text: 'PWhite(-1,1)', displayText: 'PWhite(-1,1)' },
        { text: 'PxRand()', displayText: 'PxRand' },
        { text: 'PwRand()', displayText: 'PwRand' },
        { text: 'PChain()', displayText: 'PChain' },
        { text: 'PZ12()', displayText: 'PZ12' },
        { text: 'PTree()', displayText: 'PTree' },
        { text: 'PWalk()', displayText: 'PWalk' },
        { text: 'PDelta()', displayText: 'PDelta' },
        { text: 'PSquare()', displayText: 'PSquare' },
        { text: 'PIndex()', displayText: 'PIndex' },
        { text: 'PFibMod()', displayText: 'PFibMod' },
        { text: 'PShuf()', displayText: 'PShuf' },
        { text: 'PAlt()', displayText: 'PAlt' },
        { text: 'PStretch()', displayText: 'PStretch' },
        { text: 'PPairs()', displayText: 'PPairs' },
        { text: 'PZip()', displayText: 'PZip' },
        { text: 'PZip2()', displayText: 'PZip2' },
        { text: 'PStutter()', displayText: 'PStutter' },
        { text: 'PSq()', displayText: 'PSq' },
        { text: 'P10()', displayText: 'P10' },
        { text: 'PStep()', displayText: 'PStep' },
        { text: 'PSum()', displayText: 'PSum' },
        { text: 'PRange()', displayText: 'PRange' },
        { text: 'PTri()', displayText: 'PTri' },
        { text: 'PSine()', displayText: 'PSine' },
        { text: 'PEuclid()', displayText: 'PEuclid' },
        { text: 'PEuclid2()', displayText: 'PEuclid2' },
        { text: 'PBern()', displayText: 'PBern' },
        { text: 'PBeat()', displayText: 'PBeat' },
        { text: 'PDur()', displayText: 'PDur' },
        { text: 'PDur(3,8)', displayText: 'PDur(3,8)' },
        { text: 'PDur(5,8)', displayText: 'PDur(5,8)' },
        { text: 'PBal(5,16)', displayText: 'PBal(5,16)' },
        { text: 'PDelay()', displayText: 'PDelay' },
        { text: 'PStrum()', displayText: 'PStrum' },
        { text: 'PQuicken()', displayText: 'PQuicken' },
        { text: 'PRhythm()', displayText: 'PRhythm' },
        { text: 'PJoin()', displayText: 'PJoin' },
    ],
    fFamily: [
        { text: 'fi()', displayText: 'fi - linvarIn' },
        { text: 'fo()', displayText: 'fo - linvarOut' },
        { text: 'fb()', displayText: 'fb - linvar' },
        { text: 'fe()', displayText: 'fe - expvar' },
        { text: 'fs()', displayText: 'fs - sinvar' },
        { text: 'fr()', displayText: 'fr - PWhite' },
        { text: 'fw()', displayText: 'fw - PWalk' },
        { text: 'fg()', displayText: 'fg - PGauss' },
        { text: 'ft()', displayText: 'ft - PTrir' },
        { text: 'fc()', displayText: 'fc - PCoin' },
        { text: 'fq()', displayText: 'fq - PSine' },
        { text: 'fz()', displayText: 'fz - PSaw' },
        { text: 'ff()', displayText: 'ff - PFrac' },
        { text: 'fd()', displayText: 'fd - PWalkDrunk' },
        { text: 'fl()', displayText: 'fl - PLife' },
        { text: 'fh()', displayText: 'fh - var' },
        { text: 'fn()', displayText: 'fn - linvarIn now' },
        { text: 'fon()', displayText: 'fon - linvarOut now' },
        { text: 'fbn()', displayText: 'fbn - linvar now' },
        { text: 'fen()', displayText: 'fen - expvar now' },
        { text: 'fsn()', displayText: 'fsn - Psine now' },
        { text: 'frot()', displayText: 'frot - rotate' },
        { text: 'fxr()', displayText: 'fxr - PxRand' },
        { text: 'fperlin()', displayText: 'fperlin' },
    ],
    coolFunction: [
        { text: 'ascii_gen("Crash")', displayText: 'ascii_gen' },
        { text: 'connect()', displayText: 'connect' },
        { text: 'attack()', displayText: 'attack' },
        { text: 'lost()', displayText: 'lost' },
        { text: 'psynth()', displayText: 'psynth' },
        { text: 'psample()', displayText: 'psample' },
        { text: 'pfx()', displayText: 'pfx' },
        { text: 'ploop()', displayText: 'ploop' },
        { text: 'pshort()', displayText: 'pshort' },
        { text: 'unsolo()', displayText: 'unsolo' },
        { text: 'soloRnd()', displayText: 'soloRnd' },
        { text: 'masterAll("")', displayText: 'masterAll' },
        { text: 'voice_count()', displayText: 'voice_count' },
        { text: 'random_bpm_var()', displayText: 'random_bpm_var' },
        { text: 'random_bpm()', displayText: 'random_bpm' },
        { text: 'setseed()', displayText: 'setseed' },
        { text: 'linbpm(170, 32)', displayText: 'linbpm' },
        { text: 'darker()', displayText: 'darker' },
        { text: 'lighter()', displayText: 'lighter' },
        { text: 'drop()', displayText: 'drop' },
        { text: 'drop_bpm()', displayText: 'drop_bpm' },
        { text: 'chaos()', displayText: 'chaos' },
        { text: 'Clock.bpm=', displayText: 'Clock' },
        { text: 'Scale.default=', displayText: 'Scale' },
        { text: 'Root.default=', displayText: 'Root' },
        { text: 'variation = Variation(16,4)', displayText: 'variation' },
        { text: 'Server.addFx()', displayText: 'Server.addFx' },
        { text: 'Server.removeFx()', displayText: 'Server.removeFx' },
        { text: 'Server.clearFx()', displayText: 'Server.clearFx' },
        { text: 'Server.listFx()', displayText: 'Server.listFx' },
        { text: 'Server.debugFx()', displayText: 'Server.debugFx' },
    ],
    playerFunction: [
        { text: 'gtr()', displayText: 'gtr' },
        { text: 'chroma()', displayText: 'chroma' },
        { text: 'porta()', displayText: 'porta' },
        { text: 'gtr()', displayText: 'gtr' },
        { text: 'morph()', displayText: 'morph' },
        { text: 'trim()', displayText: 'trim' },
        { text: 'unison()', displayText: 'unison' },
        { text: 'human()', displayText: 'human' },
        { text: 'fill()', displayText: 'fill' },
        { text: 'brk()', displayText: 'brk' },
        { text: 'switch()', displayText: 'switch' },
        { text: 'clone()', displayText: 'clone' },
        { text: 'once()', displayText: 'once' },
        { text: 'start(32)', displayText: 'start' },
        { text: 'drummer()', displayText: 'drummer' },
        { text: 'gen("techno", "bass")', displayText: 'gen - melody generator' },
        { text: 'pgen("techno", "bass")', displayText: 'pgen - melody player method' },
        { text: 'pgen("techno", "lead")', displayText: 'pgen - lead' },
        { text: 'pgen("techno", "pad")', displayText: 'pgen - pad' },
        { text: 'pgen("techno", "arp")', displayText: 'pgen - arp' },
        { text: 'pgen("techno", "stab")', displayText: 'pgen - stab' },
        { text: 'pgen("gesaffelstein", "bass")', displayText: 'pgen - gesaffelstein bass' },
        { text: 'pgen("metal", "bass")', displayText: 'pgen - metal bass' },
        { text: 'pgen("minimal", "bass")', displayText: 'pgen - minimal bass' },
        { text: 'pgen("dnb", "bass")', displayText: 'pgen - dnb bass' },
        { text: 'pgen("industrial", "bass")', displayText: 'pgen - industrial bass' },
        { text: 'sometimes("stutter")', displayText: 'sometimes'},
        { text: 'often()', displayText: 'often'},
        { text: 'rarely()', displayText: 'rarely'},
        { text: 'never()', displayText: 'never'},
        { text: 'solo()', displayText: 'solo'},
        { text: 'stop()', displayText: 'stop'},
        { text: 'only()', displayText: 'only'},
        { text: 'lclip()', displayText: 'lclip'},
    ],
    patternFunction: [
        { text: 'renv()', displayText: 'renv' },
        { text: 'offadd()', displayText: 'offadd' },
        { text: 'offmul()', displayText: 'offmul' },
        { text: 'amen()', displayText: 'amen' },
        { text: 'bubble()', displayText: 'bubble' },
    ],
    drumPatterns: [
        { text: 'pbuild("techno")', displayText: 'pbuild("techno")' },
        { text: 'pbuild("ebm")', displayText: 'pbuild("ebm")' },
        { text: 'pbuild("dnb")', displayText: 'pbuild("dnb")' },
        { text: 'pbuild("house")', displayText: 'pbuild("house")' },
        { text: 'pbuild("breaks")', displayText: 'pbuild("breaks")' },
        { text: 'pbuild("halftime")', displayText: 'pbuild("halftime")' },
        { text: 'pbuild("industrial")', displayText: 'pbuild("industrial")' },
        { text: 'pbuild("reggae")', displayText: 'pbuild("reggae")' },
        { text: 'pbuild("afro")', displayText: 'pbuild("afro")' },
        { text: 'pbuild("techno", 16, fill=4)', displayText: 'pbuild fill' },
        { text: 'pbuild("techno", 8, fill=4, density=0.8)', displayText: 'pbuild full' },
        { text: 'pat("t1")', displayText: 'pat("t1") techno' },
        { text: 'pat("t2")', displayText: 'pat("t2") techno' },
        { text: 'pat("t3")', displayText: 'pat("t3") techno' },
        { text: 'pat("t4")', displayText: 'pat("t4") techno' },
        { text: 'pat("t5")', displayText: 'pat("t5") techno' },
        { text: 'pat("t6")', displayText: 'pat("t6") techno' },
        { text: 'pat("e1")', displayText: 'pat("e1") ebm' },
        { text: 'pat("e2")', displayText: 'pat("e2") ebm' },
        { text: 'pat("e3")', displayText: 'pat("e3") ebm' },
        { text: 'pat("e4")', displayText: 'pat("e4") ebm' },
        { text: 'pat("e5")', displayText: 'pat("e5") ebm' },
        { text: 'pat("d1")', displayText: 'pat("d1") dnb' },
        { text: 'pat("d2")', displayText: 'pat("d2") dnb' },
        { text: 'pat("d3")', displayText: 'pat("d3") dnb' },
        { text: 'pat("d4")', displayText: 'pat("d4") dnb' },
        { text: 'pat("d5")', displayText: 'pat("d5") dnb' },
        { text: 'pat("h1")', displayText: 'pat("h1") house' },
        { text: 'pat("h2")', displayText: 'pat("h2") house' },
        { text: 'pat("h3")', displayText: 'pat("h3") house' },
        { text: 'pat("b1")', displayText: 'pat("b1") breaks' },
        { text: 'pat("b2")', displayText: 'pat("b2") breaks' },
        { text: 'pat("b3")', displayText: 'pat("b3") breaks' },
        { text: 'pat("b4")', displayText: 'pat("b4") breaks' },
        { text: 'pat("hf1")', displayText: 'pat("hf1") halftime' },
        { text: 'pat("hf2")', displayText: 'pat("hf2") halftime' },
        { text: 'pat("hf3")', displayText: 'pat("hf3") halftime' },
        { text: 'pat("i1")', displayText: 'pat("i1") industrial' },
        { text: 'pat("i2")', displayText: 'pat("i2") industrial' },
        { text: 'pat("i3")', displayText: 'pat("i3") industrial' },
        { text: 'pat("i4")', displayText: 'pat("i4") industrial' },
        { text: 'pat("rg1")', displayText: 'pat("rg1") reggae' },
        { text: 'pat("rg2")', displayText: 'pat("rg2") reggae' },
        { text: 'pat("rg3")', displayText: 'pat("rg3") reggae' },
        { text: 'pat("af1")', displayText: 'pat("af1") afro' },
        { text: 'pat("af2")', displayText: 'pat("af2") afro' },
        { text: 'pat("af3")', displayText: 'pat("af3") afro' },
    ],
    scales: [
        { text: '"aeolian"', displayText: 'aeolian' },
        { text: '"altered"', displayText: 'altered' },
        { text: '"bebopDom"', displayText: 'bebopDom' },
        { text: '"bebopDorian"', displayText: 'bebopDorian' },
        { text: '"bebopMaj"', displayText: 'bebopMaj' },
        { text: '"bebopMelMin"', displayText: 'bebopMelMin' },
        { text: '"blues"', displayText: 'blues' },
        { text: '"chinese"', displayText: 'chinese' },
        { text: '"chromatic"', displayText: 'chromatic' },
        { text: '"custom"', displayText: 'custom' },
        { text: '"default"', displayText: 'default' },
        { text: '"diminished"', displayText: 'diminished' },
        { text: '"dorian"', displayText: 'dorian' },
        { text: '"dorian2"', displayText: 'dorian2' },
        { text: '"egyptian"', displayText: 'egyptian' },
        { text: '"freq"', displayText: 'freq' },
        { text: '"halfDim"', displayText: 'halfDim' },
        { text: '"halfWhole"', displayText: 'halfWhole' },
        { text: '"harmonicMajor"', displayText: 'harmonicMajor' },
        { text: '"harmonicMinor"', displayText: 'harmonicMinor' },
        { text: '"hungarianMinor"', displayText: 'hungarianMinor' },
        { text: '"indian"', displayText: 'indian' },
        { text: '"justMajor"', displayText: 'justMajor' },
        { text: '"justMinor"', displayText: 'justMinor' },
        { text: '"locrian"', displayText: 'locrian' },
        { text: '"locrianMajor"', displayText: 'locrianMajor' },
        { text: '"lydian"', displayText: 'lydian' },
        { text: '"lydianAug"', displayText: 'lydianAug' },
        { text: '"lydianDom"', displayText: 'lydianDom' },
        { text: '"lydianMinor"', displayText: 'lydianMinor' },
        { text: '"major"', displayText: 'major' },
        { text: '"majorPentatonic"', displayText: 'majorPentatonic' },
        { text: '"melMin5th"', displayText: 'melMin5th' },
        { text: '"melodicMajor"', displayText: 'melodicMajor' },
        { text: '"melodicMinor"', displayText: 'melodicMinor' },
        { text: '"minMaj"', displayText: 'minMaj' },
        { text: '"minor"', displayText: 'minor' },
        { text: '"minorPentatonic"', displayText: 'minorPentatonic' },
        { text: '"mixolydian"', displayText: 'mixolydian' },
        { text: '"phrygian"', displayText: 'phrygian' },
        { text: '"prometheus"', displayText: 'prometheus' },
        { text: '"romanianMinor"', displayText: 'romanianMinor' },
        { text: '"susb9"', displayText: 'susb9' },
        { text: '"wholeHalf"', displayText: 'wholeHalf' },
        { text: '"wholeTone"', displayText: 'wholeTone' },
        { text: '"yu"', displayText: 'yu' },
        { text: '"zhi"', displayText: 'zhi' }
    ],
    loopList: [
        { text: '"break4", dur=4,', displayText: 'break4' },
    ],
    fxList: [
        { text: 'vib=', displayText: 'vib' },
        { text: 'slide=', displayText: 'slide' },
        { text: 'slidefrom=', displayText: 'slidefrom' },
        { text: 'bend=', displayText: 'bend' },
        { text: 'coarse=', displayText: 'coarse' },
        { text: 'striate=', displayText: 'striate' },
        { text: 'pshift=', displayText: 'pshift' },
        { text: 'hpf=', displayText: 'hpf' },
        { text: 'lpf=', displayText: 'lpf' },
        { text: 'swell=', displayText: 'swell' },
        { text: 'bpf=', displayText: 'bpf' },
        { text: 'crush=', displayText: 'crush' },
        { text: 'dist=', displayText: 'dist' },
        { text: 'spin=', displayText: 'spin' },
        { text: 'cut=', displayText: 'cut' },
        { text: 'room=', displayText: 'room' },
        { text: 'leg=', displayText: 'leg' },
        { text: 'glide=', displayText: 'glide' },
        { text: 'spf=', displayText: 'spf' },
        { text: 'test=', displayText: 'test' },
        { text: 'mpf=', displayText: 'mpf' },
        { text: 'dfm=', displayText: 'dfm' },
        { text: 'valad=', displayText: 'valad' },
        { text: 'vadiod=', displayText: 'vadiod' },
        { text: 'dafilter=', displayText: 'dafilter' },
        { text: 'fm_sin=', displayText: 'fm_sin' },
        { text: 'fm_saw=', displayText: 'fm_saw' },
        { text: 'fm_pulse=', displayText: 'fm_pulse' },
        { text: 'disto=', displayText: 'disto' },
        { text: 'chop=', displayText: 'chop' },
        { text: 'tremolo=', displayText: 'tremolo' },
        { text: 'echo=', displayText: 'echo' },
        { text: 'pong=', displayText: 'pong' },
        { text: 'flanger=', displayText: 'flanger' },
        { text: 'formant=', displayText: 'formant' },
        { text: 'shape=', displayText: 'shape' },
        { text: 'drive=', displayText: 'drive' },
        { text: 'tanh=', displayText: 'tanh' },
        { text: 'dist2=', displayText: 'dist2' },
        { text: 'fdist=', displayText: 'fdist' },
        { text: 'fdistc=', displayText: 'fdistc' },
        { text: 'chorus=', displayText: 'chorus' },
        { text: 'dubd=', displayText: 'dubd' },
        { text: 'octafuz=', displayText: 'octafuz' },
        { text: 'tek=', displayText: 'tek' },
        { text: 'krush=', displayText: 'krush' },
        { text: 'drop=', displayText: 'drop' },
        { text: 'squiz=', displayText: 'squiz' },
        { text: 'triode=', displayText: 'triode' },
        { text: 'octer=', displayText: 'octer' },
        { text: 'feed=', displayText: 'feed' },
        { text: 'a=', displayText: 'a' },
        { text: 'r=', displayText: 'r' },
        { text: 'ehpf=', displayText: 'ehpf' },
        { text: 'elpf=', displayText: 'elpf' },
        { text: 'position=', displayText: 'position' },
        { text: 'ring=', displayText: 'ring' },
        { text: 'shift=', displayText: 'shift' },
        { text: 'comp=', displayText: 'comp' },
        { text: 'mu=', displayText: 'mu' },
        { text: 'sidechain=', displayText: 'sidechain' },
        { text: 'lofi=', displayText: 'lofi' },
        { text: 'fold=', displayText: 'fold' },
        { text: 'low=', displayText: 'low' },
        { text: 'mid=', displayText: 'mid' },
        { text: 'high=', displayText: 'high' },
        { text: 'djf=', displayText: 'djf' },
        { text: 'phaser=', displayText: 'phaser' },
        { text: 'ringz=', displayText: 'ringz' },
        { text: 'resonz=', displayText: 'resonz' },
        { text: 'room2=', displayText: 'room2' },
        { text: 'mverb=', displayText: 'mverb' },
        { text: 'stut=', displayText: 'stut' },
        { text: 'sbrk=', displayText: 'sbrk' },
        { text: 'clouds=', displayText: 'clouds' },
        { text: 'mring=', displayText: 'mring' },
        { text: 'blow=', displayText: 'blow' },
        { text: 'panR=', displayText: 'panR' },
        { text: 'vol=', displayText: 'vol' },
        { text: 'fx1=', displayText: 'fx1' },
        { text: 'fx2=', displayText: 'fx2' },
        { text: 'fx=', displayText: 'fx' },
        { text: 'output=', displayText: 'output' },
        { text: 'mon=', displayText: 'mon' }
    ],
    attackList: [
        { text: 'attackTest', displayText: 'attackTest' },
    ],
    sceneNames: [
        { text: 'boot', displayText: 'boot' },
        { text: 'startup', displayText: 'startup' },
        { text: 'clift', displayText: 'clift' },
        { text: 'stock', displayText: 'stock' },
        { text: 'audio', displayText: 'audio' },
        { text: 'video', displayText: 'video' },
        { text: 'war', displayText: 'war' },
        //{ text: 'game', displayText: 'game' },
        { text: 'server', displayText: 'server' },
        { text: 'end', displayText: 'end' },
    ],
    serverFunction: [

    ],

    _currentView: 'categories',
    _currentCategory: null,
    _currentCategoryType: null,
    _completionWidget: null,
    attackCategories: {},
    fxCategories: {},
    synthCategories: {},

    hint: function(cm, CodeMirror) {
        const cursor = cm.getCursor();
        const token = this.getEffectiveToken(cm, cursor);
        const line = cm.getLine(cursor.line);
        const cursorPosition = cursor.ch;
        const beforeCursor = line.slice(0, cursorPosition);
        const afterCursor = line.slice(cursorPosition);

        // Reset view state for new hints
        this._currentView = 'categories';
        this._currentCategory = null;

        // Regex pour détecter un player suivi de '>>'
        const playerPattern = /([a-zA-Z0-9]+\d*)\s*>>\s*(\w*\(?)/;

        const matchPlayer = beforeCursor.match(playerPattern);
        const isInsideParentheses = (beforeCursor.match(/\(/g) || []).length > (beforeCursor.match(/\)/g) || []).length;
        const afterLastClosingParenthesis = /.*\)\s*\./;
        const loopPattern = /(loop|gsynth|splaffer|splitter|breakcore)\(([^,)]*)$/;
        const wavetablePattern = /wavetable\(([^,)]*)$/;
        const lostPattern =/(lost|attack|fire|compose|sections)\([^)]*$/
        const pbuildPattern = /pbuild\(([^)]*)$/;
        const patPattern = /pat\(([^)]*)$/;
        const pgenPattern = /\.pgen\(([^)]*)$/;
        const genPattern = /(?<!\.)gen\(([^)]*)$/;
        const gpPattern = /gp\(([^)]*)$/;
        const scenePattern = /!/;

        // Random player name suggestion
        if (beforeCursor.trim() === '' && afterCursor.trim() === '') {
            let randomPlayer;
            do {
                randomPlayer = String.fromCharCode(97 + Math.floor(Math.random() * 26)) + Math.floor(Math.random() * 10) + ' >> ';
            } while (playersList.includes(randomPlayer));
            return {
                list: [{ text: randomPlayer, displayText: randomPlayer }],
                from: CodeMirror.Pos(cursor.line, 0),
                to: CodeMirror.Pos(cursor.line, cursor.ch),
            };
        }
        // drum player suggestion
        else if (beforeCursor.trim().toLowerCase() === 'dr' && line.trim().toLowerCase() === 'dr') {
            let randomPlayer;
            do {
                randomPlayer = String.fromCharCode(97 + Math.floor(Math.random() * 26)) + Math.floor(Math.random() * 10) + ' >> ';
            } while (playersList.includes(randomPlayer));
            const drumPattern = `${randomPlayer}play("<x.><.><....>", sample=9, amp=1).sometimes("stutter")`;
            return {
                list: [{ text: drumPattern, displayText: 'Basic drum pattern' }],
                from: CodeMirror.Pos(cursor.line, 0),
                to: CodeMirror.Pos(cursor.line, line.length)
            };
        }
        // loop suggestion
        else if (loopPattern.test(beforeCursor) && /^[^,)]*/.test(afterCursor)) {
            const prefix = token.string.slice(0, cursorPosition - token.start).replace(/[^a-zA-Z]/g, "");
            let filteredLoops = this.loopList.filter(loop => loop.displayText.includes(prefix));
            filteredLoops = filteredLoops.filter(loop => !loop.displayText.startsWith('AKWF'));
            const loopMatch = line.match(/loop|gsynth|splaffer|splitter|breakcore\("([^"]*)"/);
            const durMatch = line.match(/dur=(\d+(\.\d+)?|\d+\/\d+)/);
            const loopStart = loopMatch ? token.start : token.start;
            const loopEnd = durMatch ? durMatch.index + durMatch[0].length : cursorPosition;
            return {
              list: filteredLoops.length > 0 ? filteredLoops.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.loopList.sort((a, b) => a.displayText.localeCompare(b.displayText)),
              from: CodeMirror.Pos(cursor.line, loopStart + (prefix.length === 0 ? 1 : 0)),
              to: CodeMirror.Pos(cursor.line, loopEnd),
            }
        }
        // wavetable suggestion
        else if (wavetablePattern.test(beforeCursor) && /^[^,)]*/.test(afterCursor)) {
            const prefix = token.string.slice(0, cursorPosition - token.start).replace(/[^a-zA-Z]/g, "");
            let filteredLoops = this.loopList.filter(loop => loop.displayText.includes(prefix));
            filteredLoops = filteredLoops.filter(loop => loop.displayText.startsWith('AKWF'));
            const loopMatch = line.match(/loop\("([^"]*)"/);
            const durMatch = line.match(/dur=(\d+(\.\d+)?|\d+\/\d+)/);
            const loopStart = loopMatch ? token.start : token.start;
            const loopEnd = durMatch ? durMatch.index + durMatch[0].length : cursorPosition;
            return {
              list: filteredLoops.length > 0 ? filteredLoops.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.loopList.sort((a, b) => a.displayText.localeCompare(b.displayText)),
              from: CodeMirror.Pos(cursor.line, loopStart + (prefix.length === 0 ? 1 : 0)),
              to: CodeMirror.Pos(cursor.line, loopEnd),
            }
        }
        // pbuild() — suggest genres and params inside parentheses
        else if (pbuildPattern.test(beforeCursor)) {
            const match = beforeCursor.match(pbuildPattern);
            const content = match[1]; // content inside pbuild(...)
            const functionStart = beforeCursor.lastIndexOf('pbuild(') + 7;
            const closingParen = line.indexOf(')', functionStart);
            const end = closingParen !== -1 ? closingParen : cursorPosition;

            // After first arg (comma present) — show params
            if (content.includes(',')) {
                const params = [
                    { text: 'fill=4', displayText: 'fill=4 — drum fill every N bars' },
                    { text: 'density=0.7', displayText: 'density — 0.0-1.0 hit density' },
                    { text: 'mute="hat"', displayText: 'mute — silence layers' },
                    { text: 'mute="snare"', displayText: 'mute="snare"' },
                    { text: 'mute="kick"', displayText: 'mute="kick"' },
                    { text: 'seed=42', displayText: 'seed — reproducible pattern' },
                    { text: 'kick="X   X X X   X   "', displayText: 'kick — override kick' },
                    { text: 'hat="----------------"', displayText: 'hat — override hat' },
                    { text: 'snare="    o       o   "', displayText: 'snare — override snare' },
                ];
                return {
                    list: params,
                    from: CodeMirror.Pos(cursor.line, cursorPosition),
                    to: CodeMirror.Pos(cursor.line, cursorPosition),
                };
            }

            // First arg — show genres
            const genres = [
                { text: '"techno"', displayText: 'techno' },
                { text: '"ebm"', displayText: 'ebm' },
                { text: '"dnb"', displayText: 'dnb' },
                { text: '"house"', displayText: 'house' },
                { text: '"breaks"', displayText: 'breaks' },
                { text: '"halftime"', displayText: 'halftime' },
                { text: '"industrial"', displayText: 'industrial' },
                { text: '"reggae"', displayText: 'reggae' },
                { text: '"afro"', displayText: 'afro' },
            ];
            const prefix = content.replace(/["']/g, '').trim().toLowerCase();
            const filtered = prefix.length > 0
                ? genres.filter(g => g.displayText.startsWith(prefix))
                : genres;
            return {
                list: filtered,
                from: CodeMirror.Pos(cursor.line, functionStart),
                to: CodeMirror.Pos(cursor.line, end),
            };
        }
        // pat() — suggest pattern codes inside parentheses
        else if (patPattern.test(beforeCursor)) {
            const match = beforeCursor.match(patPattern);
            const content = match[1];
            const functionStart = beforeCursor.lastIndexOf('pat(') + 4;
            const closingParen = line.indexOf(')', functionStart);
            const end = closingParen !== -1 ? closingParen : cursorPosition;

            const codes = [
                { text: '"t1"', displayText: 't1 — techno 1' },
                { text: '"t2"', displayText: 't2 — techno 2' },
                { text: '"t3"', displayText: 't3 — techno 3' },
                { text: '"t4"', displayText: 't4 — techno 4' },
                { text: '"t5"', displayText: 't5 — techno 5' },
                { text: '"t6"', displayText: 't6 — techno 6' },
                { text: '"e1"', displayText: 'e1 — ebm 1' },
                { text: '"e2"', displayText: 'e2 — ebm 2' },
                { text: '"e3"', displayText: 'e3 — ebm 3' },
                { text: '"e4"', displayText: 'e4 — ebm 4' },
                { text: '"e5"', displayText: 'e5 — ebm 5' },
                { text: '"d1"', displayText: 'd1 — dnb 1' },
                { text: '"d2"', displayText: 'd2 — dnb 2' },
                { text: '"d3"', displayText: 'd3 — dnb 3' },
                { text: '"d4"', displayText: 'd4 — dnb 4' },
                { text: '"d5"', displayText: 'd5 — dnb 5' },
                { text: '"h1"', displayText: 'h1 — house 1' },
                { text: '"h2"', displayText: 'h2 — house 2' },
                { text: '"h3"', displayText: 'h3 — house 3' },
                { text: '"b1"', displayText: 'b1 — breaks 1' },
                { text: '"b2"', displayText: 'b2 — breaks 2' },
                { text: '"b3"', displayText: 'b3 — breaks 3' },
                { text: '"b4"', displayText: 'b4 — breaks 4' },
                { text: '"hf1"', displayText: 'hf1 — halftime 1' },
                { text: '"hf2"', displayText: 'hf2 — halftime 2' },
                { text: '"hf3"', displayText: 'hf3 — halftime 3' },
                { text: '"i1"', displayText: 'i1 — industrial 1' },
                { text: '"i2"', displayText: 'i2 — industrial 2' },
                { text: '"i3"', displayText: 'i3 — industrial 3' },
                { text: '"i4"', displayText: 'i4 — industrial 4' },
                { text: '"rg1"', displayText: 'rg1 — reggae 1' },
                { text: '"rg2"', displayText: 'rg2 — reggae 2' },
                { text: '"rg3"', displayText: 'rg3 — reggae 3' },
                { text: '"af1"', displayText: 'af1 — afro 1' },
                { text: '"af2"', displayText: 'af2 — afro 2' },
                { text: '"af3"', displayText: 'af3 — afro 3' },
            ];
            const prefix = content.replace(/["']/g, '').trim().toLowerCase();
            const filtered = prefix.length > 0
                ? codes.filter(c => c.displayText.toLowerCase().startsWith(prefix))
                : codes;
            return {
                list: filtered,
                from: CodeMirror.Pos(cursor.line, functionStart),
                to: CodeMirror.Pos(cursor.line, end),
            };
        }
        // pgen() / gen() — suggest genres then roles inside parentheses
        else if (pgenPattern.test(beforeCursor) || genPattern.test(beforeCursor)) {
            const isPgen = pgenPattern.test(beforeCursor);
            const match = beforeCursor.match(isPgen ? pgenPattern : genPattern);
            const content = match[1];
            const funcStr = isPgen ? '.pgen(' : 'gen(';
            const functionStart = beforeCursor.lastIndexOf(funcStr) + funcStr.length;
            const closingParen = line.indexOf(')', functionStart);
            const end = closingParen !== -1 ? closingParen : cursorPosition;

            // Count commas to detect which argument
            const commaCount = (content.match(/,/g) || []).length;

            if (commaCount >= 2) {
                // Third+ arg — show params
                const params = [
                    { text: 'seed=42', displayText: 'seed — reproducible' },
                    { text: 'idx=0', displayText: 'idx — specific pattern' },
                ];
                return {
                    list: params,
                    from: CodeMirror.Pos(cursor.line, cursorPosition),
                    to: CodeMirror.Pos(cursor.line, cursorPosition),
                };
            }

            if (commaCount === 1) {
                // Second arg — show roles
                const roles = [
                    { text: '"bass"', displayText: 'bass' },
                    { text: '"lead"', displayText: 'lead' },
                    { text: '"pad"', displayText: 'pad' },
                    { text: '"arp"', displayText: 'arp' },
                    { text: '"stab"', displayText: 'stab' },
                ];
                const afterComma = content.split(',').pop().trim();
                const prefix = afterComma.replace(/["'\s]/g, '').toLowerCase();
                const filtered = prefix.length > 0
                    ? roles.filter(r => r.displayText.startsWith(prefix))
                    : roles;
                const commaPos = content.lastIndexOf(',');
                const roleStart = functionStart + commaPos + 1;
                return {
                    list: filtered,
                    from: CodeMirror.Pos(cursor.line, roleStart),
                    to: CodeMirror.Pos(cursor.line, end),
                };
            }

            // First arg — show genres
            const genres = [
                { text: '"techno"', displayText: 'techno' },
                { text: '"gesaffelstein"', displayText: 'gesaffelstein' },
                { text: '"minimal"', displayText: 'minimal' },
                { text: '"metal"', displayText: 'metal' },
                { text: '"dnb"', displayText: 'dnb' },
                { text: '"dub"', displayText: 'dub' },
                { text: '"ebm"', displayText: 'ebm' },
                { text: '"acid"', displayText: 'acid' },
                { text: '"ambient"', displayText: 'ambient' },
                { text: '"industrial"', displayText: 'industrial' },
                { text: '"idm"', displayText: 'idm' },
            ];
            const prefix = content.replace(/["']/g, '').trim().toLowerCase();
            const filtered = prefix.length > 0
                ? genres.filter(g => g.displayText.startsWith(prefix))
                : genres;
            return {
                list: filtered,
                from: CodeMirror.Pos(cursor.line, functionStart),
                to: CodeMirror.Pos(cursor.line, end),
            };
        }
        // gp() — suggest named pattern codes
        else if (gpPattern.test(beforeCursor)) {
            const match = beforeCursor.match(gpPattern);
            const content = match[1];
            const functionStart = beforeCursor.lastIndexOf('gp(') + 3;
            const closingParen = line.indexOf(')', functionStart);
            const end = closingParen !== -1 ? closingParen : cursorPosition;

            const codes = [
                { text: '"tb1"', displayText: 'tb1 — techno bass' },
                { text: '"tl1"', displayText: 'tl1 — techno lead' },
                { text: '"tp1"', displayText: 'tp1 — techno pad' },
                { text: '"ta1"', displayText: 'ta1 — techno arp' },
                { text: '"ts1"', displayText: 'ts1 — techno stab' },
                { text: '"gb1"', displayText: 'gb1 — gesaffelstein bass' },
                { text: '"gl1"', displayText: 'gl1 — gesaffelstein lead' },
                { text: '"gs1"', displayText: 'gs1 — gesaffelstein stab' },
                { text: '"mb1"', displayText: 'mb1 — minimal bass' },
                { text: '"ml1"', displayText: 'ml1 — minimal lead' },
                { text: '"mtb1"', displayText: 'mtb1 — metal bass' },
                { text: '"mtl1"', displayText: 'mtl1 — metal lead' },
                { text: '"db1"', displayText: 'db1 — dnb bass' },
                { text: '"dl1"', displayText: 'dl1 — dnb lead' },
                { text: '"dub1"', displayText: 'dub1 — dub bass' },
                { text: '"dul1"', displayText: 'dul1 — dub lead' },
                { text: '"eb1"', displayText: 'eb1 — ebm bass' },
                { text: '"el1"', displayText: 'el1 — ebm lead' },
                { text: '"acb1"', displayText: 'acb1 — acid bass' },
                { text: '"amp1"', displayText: 'amp1 — ambient pad' },
                { text: '"ib1"', displayText: 'ib1 — industrial bass' },
                { text: '"idb1"', displayText: 'idb1 — idm bass' },
                { text: '"idl1"', displayText: 'idl1 — idm lead' },
            ];
            const prefix = content.replace(/["']/g, '').trim().toLowerCase();
            const filtered = prefix.length > 0
                ? codes.filter(c => c.displayText.toLowerCase().includes(prefix))
                : codes;
            return {
                list: filtered,
                from: CodeMirror.Pos(cursor.line, functionStart),
                to: CodeMirror.Pos(cursor.line, end),
            };
        }
        // lost, attack, fire, compose, sections suggestion
        else if (lostPattern.test(beforeCursor)) {
            const prefix = token.string.slice(0, cursorPosition - token.start).replace(/[^a-zA-Z]/g, "");
            const match = line.match(/(lost|attack|fire|compose|sections)\(([^)]*)\)?$/);

            if (!match) return null;

            const funcName = match[1];
            const functionStart = match.index + match[0].indexOf('(') + 1;
            const content = match[2]; // Content between parentheses

            // Detect if we're on the second argument (section name)
            // e.g. fire("edge93", "intro") — cursor after the comma
            const secondArgFuncs = ['fire', 'compose', 'attack'];
            const commaMatch = content.match(/^["']([^"']+)["']\s*,\s*(.*)$/);
            const isSecondArg = secondArgFuncs.includes(funcName) && commaMatch;

            if (isSecondArg) {
                // Second argument: show sections for the matched attack
                const attackName = commaMatch[1];
                const secContent = commaMatch[2]; // what's after the comma
                const secPrefix = secContent.replace(/["']/g, '').trim().toLowerCase();

                // Find attack in attackList
                const attackItem = this.attackList.find(a => a.displayText === attackName);
                const sections = (attackItem && attackItem.sections) || [];

                if (sections.length === 0) {
                    return null; // No sections available
                }

                // Build section hints
                let sectionHints = sections.map(s => ({
                    text: `"${s.name}"`,
                    displayText: s.name + (s.beats ? ` (${s.beats}b)` : ''),
                }));

                if (secPrefix.length > 0) {
                    sectionHints = sectionHints.filter(s => s.displayText.toLowerCase().includes(secPrefix));
                }

                // Calculate replacement range for second arg
                const commaPos = content.indexOf(',');
                const secStart = functionStart + commaPos + 1;
                // Find where to end replacement
                const closingParen = line.indexOf(')', secStart);
                const secEnd = closingParen !== -1 ? closingParen : cursorPosition;

                return {
                    list: sectionHints,
                    from: CodeMirror.Pos(cursor.line, secStart),
                    to: CodeMirror.Pos(cursor.line, secEnd),
                };
            }

            // First argument: show attack names (existing behavior)
            let start, end;

            if (content.trim() === '') {
                start = functionStart;
                end = functionStart;
            } else if (content.includes('"') || content.includes("'")) {
                start = functionStart;
                const closingParen = line.indexOf(')', functionStart);
                end = closingParen !== -1 ? closingParen : cursorPosition;
            } else {
                start = functionStart;
                const closingParen = line.indexOf(')', functionStart);
                end = closingParen !== -1 ? closingParen : cursorPosition;
            }

            let filteredLost = [];

            // If there's a prefix, filter attacks
            if (prefix.length > 0) {
                filteredLost = this.attackList.filter(lost => lost.displayText.toLowerCase().includes(prefix.toLowerCase()));
                filteredLost.sort((a, b) => a.displayText.localeCompare(b.displayText));
            } else {
                // No prefix: show categories only
                // Add "All" category first
                filteredLost.push(this.createCategorySeparator("All", "All", "attack"));

                // Add other categories sorted alphabetically
                const sortedCategories = Object.keys(this.attackCategories)
                    .filter(key => key && key.trim() !== "" && key !== "Uncategorized")
                    .sort((a, b) => a.localeCompare(b));

                sortedCategories.forEach(categoryKey => {
                    filteredLost.push(this.createCategorySeparator(categoryKey, categoryKey, "attack"));
                });
            }

            return {
              list: filteredLost,
              from: CodeMirror.Pos(cursor.line, start),
              to: CodeMirror.Pos(cursor.line, end),
            }
        }
        // Scene suggestion
        else if (scenePattern.test(beforeCursor)) {
            const prefix = token.string.slice(0, cursorPosition).replace(/[^a-zA-Z]/g, "");
            const filteredScenes = this.sceneNames.filter(scene => scene.displayText.startsWith(prefix));
            const end = line.match(/\s./)
            return {
                list: filteredScenes.length > 0 ? filteredScenes : this.sceneNames,
                from: CodeMirror.Pos(cursor.line, token.start +1),
                to: CodeMirror.Pos(cursor.line, cursorPosition),
            };
        }
        // Scale suggestion
        else if (beforeCursor.includes('Scale.default=')) {
            const prefix = token.string.slice(0, cursorPosition).replace(/[^a-zA-Z]/g, "");
            const filteredScales = this.scales.filter(scale => scale.displayText.startsWith(prefix));
            return {
            list: filteredScales.length > 0 ? filteredScales.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.scales.sort((a, b) => a.displayText.localeCompare(b.displayText)),
            from: CodeMirror.Pos(cursor.line, token.start +1),
            to: CodeMirror.Pos(cursor.line, cursorPosition),
            };
        }
        // Fx, keyword, player function suggestion
        else if (isInsideParentheses) {
            const prefix = token.string.slice(0, cursorPosition - token.start).replace(/[^a-zA-Z:]/g, "");
            let foxdotKeyword = [];

            // Fx suggestion
            if (prefix.startsWith('x')) {
                const fxPrefix = prefix.slice(1,).toLowerCase();

                // Si on tape juste 'x' sans autre caractère, afficher les catégories
                if (fxPrefix === '') {
                    // Add "All" category first
                    foxdotKeyword.push(this.createCategorySeparator("All", "All", "fx"));

                    // Add other categories sorted alphabetically
                    const sortedFxCategories = Object.keys(this.fxCategories)
                        .filter(key => key && key.trim() !== "" && key !== "Uncategorized")
                        .sort((a, b) => a.localeCompare(b));

                    sortedFxCategories.forEach(categoryKey => {
                        foxdotKeyword.push(this.createCategorySeparator(categoryKey, categoryKey, "fx"));
                    });
                } else {
                    // Si on a tapé plus que 'x', filtrer les FX
                    foxdotKeyword = this.fxList.filter(f => f.displayText.toLowerCase().startsWith(fxPrefix));
                }
            }
            // Keyword and pattern function suggestion
            else {
                const combinedKeyword = [...this.foxKeyword, ...this.patternFunction, ...this.fFamily, ...this.drumPatterns];
                foxdotKeyword = combinedKeyword.filter(f => f.displayText.toLowerCase().startsWith(prefix.toLowerCase()));;
            }
            return {
                list: foxdotKeyword.sort((a, b) => a.displayText.localeCompare(b.displayText)),
                from: CodeMirror.Pos(cursor.line, token.start),
                to: CodeMirror.Pos(cursor.line, cursorPosition),
                };
        }
        // player function suggestion
        else if (afterLastClosingParenthesis.test(beforeCursor)) {
            const prefix = token.string;
            const filteredPlayerFunction = this.playerFunction.filter(f => f.displayText.startsWith(prefix));
            return {
                list: filteredPlayerFunction.length > 0 ? filteredPlayerFunction.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.playerFunction.sort((a, b) => a.displayText.localeCompare(b.displayText)),
                from: CodeMirror.Pos(cursor.line, token.start),
                to: CodeMirror.Pos(cursor.line, cursorPosition),
            };
        }
        // Synth suggestion
        else if (matchPlayer) {
            const prefix = token.string.slice(0, cursorPosition - token.start).replace(/[^a-zA-Z]/g, "");
            let filteredSynths = [];

            const synthPrefix = prefix.toLowerCase();

            // Détecter si des parenthèses existent déjà après le synth actuel
            const hasParenthesesAfter = afterCursor.trimStart().startsWith('(');

            if (synthPrefix === '') {
                // Add "All" category first
                filteredSynths.push(this.createCategorySeparator("All", "All", "synth"));

                // Add other categories sorted alphabetically
                const sortedSynthCategories = Object.keys(this.synthCategories)
                    .filter(key => key && key.trim() !== "" && key !== "Uncategorized")
                    .sort((a, b) => a.localeCompare(b));

                sortedSynthCategories.forEach(categoryKey => {
                    filteredSynths.push(this.createCategorySeparator(categoryKey, categoryKey, "synth"));
                });
            } else {
                filteredSynths = this.synths.filter(synth => synth.displayText.toLowerCase().startsWith(synthPrefix));

                // Si des parenthèses existent déjà, retirer les parenthèses du text des synths
                if (hasParenthesesAfter) {
                    filteredSynths = filteredSynths.map(synth => ({
                        text: synth.displayText, // Juste le nom, sans ()
                        displayText: synth.displayText,
                        tag: synth.tag
                    }));
                }
            }

            // Calculer le 'to' : si des parenthèses existent, remplacer jusqu'au nom du synth uniquement
            let toPos = cursor;
            if (hasParenthesesAfter && synthPrefix !== '') {
                // Trouver la position de la parenthèse ouvrante
                const openParenPos = line.indexOf('(', cursorPosition);
                if (openParenPos !== -1) {
                    toPos = CodeMirror.Pos(cursor.line, openParenPos);
                }
            }

            return {
                list: filteredSynths.length > 0 ? filteredSynths.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.synths.sort((a, b) => a.displayText.localeCompare(b.displayText)),
                from: CodeMirror.Pos(cursor.line, (token.string.trim() == "") ? token.start +1 : token.start ),
                to: toPos,
            };
        }
        else {
            const prefix = token.string.slice(0, cursorPosition).replace(/[^a-zA-Z]/g, "");
            const filteredCoolFunctions = this.coolFunction.filter(f => f.displayText.startsWith(prefix));
            return {
                list: filteredCoolFunctions.length > 0 ? filteredCoolFunctions.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.coolFunction.sort((a, b) => a.displayText.localeCompare(b.displayText)),
                from: CodeMirror.Pos(cursor.line, token.start),
                to: CodeMirror.Pos(cursor.line, cursorPosition),
            };

        }
    },

    // create separator for categories
    createCategorySeparator: function(text, categoryKey, categoryType = 'attack') {
        return {
            text: "",
            displayText: text + " →",
            className: "autocomplete-category-separator",
            categoryKey: categoryKey,
            categoryType: categoryType,
            render: function(element, self, data) {
                element.className += " autocomplete-category-separator";
                element.innerHTML = `<span class="category-text">${data.displayText}</span>`;
                element.style.cursor = 'pointer';
                element.setAttribute('data-category', data.categoryKey);
                element.setAttribute('data-category-type', data.categoryType);
            },
            hint: function(cm, self, data) {
                return false;
            }
        };
    },

    // create back button for categories
    createBackButton: function(categoryKey) {
        return {
            text: "",
            displayText: `← ${categoryKey}`,
            className: "autocomplete-back-button",
            render: function(element, self, data) {
                element.className += " autocomplete-back-button";
                element.innerHTML = `<span class="back-text">${data.displayText}</span>`;
                element.style.cursor = 'pointer';
            },
            hint: function(cm, self, data) {
                return false;
            }
        };
    },

    // Create category list
    /**
     * Extract unique categories from a list of items.
     * @param {Array} itemList - The list of items to categorize
     * @param {String} categoryField - The field name containing the category (e.g., 'category', 'tag')
     * @returns {Object} Object with unique categories as keys and their related items in array.
     * Exemple: { "Cover": [...], "Original": [...], "Remix": [...] }
     */
    getCategoriesFromList: function(itemList, categoryField = 'category') {
        if (!itemList || itemList.length === 0) {
            return {};
        }

        const categorizedItems = {};

        itemList.forEach(item => {
            const categoryString = item[categoryField] || '';

            const categories = categoryString.split(',').map(cat => cat.trim()).filter(cat => cat !== '');

            if (categories.length === 0) {
                categories.push('Uncategorized');
            }

            categories.forEach(category => {
                const normalizedCategory = category.charAt(0).toUpperCase() + category.slice(1).toLowerCase();

                if (!categorizedItems[normalizedCategory]) {
                    categorizedItems[normalizedCategory] = [];
                }

                categorizedItems[normalizedCategory].push(item);
            });
        });

        // Sort items within each category alphabetically
        Object.keys(categorizedItems).forEach(category => {
            categorizedItems[category].sort((a, b) =>
                a.displayText.localeCompare(b.displayText)
            );
        });

        return categorizedItems;
    },

    /**
     * Legacy method for backward compatibility
     */
    getAttackCategories: function() {
        return this.getCategoriesFromList(this.attackList, 'category');
    },

    /**
     * Get FX categories from the FX list
     */
    getFxCategories: function() {
        return this.getCategoriesFromList(this.fxList, 'tag');
    },

    /**
     * Get Synth categories from the Synth list
     */
    getSynthCategories: function() {
        return this.getCategoriesFromList(this.synths, 'tag');
    },

    // show elements of a category
    /**
     * Show category items with customizable rendering
     * @param {Object} cm - CodeMirror instance
     * @param {String} categoryKey - The category to display
     * @param {String} categoryType - Type of category ('attack' or 'fx')
     * @returns {Object} Hint object with list of items
     */
    showCategoryItems: function(cm, categoryKey, categoryType = 'attack') {
        let categoryItems;
        let categoriesMap;
        let allItemsList;

        // Determine which categories and items to use
        if (categoryType === 'fx') {
            categoriesMap = this.fxCategories;
            allItemsList = this.fxList;
        }
        else if (categoryType === 'synth') {
            categoriesMap = this.synthCategories;
            allItemsList = this.synths;
        }
        else {
            categoriesMap = this.attackCategories;
            allItemsList = this.attackList;
        }

        // Special case for "All" category
        if (categoryKey === "All") {
            categoryItems = [...allItemsList].sort((a, b) => a.displayText.localeCompare(b.displayText));
        } else {
            categoryItems = categoriesMap[categoryKey];
        }

        if (!categoryItems || categoryItems.length === 0) {
            return null;
        }

        // Calculer les bonnes positions from/to en fonction du type
        const cursor = cm.getCursor();
        const token = cm.getTokenAt(cursor);
        const line = cm.getLine(cursor.line);
        const afterCursor = line.slice(cursor.ch);
        let fromPos, toPos;

        if (categoryType === 'fx') {
            // Pour les FX, on doit remplacer le 'x' qui a été tapé
            // On cherche le début du token qui contient 'x'
            const tokenStr = token.string;

            // Si le token commence par 'x', on remplace depuis le début du token
            if (tokenStr.toLowerCase().startsWith('x')) {
                fromPos = cm.constructor.Pos(cursor.line, token.start);
                toPos = cm.constructor.Pos(cursor.line, cursor.ch);
            } else {
                // Sinon, utiliser la position du curseur
                fromPos = cm.getCursor();
                toPos = cm.getCursor();
            }
        } else if (categoryType === 'synth') {
            // Pour les synths, vérifier si des parenthèses existent déjà
            const hasParenthesesAfter = afterCursor.trimStart().startsWith('(');

            // Trouver la position de début du synth (après >>)
            const playerMatch = line.match(/([a-zA-Z0-9]+\d*)\s*>>\s*/);
            if (playerMatch) {
                const synthStart = playerMatch[0].length;
                // Trouver où se termine le nom du synth actuel
                let synthEnd = cursor.ch;
                if (hasParenthesesAfter) {
                    const openParenPos = line.indexOf('(', synthStart);
                    if (openParenPos !== -1) {
                        synthEnd = openParenPos;
                    }
                }
                fromPos = cm.constructor.Pos(cursor.line, synthStart);
                toPos = cm.constructor.Pos(cursor.line, synthEnd);
            } else {
                fromPos = cm.getCursor();
                toPos = cm.getCursor();
            }
        } else {
            // Pour les attacks, on utilise la position du curseur
            fromPos = cm.getCursor();
            toPos = cm.getCursor();
        }

        const formattedItems = categoryItems.map(item => {
            if (categoryType === 'attack') {
                // Extraire le BPM (2 ou 3 chiffres après un espace)
                const bpmMatch = item.displayText.match(/\s(\d{2,4})$/);
                const bpm = bpmMatch ? bpmMatch[1] : null;

                // Nettoyer le displayText en enlevant le BPM
                let cleanName = bpm ? item.displayText.replace(/\s\d{2,4}$/, '').trim() : item.displayText;
                cleanName = cleanName.charAt(0).toUpperCase() + cleanName.slice(1);

                return {
                    text: item.text,
                    displayText: cleanName,
                    bpm: bpm,
                    render: function(element, self, data) {
                        element.innerHTML = '';

                        // Créer le nom de l'attack
                        const nameSpan = document.createElement('span');
                        nameSpan.className = 'attack-name';
                        nameSpan.textContent = data.displayText;
                        element.appendChild(nameSpan);

                        // Ajouter le tag BPM si présent
                        if (data.bpm) {
                            const bpmTag = document.createElement('span');
                            bpmTag.className = 'attack-bpm-tag';
                            bpmTag.textContent = data.bpm;
                            element.appendChild(bpmTag);
                        }
                    }
                };
            } else if (categoryType === 'fx') {
                // Pour les FX, afficher simplement le nom (avec ou sans underscore)
                return {
                    text: item.text,
                    displayText: item.displayText,
                    render: function(element, self, data) {
                        element.innerHTML = '';

                        // Créer le nom du FX
                        const nameSpan = document.createElement('span');
                        nameSpan.className = 'fx-name';
                        nameSpan.textContent = data.displayText;
                        element.appendChild(nameSpan);
                    }
                };
            } else if (categoryType === 'synth') {
                // Pour les Synths, vérifier si des parenthèses existent déjà
                const line = cm.getLine(cm.getCursor().line);
                const afterCursor = line.slice(cm.getCursor().ch);
                const hasParenthesesAfter = afterCursor.trimStart().startsWith('(');

                // Si des parenthèses existent, ne pas inclure les () dans le text
                const synthText = hasParenthesesAfter ? item.displayText : item.text;

                return {
                    text: synthText,
                    displayText: item.displayText,
                    render: function(element, self, data) {
                        element.innerHTML = '';

                        // Créer le nom du Synth
                        const nameSpan = document.createElement('span');
                        nameSpan.className = 'synth-name';
                        nameSpan.textContent = data.displayText;
                        element.appendChild(nameSpan);
                    }
                };
            }
        });

        const items = [
            this.createBackButton(categoryKey),
            ...formattedItems
        ];

        this._currentView = 'items';
        this._currentCategory = categoryKey;
        this._currentCategoryType = categoryType;

        return {
            list: items,
            from: fromPos,
            to: toPos
        };
    },

    getEffectiveToken: function(cm, cursor) {
        const token = cm.getTokenAt(cursor);

        if (token.type === "comment") {
            const line = cm.getLine(cursor.line);
            const cursorCh = cursor.ch;

            let start = cursorCh;
            let end = cursorCh;

            // Caractères valides pour un identifiant
            const validChar = /[a-zA-Z_0-9]/;

            while (start > 0 && validChar.test(line[start - 1])) {
            start--;
            }

            while (end < line.length && validChar.test(line[end])) {
            end++;
            }

            return {
            ...token,
            start: start,
            end: end,
            string: line.slice(start, end),
            type: "comment"
            };
        }

        return token;
    },
}
