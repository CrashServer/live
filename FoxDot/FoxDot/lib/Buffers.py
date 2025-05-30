"""

This module manages the allocation of buffer numbers and samples. To see
a list of descriptions of what sounds are mapped to what characters,
simply evaluate

    print(Samples)

Future:

Aiming on being able to set individual sample banks for different players
that can be proggrammed into performance.

"""
from __future__ import absolute_import, division, print_function

import fnmatch
import os
import wave
from contextlib import closing
from itertools import chain
from os.path import abspath, join, isabs, isfile, isdir, splitext

from .Code import WarningMsg
from .Logging import Timing
from .SCLang import SampleSynthDef
from .ServerManager import Server
from .Settings import FOXDOT_SND, FOXDOT_LOOP, SAMPLES_BANK

import json

alpha    = "abcdefghijklmnopqrstuvwxyz"

nonalpha = {"&" : "ampersand",
            "*" : "asterix",
            "@" : "at",
            "^" : "caret",
            ":" : "colon",
            "$" : "dollar",
            "=" : "equals",
            "!" : "exclamation",
            "/" : "forwardslash",
            "#" : "hash",
            "-" : "hyphen",
            "%" : "percent",
            "+" : "plus",
            "?" : "question",
            "~" : "tilde",
            "\\" :"backslash",
            "1" : "1",
            "2" : "2",
            "3" : "3",
            "4" : "4",
            "5" : "5",
            "6" : "6",
            "7" : "7",
            "8" : "8",
            "9" : "9"}

DESCRIPTIONS = { 'a' : "Gameboy hihat",      'A' : "Gameboy kick drum",
                 'b' : "Noisy beep",         'B' : "Short saw",
                 'c' : "Voice/string",       'C' : "Choral",
                 'd' : "Woodblock",          'D' : "Dirty snare",
                 'e' : "Electronic Cowbell", 'E' : "Ringing percussion",
                 'f' : "Pops",               'F' : "Trumpet stabs",
                 'g' : "Ominous",            'G' : "Ambient stabs",
                 'h' : "Finger snaps",       'H' : "Clap",
                 'i' : "Jungle snare",       'I' : "Rock snare",
                 'j' : "Whines",             'J' : "Ambient stabs",
                 'k' : "Wood shaker",        'K' : "Percussive hits",
                 'l' : "Robot noise",        'L' : "Noisy percussive hits",
                 'm' : "808 toms",           'M' : "Acoustic toms",
                 'n' : "Noise",              'N' : "Gameboy SFX",
                 'o' : "Snare drum",         'O' : "Heavy snare",
                 'p' : "Tabla",              'P' : "Tabla long",
                 'q' : "Ambient stabs",      'Q' : "Electronic stabs",
                 'r' : "Metal",              'R' : "Metallic",
                 's' : "Shaker",             'S' : "Tamborine",
                 't' : "Rimshot",            'T' : "Cowbell",
                 'u' : "Soft snare",         'U' : "Misc. Fx",
                 'v' : "Soft kick",          'V' : "Hard kick",
                 'w' : "Dub hits",           'W' : "Distorted",
                 'x' : "Bass drum",          'X' : "Heavy kick",
                 'y' : "Percussive hits",    'Y' : "High buzz",
                 'z' : "Scratch",            "Z" : "Loud stabs",
                 '-' : "Hi hat closed",      "|" : "Hangdrum",
                 '=' : "Hi hat open",        "/" : "Reverse sounds",
                 '*' : "Clap",               "\\" : "Lazer",
                 '~' : "Ride cymbal",        "%" : "Noise bursts",
                 '^' : "'Donk'",             "$" : "Beatbox",
                 '#' : "Crash",              "!" : "Yeah!",
                 '+' : "Clicks",             "&" : "Chime",
                 '@' : "Gameboy noise",      ":" : "Hi-hats",
                 '1' : "Vocals (One)",
                 '2' : 'Vocals (Two)',
                 '3' : 'Vocals (Three)',
                 '4' : 'Vocals (Four)'}

bank = SAMPLES_BANK

