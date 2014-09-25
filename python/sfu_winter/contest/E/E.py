import sys

prob = []
P = [[0] * 14000 for __ in xrange(1400)]

for line in sys.stdin:
    s = [int(x) for x in line.split()]
    prob = [0.0] + [x/100.0 for x in sorted(s[1:], reverse=1)]

    P[0][0] = 1.0
    for n in xrange(1, len(prob)):
        for k in xrange(0, n + 1):
            P[n][k] = (P[n-1][k-1] * prob[n] if k > 0 else 0.0) + (P[n-1][k] *(1.0 -prob[n]) if k < n else 0.0)

    maxp = 0.0
    for n in xrange(1, len(prob), 2):
        p = 0.0
    for k in xrange(n, n >> 1, -1):
        p += P[n][k]
    if p > maxp:
        maxp = p

    if s:
        print "{0:0.5f}".format(maxp)
