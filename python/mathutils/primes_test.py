import unittest
import math

from numbertheory import simple_is_prime, rabin_miller_is_prime, generate_random_prime
import primes_list
from utils.decorators import logged


class TestPrimes(unittest.TestCase):
    def primality_tester(self, test):
        for p in primes_list.less_than_hundred_thousand[1000:1200]:
            self.assert_(test(p), "%s failed with %ld" % (test.__name__, p))
        for p in primes_list.less_than_hundred_thousand[1000:1010]:
            for q in primes_list.less_than_hundred_thousand[1000:1010]:
                self.assert_(not test(p * q), "%s failed with %ld" % (test.__name__, p * q))

    @logged()
    def test_is_prime(self):
        self.primality_tester(simple_is_prime)

    @logged()
    def test_is_prime_rabin_miller(self):
        self.primality_tester(rabin_miller_is_prime)

    @logged()
    def test_prime_generation(self):
        bits = 1024
        for __ in xrange(5):
            p = generate_random_prime(bits, rabin_miller_is_prime)
            print p
            self.assert_(int(math.log(p, 2)) == bits)

if __name__ == '__main__':
    unittest.main()
    #cProfile.run("unittest.main()")
