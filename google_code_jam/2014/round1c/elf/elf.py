from __future__ import print_function
from __future__ import division

import sys
from fractions import gcd


def read_case(reader):
    p, q = next(reader).split('/')
    return int(p), int(q)


def solve(p, q):
    g = gcd(p, q)
    p /= g
    q /= g
    if p == q:
        return 0
    if p == 0:
        return 'impossible'
    i = 0
    k = 1
    # print(p, q, p * k)
    while p * k < q and i <= 40:
        k *= 2
        i += 1
    if i > 40:
        return 'impossible'
    numerator = p * k - q
    if numerator == 0:
        return i
    if solve(numerator, q * k) != 'impossible':
        return i
    else:
        return 'impossible'


if __name__ == '__main__':
    reader = iter(sys.stdin)
    T = int(next(reader))
    for t in xrange(T):
        print('Case #{}: {}'.format(t + 1, solve(*read_case(reader))))
