# tpl comp structure
# template

# Setup
Clock.bpm = 128

# ============================================================================
# @NEXTBAR - SYNCHRONIZED CHANGES
# ============================================================================

# @nextBar ensures changes happen on the next bar boundary
# Prevents mid-bar glitches during live coding

# ===== EXAMPLE 1: BASIC @NEXTBAR =====
# Define a function that changes on next bar
@nextBar
def intro():
    Clock.bpm = 128
    d1 >> play("x-o-", dur=0.5, amp=1.0)
    b1 >> bass([0, 0, 3, 7], dur=1, amp=0.9)

# Call it - will execute on next bar boundary
# intro()

# ===== EXAMPLE 2: MULTIPLE SECTIONS =====
@nextBar
def section_a():
    # Minimal drums
    d1 >> play("x", dur=1, amp=1.0)
    b1 >> bass([0, 0, 3, 7], dur=1, amp=0.9)

@nextBar
def section_b():
    # Add hi-hats
    d1 >> play("x", dur=1, amp=1.0)
    d2 >> play("-", dur=0.5, amp=0.6)
    b1 >> bass([0, 0, 3, 7, 10, 7], dur=0.5, amp=0.9)

@nextBar
def section_c():
    # Full arrangement
    d1 >> play("x-o-", dur=0.5, amp=1.0)
    d2 >> play("-", dur=0.25, amp=0.6)
    b1 >> bass([0, 0, 3, 7], dur=0.5, amp=0.9)
    p1 >> pluck([0, 2, 4, 7, 9], dur=0.5, oct=6, amp=0.8)

# ===== EXAMPLE 3: STOP SECTION =====
@nextBar
def stop_all():
    # Clean stop on bar boundary
    Group.all.stop()

# Or stop specific groups
@nextBar
def stop_drums():
    d1.stop()
    d2.stop()

# ============================================================================
# CLOCK.SCHEDULE - TIMED EVENTS
# ============================================================================

# Clock.schedule() runs functions at specific beats

# ===== EXAMPLE 4: SCHEDULE SINGLE EVENT =====
def add_bass():
    b1 >> bass([0, 3, 7], dur=1, amp=0.9)

# Schedule for beat 16
Clock.schedule(add_bass, 16)

# ===== EXAMPLE 5: SCHEDULE MULTIPLE EVENTS =====
def add_drums():
    d1 >> play("x", dur=1)

def add_hats():
    d2 >> play("-", dur=0.5)

def add_melody():
    p1 >> pluck([0, 2, 4, 7], dur=0.5)

# Build arrangement over time
Clock.schedule(add_drums, 0)     # Start immediately
Clock.schedule(add_hats, 16)     # Bar 4
Clock.schedule(add_melody, 32)   # Bar 8

# ===== EXAMPLE 6: SCHEDULED CHANGES =====
def drop():
    d1 >> play("x-o-", dur=0.5, amp=1.2)
    b1 >> bass([0, 0, 3, 7, 10, 7], dur=0.25, amp=1.0)

def breakdown():
    d1 >> play("x", dur=2, amp=0.8)
    b1.stop()
    p1 >> pads((0, 4, 7), dur=8, sus=7.5, amp=0.7, mverb=0.8)

Clock.schedule(drop, 64)         # Drop at bar 16
Clock.schedule(breakdown, 96)    # Breakdown at bar 24

# ============================================================================
# COMBINING @NEXTBAR AND CLOCK.SCHEDULE
# ============================================================================

# ===== EXAMPLE 7: FULL TRACK ARRANGEMENT =====
@nextBar
def intro_section():
    Clock.bpm = 128
    d1 >> play("x", dur=1, amp=0.9)

    # Schedule next sections
    Clock.schedule(verse, Clock.now() + 16)
    Clock.schedule(chorus, Clock.now() + 48)
    Clock.schedule(outro, Clock.now() + 80)

@nextBar
def verse():
    d1 >> play("x-o-", dur=0.5, amp=1.0)
    b1 >> bass([0, 0, 3, 7], dur=1, amp=0.9)
    p1 >> pluck([0, 2, 4, 7], dur=0.5, oct=5, amp=0.7)

@nextBar
def chorus():
    d1 >> play("x-o-", dur=0.5, amp=1.2)
    d2 >> play("-", dur=0.25, amp=0.8)
    b1 >> bass([0, 0, 3, 7, 10, 7], dur=0.5, amp=1.0)
    p1 >> pluck([0, 2, 4, 7, 9, 11], dur=0.25, oct=6, amp=0.9)
    p2 >> pads((0, 4, 7), dur=8, sus=7.5, amp=0.6, mverb=0.7)

@nextBar
def outro():
    d1 >> play("x", dur=2, amp=linvar([1.0, 0.0], 32))
    b1.stop()
    p1.stop()
p2 >> pads((0, 4, 7), dur=8, sus=7.5,amp=linvar([0.8, 0.0], 32),lpf=linvar([2400, 400], 32),mverb=0.9)

# ============================================================================
# CLOCK.NOW() - CURRENT BEAT
# ============================================================================