# Function-like class for searching directory for sample based on symbol

class _symbolToDir:

    def __init__(self, root):

        self.set_root(root)

    def set_root(self, root):
        """ Check if root is a valid directory then points FoxDot to that
            folder for searching for samples. Raises an OSError if 'root'
            is not a valid directory """

        if os.path.isdir(root):
            self.root = os.path.realpath(root)
        else:
            raise OSError("{!r} is not a valid directory".format(root))
        return

    def __call__(self, symbol, bank):
        """ Return the sample search directory for a symbol """
        if symbol.isalpha():
            return join(
                self.root,
                str(bank),
                symbol.lower(),
                'upper' if symbol.isupper() else 'lower'
            )
        elif symbol in nonalpha:
            longname = nonalpha[symbol]
            return join(self.root, str(bank), '_', longname)
        else:
            return None

symbolToDir = _symbolToDir(FOXDOT_SND) # singleton

class Buffer(object):
    def __init__(self, fn, number, channels=1):
        self.fn = fn
        self.bufnum   = int(number)
        self.channels = channels

    def __repr__(self):
        return "<Buffer num {}>".format(self.bufnum)

    def __int__(self):
        return self.bufnum

    @classmethod
    def fromFile(cls, filename, number):
        try:
            with closing(wave.open(filename)) as snd:
                numChannels = snd.getnchannels()
        except wave.Error:
            numChannels = 1
        return cls(filename, number, numChannels)


nil = Buffer('', 0)


