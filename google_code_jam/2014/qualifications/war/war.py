from __future__ import print_function
from __future__ import division

import sys


__author__ = 'Sahand Saba'


def read_case(reader):
    N = int(next(reader))
    A = (float(x) * 1000.0 for x in next(reader).split())
    B = (float(x) * 1000.0 for x in next(reader).split())
    return N, A, B


def binary_search(A, x):
    """Return the index of y in A such that y is the first number > x"""
    start = 0
    end = len(A)
    while start < end:
        m = (end + start) // 2
        if A[m] < x:
            start = m + 1
        else:
            end = m

    return end if end < len(A) else None


def war(N, A, B):
    naomi = 0
    while A:
        k = binary_search(B, A[-1])
        del A[-1]
        if k is not None:
            del B[k]
        else:
            naomi += 1

    return naomi


def deceit(N, A, B):
    naomi = 0
    while A:
        # Here's Naomi's strategy
        # 1) If she can score a point, she will immediately
        # 2) If not, she will use her smallest block to destroy Ken's largest.
        # Quite simple!
        k = binary_search(A, B[-1])
        if k is not None:
            del B[-1]
            del A[k]
            naomi += 1
        else:
            del A[0]
            del B[-1]

    return naomi


def solve(N, A, B):
    return deceit(N, A[:], B[:]), war(N, A, B)


if __name__ == '__main__':
    reader = iter(sys.stdin)
    T = int(next(reader))
    for t in xrange(T):
        N, A, B = read_case(reader)
        d, w = solve(N, sorted(A), sorted(B))
        print('Case #{0}: {1} {2}'.format(t + 1, d, w))
