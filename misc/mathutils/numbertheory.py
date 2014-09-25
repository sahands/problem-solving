import random
import itertools
import math
from operator import mul
from collections import Counter
import primes_list


# I wrote this, then realized that pow(a, k, n) does the same thing except
# faster since it's implemented in C. See
# http://svn.python.org/view/python/tags/r271/Objects/longobject.c?view=markup
def pow_mod(a, k, n):
    """Calculate a^k modulo n using O(log(k)) operations."""
    x = 1
    while k > 0:
        if k % 2 == 1:
            x = (x * a) % n
        a = (a * a) % n
        k //= 2
    return x


def square_root(n, p):
    """
    Finds the square root of n modulo prime p. Uses Tonelli-Shanks
    algorithm.
    """
    # First the easy, obvious case:
    if p % 4 == 3:
        return pow(n, (p + 1) / 4, p)

    q, s = (p - 1) / 4, 2
    while q % 2 == 0:
        q /= 2
        s += 1

    # Find a quadratic non-residue z
    z = 0
    for z in prime_generator(p - 1):
        if not is_quadratic_residue_eulers_criterion(z, p):
            break
    if z == 0:
        raise RuntimeError()
    c = pow(z, q, p)
    r = pow(n, (q + 1) / 2, p)
    t = pow(n, q, p)
    m = s
    while t != 1:
        i = 1
        t1 = (t * t) % p
        while t1 != 1:
            t1 = (t1 ** 2) % p
            i += 1
        b = pow(c, 2 ** (m - i - 1), p)
        r = (r * b) % p
        t = (t * b ** 2) % p
        c = (b ** 2) % p
        m = i

    return r


def factor_out_twos(n):
    """Returns q and s such that n = q*2^s."""
    q = n
    s = 0
    while q % 2 == 0:
        q /= 2
        s += 1
    return q, s


def jacobi_symbol(m, n):
    print "WARNING: jacobi_symbol used before being fully tested!"
    m = m % n
    if m == 1:
        return 1
    q, s = factor_out_twos(m)
    r1 = 1
    if s % 2 == 1:
        r1 = 1 if ((n % 8) in [1, 7]) else -1
    if q == 1:
        return r1
    return r1 * jacobi_symbol(n % q, q)


def is_quadratic_residue_eulers_criterion(a, p):
    """
    Assumes a is coprime with p and p is an odd prime. Returns true if a is a
    quadratic residue of p.
    """
    return pow(a, (p - 1) / 2, p) == 1


def is_primitive_root(n, p):
    """Returns true if n is a primitive root modulo prime p."""
    for q in factor(p - 1):
        if pow(n, (p - 1) / q, p) == 1:
            return False
    return True


def prime_generator(max_p=None):
    for p in primes_list.less_than_hundred_thousand:
        if max_p is not None and p > max_p:
            break
        yield p

    p = primes_list.less_than_hundred_thousand[-1] + 2
    while True:
        if max_p is not None and p > max_p:
            break
        if rabin_miller_is_prime(p):
            yield p
        p += 2


def factor(n):
    k = 0
    while n % 2 == 0:
        k += 1
        n //= 2

    r = [2] * k
    if n == 1:
        return r
    p = int(math.sqrt(n))
    if p % 2 == 0:
        p -= 1
    if p == 1:
        return r + [n]
    while p > 2:
        if n % p == 0:
            return r + factor(p) + factor(n//p)
        p -= 2
    return r + [n]


def number_of_factors(n):
    c = Counter(factor(n))
    return reduce(mul, [c[k] + 1 for k in c], 1)


def basic_is_prime(n, K=-1):
    """Returns True if n is a prime, and False it is a composite
    by trying to divide it by two and first K odd primes. Returns
    None if test is inconclusive."""
    if n % 2 == 0:
        return n == 2
    for p in primes_list.less_than_hundred_thousand[:K]:
        if n % p == 0:
            return n == p
        # if p * p > n:
        #    return True

    return None


def rabin_miller_is_prime(n, k=20):
    """
    Test n for primality using Rabin-Miller algorithm, with k
    random witness attempts. False return means n is certainly a composite.
    True return value indicates n is *probably* a prime. False positive
    probability is reduced exponentially the larger k gets.
    """
    b = basic_is_prime(n, K=100)
    if b is not None:
        return b

    m = n - 1
    s = 0
    while m % 2 == 0:
        s += 1
        m //= 2
    liars = set()
    get_new_x = lambda: random.randint(2, n - 1)
    while len(liars) < k:
        x = get_new_x()
        while x in liars:
            x = get_new_x()
        xi = pow(x, m, n)
        witness = True
        if xi == 1 or xi == n - 1:
            witness = False
        else:
            for __ in xrange(s - 1):
                xi = (xi ** 2) % n
                if xi == 1:
                    return False
                elif xi == n - 1:
                    witness = False
                    break
            xi = (xi ** 2) % n
            if xi != 1:
                return False
        if witness:
            return False
        else:
            liars.add(x)
    return True


def simple_is_prime(n):
    """Returns True if n is a prime. False otherwise."""
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    k = 6L
    while (k - 1) ** 2 <= n:
        if n % (k - 1) == 0 or n % (k + 1) == 0:
            return False
        k += 6
    return True


def generate_random_prime(bits, primality_test=rabin_miller_is_prime):
    """Generate random prime number with n bits."""
    get_random_t = lambda: random.getrandbits(bits) | 1 << bits | 1
    p = get_random_t()
    for i in itertools.count(1):
        if primality_test(p):
            return p
        else:
            if i % (bits * 2) == 0:
                p = get_random_t()
            else:
                p += 2  # Add 2 since we are only interested in odd numbers


if __name__ == '__main__':
    print square_root(10, 13)
    print square_root(5, 41)
    print square_root(5, 449)
