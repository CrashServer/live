"""
DrumPatterns - Pattern Dictionary for FoxDot

Usage:
    from FoxDot.lib.DrumPatterns import pat, ppat, pbuild

    # Play patterns
    d1 >> play(pat("t1"), dur=1/4)

    # Build longer patterns
    d1 >> play(pbuild(["t1", "t2", "t1", "t3"]), dur=1/4)

    # Use groups
    d1 >> play(pbuild(GROUPS["tverse"]), dur=1/4)

    # Duration for synths
    b1 >> bass([0,0,0,0], dur=ppat("tk1"))
"""

# =============================================================================
# BASE PATTERNS (16 steps unless noted)
# =============================================================================

PATTERNS = {

    # =========================================================================
    # TECHNO KICKS
    # =========================================================================

    "tk1":  "x---x---x---x---",                 # 4/4 straight
    "tk2":  "x---x---x---x-x-",                 # extra 16th end
    "tk3":  "x---x---x-x-x---",                 # syncopated
    "tk4":  "x-x-x-x-x-x-x-x-",                 # 8th notes
    "tk5":  "x---x---x-------",                 # sparse
    "tk6":  "x-------x---x---",                 # offset
    "tk7":  "x---x-x-x---x---",                 # shuffle feel
    "tk8":  "x-x---x-x-x---x-",                 # breakbeat hint
    "tk9":  "x---x---x---x-xx",                 # double end
    "tk10": "x--xx---x---x---",                 # double early

    # =========================================================================
    # TECHNO HATS
    # =========================================================================

    "th1":  "--:-:-:---:-:-:-",                 # offbeat short
    "th2":  ":-:-:-:-:-:-:-:-",                 # 8th short
    "th3":  "=--=--=-=--=--=-",                 # open groove
    "th4":  "::::::::::::::::",                 # 16th short
    "th5":  "--:-:-:---:-:-:=",                 # phrase open
    "th6":  "----------------",                 # 16th closed
    "th7":  "--=---=---=---=-",                 # offbeat open
    "th8":  ":--:--:--:--:--:",                 # triplet feel
    "th9":  "=---=---=---=---",                 # quarter open
    "th10": "-:-:-:-:=:-:-:-:",                 # accent mid
    "th11": "---:---:---:---:",                 # sparse short
    "th12": "=-:-=-=-:-=-=-:-",                 # complex open

    # =========================================================================
    # TECHNO CLAPS/SNARES
    # =========================================================================

    "tc1":  "----c-------c---",                 # 2 and 4
    "tc2":  "----c-----c-c---",                 # extra hit
    "tc3":  "----C-------C---",                 # electro
    "tc4":  "----c---------c-",                 # shifted 4
    "tc5":  "----c---c---c---",                 # 2,3,4
    "tc6":  "------c-------c-",                 # offbeat
    "tc7":  "----c--c----c---",                 # syncopated
    "tc8":  "----o-------o---",                 # snare instead

    # =========================================================================
    # TECHNO RIDES/CYMBALS
    # =========================================================================

    "tr1":  "~-~-~-~-~-~-~-~-",                 # 8th ride
    "tr2":  "~---~---~---~---",                 # quarter ride
    "tr3":  "~~-~~-~~-~~-~~-~",                 # gallop ride
    "tr4":  "~-~-~-~-~-~-~-~#",                 # ride + crash

    # =========================================================================
    # TECHNO COMBINED (32 steps = 2 bars)
    # =========================================================================

    "t1":   "x-:-c-:-x-:-c-:-x-:-c-:-x-:-c-:-", # classic
    "t2":   "x-:-c-:-x-:-c-:-x-:-c-:-x-:=c-:-", # open end
    "t3":   "x:::c:::x:::c:::x:::c:::x:::c:::", # driving
    "t4":   "x---c---x-x-c---x---c---x-x-c---", # minimal
    "t5":   "x-:-:-:-x-:-:-:-x-:-:-:-x-:-:-:=", # no snare
    "t6":   "x=-=c=-=x=-=c=-=x=-=c=-=x=-=c=-=", # acid
    "t7":   "x-:-c-:-x-:-c-x-x-:-c-:-x-:-c-:-", # extra kick
    "t8":   "x---c---x---c---x---c-x-x-x-c---", # build end
    "t9":   "x-:-c-:-x-x-c-:-x-:-c-:-x-:-c-x-", # shuffle
    "t10":  "x:::c:::x:::c:::x:::c:::x::=c:::", # driving open
    "t11":  "x-:-c-:-x-:-c-:-x-:-c-:-x-:-c-:#", # crash end
    "t12":  "x---c---x---c---x-x-c-x-x---c---", # syncopated


    # =========================================================================
    # HOUSE KICKS
    # =========================================================================

    "hk1":  "x---x---x---x---",                 # 4/4
    "hk2":  "x---x---x---x-x-",                 # fill
    "hk3":  "x---x---x-x-x---",                 # swing
    "hk4":  "v---v---v---v---",                 # deep kick

    # =========================================================================
    # HOUSE HATS
    # =========================================================================

    "hh1":  "--=---=---=---=-",                 # classic
    "hh2":  "=--==--==--==--=",                 # disco
    "hh3":  "-=:-=:-=:-=:-=:-",                 # shuffled
    "hh4":  "---=---=---=---=",                 # sparse open
    "hh5":  "=-=-=-=-=-=-=-=-=-",               # all open
    "hh6":  "-:-:-:-:-:-:-:-:",                 # 8th mixed

    # =========================================================================
    # HOUSE CLAPS
    # =========================================================================

    "hc1":  "----c-------c---",                 # 2 and 4
    "hc2":  "----o-------o---",                 # snare
    "hc3":  "----c-----c-c---",                 # extra
    "hc4":  "----c---c---c---",                 # busy

    # =========================================================================
    # HOUSE COMBINED (32 steps)
    # =========================================================================

    "h1":   "x-:=c-:=x-:=c-:=x-:=c-:=x-:=c-:=", # classic
    "h2":   "x---c---x---c---x---c---x-:-c---", # deep
    "h3":   "x=:=c=:=x=:=c=:=x=:=c=:=x=:=c=:#", # disco
    "h4":   "x:::c:::x:::c:::x:::c:::x:::c:::", # jackin
    "h5":   "x-:=c-:-x-:=c=:-x-:=c-:-x=:=c=:-", # garage
    "h6":   "x-e-c-:-x-:-c-e-x-e-c-:-x-:-c-:-", # tribal
    "h7":   "v-:=c-:=v-:=c-:=v-:=c-:=v-:=c-:=", # deep kick
    "h8":   "x-:=c-:=x-x-c-:=x-:=c-:=x-:=c-:=", # extra kick
    "h9":   "x-:=c-:=x-:=c-:=x-:=c-:=x-:=c=:=", # open end
    "h10":  "x---c---x---c---x---c---x---c---", # minimal


    # =========================================================================
    # BREAKS KICKS
    # =========================================================================

    "bk1":  "x-x-------xx----",                 # amen
    "bk2":  "x-x-------x-----",                 # amen var
    "bk3":  "x-----x-x-------",                 # think
    "bk4":  "x---x-----x-x---",                 # funky
    "bk5":  "x-x---x-x-------",                 # apache
    "bk6":  "x-------x-x-----",                 # soul
    "bk7":  "x--x--x--x------",                 # triplet
    "bk8":  "x-x-x-------x---",                 # syncopated

    # =========================================================================
    # BREAKS SNARES (acoustic)
    # =========================================================================

    "bs1":  "----u--u-u--u--u",                 # amen
    "bs2":  "----u--u--u---u-",                 # amen var
    "bs3":  "----u-------u---",                 # backbeat
    "bs4":  "----u-u-----u-u-",                 # double
    "bs5":  "--u---u---u---u-",                 # offbeat
    "bs6":  "----u--u----u-uu",                 # fill end
    "bs7":  "u---u---u---u---",                 # 4 snares
    "bs8":  "----U-------U---",                 # break snare

    # =========================================================================
    # BREAKS RIDES
    # =========================================================================

    "br1":  "-~-~-~-~-~-~-~-~",                 # 8th ride
    "br2":  "~-~-~-~-~-~-~-~-",                 # 8th offset
    "br3":  "~---~---~---~---",                 # quarter

    # =========================================================================
    # BREAKS COMBINED (32 steps)
    # =========================================================================

    "b1":   "x~x~u~~u~uxxu-~ux~x~u~~u~~uxu-~u", # amen full
    "b2":   "x~x~u~~u~~xu-~ux~x~u~~u~uxxu~~u",  # amen var
    "b3":   "x-:-u-:-x-x-u---x-:-u-x-x-:-u---", # think
    "b4":   "x-:-u-:-x-:-u---x--:u-:-x-u-u---", # funky
    "b5":   "x---u---x-x-u---x---u-:-x-:-u---", # soul
    "b6":   "x-u:--u-x-:-u-u-x-u:--u-x-:-u-:-", # apache
    "b7":   "x~x~u~~u~uxxu-~ux~x~u~~u~uxxu-:#", # amen crash
    "b8":   "x-:-U-:-x-x-U---x-:-U-:-x-:-U---", # break snare
    "b9":   "x-x-u--ux-x-u--ux-x-u--ux-x-u-uu", # rolling
    "b10":  "x---u---x---u---x---u---x-x-u-uu", # simple build


    # =========================================================================
    # DNB KICKS
    # =========================================================================

    "dk1":  "x-------x-------",                 # twostep
    "dk2":  "x-----x-x-------",                 # roller
    "dk3":  "x-x-------xx----",                 # jungle
    "dk4":  "x-------x---x---",                 # syncopated
    "dk5":  "x---------x-----",                 # minimal
    "dk6":  "x-----x-----x---",                 # triplet feel

    # =========================================================================
    # DNB SNARES
    # =========================================================================

    "ds1":  "----o-------o---",                 # twostep
    "ds2":  "------o-------o-",                 # roller
    "ds3":  "----U--U-U--U--U",                 # jungle
    "ds4":  "----O-------O---",                 # heavy
    "ds5":  "--------o-------",                 # half time
    "ds6":  "----o---o---o---",                 # busy

    # =========================================================================
    # DNB HATS
    # =========================================================================

    "dh1":  ":-:-:-:-:-:-:-:-",                 # 8th
    "dh2":  "::::::::::::::::",                 # 16th
    "dh3":  ":--:--:--:--:--:",                 # triplet
    "dh4":  ":-:-:-:-:-:-:-:=",                 # open end

    # =========================================================================
    # DNB COMBINED (32 steps)
    # =========================================================================

    "d1":   "x---:-:-o---:-:-x-:-:-x-o---:-:-", # twostep
    "d2":   "x-:-:-o-x-:-:-:-x-:-:-o-x-:-x-:-", # roller
    "d3":   "x~x~U~~u~Uxxu-~Ux~x~U~~u~~UxU-~U", # jungle
    "d4":   "x---:-:-o---:-:-x---:-:-o---:-:=", # liquid
    "d5":   "x-:-:-:-O---:-:-x---:-x-O---:-:-", # neuro
    "d6":   "x-------o-------x-------o-------", # minimal
    "d7":   "x---:-:-o---:-:-x-x-:-:-o---:-:-", # twostep var
    "d8":   "x-:-:-o-x-:-:-:-x-:-:-o-x-:-:-:#", # roller crash


    # =========================================================================
    # HIP-HOP KICKS
    # =========================================================================

    "hpk1": "x-------x-x-----",                 # boom bap
    "hpk2": "x---x-----------",                 # sparse
    "hpk3": "x-------x-------",                 # half
    "hpk4": "x-----x-x-----x-",                 # syncopated
    "hpk5": "x---------x-----",                 # lazy
    "hpk6": "k-------k-k-----",                 # organic

    # =========================================================================
    # HIP-HOP SNARES
    # =========================================================================

    "hps1": "----u-------u---",                 # acoustic 2&4
    "hps2": "----o-------o---",                 # electro 2&4
    "hps3": "------------O---",                 # trap (4 only)
    "hps4": "----u-------u-u-",                 # ghost end
    "hps5": "----U-------U---",                 # break snare
    "hps6": "----u---u---u---",                 # busy

    # =========================================================================
    # HIP-HOP HATS
    # =========================================================================

    "hph1": "-:-:-:-:-:-:-:-:",                 # 8th
    "hph2": "-(--)--(----)-(-",                 # trap rolls
    "hph3": "----------------",                 # 16th
    "hph4": "-:---:---:---:--",                 # lazy
    "hph5": "(--)(--)(--)(--)(--)(--)(--)(-(-)",# fast rolls

    # =========================================================================
    # HIP-HOP COMBINED (32 steps)
    # =========================================================================

    "hp1":  "x--:u-:-x---u--:x-:-u-:-x-u-u--:", # boom bap
    "hp2":  "x---u---x-x-u---x---u---x---u-x-", # golden era
    "hp3":  "k-:-U-:-k---U-:-k-:-U-:-k-:-U-u-", # dusty
    "hp4":  "x---o---x---o---x---o-x-x---o---", # west coast
    "hp5":  "x-------O-------x---x---O-------", # trap
    "hp6":  "x-:-u-:-x-:-u-:-x-:-u-:-x-:-u-:-", # simple
    "hp7":  "x---u---x---u---x---u---x-x-u-uu", # build end
    "hp8":  "x-------O---------------O-------", # trap minimal


    # =========================================================================
    # EBM / INDUSTRIAL
    # =========================================================================

    "ek1":  "x---x---x-x-x---",                 # ebm kick
    "ek2":  "X---X---X-X-X---",                 # heavy
    "ek3":  "X-X-X-X-X-X-X-X-",                 # 8th heavy

    "ec1":  "----C-------C---",                 # electro clap
    "ec2":  "------C-------C-",                 # shifted
    "ec3":  "----C---C---C---",                 # busy

    "e1":   "x-:-:-C=x-:-x-C=x-:-:-C=x-:-x-C=", # ebm
    "e2":   "X::::-C:X:X::-C:X::::-C:X:X::-C:", # hard
    "e3":   "X---C---X-X-C---X---C---X-X-C-X-", # industrial
    "e4":   "X-X-C-X-X-X-C-X-X-X-C-X-X-X-C-X-", # pounding
    "e5":   "x-:-C-:-x-:-C-:-x-:-C-:-x-:-C-:#", # ebm crash


    # =========================================================================
    # GABBER / HARDCORE
    # =========================================================================

    "gk1":  "g-g-g-g-g-g-g-g-",                 # 8th
    "gk2":  "gggggggggggggggg",                 # 16th
    "gk3":  "g-g-g-g-g-g-g-gg",                 # fill end

    "g1":   "g-g-C-g-g-g-C-g-g-g-C-g-g-g-C-g-", # gabber
    "g2":   "g:g:C:g:g:g:C:g:g:g:C:g:g:g:C:g:", # gabber hat
    "g3":   "ggggggggCgggggggggggggggCggggggg", # hardcore
    "g4":   "g-g-C-g-g-g-C-g-g-g-C-g-g-g-C-gg", # fill end
    "g5":   "G-G-C-G-G-G-C-G-G-G-C-G-G-G-C-G-", # distorted


    # =========================================================================
    # LATIN / WORLD
    # =========================================================================

    "lc1":  "x--x---x--x-x---",                 # son clave 3-2
    "lc2":  "--x-x---x--x--x-",                 # son clave 2-3
    "lc3":  "x--x----x-x-x---",                 # rumba 3-2
    "lc4":  "--x-x---x-x---x-",                 # rumba 2-3

    "l1":   "x-x---x-x-x---x-x-x---x-x-x---x-", # bossa
    "l2":   "x-x-o-x-x-x-o-x-x-x-o-x-x-x-o-x-", # samba
    "l3":   "x--x-ox--x-xo-x-x--x-ox--x-xo---", # afrobeat
    "l4":   "x--x---x--x-x---x--x---x--x-x-x-", # clave phrase
    "l5":   "x-x-x-x-o-x-x-x-x-x-x-x-o-x-x-x-", # samba full


    # =========================================================================
    # EXPERIMENTAL
    # =========================================================================

    "x1":   "x--x--x--x--x--x--x--x--x--x--x-", # 3 over 4
    "x2":   "x---------------o---------------", # sparse
    "x3":   "[xov]-[:-]u-[x-][xov]-:-u-[-=o-]", # glitch
    "x4":   "x-o-x-o-x-o-x-o-",                 # simple 8th
    "x5":   "x----x----x----x----x----x----x-", # 5 over 4
    "x6":   "x------x------x------x------x---", # 7 over 4
    "x7":   "x-x-x-x-o-x-x-x-x-x-x-x-o-x-x-x-", # displaced
    "x8":   "[xkv][xkv][ouc][xkv]",             # random kit


    # =========================================================================
    # FILLS (16 steps)
    # =========================================================================

    "fo1":  "o-o-ooooOOOOOOOO",                 # snare build
    "fo2":  "oooooooooooooooo",                 # snare roll
    "fo3":  "----o---oo--oooo",                 # snare fill
    "fo4":  "o---o---o-o-oooo",                 # snare phrase

    "fx1":  "x-x-xxxxXXXXXXXX",                 # kick build
    "fx2":  "xxxxxxxxxxxxxxxx",                 # kick roll
    "fx3":  "x---x---x-x-xxxx",                 # kick fill

    "ft1":  "t-m-M-T-tmMTtmMT",                 # tom roll down
    "ft2":  "T-M-m-t-TMmtTMmt",                 # tom roll up
    "ft3":  "t-t-m-m-M-M-T-T-",                 # tom pairs
    "ft4":  "tmMTtmMTtmMTtmMT",                 # tom 16th

    "fc1":  "#---------------",                 # crash
    "fc2":  "#-------#-------",                 # double crash
    "fc3":  "#---#---#---#---",                 # crash roll

    "fb":   "                ",                 # break/silence


    # =========================================================================
    # PERCUSSION LAYERS
    # =========================================================================

    "ps1":  "s-s-s-s-s-s-s-s-",                 # shaker 8th
    "ps2":  "ssssssssssssssss",                 # shaker 16th
    "ps3":  "s---s---s---s---",                 # shaker quarter

    "pt1":  "S---S---S---S---",                 # tambourine
    "pt2":  "S-S-S-S-S-S-S-S-",                 # tambourine 8th

    "pe1":  "----e-----e-----",                 # cowbell sparse
    "pe2":  "--e---e---e---e-",                 # cowbell offbeat
    "pe3":  "e---e---e---e---",                 # cowbell quarter

    "pr1":  "----r-------r---",                 # rim 2&4
    "pr2":  "--r---r---r---r-",                 # rim offbeat

}