# ===== EXAMPLE 8: RELATIVE SCHEDULING =====
# Schedule relative to current time
def schedule_relative():
    current_beat = Clock.now()

    Clock.schedule(add_drums, current_beat + 4)   # 4 beats from now
    Clock.schedule(add_bass, current_beat + 8)    # 8 beats from now
    Clock.schedule(add_melody, current_beat + 16) # 16 beats from now

# ===== EXAMPLE 9: CONDITIONAL SCHEDULING =====
def smart_schedule():
    # Schedule on next multiple of 16
    next_section = (int(Clock.now() / 16) + 1) * 16
    Clock.schedule(chorus, next_section)

# ============================================================================
# GROUP CONTROL
# ============================================================================

# ===== EXAMPLE 10: USING GROUPS =====
@nextBar
def group_example():
    # Define groups
    drums = Group(d1, d2, d3)
    melody = Group(p1, p2)
    bass_group = Group(b1, b2)

    # Control groups together
    # drums.stop()
    # melody.only()
    # bass_group.solo()

# ===== EXAMPLE 11: GROUP.ALL =====
@nextBar
def stop_everything():
    # Stop all players
    Group.all.stop()

@nextBar
def solo_melody():
    # Solo just melody players
    Group(p1, p2).only()

# ============================================================================
# LIVE CODING WORKFLOW
# ============================================================================

# ===== EXAMPLE 12: LIVE SESSION STRUCTURE =====
# Typical live coding session flow

# 1. Setup
@nextBar
def setup():
    Clock.bpm = 128
    Scale.default = "minor"
    Root.default = 0

# 2. Build drums
@nextBar
def drums_in():
    d1 >> play("x", dur=1)
    Clock.schedule(drums_full, Clock.now() + 16)

@nextBar
def drums_full():
    d1 >> play("x-o-", dur=0.5)
    d2 >> play("-", dur=0.25)

# 3. Add bass
@nextBar
def bass_in():
    b1 >> bass([0, 0, 3, 7], dur=1)

# 4. Add melody
@nextBar
def melody_in():
    p1 >> pluck([0, 2, 4, 7], dur=0.5, oct=5)

# 5. Build to drop
@nextBar
def build():
    d1 >> play("x-o-", dur=0.5, amp=linvar([1.0, 1.5], 16))
    d2 >> play("-", dur=0.125, amp=linvar([0.6, 1.0], 16))
    b1 >> bass([0, 0, 3, 7], dur=0.5, lpf=linvar([400, 2400], 16))
    p1 >> pluck([0, 2, 4, 7, 9], dur=0.25, oct=var([5, 6], 8))

# 6. Drop
@nextBar
def drop():
    d1 >> play("x-o-", dur=0.5, amp=1.2)
    d2 >> play("-", dur=0.25, amp=0.8)
    b1 >> bass([0, 0, 3, 7, 10, 7], dur=0.25, amp=1.0)
    p1 >> pluck([0, 2, 4, 7, 9, 11], dur=0.125, oct=6, amp=0.9)

# ============================================================================
# TEMPO CHANGES
# ============================================================================

# ===== EXAMPLE 13: SCHEDULED BPM CHANGES =====
@nextBar
def speed_up():
    Clock.bpm = 135

@nextBar
def slow_down():
    Clock.bpm = 110

# Schedule tempo changes
def tempo_journey():
    Clock.schedule(speed_up, 32)
    Clock.schedule(slow_down, 64)

# ===== EXAMPLE 14: GRADUAL TEMPO CHANGE =====
# Note: FoxDot doesn't have built-in tempo ramping
# But you can approximate it with scheduled steps

@nextBar
def accelerate():
    for i in range(16):
        beat = Clock.now() + (i * 4)
        new_bpm = 120 + (i * 2)  # 120 -> 150
        Clock.schedule(lambda bpm=new_bpm: setattr(Clock, 'bpm', bpm), beat)

# ============================================================================
# SCALE AND ROOT CHANGES
# ============================================================================

# ===== EXAMPLE 15: SCHEDULED SCALE CHANGES =====
@nextBar
def minor_section():
    Scale.default = "minor"
    Root.default = 0

@nextBar
def major_section():
    Scale.default = "major"
    Root.default = 0

@nextBar
def dorian_section():
    Scale.default = "dorian"
    Root.default = 0

# ===== EXAMPLE 16: MODAL PROGRESSION =====
@nextBar
def modal_journey():
    # Schedule scale changes
    Clock.schedule(lambda: setattr(Scale, 'default', Scale.minor), 0)
    Clock.schedule(lambda: setattr(Scale, 'default', Scale.dorian), 32)
    Clock.schedule(lambda: setattr(Scale, 'default', Scale.mixolydian), 64)
    Clock.schedule(lambda: setattr(Scale, 'default', Scale.major), 96)

# ============================================================================
# CONDITIONAL PLAYER METHODS
# ============================================================================

