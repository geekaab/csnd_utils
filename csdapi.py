import csnd6
from random import randint

orc = """
sr=44100
ksmps=32
nchnls=2
0dbfs=1

instr 1
ipch = cps2pch(p5, 12)
kenv linsegr 0, .05, 1, .05, .7, .4, 0
aout vco2 p4*kenv, ipch
aout moogladder aout, 2000, .25
outs aout, aout
endin
"""
c = csnd6.Csound()
c.SetOption("-odac")
c.CompileOrc(orc)

sco = ""
vals = []
for i in xrange(256): vals.append([1, i*.25, .25, .5, "8.%02g\n"%(randint(0, 15))])
vals = ["i" + " ".join(map(str, a)) for a in vals]
sco = "\n".join(vals)

c.ReadScore(sco)
c.Start()

while (c.PerformKsmps() == 0): pass
c.Stop()
