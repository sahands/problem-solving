import sys


def process(l):
    travel = 0
    while len(l) > 0:
        k = min(5, len(l))
        travel += 2 * l[-1]
        l = l[:-k]
    return travel


for line in sys.stdin:
    l = [int(x) for x in line.split()]
    n = l[0]
    h = l[-1]
    l = l[1:-1]

    l1 = sorted(x - h for x in l if x > h)
    l2 = sorted(h - x for x in l if x < h)

    # print l1, l2

    p1 = process(l1[:])
    p2 = process(l2[:])

    if not l1:
        l1 = [0]
    if not l2:
        l2 = [0]

    # print p1, p2, n, max(l1[-1], l2[-1])
    print p1 + p2 + n - max(l1[-1], l2[-1])

