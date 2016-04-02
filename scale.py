from sys import argv

def scale(n, o, N): return float(o)**(float(n)/float(N))

if len(argv) != 3: exit('usage: scale octave N')
print argv[0], argv[1], argv[2]

table = [scale(i, float(argv[1]), float(argv[2])) for i in xrange(0, int(argv[2])+1)]

for val in table: print '%.32f'%val
