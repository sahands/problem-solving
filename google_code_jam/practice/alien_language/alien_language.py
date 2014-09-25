import sys
import re


L, D, N = (int(x) for x in next(sys.stdin).strip().split())
words = [next(sys.stdin).strip() for __ in range(D)]
for i in range(N):
    p = next(sys.stdin).strip()
    r = ""
    op = False
    for c in p:
        if c == '(':
            op = True
            r += '('
        elif c == ')':
            r = r[:-1] + ')'
            op = False
        else:
            r += c + ("|" if op else "")
    reg = re.compile(r)
    matches = len([1 for w in words if reg.match(w) is not None])
    print('Case #{0}: {1}'.format(i + 1, matches))
