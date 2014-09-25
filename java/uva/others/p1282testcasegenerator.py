from itertools import product

for n in xrange(18):
    for i in xrange(1,n):
        for f in product(*[["0","1"]]*i):
                print n
                print ''.join(f)
