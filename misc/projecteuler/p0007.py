from itertools import count
from mathutils.primes import rabin_miller_is_prime as is_prime

N = 10001
c = 2
for n in count(3):
    if is_prime(n):
        print c, n
        if c == N:
            exit()
        c += 1
    n += 2