# =============================================================================
# GROUPS (pre-defined combinations)
# =============================================================================

GROUPS = {

    # =========================================================================
    # TECHNO KITS (layers)
    # =========================================================================

    "tkit1": ["tk1", "th1", "tc1"],             # basic
    "tkit2": ["tk1", "th4", "tc1"],             # 16th hats
    "tkit3": ["tk4", "th2", "tc1"],             # driving
    "tkit4": ["tk1", "th3", "tc1"],             # open hats
    "tkit5": ["tk1", "th6", "tc3"],             # industrial

    # =========================================================================
    # TECHNO PHRASES (sequences)
    # =========================================================================

    "tverse1":  ["t1", "t1", "t2", "t1"],       # 4 bar verse
    "tverse2":  ["t1", "t1", "t1", "t2"],       # variation end
    "tchorus1": ["t3", "t3", "t6", "t3"],       # 4 bar chorus
    "tchorus2": ["t6", "t6", "t3", "t6"],       # acid chorus
    "tbuild1":  ["t5", "t4", "t1", "t3"],       # sparse to full
    "tbuild2":  ["t10", "t10", "t3", "t3"],     # driving build
    "tdrop1":   ["fb", "t3"],                   # silence + drop
    "tdrop2":   ["fb", "t6"],                   # silence + acid
    "tfill1":   ["t1", "t1", "t1", "fo1"],      # phrase + fill
    "tfill2":   ["t3", "t3", "t3", "fx1"],      # driving + fill

    # =========================================================================
    # HOUSE KITS
    # =========================================================================

    "hkit1": ["hk1", "hh1", "hc1"],             # classic
    "hkit2": ["hk1", "hh2", "hc1"],             # disco
    "hkit3": ["hk4", "hh1", "hc1"],             # deep
    "hkit4": ["hk1", "hh5", "hc1"],             # open

    # =========================================================================
    # HOUSE PHRASES
    # =========================================================================

    "hverse1":  ["h1", "h1", "h2", "h1"],
    "hverse2":  ["h2", "h2", "h1", "h2"],       # deep verse
    "hchorus1": ["h3", "h3", "h4", "h3"],       # disco
    "hchorus2": ["h4", "h4", "h3", "h4"],       # jackin
    "hbuild1":  ["h10", "h2", "h1", "h4"],
    "hdrop1":   ["fb", "h4"],
    "hfill1":   ["h1", "h1", "h1", "fo1"],

    # =========================================================================
    # BREAKS KITS
    # =========================================================================

    "bkit1": ["bk1", "br1", "bs1"],             # amen
    "bkit2": ["bk3", "br1", "bs3"],             # think
    "bkit3": ["bk4", "br2", "bs1"],             # funky

    # =========================================================================
    # BREAKS PHRASES
    # =========================================================================

    "bverse1":  ["b1", "b1", "b2", "b1"],       # amen phrase
    "bverse2":  ["b3", "b3", "b4", "b3"],       # think/funky
    "bchorus1": ["b1", "b2", "b1", "b7"],       # amen + crash
    "bbuild1":  ["b10", "b10", "b9", "b1"],
    "bdrop1":   ["fb", "b1"],
    "bfill1":   ["b1", "b1", "b1", "ft1"],      # amen + toms

    # =========================================================================
    # DNB KITS
    # =========================================================================

    "dkit1": ["dk1", "dh1", "ds1"],             # twostep
    "dkit2": ["dk2", "dh2", "ds2"],             # roller
    "dkit3": ["dk3", "dh1", "ds3"],             # jungle

    # =========================================================================
    # DNB PHRASES
    # =========================================================================

    "dverse1":  ["d1", "d1", "d7", "d1"],       # twostep
    "dverse2":  ["d2", "d2", "d2", "d8"],       # roller
    "dchorus1": ["d3", "d3", "d3", "d3"],       # jungle
    "dbuild1":  ["d6", "d4", "d1", "d3"],
    "ddrop1":   ["fb", "d3"],

    # =========================================================================
    # HIP-HOP KITS
    # =========================================================================

    "hpkit1": ["hpk1", "hph1", "hps1"],         # boom bap
    "hpkit2": ["hpk3", "hph2", "hps3"],         # trap
    "hpkit3": ["hpk6", "hph4", "hps5"],         # dusty

    # =========================================================================
    # HIP-HOP PHRASES
    # =========================================================================

    "hpverse1": ["hp1", "hp1", "hp2", "hp1"],   # boom bap
    "hpverse2": ["hp5", "hp5", "hp8", "hp5"],   # trap
    "hpchorus1":["hp2", "hp2", "hp1", "hp7"],
    "hpbuild1": ["hp6", "hp6", "hp1", "hp7"],
    "hpdrop1":  ["fb", "hp5"],

    # =========================================================================
    # EBM PHRASES
    # =========================================================================

    "everse1":  ["e1", "e1", "e2", "e1"],
    "echorus1": ["e4", "e4", "e3", "e5"],
    "ebuild1":  ["e1", "e2", "e4", "e4"],

    # =========================================================================
    # INTENSITY PROGRESSIONS
    # =========================================================================

    "tintensity": ["t5", "t4", "t1", "t3", "t6"],  # techno levels
    "hintensity": ["h10", "h2", "h1", "h4", "h3"], # house levels
    "dintensity": ["d6", "d4", "d1", "d2", "d3"],  # dnb levels

    # =========================================================================
    # GENERIC BUILDS (work across genres)
    # =========================================================================

    "build4":   ["fb", "fb", "fo3", "fo1"],     # 4 bar snare build
    "build8":   ["fb"]*4 + ["fo3", "fo3", "fo1", "fo1"],
    "drop":     ["fb", "fb"],                    # 2 bar silence

}


