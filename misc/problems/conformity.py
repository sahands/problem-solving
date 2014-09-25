# Problem 11286 - Conformity from UVA online judge
# http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2261
from collections import Counter

text1 = """100 101 102 103 488
100 200 300 101 102
103 102 101 488 100"""

text2 = """200 202 204 206 208
123 234 345 456 321
100 200 300 400 444"""

def conformity(t):
    c = Counter(tuple(sorted([int(x) for x in l.split(' ')])) for l in t.split('\n'))
    return sum(c[k] for k in c if c[k]==c.most_common(1)[0][1])


print conformity(text1)
print conformity(text2)
