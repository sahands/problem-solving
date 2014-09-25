from __future__ import division
import sys
import fileinput

lines = fileinput.input()
for line in lines:
    s = [int(x) for x in line.strip().split()]
    print reduce(lambda (m, S), x: (max(m, x), S + x if x > m else S), s[1:], (0, 0))[1]

