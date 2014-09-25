import fileinput


def abs_error(X, Y1, Y2, m, b):
    """Abs error of line y = mx + b"""



lines = fileinput.input()
T = int(lines.next().strip())

for __ in xrange(T):
    n = int(lines.next().strip())
    X = [0.0] * n
    Y1 = [0.0] * n
    Y2 = [0.0] * n

    for i in xrange(n):
        X[i], Y1[i], Y2[i] = [float(x) for x in lines.next().split()]

    print X
    print Y1
    print Y2