class BufferManager(object):
    def __init__(self, server=Server, paths=()):
        self._server = server
        self._max_buffers = server.max_buffers
        # Keep buffer 0 unallocated because we use it as the "nil" buffer
        self._nextbuf = 1
        self._buffers = [None for _ in range(self._max_buffers)]
        self._fn_to_buf = {}
        self._paths = [join(FOXDOT_SND, str(bank), FOXDOT_LOOP)] + list(paths)
        self._ext = ['wav', 'wave', 'aif', 'aiff', 'flac']

        self.loops = [fn.rsplit(".",1)[0] for fn in os.listdir(join(FOXDOT_SND, str(bank), FOXDOT_LOOP))]

        # Crashmod
        # self.onsetDict = {}
        # self.loadOnset()

    def __str__(self):
        return "\n".join(["%r: %s" % (k, v) for k, v in sorted(DESCRIPTIONS.items())])

    def __repr__(self):
        return '<BufferManager>'

    def __getitem__(self, key):
        """ Short-hand access for getBufferFromSymbol() i.e. Samples['x'] """
        if isinstance(key, tuple):
            return self.getBufferFromSymbol(*key)
        return self.getBufferFromSymbol(key)

    def _reset_buffers(self):
        """ Clears the cache of loaded buffers """
        files = list(self._fn_to_buf.keys())
        self._fn_to_buf = {}
        for fn in files:
            self.loadBuffer(fn)
        return

    def reset(self):
        return self._reset_buffers()

    def _incr_nextbuf(self):
        self._nextbuf += 1
        if self._nextbuf >= self._max_buffers:
            self._nextbuf = 1

    def _getNextBufnum(self):
        """ Get the next free buffer number """
        start = self._nextbuf
        while self._buffers[self._nextbuf] is not None:
            self._incr_nextbuf()
            if self._nextbuf == start:
                raise RuntimeError("Buffers full! Cannot allocate additional buffers.")
        freebuf = self._nextbuf
        self._incr_nextbuf()
        return freebuf

    def addPath(self, path):
        """ Add a path to the search paths for samples """
        self._paths.append(abspath(path))

    def free(self, filenameOrBuf):
        """ Free a buffer. Accepts a filename or buffer number """
        if isinstance(filenameOrBuf, int):
            buf = self._buffers[filenameOrBuf]
        else:
            buf = self._fn_to_buf[filenameOrBuf]
        del self._fn_to_buf[buf.fn]
        self._buffers[buf.bufnum] = None
        self._server.bufferFree(buf.bufnum)

    def freeAll(self):
        """ Free all buffers """
        buffers = list(self._fn_to_buf.values())
        for buf in buffers:
            self.free(buf.bufnum)

    def setMaxBuffers(self, max_buffers):
        """ Set the max buffers on the SC server """
        if max_buffers < self._max_buffers:
            if any(self._buffers[max_buffers:]):
                raise RuntimeError(
                    "Cannot shrink buffer size. Buffers already allocated."
                )
            self._buffers = self._buffers[:max_buffers]
        elif max_buffers > self._max_buffers:
            while len(self._buffers) < max_buffers:
                self._buffers.append(None)
        self._max_buffers = max_buffers
        self._nextbuf = self._nextbuf % max_buffers

    def getBufferFromSymbol(self, symbol, bank, index=0):
        """ Get buffer information from a symbol """
        if symbol.isspace():
            return nil
        dirname = symbolToDir(symbol, bank)
        if dirname is None:
            return nil
        samplepath = self._findSample(dirname, index)
        if samplepath is None:
            return nil
        return self._allocateAndLoad(samplepath)

    def getBuffer(self, bufnum):
        """ Get buffer information from the buffer number """
        return self._buffers[bufnum]

    def _allocateAndLoad(self, filename, force=False):
        """ Allocates and loads a buffer from a filename, with caching """
        if filename not in self._fn_to_buf:
            bufnum = self._getNextBufnum()
            buf = Buffer.fromFile(filename, bufnum)
            self._server.bufferRead(filename, bufnum)
            self._fn_to_buf[filename] = buf
            self._buffers[bufnum] = buf
        elif force:
            buf = self._fn_to_buf[filename]
            self._server.bufferRead(filename, buf.bufnum)
        return self._fn_to_buf[filename]
    
    def _allocateAndLoadMono(self, filename, force=False):
        """ Allocates and loads a buffer from a filename, with caching """
        if filename not in self._fn_to_buf:
            bufnum = self._getNextBufnum()
            buf = Buffer.fromFile(filename, bufnum)
            self._server.bufferReadMono(filename, bufnum)
            self._fn_to_buf[filename] = buf
            self._buffers[bufnum] = buf
        elif force:
            buf = self._fn_to_buf[filename]
            self._server.bufferReadMono(filename, buf.bufnum)
        return self._fn_to_buf[filename]

    def reload(self, filename):
        return self.loadBuffer(filename, force=True)

    def _getSoundFile(self, filename):
        """ Look for a file with all possible extensions """
        base, cur_ext = splitext(filename)
        if cur_ext:
            # If the filename already has an extensions, keep it
            if isfile(filename):
                return filename
        else:
            # Otherwise, look for all possible extensions
            for ext in self._ext:
                # Look for .wav and .WAV
                for tryext in [ext, ext.upper()]:
                    extpath = filename + '.' + tryext
                    if isfile(extpath):
                        return extpath
        return None

    def _getSoundFileOrDir(self, filename):
        """ Get a matching sound file or directory """
        if isdir(filename):
            return abspath(filename)
        foundfile = self._getSoundFile(filename)
        if foundfile:
            return abspath(foundfile)
        return None

    def _searchPaths(self, filename):
        """ Search our search paths for an audio file or directory """
        if isabs(filename):
            return self._getSoundFileOrDir(filename)
        else:
            for root in self._paths:
                fullpath = join(root, filename)
                foundfile = self._getSoundFileOrDir(fullpath)
                if foundfile:
                    return foundfile
        return None

    def _getFileInDir(self, dirname, index):
        """ Return nth sample in a directory """
        candidates = []
        for filename in sorted(os.listdir(dirname)):
            name, ext = splitext(filename)
            if ext.lower()[1:] in self._ext:
                fullpath = join(dirname, filename)
                if len(candidates) == index:
                    return fullpath
                candidates.append(fullpath)
        if candidates:
            return candidates[int(index) % len(candidates)]
        return None

    def _patternSearch(self, filename, index):
        """
        Return nth sample that matches a path pattern

        Path pattern is a relative path that can contain wildcards such as *
        and ? (see fnmatch for more details). Some example paths:

            samp*
            **/voices/*
            perc*/bass*

        """

        def _findNextSubpaths(path, pattern):
            """ For a path pattern, find all subpaths that match """
            # ** is a special case meaning "all recursive directories"
            if pattern == '**':
                for dirpath, _, _ in os.walk(path):
                    yield dirpath
            else:
                children = os.listdir(path)
                for c in fnmatch.filter(children, pattern):
                    yield join(path, c)

        candidates = []
        queue = self._paths[:]
        subpaths = filename.split(os.sep)
        filepat = subpaths.pop()
        while subpaths:
            subpath = subpaths.pop(0)
            queue = list(chain.from_iterable(
                (_findNextSubpaths(p, subpath) for p in queue)
            ))

        # If the filepat (ex. 'foo*.wav') has an extension, we want to match
        # the full filename. If not, we just match against the basename.
        match_base = not hasext(filepat)

        for path in queue:
            for subpath, _, filenames in os.walk(path):
                for filename in sorted(filenames):
                    basename, ext = splitext(filename)
                    if ext[1:].lower() not in self._ext:
                        continue
                    if match_base:
                        ismatch = fnmatch.fnmatch(basename, filepat)
                    else:
                        ismatch = fnmatch.fnmatch(filename, filepat)
                    if ismatch:
                        fullpath = join(subpath, filename)
                        if len(candidates) == index:
                            return fullpath
                        candidates.append(fullpath)
        if candidates:
            return candidates[index % len(candidates)]
        return None

    @Timing('bufferSearch', logargs=True)
    def _findSample(self, filename, index=0):
        """
        Find a sample from a filename or pattern

        Will first attempt to find an exact match (by abspath or relative to
        the search paths). Then will attempt to pattern match in search paths.

        """
        path = self._searchPaths(filename)
        if path:
            # If it's a file, use that sample
            if isfile(path):
                return path
            # If it's a dir, use one of the samples in that dir
            elif isdir(path):
                foundfile = self._getFileInDir(path, index)
                if foundfile:
                    return foundfile
                else:
                    WarningMsg("No sound files in %r" % path)
                    return None
            else:
                WarningMsg("File %r is neither a file nor a directory" % path)
                return None
        else:
            # If we couldn't find a dir or file with this name, then we use it
            # as a pattern and recursively walk our paths
            foundfile = self._patternSearch(filename, index)
            if foundfile:
                return foundfile
            WarningMsg("Could not find any sample matching %r" % filename)
            return None

    def loadBuffer(self, filename, index=0, force=False):
        """ Load a sample and return the number of a buffer """
        samplepath = self._findSample(filename, index)
        if samplepath is None:
            return 0
        else:
            buf = self._allocateAndLoad(samplepath, force=force)
            return buf.bufnum
        
    def loadBufferMono(self, filename, index=0, force=False):
        """ Load a sample and return the number of a buffer """
        samplepath = self._findSample(filename, index)
        if samplepath is None:
            return 0
        else:
            buf = self._allocateAndLoadMono(samplepath, force=force)
            return buf.bufnum

    ### crashmod
    # def loadOnset(self):
    #     with open(os.path.join(FOXDOT_LOOP, "onsetDict.py")) as f:
    #         self.onsetDict = json.load(f)


