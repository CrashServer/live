#coding: utf8
#!/usr/bin/env python3

##### Server configurator #####

# Global
maxPlayer = 16 # Number of max players playing together

timeChange = 8 # Time in beats for a new event
multDurationMin = 1 #
multDurationMax = 4


## Server routine orders probabilty ###
probAddPlayer = 5  # probability to add a player (synth, drum, loop)
probStopPlayer = 4 # probability to stop one or more running players
probAddFx = 2 # probabilty to add a Fx
probChangeDegree = 1 # probability to change a synth degree, drum char or loop position
probAddPlayerParam = 4 # probability to add a player param (.stutter, .spread, .shuffle)
probAddPlayerAttribute = 4 # probability to a change a player attributes (dur, pan, sus)
probAddEvent = 3 #probabilty to add a master event (change bpm, change root, master.lpf(), drop)
probChangeSynthAttr = 2 # probabilty to change player adsr

#Add Master event Probability
probChangeScale = 1
probChangeRoot = 1
probChangeHumanizer = 3
probChangeBpm = 2
probAddLpf = 6
probAddDrop = 3
probAddKick = 4
probAddAccompany = 3
probAddFxOut = 1 # probability to add an fx output

# Add player probability
probAddSynth = 1
probAddDrum = 4 #2
probAddLoop = 8 #1

# Stop player
minPlayerTurn = 8 # min number of player turn before a possibility stop
maxPlayerTurn = 16 # max number of player turn until a stop

# Add Player Probability
probPatternDur = [30,60,10] # probability dur synth player [PDur(random,8), SDur(), Generate Pattern]

# Add Drum Probabilty
probAddStyleDrum = 8 # probability to pick a style drum pattern
probAddRandomDrum = 1 # probability to generate random char pattern
probAddDrummer = 30

# Stop player Probability
probStopOnePlayer = 6  # porbability to stop randomly only one player
probStopMorePlayers = 1 # probabilty to stop 1 to (all-1) players

# Change degree
probLoopChangeDegree = [4,	# probability to change loop degree
						4,	# probability to change loop position
						4]   # probability to change loop sample

probSynthChangeDegree = [2, # probability to change synth degree player to PArp()
						 5, # probabiltiy to change synth degree player to Melody()
						 2, # probabiltiy to change synth degree player to PGauss()
						 3] # probability to change synth degree player to PChain2(chords)

probChangeDrumChar = [7,2] # probability to change to [same type char (kick, snare, hh) or random char]

# Change bpm parameters
changeBpmMin = 30 # min bpm
changeBpmMax = 162 # max bpm
changeBpmTimeMin = 32  # min beats
changeBpmTimeMax = 256 # max beats

# Change Root parameters
changeRootMin = -1
changeRootMax = 1

# Humanizer parameters
humanAmpMin = 5   # % min random human amp
humanAmpMax = 60  # % max random human amp
humanDelayMin = -10 # % min random dur delay
humanDelayMax = 10 # % max random dur delay
humanSwingMin = -10 # % min swing
humanSwingMax = 10 # % max swing

# Drop parameters
dropTimeMin = 2
dropTimeMax = 8
dropLoop = 4

# change probability player parameters
probPlayerAttributes = [2, #amp
						2, #amplify
						7, #dur
						1, #sus
						4] #pan

#Probability to change player duration (not loop) 
probChangeDur = [75,15] # SDur, generate_rytm

# Synth player generator
synthOctMin = 3   # octave min
synthOctMax = 6   # octave max

# Drum player generator
drumRateMin = -1  # rate drum PWhite min
drumRateMax = 4 # rate drum PWhite max

# Loop player generator
multDurLoopPLayer = [1,2]  # list of multiply the loop player duration
probDurLoopPlayer = [4,1]  # probability of this list

# drum style generator
probDrumStyleRate = [1,5] # probabilty to change drm style rate to: [randomRateList, 1]
DrumStyleDur = [0.25,0.5,1]  # list of dur for drum style
probDrumStyleDur = [3,1,1]  # probability of this list

# gen filter player
probLowPass = 8  # probability to add a low pass
probHighPass = 2 # probability to add a high pass
filterFreqMin = 400 # freq min
filterFreqMax = 7000 # freq max
probFilterFreq = [8,3,1] # probability to [linvar, integer, 0]