# =============================================================================
# CHARACTER CLASSES
# =============================================================================

HITS = set("xXkvgVWoOuUcCrR#^")
FILLS = set("-=:~sSeS")
REST = set(" ")


# =============================================================================
# FUNCTIONS
# =============================================================================

def pat(name):
    """
    Look up a pattern by short code.
    Returns the pattern string, or the input if not found.

    Usage:
        d1 >> play(pat("t1"), dur=1/4)
    """
    return PATTERNS.get(name, name)


def p(name):
    """Alias for pat()"""
    return pat(name)


def pbuild(items, mode="concat"):
    """
    Build a longer pattern from multiple patterns or a group.

    Args:
        items: List of pattern codes, or group name string
        mode: "concat" (append) or "layer" (merge)

    Usage:
        # From list
        d1 >> play(pbuild(["t1", "t2", "t1", "t3"]), dur=1/4)

        # From group
        d1 >> play(pbuild(GROUPS["tverse1"]), dur=1/4)
        d1 >> play(pbuild("tverse1"), dur=1/4)  # shorthand

        # Layer mode (merge patterns)
        d1 >> play(pbuild(["tk1", "th1", "tc1"], mode="layer"), dur=1/4)

    Returns:
        Combined pattern string
    """
    # If string, look up in groups
    if isinstance(items, str):
        items = GROUPS.get(items, [items])

    # Get pattern strings
    patterns = [PATTERNS.get(p, p) for p in items]

    if mode == "concat":
        return "".join(patterns)

    elif mode == "layer":
        # Merge patterns (longest wins, overlay characters)
        if not patterns:
            return ""
        max_len = max(len(p) for p in patterns)
        result = [" "] * max_len

        # Priority: HITS > FILLS > REST
        for pattern in patterns:
            for i, char in enumerate(pattern):
                if i < max_len:
                    current = result[i]
                    # Replace if new char has higher priority
                    if current == " ":
                        result[i] = char
                    elif current in FILLS and char in HITS:
                        result[i] = char
                    elif current in FILLS and char in FILLS:
                        result[i] = char  # later pattern wins

        return "".join(result)

    return "".join(patterns)