def hasext(filename):
    return bool(splitext(filename)[1])


Samples = BufferManager()


class LoopSynthDef(SampleSynthDef):
    def __init__(self):
        SampleSynthDef.__init__(self, "loop")
        self.pos = self.new_attr_instance("pos")
        self.sample = self.new_attr_instance("sample")
        self.beat_stretch = self.new_attr_instance("beat_stretch")
        self.filename = self.new_attr_instance("filename")
        self.looping = self.new_attr_instance("looping")
        self.clip = self.new_attr_instance("clip")
        self.defaults['pos']   = 0
        self.defaults['sample']   = 0
        self.defaults['beat_stretch'] = 1
        self.defaults['looping'] = 1.0
        self.defaults['clip'] = 0
        self.base.append("rate = (rate * (1-(beat_stretch>0))) + ((BufDur.kr(buf) / sus) * (beat_stretch>0));")
        self.base.append("rate = if(ratelfo<=0, rate, rate * SinOsc.kr(ratelfo, 0, ratelfomul, ratelfoadd));")
        self.base.append("clip = if(clip<=0, 1, (clip/sus)*0.5);")
        self.base.append("osc = PlayBuf.ar(2, buf, BufRateScale.kr(buf) * rate, startPos: BufSampleRate.kr(buf) * pos, loop: looping);")
        self.base.append("osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, (sus*clip)-0.05, 0.05]));")
        self.osc = self.osc * self.amp
        self.add()
    def __call__(self, filename, pos=0, sample=0, **kwargs):
        #kwargs["buf"] = Samples.loadBuffer(filename, sample)
        kwargs["filename"] = filename
        kwargs["sample"] = sample
        proxy = SampleSynthDef.__call__(self, pos, **kwargs)
        proxy.kwargs["filename"] = filename
        self.filename = filename
        return proxy

