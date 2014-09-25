from __future__ import print_function
from __future__ import division

from itertools import combinations
from itertools import product
import sys
import math


__author__ = 'Sahand Saba'


def get_data():
    matrix = []
    for line in sys.stdin:
        matrix.append(list(-math.log(float(x)) for x in line.split()))
    return matrix


def dist(matrix, A, B, func, m):
    for x in A:
        for y in B:
            m = func(m, matrix[x][y])
    return m


def avg_dist(matrix, A, B):
    s = sum(matrix[x][y] for x, y in product(A, B))
    return s / (len(A) * len(B))


def min_dist(matrix, A, B):
    return dist(matrix, A, B, min, 100000)


def max_dist(matrix, A, B):
    return dist(matrix, A, B, max, -100000)


def set_tostring(A):
    return '{' + ', '.join(str(x + 1) for x in A) + '}'


def hcluster(clusters, matrix, dist_func):
    A, B = None, None
    dist = 10000000
    for AA, BB in combinations(clusters, 2):
        d = dist_func(matrix, AA, BB)
        A, B, dist = (A, B, dist) if dist <= d else (AA, BB, d)

    # Remove A and B and add A union B
    clusters = clusters - frozenset([A, B]) | frozenset([A | B])
    print('Merging {0} and {1}'.format(set_tostring(A), set_tostring(B)))
    return clusters


def test_dist_func(matrix, dist_func):
    clusters = frozenset(frozenset([i]) for i in range(len(matrix)))
    while len(clusters) > 1:
        clusters = hcluster(clusters, matrix, dist_func)


if __name__ == '__main__':
    matrix = get_data()
    print('Testing MIN')
    print('--')
    test_dist_func(matrix, min_dist)
    print('--')

    print('Testing MAX')
    print('--')
    test_dist_func(matrix, max_dist)
    print('--')

    print('Testing AVG')
    print('--')
    test_dist_func(matrix, avg_dist)
    print('--')
