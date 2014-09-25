#!/usr/bin/env python

"""
max_sum_submatrix.py: Code to calculate the maximal sum submatrix and
subarray.
"""

__author__ = "Sahand Saba"
__email__ = "sahands@gmail.com"
__copyright__ = "Copyright 2013, Sahand Saba"


def max_sum_submatrix(m):
    """
    Returns the maximal sum in any of the submatrices, followed by the
    coordinates of one of the matrices that achieves the maximal sum.

    Running time is O(r c^2) where c is the number of columns and r is the
    number of rows. Note that if c is significantly larger than r then the
    function can be called on the transpose of the list and the coords
    translated afterwards accordingly to achieve a better running time.
    """

    rows = len(m)
    columns = len(m[0])

    # M holds the partial sums for each row such that the sum of numbers in row
    # r and columns c with i<= c <= j will be M[r, j] - M[r, i - 1]. Using a
    # dict for simplicity.
    M = dict()

    for r in xrange(rows):
        M[r, -1] = 0
        M[r, 0] = m[r][0]
        for c in xrange(1, columns):
            M[r, c] = M[r, c-1] + m[r][c]

    global_max = m[0][0]
    global_max_coords = (0, 0, 0, 0)

    for column_start in xrange(columns):
        for column_end in xrange(column_start, columns):
            # Consider the sum of columns between column_start and column_end
            # in all the rows as one array and run the maximal sub-array
            # algorithm on it to find the maximal submatrix with columns
            # starting at column_start and ending at column_end.
            a = lambda r: M[r, column_end] - M[r, column_start - 1]
            local_max, row_start, row_end = max_sum_subarray(a, rows)
            if local_max > global_max:
                global_max = local_max
                global_max_coords = (row_start,
                                     row_end,
                                     column_start,
                                     column_end)

    return global_max, global_max_coords


def max_sum_subarray(a, n):
    """Assumes a is a callable, with the index passed to it as a parameter."""
    local_max = global_max = a(0)
    global_start = local_start = end = 0

    for i in xrange(1, n):
        if local_max > 0:
            local_max += a(i)
        else:
            local_max = a(i)
            local_start = i

        if global_max < local_max:
            global_max = local_max
            global_start = local_start
            end = i

    return global_max, global_start, end


if __name__ == "__main__":
    # Sample test from UVA problem
    T = """0 -2 -7 0
9 2 -6 2
-4 1 -4 1
-1 8 0 -2"""

    m = [[int(x) for x in r.split(' ')] for r in T.split('\n')]
    s, coords = max_sum_submatrix(m)
    print s, coords
    print '\n'.join([' '.join(str(x) for x in r[coords[2]:coords[3]+1])
                    for r in m[coords[0]:coords[1]+1]])