class NoLoopSynthDef(SampleSynthDef):
    def __init__(self):
        SampleSynthDef.__init__(self, "noloop")
        self.pos = self.new_attr_instance("start")
        self.sample = self.new_attr_instance("sample")
        self.filename = self.new_attr_instance("filename")
        self.trig = self.new_attr_instance("trig")
        self.defaults['start']   = 0
        self.defaults['sample']   = 0
        self.defaults['trig'] = 0
        # self.base.append("rate = (rate * (1-(beat_stretch>0))) + ((BufDur.kr(buf) / sus) * (beat_stretch>0));")
        self.base.append("osc = PlayBuf.ar(2, buf, BufRateScale.kr(buf) * rate, trigger: Impulse.kr(trig*sus), startPos: start * BufFrames.kr(buf), loop: 0);")
        self.base.append("osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.05, 0.05]));")
        self.osc = self.osc * self.amp
        self.add()
    def __call__(self, filename, pos=0, sample=0, **kwargs):
        kwargs["filename"] = filename
        kwargs["sample"] = sample
        proxy = SampleSynthDef.__call__(self, pos, **kwargs)
        proxy.kwargs["filename"] = filename
        self.filename = filename
        return proxy

class StretchSynthDef(SampleSynthDef):
    def __init__(self):
        SampleSynthDef.__init__(self, "stretch")
        self.base.append("osc = Warp1.ar(2, buf, Line.kr(0,1,sus), rate, windowSize: 0.2, overlaps: 4, interp:2);")
        self.base.append("osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.05, 0.05]));")
        self.osc = self.osc * self.amp
        self.add()
    def __call__(self, filename, pos=0, sample=0, **kwargs):
        kwargs["buf"] = Samples.loadBuffer(filename, sample)
        proxy = SampleSynthDef.__call__(self, pos, **kwargs)
        proxy.kwargs["filename"] = filename
        return proxy

class GranularSynthDef(SampleSynthDef):
    def __init__(self):
        SampleSynthDef.__init__(self, "gsynth")
        self.pos = self.new_attr_instance("pos")
        self.sample = self.new_attr_instance("sample")
        self.gdur = self.new_attr_instance("gdur")
        self.defaults['pos']   = 0
        self.defaults['sample']   = 0
        self.defaults['size'] = 0.5
        self.defaults['density'] = 10
        self.defaults['deg'] = 1
        self.base.append("osc = TGrains.ar(2, trigger:Impulse.ar(density), bufnum:buf, rate: deg, centerPos: pos*BufDur.kr(buf), dur: size);")
        self.base.append("osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.05, 0.05]));")
        self.osc = self.osc * self.amp * 2
        self.add()
    def __call__(self, filename, pos=0, sample=0, **kwargs):
        kwargs["buf"] = Samples.loadBufferMono(filename, sample)
        proxy = SampleSynthDef.__call__(self, pos, **kwargs)
        proxy.kwargs["filename"] = filename
        return proxy


