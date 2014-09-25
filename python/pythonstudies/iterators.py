import unittest
import itertools
import operator


def collatz(n):
    m = n
    while True:
        yield m
        if m == 1:
            raise StopIteration
        if m % 2 == 0:
            m /= 2
        else:
            m = 3 * m + 1


def tent_map(mu, x0):
    x = x0
    while True:
        yield x
        x = mu * min(x, 1.0 - x)


def Q1(s, n):
    """
    Returns the first min(n,len(s)) elements of the Hofstadter Q sequence,
    given initial conditions s.
    """
    a = s[:]
    try:
        for __ in xrange(n - 2):
            a.append(a[-a[-1]] + a[-a[-2]])
    except IndexError:
        pass
    finally:
        return a


def Q2(s):
    """Returns a generator for Hofstadter Q
    sequence given initial conditions s.
    """
    a = s[:]
    while True:
        try:
            q = a[-a[-1]] + a[-a[-2]]
            a.append(q)
            yield q
        except IndexError:
            raise StopIteration()


class Q3(object):
    s = []

    def __init__(self, s):
        self.s = s[:]

    def current_state(self):
        return self.s

    def next(self):
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def fast_forward(self, n):
        for __ in range(n):
            self.next()

    def __iter__(self):
        return self


def inversion_number(A):
    """Return the inversion number of list A."""
    return sum(1 for x, y in itertools.combinations(xrange(len(A)), 2) if A[x] > A[y])


def inversion_set(A):
    """Return the inversion set of list A."""
    return set((x,y) for x,y in itertools.combinations(xrange(len(A)),2) if A[x]>A[y])


def permutation_parity(A):
    """Return the inversion set of list A."""
    return reduce(operator.mul, (-1 for x,y in itertools.combinations(xrange(len(A)),2) if A[x]>A[y]), 1)


def total_inversions(n):
    """Returns the total number of inversions in all permutations of a set of size n."""
    return sum(inversion_number(A) for A in itertools.permutations(xrange(n)))


def count_fixed_points(p):
    """Return the number of fixed points of p as a permutation."""
    return sum(1 for x in p if p[x]==x)


# Note: This is NOT an efficient way of doing this.
# Just to demonstrate the use of itertools and generators
def count_partial_derangements(n, k):
    """Returns the number of permutations of a set of size n with exactly k fixed points."""
    return sum(1 for p in itertools.permutations(xrange(n)) if count_fixed_points(p) == k)


def count_cycles(p):
    p1 = list(p)[:]
    c = 0
    while p1:
        c += 1
        x = p1.pop()
        y = p[x]
        while x != y:
            p1.remove(y)
            y = p[y]
    return c


class TestHofstadterQ(unittest.TestCase):
    def test_misc(self):
        # If the Collatz conjecture is true then this program will
        # always terminate.
        c = collatz(7)
        for m in c:
            print m
        # Test the tent map
        t = tent_map(2.0, 0.1)
        for __ in xrange(30):
            print t.next()

    def test_simple(self):
        q = Q1([1, 3], 10)
        print q

    def test_generator(self):
        q = Q2([1, 1])
        i = 0
        for __ in q:
            #print x;
            i += 1
            if i > 100:
                break

    def test_iterator(self):
        q = Q3([1, 1])
        print q.current_state()
        q.fast_forward(100)
        print q.current_state()


if __name__ == "__main__":
    unittest.main()
