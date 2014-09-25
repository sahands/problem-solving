from __future__ import print_function
from __future__ import division

import sys
from itertools import product


__author__ = 'Sahand Saba'


def read_case(reader):
    R, C, M = (int(x) for x in next(reader).split())
    return R, C, M


def solve(R, C, M):
    """
    Assumes R <= C
    """
    S = R * C - M  # "safe" tiles
    if M == 0:
        return [['.'] * C] * R

    if R == 1:
        return [['c'] + ['.'] * (S - 1) + ['*'] * M]

    if R == 2:
        if M % 2 == 1:
            return None
        return [['c'] + ['.'] * (S // 2 - 1) + ['*'] * (S // 2)] * 2

    # OK now we can assume 3 <= R <= C

    if S in [2, 3, 5, 7]:
        return None

    if S == 1:
        r = [['*'] * C for __ in xrange(R)]
        r[0][0] = 'c'
        return r

    if S == 4:
        r = [['*'] * C for __ in xrange(R)]
        for i, j in product([0, 1], repeat=2):
            r[i][j] = '.'
        r[0][0] = 'c'
        return r

    if S == 6:
        r = [['*'] * C for __ in xrange(R)]
        for i, j in product([0, 1], repeat=2):
            r[i][j] = '.'
        r[0][0] = 'c'
        return r

    if S == 8:
        r = [['*'] * C for __ in xrange(R)]
        for i, j in product([0, 1, 2], repeat=2):
            r[i][j] = '.'
        r[0][0] = 'c'
        r[2][2] = '*'
        return r

    # OK now we can assume S >= 9

    return []

if __name__ == '__main__':
    reader = iter(sys.stdin)
    T = int(next(reader))
    for t in xrange(T):
        R, C, M = read_case(reader)
        Rp, Cp = min(R, C), max(R, C)
        print('Case #{0}:'.format(t + 1))
        # solve assumes Rp <= Cp
        s = solve(Rp, Cp, M)
        if s is None:
            print('Impossible')
        else:
            if C < R:
                s = zip(*s)
            print('\n'.join(''.join(x) for x in s))