class BreakcoreSynthDef(SampleSynthDef):
    def __init__(self):
        SampleSynthDef.__init__(self, "breakcore")
        self.sample = self.new_attr_instance("sample")
        self.core = self.new_attr_instance("core")
        self.brk = self.new_attr_instance("brk")
        self.defaults['pos']   = 0
        self.defaults['sample']   = 0
        self.defaults['core'] = 1
        self.defaults['brk'] = 12
        self.base.append("target = Array.fill([4,4,8,4,8,4,4,8,8].size, buf);")
        self.base.append("osc = Breakcore.ar(buf, playbuf,  Impulse.kr(LFNoise0.ar(4, 10, brk)), LFNoise0.kr(8, 19000*core, 2000),0);")
        self.base.append("osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.05, 0.05]));")
        self.osc = self.osc * self.amp
        self.add()
    def __call__(self, filename, pos=0, sample=0, **kwargs):
        kwargs["buf"] = Samples.loadBuffer(filename, sample)
        return SampleSynthDef.__call__(self, pos, **kwargs)

class SplitterSynthDef(SampleSynthDef):
    def __init__(self):
        SampleSynthDef.__init__(self, "splitter")
        self.pos = self.new_attr_instance("pos")
        self.sample = self.new_attr_instance("sample")
        self.rd = self.new_attr_instance("rd")
        self.beat_stretch = self.new_attr_instance("beat_stretch")
        self.filename = self.new_attr_instance("filename")
        self.defaults['pos']   = 0
        self.defaults['sample']   = 0
        self.defaults['rd'] = 0
        self.defaults['beat_stretch'] = 0
        self.base.append("rate = (rate * (1-(beat_stretch>0))) + ((BufDur.kr(buf) / ((beat_stretch<=0) + abs(beat_stretch))) * (beat_stretch>0));")
        self.base.append("osc1 = PlayBuf.ar(2,buf, BufRateScale.kr(buf)*rate, 1, BufFrames.ir(buf)*(0+pos+LFNoise1.kr(50,rd)), 0)*(EnvGen.kr(Env.perc(0.01,sus),doneAction:2)-0.001);")
        self.base.append("osc2 = PlayBuf.ar(2,buf, BufRateScale.kr(buf)*rate, 1, BufFrames.ir(buf)*(0.25+pos+LFNoise1.kr(50,rd)), 0)*(EnvGen.kr(Env.perc(0.01,sus),doneAction:2)-0.001);")
        self.base.append("osc3 = PlayBuf.ar(2,buf, BufRateScale.kr(buf)*rate, 1, BufFrames.ir(buf)*(0.5+pos+LFNoise1.kr(50,rd)), 0)*(EnvGen.kr(Env.perc(0.01,sus),doneAction:2)-0.001);")
        self.base.append("osc4 = PlayBuf.ar(2,buf, BufRateScale.kr(buf)*rate, 1, BufFrames.ir(buf)*(0.75+pos+LFNoise1.kr(50,rd)), 0)*(EnvGen.kr(Env.perc(0.01,sus),doneAction:2)-0.001);")
        self.base.append("osc = Mix(osc1+osc2+osc3+osc4);")
        self.osc = self.osc * self.amp
        self.add()
    def __call__(self, filename, pos=0, sample=0, **kwargs):
        kwargs["buf"] = Samples.loadBuffer(filename, sample)
        kwargs["filename"] = filename
        proxy = SampleSynthDef.__call__(self, pos, **kwargs)
        proxy.kwargs["filename"] = filename
        return proxy

