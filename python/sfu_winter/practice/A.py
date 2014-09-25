from __future__ import division
import sys
import fileinput

lines = fileinput.input()

T = int(lines.next().strip())
for i in xrange(T):
    a, b, c = [int(x) for x in lines.next().strip().split(' ')]
    p = (c - a) / (b - a)
    if c < a:
        p = 0.0
    elif c > b:
        p = 1.0
    print '{0:0.2f}'.format(p)