def ppat(name, hits_only=True, chars=None, base=0.25):
    """
    Convert drum pattern to duration list for melodic players.

    Args:
        name: Pattern code, list of codes, or group name
        hits_only: Only count kicks/snares/claps (default True)
        chars: Custom characters to count
        base: Duration per step (default 0.25)

    Usage:
        b1 >> bass([0,0,0,0], dur=ppat("tk1"))
        p1 >> pluck([0,2,4], dur=ppat("tverse1"))
    """
    # Build pattern first if list or group
    if isinstance(name, list):
        pattern = pbuild(name)
    elif name in GROUPS:
        pattern = pbuild(name)
    else:
        pattern = PATTERNS.get(name, name)

    # Determine hit characters
    if chars is not None:
        hit_chars = set(chars)
    elif hits_only:
        hit_chars = HITS
    else:
        hit_chars = HITS | FILLS

    # Find hit positions
    positions = [i for i, c in enumerate(pattern) if c in hit_chars]

    if len(positions) <= 1:
        return [len(pattern) * base]

    # Calculate durations
    durations = []
    for i in range(len(positions) - 1):
        durations.append((positions[i + 1] - positions[i]) * base)

    # Loop back duration
    last_gap = (len(pattern) - positions[-1]) + positions[0]
    durations.append(last_gap * base)

    return durations


