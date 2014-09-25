from __future__ import division
from sys import stdin


def expected_iterations(A, cache, candidates, cost):
    n = len(A)
    h = tuple(A)
    if h in cache:
        return cache[h]
    E = 0.0
    C = candidates(A)
    if C:
        for (i, j) in C:
            A[i], A[j] = A[j], A[i]
            E += expected_iterations(A, cache, candidates, cost)
            A[i], A[j] = A[j], A[i]
        E += cost(n)
        E /= len(C)
    cache[h] = E
    return E

def inversions(A):
    return [(i, j)
            for i in xrange(len(A) - 1)
            for j in xrange(i + 1, len(A))
            if A[i] > A[j]]

def adj_inversions(A):
    return [(i, i + 1)
            for i in xrange(len(A) - 1)
            if A[i] > A[i + 1]]


monty_cost = lambda n: n * n / 2.0
carlos_cost = lambda n: n - 1

def process_test_case(A):
    carlos_cache = {}
    monty_cache = {}
    m = expected_iterations(A, monty_cache, inversions, monty_cost)
    c = expected_iterations(A, carlos_cache, adj_inversions, carlos_cost)
    print 'Monty {:.6f} Carlos {:.6f}'.format(m, c)


if __name__ == '__main__':
    T = int(stdin.readline())
    for __ in xrange(T):
        A = [int(x) for x in stdin.readline().split(' ')]
        # ignore the first element since is is length of the array
        process_test_case(A[1:])
