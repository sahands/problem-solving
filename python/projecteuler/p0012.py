from mathutils.primes import number_of_factors

for n in xrange(1, 100000):
    c = n * (n+1) // 2
    if number_of_factors(c) > 500:
        print c
        exit()
