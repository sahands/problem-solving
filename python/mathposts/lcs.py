from collections import defaultdict


def antidiagonal_traverse(n, m, visit_function):
    """Visits the entries an n by m matrix in antidiagonal order.
    This ensures any elements to the top and left (inclusive) of the entry
    are visited before the entry itself."""
    for d in xrange(m + n - 1):
        i = max(0, d - m + 1)
        j = min(d, m - 1)
        while j >= 0 and i < n:
            visit_function(i, j)
            i += 1
            j -= 1


def lcs(x, y):
    n = len(x)
    m = len(y)
    M = dict()
    L = defaultdict(int)
    M[-1, -1] = [set()]
    M[0, -1] = [set()]
    M[-1, 0] = [set()]

    def visit(i, j):
        if x[i] == y[j]:
            L[i, j] = 1 + L[i - 1, j - 1]
            if (i - 1, j - 1) in M:
                M[i, j] = [s.union([(i, j)]) for s in M[i - 1, j - 1]]
            else:
                M[i, j] = [set([(i, j)])]

            if L[i, j] == L[i - 1, j]:
                M[i, j] += M[i - 1, j]

            if L[i, j] == L[i, j - 1] and M[i, j - 1] not in M[i, j]:
                M[i, j] += M[i, j - 1]

        else:
            top = L[i - 1, j]
            left = L[i, j - 1]
            L[i, j] = max(top, left)
            if top > left:
                M[i, j] = M[i - 1, j]
            elif top == left:
                M[i, j] = M[i - 1, j]
                if M[i, j - 1] != M[i - 1, j]:
                    M[i, j] = M[i, j - 1]
            else:
                M[i, j] = M[i, j - 1]

    antidiagonal_traverse(n, m, visit)
    return L[n - 1, m - 1], M[n - 1, m - 1]


L, M = lcs("aaabcc", "abbc")
print "Longest LCS has length:", L
print "Total LCS's found:", len(M)
print "List of all LCS's:"
for l in sorted(sorted(x) for x in M):
    print list(l)