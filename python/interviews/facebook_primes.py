import itertools
import collections


def products_simple(primes):
    c = collections.Counter(primes)
    result = [1]
    for p in c.keys():
        result += [x * p ** k for x in result for k in xrange(1, c[p] + 1)]
    return result


def products(primes):
    product_reducer = lambda product, (i, k): product * c[i][0] ** k
    c = collections.Counter(primes).items()
    A = [xrange(k + 1) for __, k in c]
    for f in itertools.product(*A):
        yield reduce(product_reducer, enumerate(f), 1)


for primes in [
               [2, 3, 11],
               [2, 2, 3, 5],
               [2, 2, 2, 2]
               ]:
    print sorted(list(products(primes)))
    print sorted(products_simple(primes))
