def explain(M, numbers, i, j, k, d):
    print 'Number of ways to pick %d numbers from %s so that the sum adds up to %d modulo %d = %d' % (i, repr(numbers[:j+1]), k, d, M[i][j][k])

def solve(numbers, d, m):
    """
    Output how many ways m elements of numbers can be picked so that their
    sum is divisible by d
    """
    n = len(numbers)
    # M[i][j][k] is the number of ways to pick i elements of numbers numbers[0] to numbers[j]
    # so that their sum is k modulo d

    M = [[[0 for __ in xrange(d)] for __ in xrange(n)] for _ in xrange(m+1)]
    MS = [[[[] for __ in xrange(d)] for __ in xrange(n)] for _ in xrange(m+1)]

    for j in xrange(n):
        M[0][j][0] = 1 
        MS[0][j][0] = [[]]

    for i in xrange(1, m + 1):
        for j in xrange(n):
            for k in xrange(d):
                if j + 1 < i:
                    M[i][j][k] = 0
                    MS[i][j][k] = [] 
                elif j == 0:
                    M[i][j][k] = 1 if numbers[j] % d == k else 0
                    MS[i][j][k] = [[numbers[j]]] if numbers[j] % d == k else []
                else:
                    M[i][j][k] = M[i][j-1][k] + M[i-1][j-1][(-numbers[j] + k) % d]
                    MS[i][j][k] = MS[i][j-1][k] + [l + [numbers[j]] for l in MS[i-1][j-1][(-numbers[j] + k) % d]]  

    # print '\n---\n'.join('\t\n'.join(repr(x) for x in l) for l in M)
    print M[m][n-1][0]
    print MS[m][n-1][0]


if __name__ == "__main__":
    # solve(range(1, 11), 5, 1)
    # solve(range(1, 11), 5, 2)
    # solve(range(2, 7), 7, 3)
    solve([2147483647, 2147483647, 2147483647, 2, -2147483648], 5, 2);

