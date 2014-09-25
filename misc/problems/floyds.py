"""floyds.py: Python implementation of Floyd's all-pair shortest paths."""

__author__ = 'Sahand Saba'
__email__ = 'sahands@gmail.com'
__copyright__ = 'Copyright 2013, Sahand Saba'

INFINITY = float("inf")

def floyds_shortest_paths(w):
    """
    Floyd's shortest path on weight matrix w. Constant INFINITY is used to
    denote no path.  Matrix w is assumed to be a list of length n of lists of
    length n.
    """

    n = len(w)
    W = [r[:] for r in w]  # copy of w
    # P is used to reconstruct paths
    P = [[None] * n for j in xrange(n)]

    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if W[i][j] > W[i][k] + W[k][j]:
                    W[i][j] = W[i][k] + W[k][j]
                    P[i][j] = k
    return W, P


def get_shortest_path(W, P, i, j):
    if W[i][j] is INFINITY:
        return None
    if i == j:
        return [i]
    k = P[i][j]
    if k is None:
        return []
    return get_shortest_path(W, P, i, k) + [k] + get_shortest_path(W, P, k, j)

if __name__ == '__main__':
    w = [
            [0, 8, INFINITY, 1],
            [INFINITY, 0, 1, INFINITY],
            [4, INFINITY, 0, INFINITY],
            [INFINITY, 2, 9, 0]
        ]

    W, P = floyds_shortest_paths(w)
    print W
    print P
    print get_shortest_path(W, P, 0, 2)
    print get_shortest_path(W, P, 2, 3)

