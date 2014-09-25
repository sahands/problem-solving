import unittest
import random
import math
import cProfile
import fractions
from utils.decorators import logged
from utils.primes import generate_random_prime
from utils import modular


def extended_gcd(a, b):
    """Returns pair (x, y) such that xa + yb = gcd(a, b)"""
    x, lastx, y, lasty = 0, 1, 1, 0
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return lastx, lasty


def multiplicative_inverse(e, n):
    """Find the multiplicative inverse of e mod n."""
    x, y = extended_gcd(e, n)
    if x < 0:
        return n + x
    return x


def rsa_generate_key(bits):
    p = generate_random_prime(bits / 2)
    q = generate_random_prime(bits / 2)
    # Ensure q != p, though for large values of bits this is
    # statistically very unlikely
    while q == p:
        q = generate_random_prime(bits / 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    # Here we pick a random e, but a fixed value for e can also be used.
    while True:
        e = random.randint(3, phi - 1)
        if fractions.gcd(e, phi) == 1:
            break
    d = multiplicative_inverse(e, phi)
    return (n, e, d)


def rsa_encrypt(message, n, e):
    return modular.power(message, e, n)


def rsa_decrypt(cipher, n, d):
    return modular.power(cipher, d, n)


class TestRSA(unittest.TestCase):
    @logged()
    def test_extended_gcd(self):
        numbers = [(1071, 462, 21)]
        for (n, m, r) in numbers:
            (x, y) = extended_gcd(m, n)
            self.assert_(x * m + y * n == r)

    @logged()
    def test_rsa(self):
        bits = 1024
        (n, d, e) = rsa_generate_key(bits)
        for __ in xrange(10):
            message = random.randint(0, n - 1)
            cipher = rsa_encrypt(message, n, e)
            message2 = rsa_decrypt(cipher, n, d)
            self.assert_(message == message2)

    @logged()
    def test_exponentiate_mod(self):
        for __ in xrange(1000):
            a = random.randint(2, 10000)
            k = random.randint(4, 10000)
            n = random.randint(10, 10000)
            e1 = modular.power(a, k, n)
            e2 = (a ** k) % n
            self.assert_(e1 == e2, str([a, k, n, e1, e2]))


if __name__ == '__main__':
    unittest.main()
    #cProfile.run("unittest.main()")