def pamp(name, hits_only=True, chars=None, amp_on=1, amp_off=0):
    """
    Convert drum pattern to amplitude list.

    Usage:
        p1 >> pluck([0,2,4], dur=1/4, amp=pamp("tk1"))
    """
    if isinstance(name, list):
        pattern = pbuild(name)
    elif name in GROUPS:
        pattern = pbuild(name)
    else:
        pattern = PATTERNS.get(name, name)

    if chars is not None:
        hit_chars = set(chars)
    elif hits_only:
        hit_chars = HITS
    else:
        hit_chars = HITS | FILLS

    return [amp_on if c in hit_chars else amp_off for c in pattern]


def phits(name, hits_only=True, chars=None):
    """
    Get step positions where hits occur.

    Usage:
        phits("tk1") → [0, 4, 8, 12]
    """
    if isinstance(name, list):
        pattern = pbuild(name)
    elif name in GROUPS:
        pattern = pbuild(name)
    else:
        pattern = PATTERNS.get(name, name)

    if chars is not None:
        hit_chars = set(chars)
    elif hits_only:
        hit_chars = HITS
    else:
        hit_chars = HITS | FILLS

    return [i for i, c in enumerate(pattern) if c in hit_chars]


def patterns():
    """Print all available patterns"""
    print("\n=== PATTERNS ===\n")
    genres = {'t':'Techno', 'h':'House', 'b':'Breaks', 'd':'DnB',
              'hp':'Hip-Hop', 'e':'EBM', 'g':'Gabber', 'l':'Latin',
              'x':'Experimental', 'f':'Fills', 'p':'Percussion'}

    current = None
    for key in sorted(PATTERNS.keys()):
        g = 'hp' if key.startswith('hp') else ('p' if key.startswith('p') else key[0])
        if g != current:
            current = g
            print(f"\n{genres.get(g, 'Other')}:")
        print(f"  {key:6} {PATTERNS[key][:20]}{'...' if len(PATTERNS[key])>20 else ''}")


