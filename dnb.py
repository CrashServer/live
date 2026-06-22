# dnb — 174 bpm, F minor, drum and bass
# 2-step rolling groove, heavy sub, reese bass, dark atmosphere
Clock.bpm = 174
Scale.default = "minor"
Root.default = "F"

#@#@ dnb

#@ intro

# 2-step kick — rolling DnB pattern
dk >> play("X.....X.X...X...", dur=0.25, amp=var([1,0.9,1,0.85],4), hpf=50)

# snare — crisp on 2 and 4
sn >> play("....o.......o...", dur=0.25, amp=0.88, sample=2, hpf=300, cheapverb=0.12, cvdecay=0.4)

# sub bass — rolling 16th line, heavy floor
su >> subbass([0,0,0,-7,0,0,-5,0,0,-3,0,-5,0,0,0,-7], oct=2, dur=0.25, sus=0.22, amp=0.95, lpf=sinvar([60,250],16))

# reese-style bass — jbass + dynfuzz
rb >> jbass([0,0,-5,0,-7,-5,0,-7], oct=4, dur=0.5, sus=var([0.3,0.25,0.35,0.3],[4,4,4,4]), amp=0.75, dynfuzz=0.6, dfgain=1.8, lpf=sinvar([300,2500],24), hpf=80)

#@ build

# hats — 32nd note pressure
ht >> play("i", dur=0.125, amp=PLife(0.55), hpf=8000, pan=PRand([-0.3,0,0.3],4))

# dark pad — atmospheric backdrop
pd >> pad2([0,-5,3,-7], oct=4, dur=4, sus=5, amp=sinvar([0.08,0.25],32), lpf=linvar([400,1800],64), room=0.95, mix=0.88)

# wobble2 bass stab — neuro element
wb >> wobble2([0,-7,-5,-7], oct=4, dur=2, sus=1.8, amp=sinvar([0.3,0.65],16), wflo=0.1, wfhi=8, wfmax=sinvar([2000,8000],8), wet=0.6)

#@ drop

# clap layer — adds sharp attack
cl >> play("....o.......o...", dur=0.25, amp=0.65, sample=4, amplify=PEuclid(3,8), hpf=4000)

# glitchbass — gritty mid bass stabs
gb >> glitchbass([0,-5,0,-7], oct=5, dur=PFDur((5,8),(3,16)), sus=0.15, amp=sinvar([0.3,0.65],8), cutoff=sinvar([800,6000],8), rq=0.5, rate=sinvar([0.5,2],8))

# angst scream — high pitched noise stabs
ag >> angst([7,5,rest(0),7,rest(0),5,rest(0),rest(0)], oct=6, dur=0.5, sus=0.12, amp=sinvar([0,0.5],8), cutoff=sinvar([4000,16000],4), rq=0.3, rate=sinvar([0.4,0.9],8))

# sub pushes harder
su.amp = sinvar([0.9, 1.1], 8)
rb.dynfuzz = sinvar([0.5, 0.8], 8)

#@ peak

dk >> play("X.....X.X.X.X...", dur=0.25, amp=var([1,0.9,1,0.85],4))
wb.wfhi = sinvar([8, 16], 8)
wb.wfmax = sinvar([3000, 12000], 4)
ag.oct = var([6,7],[8,4])
pd.lpf = sinvar([1000, 4000], 16)
gb.amp = sinvar([0.4, 0.8], 4)

#@ end(32)
