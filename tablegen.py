from math import log,log10,exp,tan

def scale(n, o, N): return float(o)**(float(n)/float(N))
def expon(n): return exp(float(n))

table = [scale(i, 3.0, 36.0) for i in xrange(0, 37)]

for val in table: print '%.32f'%val
