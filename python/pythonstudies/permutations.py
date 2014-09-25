def permutations(items):
    if len(items) == 0:
        yield []
    else:
        pi = items[:]
        for i in xrange(len(pi)):
            pi[0], pi[i] = pi[i], pi[0]
            for p in permutations(pi[1:]):
                yield [pi[0]] + p
