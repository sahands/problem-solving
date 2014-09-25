from itertools import permutations, product


class Permutation(object):
    pi = []

    def __init__(self, *p):
        self.pi = p

    def __str__(self):
        n = len(self.pi)
        seen = dict()
        s = ""
        while len(seen) < n:
            start = 0
            while start in seen:
                start += 1
            seen[start] = True
            cycle = [start]
            t = self.pi[start]
            while  t != start:
                seen[t] = True
                cycle.append(t)
                t = self.pi[t]
            s += '(' + ','.join(str(c) for c in cycle) + ')'
        return s


class BooleanFunction(object):
    truth = 0
    n = 0

    def __init__(self, truth, n):
        self.truth = truth
        self.n = n

    def evaluate(self, assignment):
        assignment = 2 ** self.n - assignment - 1
        return (self.truth >> assignment) & 1


def fixed_boolean_functions(p):
    """Returns the number of boolean functions fixed under permutation pi."""
    n = len(p)
    bits = 2 ** n
    for t in xrange(2 ** bits):
        pass


def permute_truth_table(truth, p, n):
    t = 0
    print "pi = ", p
    for assignment in xrange(2 ** n):
        print "assignment ", bin(assignment)
        permuted_assignment = 0
        for i in xrange(n):
            permuted_assignment *= 2
            permuted_assignment += (assignment >> p.pi[i]) & 1
        print "permuted assignment ", bin(permuted_assignment)
        # t = t | (truth & (n - (2 ** - permuted_assignment)))

    return t


print bin(permute_truth_table(0b1010, Permutation(0, 1), 2))
print bin(permute_truth_table(0b1010, Permutation(1, 0), 2))



for pi in permutations([0, 1, 2]):
    print Permutation(*pi)

f = BooleanFunction(0b1001, 2)
print f.evaluate(0b00)
print f.evaluate(0b01)
print f.evaluate(0b10)
print f.evaluate(0b11)
