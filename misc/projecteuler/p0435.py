def find_fib_period(k, x):
    h = {}
    a, b, n, s, x0 = 0, 1, 0, 0, x
    while True:
        # print n, '-', a, b
        if (a, b) in h:
            # print h[a, b], n, n - h[a, b], s, x
            print x0, s
            return n - h[a, b], s

        h[a, b] = n
        a, b, n, s, x = b, a + b, n + 1, s + a*x, x*x0
        a %= k
        b %= k
        s %= k
        x %= k

for x in xrange(0, 101):
    find_fib_period(2 ** 11, x)

for x in xrange(0, 101):
    find_fib_period(3 ** 6, x)

# find_fib_period(3 ** 6)
# find_fib_period(5 ** 3)
# find_fib_period(7 ** 2)
# find_fib_period(11)
# find_fib_period(13)