def groups():
    """Print all available groups"""
    print("\n=== GROUPS ===\n")
    for key in sorted(GROUPS.keys()):
        items = GROUPS[key]
        print(f"  {key:12} {items}")


# =============================================================================
# JSON EXPORT (for webTroop autocomplete)
# =============================================================================

def get_pattern_category(key):
    """Determine category from pattern key"""
    # Groups
    if key in GROUPS:
        if 'kit' in key: return 'Kits'
        if 'verse' in key: return 'Verses'
        if 'chorus' in key: return 'Choruses'
        if 'build' in key: return 'Builds'
        if 'drop' in key: return 'Drops'
        if 'fill' in key: return 'Fills'
        if 'intensity' in key: return 'Intensity'
        return 'Groups'

    # Patterns by prefix
    prefixes = {
        'tk': 'Techno Kick', 'th': 'Techno Hat', 'tc': 'Techno Clap', 'tr': 'Techno Ride',
        't': 'Techno',
        'hk': 'House Kick', 'hh': 'House Hat', 'hc': 'House Clap',
        'h': 'House',
        'bk': 'Breaks Kick', 'bs': 'Breaks Snare', 'br': 'Breaks Ride',
        'b': 'Breaks',
        'dk': 'DnB Kick', 'ds': 'DnB Snare', 'dh': 'DnB Hat',
        'd': 'DnB',
        'hpk': 'HipHop Kick', 'hps': 'HipHop Snare', 'hph': 'HipHop Hat',
        'hp': 'HipHop',
        'ek': 'EBM Kick', 'ec': 'EBM Clap',
        'e': 'EBM',
        'gk': 'Gabber Kick',
        'g': 'Gabber',
        'lc': 'Latin Clave',
        'l': 'Latin',
        'x': 'Experimental',
        'fo': 'Fill Snare', 'fx': 'Fill Kick', 'ft': 'Fill Tom', 'fc': 'Fill Crash', 'fb': 'Fill Break', 'fr': 'Fill Roll',
        'f': 'Fills',
        'ps': 'Perc Shaker', 'pt': 'Perc Tambourine', 'pe': 'Perc Cowbell', 'pr': 'Perc Rim',
        'p': 'Percussion',
    }

    # Match longest prefix first
    for prefix in sorted(prefixes.keys(), key=len, reverse=True):
        if key.startswith(prefix):
            return prefixes[prefix]

    return 'Other'


