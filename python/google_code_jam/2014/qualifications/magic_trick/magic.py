from __future__ import print_function
from __future__ import division

import sys
from itertools import izip


__author__ = 'Sahand Saba'


def read_case(reader):
    a1 = int(next(reader))
    M1 = []
    for i, line in izip(xrange(4), reader):
        M1.append(set(int(x) for x in line.split()))
    a2 = int(next(reader))
    M2 = []
    for i, line in izip(xrange(4), reader):
        M2.append(set(int(x) for x in line.split()))

    return M1[a1 - 1], M2[a2 - 1]


if __name__ == '__main__':
    reader = iter(sys.stdin)
    T = int(next(reader))
    for t in xrange(T):
        print('Case #{0}: '.format(t + 1), end='')
        A, B = read_case(reader)
        C = A & B
        if len(C) == 1:
            print(next(iter(C)))
        elif len(C) == 0:
            print('Volunteer cheated!')
        else:
            print('Bad magician!')