class SplafferSynthDef(SampleSynthDef):
    def __init__(self):
        SampleSynthDef.__init__(self, "splaffer")
        self.pos = self.new_attr_instance("pos")
        self.sample = self.new_attr_instance("sample")
        self.beat_stretch = self.new_attr_instance("beat_stretch")
        self.fmod = self.new_attr_instance("fmod")
        self.defaults['pos']   = 0
        self.defaults['sample']   = 0
        self.defaults['fmod']   = 0
        self.defaults['beat_stretch'] = 0
        self.base.append("rate = (rate * (1-(beat_stretch>0))) + ((BufDur.kr(buf) / sus) * (beat_stretch>0));")
        self.base.append("posses = (pos + ((0..2)/5)).wrap(0.0, 1.0);")
        self.base.append("pitches = (0.2 * 2.0.pow(posses *rate) + SinOsc.kr(fmod, mul: fmod));")
        self.base.append("osc = PlayBuf.ar(2, buf, pitches, startPos: BufSampleRate.kr(buf) * pos, loop: 1.0);")
        self.base.append("osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.05, 0.05]));")
        self.osc = self.osc * self.amp
        self.add()
    def __call__(self, filename, pos=0, sample=0, **kwargs):
        kwargs["buf"] = Samples.loadBuffer(filename, sample)
        proxy = SampleSynthDef.__call__(self, pos, **kwargs)
        proxy.kwargs["filename"] = filename
        return proxy

# class OnsetSynthDef(SampleSynthDef):
#     def __init__(self):
#         SampleSynthDef.__init__(self, "onset")
#         self.pos = self.new_attr_instance("pos")
#         self.sample = self.new_attr_instance("sample")
#         self.beat_stretch = self.new_attr_instance("beat_stretch")
#         self.filename = self.new_attr_instance("filename")
#         self.onsetCut = self.new_attr_instance("onsetCut")
#         self.onset = self.new_attr_instance("onset")
#         self.defaults['pos']   = 0
#         self.defaults['sample']   = 0
#         self.defaults['beat_stretch'] = 0
#         self.defaults['onsetCut'] = 1
#         self.defaults["onset"] = 0
#         self.base.append("rate = (rate * (1-(beat_stretch>0))) + ((BufDur.kr(buf) / sus) * (beat_stretch>0));")
#         self.base.append("osc = PlayBuf.ar(2, buf, BufRateScale.kr(buf) * rate, startPos: BufSampleRate.kr(buf) * pos, loop: 1.0);")
#         self.base.append("osc = osc * EnvGen.ar(Env([1,1,0.0001],[onsetCut, 0.01]));")
#         self.osc = self.osc * self.amp
#         self.add()
#     def __call__(self, filename, pos=0, sample=0, onset=0, **kwargs):
#         kwargs["onset"] = onset
#         kwargs["filename"] = filename
#         kwargs["sample"] = sample 
#         proxy = SampleSynthDef.__call__(self, pos, **kwargs)
#         proxy.kwargs["filename"] = filename
#         proxy.kwargs["pos"] = pos
#         proxy.kwargs["onset"] = onset
#         self.filename = filename
#         return proxy

class WavetableSynthDef(SampleSynthDef):
    def __init__(self):
        SampleSynthDef.__init__(self, "wavetable")
        self.phase = self.new_attr_instance("phase")
        self.sample = self.new_attr_instance("sample")
        self.filename = self.new_attr_instance("filename")
        self.detune = self.new_attr_instance("detune")

        self.defaults['phase']   = 0
        self.defaults['sample'] = 0
        self.defaults['detune'] = 0.2
        
        self.base.append("osc = Osc.ar(buf, rate*LFNoise1.ar(detune!4).bipolar(detune).midiratio, phase.range(0,2pi));")
        self.base.append("osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.1, 0.05]));")
        self.base.append("osc = HPF.ar(osc, 20);")
        self.base.append("osc = LPF.ar(osc, 8000);")
        self.base.append("osc = LeakDC.ar(osc);")

        self.osc = self.osc * self.amp
        self.add()
        
    def __call__(self, filename, sample=0, **kwargs):
        kwargs["buf"] = Samples.loadBuffer(filename, sample)
        kwargs["filename"] = filename
        kwargs["sample"] = sample
        proxy = SampleSynthDef.__call__(self, **kwargs)
        proxy.kwargs["filename"] = filename
        self.filename = filename
        return proxy


loop = LoopSynthDef()
noloop = NoLoopSynthDef()
stretch = StretchSynthDef()
gsynth = GranularSynthDef()
breakcore = BreakcoreSynthDef()
splitter = SplitterSynthDef()
splaffer = SplafferSynthDef()
# onset = OnsetSynthDef()
wavetable = WavetableSynthDef()