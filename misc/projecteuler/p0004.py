M = 100  # smallest three digit number
N = 999  # and the largest one

palindromes = []
for n in xrange(N, M - 1, -1):
    for m in xrange(N, M - 1, -1):
        if str(n * m) == ''.join(reversed(str(n * m))):
            print n, m, n * m
            palindromes.append(n * m)

print max(palindromes)
