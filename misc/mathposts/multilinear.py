__author__ = "Sahand Saba"

from itertools import product
from random import randint


def _multilinear(truth, n, N, k):
    if n == 0:
        return Constant(truth)

    L = truth >> k
    R = truth & (2 ** k - 1)
    g = _multilinear(L, n - 1, N, k // 2)
    h = _multilinear(L ^ R, n - 1, N, k // 2)
    if h == 0:
        return g
    if h == 1:
        if g == 0:
            return Variable(N - n)
        else:
            return Xor(Variable(N - n), g)
    else:
        if g == 0:
            return Conjunction(Variable(N - n), h)
        else:
            return Xor(g, Conjunction(Variable(N - n), h))


def multilinear(truth, n):
    """
    Treating input 'truth' as a 2^n bit number representing the truth table of
    a boolean function of n variables, calculate the multilinear representation
    of the boolean function and return it.
    """
    return _multilinear(truth, n, n, 2 ** (n - 1))


class Expression(object):
    def flatten(self):
        pass

    def expand(self):
        return self


class Constant(Expression):
    value = 0

    def __init__(self, val):
        self.value = val

    def __eq__(self, v):
        return self.value == v

    def __str__(self):
        return str(self.value)

    def evaluate(self, assignment):
        return self.value


class Variable(Expression):
    index = 0

    def __init__(self, index):
        self.index = index

    def __str__(self):
        return chr(ord('a') + self.index)

    def evaluate(self, assignment):
        return assignment[self.index]


class AssociativeOperator(Expression):
    operands = []

    def flatten(self):
        for o in self.operands:
            o.flatten()

    def sort(self):
        self.operands.sort(key=lambda x: str(x))


class Conjunction(AssociativeOperator):
    def __init__(self, *args):
        self.operands = args

    def __str__(self):
        return ''.join('(' + str(a) + ')' if type(a) is Xor else str(a)
                       for a in self.operands)

    def evaluate(self, assignment):
        return reduce(lambda s, a: a.evaluate(assignment) * s,
                      self.operands, 1)

    def flatten(self):
        operands = []
        for o in self.operands:
            o.flatten()
            if type(o) is Conjunction:
                operands.extend(o.operands)
            elif type(o) is Constant and o.value == 1:
                continue
            elif type(o) is Constant and o.value == 0:
                operands = [Constant(0)]
                break
            else:
                operands.append(o)
        self.operands = operands

    def expand(self):
        self.flatten()
        p = [o.expand().operands if type(o) is Xor else [o.expand()]
             for o in self.operands]
        operands = []
        for t in product(*p):
            operands.append(Conjunction(*t))
        m = Xor(*operands)
        m.flatten()
        return m


class Xor(AssociativeOperator):
    def __init__(self, *args):
        self.operands = args

    def __str__(self):
        return '+'.join(str(a) for a in self.operands)

    def evaluate(self, assignment):
        return reduce(lambda s, a: (a.evaluate(assignment) + s) % 2,
                      self.operands, 0)

    def flatten(self):
        super(Xor, self).flatten()
        operands = []
        for o in self.operands:
            if type(o) is Xor:
                operands.extend(o.operands)
            else:
                operands.append(o)
        self.operands = operands

    def expand(self):
        operands = [o.expand() for o in self.operands]
        m = Xor(*operands)
        m.flatten()
        return m


def test(truth, n):
    m = multilinear(truth, n)
    m = m.expand()
    m.sort()
    s = ""
    for assignment in product(*[[0, 1] for i in xrange(n)]):
        s += str(m.evaluate(assignment))

    check = int(s, 2) == truth
    return s, m, check


if __name__ == '__main__':
    N = 100  # Test with this many test cases
    n = 4  # Number of variables for the test boolean functions
    table_row_format = "{0: <20}\t{1: <32}\t{2: <20}\t{3: <6}"
    print table_row_format.format("Truth table", "Multilinear expression",
                                  "Evaluated truth table", "Check")
    for __ in xrange(N):
        truth = randint(0, 2 ** (2 ** n))
        s, m, check = test(truth, n)
        print table_row_format.format(bin(truth), m, s, str(check))
        if not check:
            print "Mismath: test failed with truth table " + str(truth)
