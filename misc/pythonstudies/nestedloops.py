from itertools import combinations, product


n = 4
d = 3


def visit(*indices):
    print indices

# Loop through all possible indices of a 3-D array
for i in xrange(n):
    for j in xrange(n):
        for k in xrange(n):
            visit(i, j, k)

# Equivalent using itertools.product
for indices in product(*([xrange(n)] * d)):
    visit(*indices)

# Now loop through all indices 0 <= i < j < k <= n
for i in xrange(n):
    for j in xrange(i + 1, n):
        for k in xrange(j + 1, n):
            visit(i, j, k)

# And equivalent using itertools.combinations
for indices in combinations(xrange(n), d):
    visit(*indices)
