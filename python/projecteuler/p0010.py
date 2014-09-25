from mathutils.primes import rabin_miller_is_prime as is_prime

N = 2 * 10 ** 6 
s = 2
for n in xrange(3, N, 2):
    if is_prime(n):
        print n, s
        s += n

print s