def export_json(filepath=None):
    """
    Export patterns and groups to JSON for webTroop autocomplete.

    Usage:
        export_json()  # prints to stdout
        export_json("/path/to/drumPatterns.json")  # writes to file
    """
    import json

    data = {
        "patterns": [],
        "groups": [],
        "categories": {}
    }

    # Export patterns
    for key, value in sorted(PATTERNS.items()):
        category = get_pattern_category(key)
        preview = value[:24] + "..." if len(value) > 24 else value

        entry = {
            "code": key,
            "pattern": value,
            "preview": preview,
            "category": category,
            "length": len(value)
        }
        data["patterns"].append(entry)

        # Build categories index
        if category not in data["categories"]:
            data["categories"][category] = []
        data["categories"][category].append(key)

    # Export groups
    for key, value in sorted(GROUPS.items()):
        category = get_pattern_category(key)
        preview = str(value)[:30] + "..." if len(str(value)) > 30 else str(value)

        entry = {
            "code": key,
            "items": value,
            "preview": preview,
            "category": category
        }
        data["groups"].append(entry)

        # Add to categories
        if category not in data["categories"]:
            data["categories"][category] = []
        data["categories"][category].append(key)

    json_str = json.dumps(data, indent=2)

    if filepath:
        with open(filepath, 'w') as f:
            f.write(json_str)
        print(f"Exported to {filepath}")
    else:
        print(json_str)

    return data


# =============================================================================
# EXPORTS
# =============================================================================

__all__ = ['pat', 'p', 'pbuild', 'ppat', 'pamp', 'phits',
           'patterns', 'groups', 'export_json', 'PATTERNS', 'GROUPS', 'HITS', 'FILLS']


# CLI support: python -m FoxDot.lib.DrumPatterns [output_path]
if __name__ == "__main__":
    import sys
    output = sys.argv[1] if len(sys.argv) > 1 else None
    export_json(output)
