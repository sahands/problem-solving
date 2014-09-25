import sys

t = int(next(sys.stdin).strip())
for tc in range(t):
    n = int(next(sys.stdin).strip())
    x = [int(z) for z in next(sys.stdin).strip().split(' ')]
    y = [int(z) for z in next(sys.stdin).strip().split(' ')]
    x.sort()
    y.sort(reverse=True)
    m = sum(u * v for u, v in zip(x, y))
    print('Case #{0}: {1}'.format(tc + 1, m))
