from __future__ import division
import math


def fib(n):
    SQRT5 = math.sqrt(5)
    PHI = (SQRT5 + 1) / 2
    return int(PHI ** n / SQRT5 + 0.5)
