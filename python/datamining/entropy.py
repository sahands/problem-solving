from __future__ import division, print_function
from math import log

EPS = 0.000001

def entropy(*a):
    e = []
    N = 0
    for b in a:
        n = sum(b)
        N += n
        local_e = -sum(p * log(p, 2) for p in (x / n for x in b) if p > EPS)
        e.append((local_e, n))
    return sum(x * n / N for x, n in e)



