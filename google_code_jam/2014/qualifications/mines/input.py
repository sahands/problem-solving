from __future__ import print_function
from __future__ import division

import sys
from itertools import product


__author__ = 'Sahand Saba'


for i, j in product(range(1, 6), repeat=2):
    for k in range(i * j):
        print(i, j, k)
