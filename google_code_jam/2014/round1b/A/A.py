from __future__ import print_function
from __future__ import division

import sys


def canonical(s):
    if not s:
        return []
    r = [[s[0], 1]]
    for c in s[1:]:
        if c == r[-1][0]:
            r[-1][1] += 1
        else:
            r.append([c, 1])
    return r


def min_change(l):
    l = list(l)
    # a = sum(l) // len(l)
    return min(sum(abs(a - x) for x in l) for a in l)


def read_case(reader):
    n = int(next(reader))
    return [canonical(next(reader).strip()) for __ in range(n)]


def unique(x):
    return [x[i][0] for i in range(len(x))]


def solve(X):
    t = unique(X[0])
    for x in X[1:]:
        if t != unique(x):
            return "Fegla Won"
    return sum(min_change(x[i][1] for x in X) for i in range(len(X[0])))


if __name__ == '__main__':
    reader = iter(sys.stdin)
    T = int(next(reader))
    for t in xrange(T):
        print('Case #{}: {}'.format(t + 1, solve(read_case(reader))))
