from mathutils.numbertheory import rabin_miller_is_prime as is_prime,\
    square_root, is_primitive_root


def fibonacci_primitive_root(p):
    """
    Returns a fibonacci primitive root if p has one and None otherwise.
    Assumes p is a prime and that p is congruent to 1 or -1 modulo 5.
    """
    # The fibonacci root is a root of the polynomial x^2-x-1.  The roots of
    # this polynomial are given by 1+sqrt(5) and 1-sqrt(5) So the basic idea is
    # to simply find the square root, and check to see if either of those
    # values are a primitive root.

    q = square_root(5, p)
    half = (p + 1) / 2

    q1 = half + half * q
    q2 = half - half * q

    q1 %= p
    q2 %= p

    if is_primitive_root(q1, p):
        return q1
    elif is_primitive_root(n - q1, p):
        return q2
    return None


def test_root(r, p):
    print "Testing p =", p, "root =", r
    subgroup = [(r ** k) % p for k in xrange(p - 1)]
    if len(set(subgroup)) != p - 1:
        print "Not a primitive root!"
        return

    print subgroup

    fib = [1, r]
    for __ in xrange(p - 3):
        fib.append((fib[-1] + fib[-2]) % p)

    print fib
    if len(set(fib)) != p - 1:
        print "Not a FIBONACCI primitive root!"
        return

    print "Good!"


# N = 10 ** 4  # for testing
# N = 10 ** 6  # for more testing
N = 10 ** 8  # for the actual question
s = 5L  # manually checked five. It has a fibonacci primitive root of 3.
l = []
for n in xrange(10, N, 5):
    for i in [-1, 1]:
        if is_prime(n + i, k=10):
            # print n + i
            root = fibonacci_primitive_root(n + i)
            if root:
                # test_root(root, n + i)
                # l.append(n + i)
                s += n + i
    # if n % 10000 == 0:
    #    print '%0.2f%%' % (100.0 * float(n)/float(N))

print "---"
# print '\n'.join(str(s) for s in l)
# print len(l)
print s

exit()

for p in [11, 19, 29, 31]:
    print "p = " + str(p)
    q = square_root(5, 11)
    print "square root of 5 is " + str(q)
    print 1 + q, is_primitive_root(1 + q, p)
    print p + 1 - q, is_primitive_root(p + 1 - q, p)
    print is_primitive_root(p + 1 - q, p)
    print '----'
