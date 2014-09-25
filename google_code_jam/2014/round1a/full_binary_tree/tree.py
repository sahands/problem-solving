from __future__ import print_function
from __future__ import division

from collections import defaultdict
import sys


__author__ = 'Sahand Saba'


def read_case(reader):
    N = int(next(reader))
    E = set()
    G = defaultdict(list)
    for i in xrange(N - 1):
        u, v = (int(x) for x in next(reader).split())
        G[u].append(v)
        G[v].append(u)
        E.add((u, v))
    return N, E, G


def try_root(G, r, parent=None):
    children = [v for v in G[r] if v != parent]
    if len(children) == 1:
        s, c = try_root(G, children[0], r)
        return c, c + 1
    else:
        s, c = 0, 1
        for child in children:
            sc, cc = try_root(G, child, r)
            s += sc
            c += cc
        print(r, ' has ', c, 'nodes')
        return s, c


def solve(N, G):
    s = 100000000
    for r in range(1, N + 1):
        print("Trying ", r)
        sr, cr = try_root(G, r)
        print("Need to remove ", sr, " nodes")
        s = min(s, sr)
    return s


if __name__ == '__main__':
    reader = iter(sys.stdin)
    T = int(next(reader))
    for t in xrange(T):
        N, E, G = read_case(reader)
        s = solve(N, G)
        print('Case #{0}: {1} '.format(t + 1, s))
