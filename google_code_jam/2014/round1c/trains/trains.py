from __future__ import print_function
from __future__ import division

import sys
import math
from fractions import gcd
from collections import Counter
from collections import defaultdict


M = 1000000007


def read_case(reader):
    next(reader)
    return next(reader).split()


def simplify(s):
    def gen():
        cur = s[0]
        yield cur
        for i in range(1, len(s)):
            if cur != s[i]:
                cur = s[i]
                yield cur
    return ''.join(gen())


def is_simple_valid(s):
    seen = set()
    for c in s[1:-1]:
        if c in seen:
            return False
        seen.add(c)
    return True


def count_starting_with(c, S, CS, CCS, starting_with, ending_with, used=None, used_n=0):
    print(c, S, used, used_n)
    if used_n == len(S):
        return 1
    if used is None:
        used = Counter()
    n = 0
    if c is None:
        col = [s for s in S if used[s] < CS[s]]
        starting_options = set(s[0] for s in col) - set(s[1] for s in col)
        col = [s for cc in starting_options for s in starting_with[cc]]
    else:
        col = [s for s in starting_with[c] if used[s] < CS[s]]

    for s in col:
        q = s[1]
        if CCS[s[1]] == 1:
            q = None
        used[s] += 1
        n += count_starting_with(q,
                                 S,
                                 CS,
                                 CCS,
                                 starting_with,
                                 ending_with,
                                 used,
                                 used_n + 1)
        used[s] -= 1
    return n % M


def count_based_on_T(T):
    n = 1
    for x in T.values():
        n *= (math.factorial(x)) % M
    return n % M


def solve(S):
    S = [simplify(s) for s in S]
    # print(S)
    if False in (is_simple_valid(s) for s in S):
        return 0

    for s in S:
        for t in S:
            if s is not t:
                for c in s[1:-1]:
                    if c in t:
                        return 0

    # Now we can assume only the first and last char count
    S = [s[0] + s[-1] for s in S]
    T = Counter([s[0] for s in S if s[0] == s[1]])
    S = [s for s in S if s[0] != s[1]]
    CS = Counter(S)
    CCS = Counter([s[0] for s in S])
    CCS.update([s[1] for s in S])
    # print(S)
    # print(T)
    if len(S) == 0:
        return count_based_on_T(T) * math.factorial(len(T))

    starting_with = defaultdict(list)
    ending_with = defaultdict(list)
    for s in S:
        starting_with[s[0]].append(s)
    for s in S:
        ending_with[s[1]].append(s)

    n = 0
    starting_options = set(starting_with.keys()) - set(ending_with.keys())
    # print(starting_options)
    n = sum(count_starting_with(c, S, CS, CCS, starting_with, None) % M
            for c in starting_options)

    # TODO: Take T into consideration
    n *= count_based_on_T(T)
    n = n % M
    TT = set(T) - set(starting_with.keys()) - set(ending_with.keys())
    n *= math.factorial(len(TT) + 1)
    return n % M


if __name__ == '__main__':
    reader = iter(sys.stdin)
    T = int(next(reader))
    for t in xrange(T):
        print('Case #{}: {}'.format(t + 1, solve(read_case(reader)) % M))
        # break
