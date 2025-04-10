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
        { text: 'PSaw()', displayText: 'PSaw' },
        { text: 'PTime()', displayText: 'PTime' },
        { text: 'PFrac()', displayText: 'PFrac' },
        { text: 'PFr()', displayText: 'PFr' },
        { text: 'lininf()', displayText: 'lininf' },
        { text: 'expinf()', displayText: 'expinf' },
        { text: 'PTimebin()', displayText: 'PTimebin' },
        { text: 'linmod()', displayText: 'linmod' },
        { text: 'PDrum()', displayText: 'PDrum' },
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
        { text: 'PDelay()', displayText: 'PDelay' },
        { text: 'PStrum()', displayText: 'PStrum' },
        { text: 'PQuicken()', displayText: 'PQuicken' },
        { text: 'PRhythm()', displayText: 'PRhythm' },
        { text: 'PJoin()', displayText: 'PJoin' },
    ],
    coolFunction: [
        { text: 'ascii_gen()', displayText: 'ascii_gen' },
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
        { text: 'masterAll()', displayText: 'masterAll' },  
        { text: 'voice_count()', displayText: 'voice_count' },  
        { text: 'random_bpm_var()', displayText: 'random_bpm_var' },  
        { text: 'random_bpm()', displayText: 'random_bpm' },  
        { text: 'setseed()', displayText: 'setseed' },  
        { text: 'linbpm()', displayText: 'linbpm' },  
        { text: 'darker()', displayText: 'darker' },  
        { text: 'lighter()', displayText: 'lighter' },  
        { text: 'drop()', displayText: 'drop' },  
        { text: 'drop_bpm()', displayText: 'drop_bpm' },  
        { text: 'chaos()', displayText: 'chaos' },
        { text: 'Clock', displayText: 'Clock' },
        { text: 'Scale.default=', displayText: 'Scale' },
        { text: 'Root.default=', displayText: 'Root' },
        { text: 'variation = Variation(16,4)', displayText: 'variation' },
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
        { text: 'start()', displayText: 'start' }, 
        { text: 'drummer()', displayText: 'drummer' },
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
        { text: 'init', displayText: 'init' },
        { text: 'screensaver', displayText: 'screensaver' },
        { text: 'home', displayText: 'home' },
        { text: 'boot', displayText: 'boot' },
        { text: 'scan', displayText: 'scan' },
        { text: 'warp', displayText: 'warp' },
        { text: 'scene', displayText: 'scene' },
        { text: 'shutdown', displayText: 'shutdown' },
        { text: 'target', displayText: 'target' },
    ],

    hint: function(cm, CodeMirror) {
        const cursor = cm.getCursor();
        const token = cm.getTokenAt(cursor);
        const line = cm.getLine(cursor.line);
        const cursorPosition = cursor.ch;
        const beforeCursor = line.slice(0, cursorPosition);
        const afterCursor = line.slice(cursorPosition);

        // Regex pour détecter un player suivi de '>>'
        // const playerPattern = /([a-zA-Z0-9]+\d*)\s*>>\s*/;
        const playerPattern = /([a-zA-Z0-9]+\d*)\s*>>\s*(\w*\(?)/;

        const matchPlayer = beforeCursor.match(playerPattern);
        const isInsideParentheses = (beforeCursor.match(/\(/g) || []).length > (beforeCursor.match(/\)/g) || []).length;        
        const afterLastClosingParenthesis = /.*\)\s*\./;
        const loopPattern = /loop\(([^,)]*)$/;
        const wavetablePattern = /wavetable\(([^,)]*)$/;
        const lostPattern =/(lost|attack)\([^)]*$/
        const scenePattern = /!/;

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
        else if (beforeCursor.trim().toLowerCase() === 'dr' && line.trim().toLowerCase() === 'dr') {
            let randomPlayer;
            do {
                randomPlayer = String.fromCharCode(97 + Math.floor(Math.random() * 26)) + Math.floor(Math.random() * 10) + ' >> ';
            } while (playersList.includes(randomPlayer));
            const drumPattern = `${randomPlayer}play("<x.><.><....>", sample=0, amp=1).sometimes("stutter")`;
            return {
                list: [{ text: drumPattern, displayText: 'Basic drum pattern' }],
                from: CodeMirror.Pos(cursor.line, 0),
                to: CodeMirror.Pos(cursor.line, line.length)
            };
        }
        else if (loopPattern.test(beforeCursor) && /^[^,)]*/.test(afterCursor)) {
            const prefix = token.string.slice(0, cursorPosition - token.start).replace(/[^a-zA-Z]/g, "");
            let filteredLoops = this.loopList.filter(loop => loop.displayText.includes(prefix));
            filteredLoops = filteredLoops.filter(loop => !loop.displayText.startsWith('AKWF'));
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
        else if (lostPattern.test(beforeCursor)) {
            const prefix = token.string.slice(0, cursorPosition - token.start).replace(/[^a-zA-Z]/g, "");
            const filteredLost = this.attackList.filter(lost => lost.displayText.includes(prefix));
            const match = line.match(/(lost|attack)\(([^)]*)\)$/);
            const start = match.index + match[0].indexOf('(') + 1;
            const endMatch = line.match(/\)/);
            const end = endMatch ? endMatch.index : cursorPosition;
            return {
              list: filteredLost.length > 0 ? filteredLost.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.attackList.sort((a, b) => a.displayText.localeCompare(b.displayText)),
              from: CodeMirror.Pos(cursor.line, start),
              to: CodeMirror.Pos(cursor.line, end),
            }
        }
        else if (scenePattern.test(beforeCursor)) {
            const prefix = token.string.slice(0, cursorPosition).replace(/[^a-zA-Z]/g, "");
            const filteredScenes = this.sceneNames.filter(scene => scene.displayText.startsWith(prefix));
            const end = line.match(/\s./)
            return {
                list: filteredScenes.length > 0 ? filteredScenes.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.sceneNames.sort((a, b) => a.displayText.localeCompare(b.displayText)),
                from: CodeMirror.Pos(cursor.line, token.start +1),
                to: CodeMirror.Pos(cursor.line, cursorPosition),
            };
        }
        else if (beforeCursor.includes('Scale.default=')) {
            const prefix = token.string.slice(0, cursorPosition).replace(/[^a-zA-Z]/g, "");
            const filteredScales = this.scales.filter(scale => scale.displayText.startsWith(prefix));
            return {
            list: filteredScales.length > 0 ? filteredScales.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.scales.sort((a, b) => a.displayText.localeCompare(b.displayText)),
            from: CodeMirror.Pos(cursor.line, token.start +1),
            to: CodeMirror.Pos(cursor.line, cursorPosition),
            };
        }

        else if (isInsideParentheses) {
            const prefix = token.string.slice(0, cursorPosition - token.start).replace(/[^a-zA-Z:]/g, "");
            let foxdotKeyword = [];
            if (prefix.startsWith('x')) {
                foxdotKeyword = this.fxList.filter(f => f.displayText.toLowerCase().startsWith(prefix.slice(1,).toLowerCase()));;
            }
            else {
                const combinedKeyword = [...this.foxKeyword, ...this.patternFunction];
                foxdotKeyword = combinedKeyword.filter(f => f.displayText.toLowerCase().startsWith(prefix.toLowerCase()));;
            }
            // const foxdotKeyword = filterKeyword.filter(f => f.displayText.toLowerCase().startsWith(prefix.toLowerCase()));
            return {
                list: foxdotKeyword.length > 0 ? foxdotKeyword.sort((a, b) => a.displayText.localeCompare(b.displayText)) : foxdotKeyword.sort((a, b) => a.displayText.localeCompare(b.displayText)),
                from: CodeMirror.Pos(cursor.line, token.start),
                to: CodeMirror.Pos(cursor.line, cursorPosition),
                };
        }
        else if (afterLastClosingParenthesis.test(beforeCursor)) {
            const prefix = token.string;
            const filteredPlayerFunction = this.playerFunction.filter(f => f.displayText.startsWith(prefix));
            return {
                list: filteredPlayerFunction.length > 0 ? filteredPlayerFunction.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.playerFunction.sort((a, b) => a.displayText.localeCompare(b.displayText)),
                from: CodeMirror.Pos(cursor.line, token.start),
                to: CodeMirror.Pos(cursor.line, cursorPosition),
            };
        }
        else if (matchPlayer) {
            // const prefix = line.slice(matchPlayer.index + matchPlayer[0].length).trim();
            const filteredSynths = this.synths.filter(synth => synth.displayText.includes(token.string));
            const synthMatch = line.match(/>>\s*([a-zA-Z0-9_]+)\(/);
            if (synthMatch) {
                const synthWithoutUndescore = filteredSynths.filter(synth => !synth.displayText.endsWith("_"));
                return {
                    list: synthWithoutUndescore.length > 0 ? synthWithoutUndescore.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.synths.sort((a, b) => a.displayText.localeCompare(b.displayText)),
                    from: CodeMirror.Pos(cursor.line, token.start),
                    to: CodeMirror.Pos(cursor.line, token.end),
                };
            } else {
                return {
                    list: filteredSynths.length > 0 ? filteredSynths.sort((a, b) => a.displayText.localeCompare(b.displayText)) : this.synths.sort((a, b) => a.displayText.localeCompare(b.displayText)),
                    from: CodeMirror.Pos(cursor.line, (token.string.trim() == "") ? token.start +1 : token.start ),
                    to: cursor,
                };
            }
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
    }
}