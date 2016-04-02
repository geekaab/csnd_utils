from math import exp

expvals = [exp(n) for n in xrange(1024)]
expvals = [int(expval/expvals[-1]*1024) for expval in expvals]
print expvals
