from __future__ import print_function
from __future__ import division

import sys


__author__ = 'Sahand Saba'


def read_case(reader):
    C, F, X = (float(x) for x in next(reader).split())
    return C, F, X


def solve(C, F, X):
    r = 2.0
    t = 0.0
    while True:
        if C + (r * X) / (r + F) < X:
            t += C / r
            r += F
        else:
            return t + X / r


if __name__ == '__main__':
    reader = iter(sys.stdin)
    T = int(next(reader))
    for t in xrange(T):
        C, F, X = read_case(reader)
        s = solve(C, F, X)
        print('Case #{0}: {1} '.format(t + 1, s))
