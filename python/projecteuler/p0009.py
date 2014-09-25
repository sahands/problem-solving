n = 1000
for a in xrange(1, n):
    for b in xrange(a + 1, n):
        c = n - b - a
        if a ** 2 + b ** 2 == c ** 2:
            print a, b, c, a * b * c