# ===== EXAMPLE 17: SCHEDULED .EVERY() CHANGES =====
@nextBar
def evolving_pattern():
    p1 >> pluck([0, 2, 4, 7], dur=0.5)

    # Schedule pattern evolution
    Clock.schedule(lambda: p1.every(4, 'shuffle'), 16)
    Clock.schedule(lambda: p1.every(4, 'reverse'), 32)
    Clock.schedule(lambda: p1.every(8, 'stutter', 4), 48)

# ============================================================================
# COMPLEX ARRANGEMENTS
# ============================================================================

# ===== EXAMPLE 18: 8-SECTION TRACK =====
@nextBar
def full_track():
    # Section A: Intro (0-16)
    Clock.schedule(section_a, 0)

    # Section B: Build (16-32)
    Clock.schedule(section_b, 16)

    # Section C: Verse (32-48)
    Clock.schedule(section_c, 32)

    # Section D: Pre-chorus (48-56)
    Clock.schedule(section_d, 48)

    # Section E: Chorus (56-72)
    Clock.schedule(section_e, 56)

    # Section F: Breakdown (72-88)
    Clock.schedule(section_f, 72)

    # Section G: Build 2 (88-96)
    Clock.schedule(section_g, 88)

    # Section H: Outro (96-112)
    Clock.schedule(section_h, 96)

# ============================================================================
# LIVE IMPROVISATION HELPERS
# ============================================================================

# ===== EXAMPLE 19: QUICK SECTION SWITCHER =====
current_section = 0

@nextBar
def next_section():
    global current_section
    current_section += 1

    if current_section == 1:
        section_a()
    elif current_section == 2:
        section_b()
    elif current_section == 3:
        section_c()
    else:
        stop_all()
        current_section = 0

# ===== EXAMPLE 20: MUTE/UNMUTE SCHEDULER =====
@nextBar
def mute_drums():
    d1.stop()
    d2.stop()
    # Schedule them to come back
    Clock.schedule(unmute_drums, Clock.now() + 16)

@nextBar
def unmute_drums():
    d1 >> play("x-o-", dur=0.5)
    d2 >> play("-", dur=0.25)

# ============================================================================
# MASTER BUS AUTOMATION
# ============================================================================

# ===== EXAMPLE 21: SCHEDULED MASTER EFFECTS =====
@nextBar
def add_master_delay():
    Master().hpf = 100
    Master().echo = 0.5
    Master().echotime = 0.375

@nextBar
def remove_master_effects():
    Master().hpf = 0
    Master().echo = 0

# ===== EXAMPLE 22: MASTER FADE OUT =====
@nextBar
def fade_out():
    Master().amp = linvar([1.0, 0.0], 32)
    # Schedule stop
    Clock.schedule(lambda: Group.all.stop(), Clock.now() + 32)

# ============================================================================
# PERFORMANCE PATTERNS
# ============================================================================

# ===== EXAMPLE 23: BUILD-DROP PATTERN =====
@nextBar
def build_section():
    # 16-bar build
    d1 >> play("x-o-", dur=0.5, amp=linvar([0.8, 1.3], 64))
    d2 >> play("-", dur=0.125, amp=linvar([0.4, 1.0], 64))
    b1 >> bass([0], dur=0.5, lpf=linvar([300, 3200], 64), lpr=0.5)
    p1 >> pluck([0, 2, 4], dur=0.25, oct=linvar([5, 7], 64))

    # Schedule the drop
    Clock.schedule(drop_section, Clock.now() + 64)

@nextBar
def drop_section():
    d1 >> play("x-o-", dur=0.5, amp=1.2)
    d2 >> play("-", dur=0.25, amp=0.8)
    b1 >> bass([0, 0, 3, 7, 10, 7], dur=0.25, lpf=600, amp=1.0)
    p1 >> pluck([0, 2, 4, 7, 9, 11], dur=0.125, oct=6, amp=0.9)
    p2 >> pads((0, 4, 7), dur=8, sus=7.5, amp=0.7, mverb=0.8)

# ============================================================================
# CLOCK.CLEAR() - CANCEL SCHEDULED EVENTS
# ============================================================================

# ===== EXAMPLE 24: CANCEL SCHEDULED EVENTS =====
def emergency_stop():
    Clock.clear()  # Cancel all scheduled events
    Group.all.stop()

# ============================================================================
# PRACTICAL TIPS
# ============================================================================

# Live performance workflow:
# 1. Define sections with @nextBar
# 2. Use Clock.schedule() for automated progression
# 3. Use Group.all.stop() for emergency stops
# 4. Use Clock.now() for relative scheduling
# 5. Test sections individually before scheduling

# Timing tips:
# - 4 bars = 16 beats (at 4/4)
# - 8 bars = 32 beats
# - 16 bars = 64 beats
# - Use multiples of 16 for section boundaries

# Common section lengths:
# - Intro: 8-16 bars
# - Verse: 16-32 bars
# - Chorus: 8-16 bars
# - Breakdown: 8-16 bars
# - Build: 8-16 bars
# - Outro: 8-16 bars

# Emergency commands:
# Group.all.stop()     # Stop everything
# Clock.clear()        # Cancel scheduled events
# Master().reset()     # Reset master bus
