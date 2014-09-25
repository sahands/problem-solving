from itertools import product
from collections import defaultdict


def construct_distribution(A, M, x, y, i, seen):
    if i < 0:
        return [[], []]

    b = M[x, y, i]
    # print x, y, i, b
    a = A[i]
    if b == 1:
        x -= a
    elif b == 2:
        y -= a
    dist = construct_distribution(A, M, x, y, i - 1, seen)
    if b < 3:
        seen[i] = True
        dist[b - 1].append(a)
    return dist


def scheduler3(A):
    """Schedule tasks taking times in A for 3 machines."""
    # P = []
    S = sum(A)
    M = defaultdict(int)
    global_min = S
    global_min_boxes = (0, 0, S)
    M[0, 0, -1] = 3
    for i, a in enumerate(A):
        for x in xrange(S + 1):
            for y in xrange(x, S + 1):
                if M[x - a, y, i - 1] > 0:
                    M[x, y, i] = 1
                elif M[x, y - a, i - 1] > 0:
                    M[x, y, i] = 2
                elif M[x, y, i - 1] > 0:
                    M[x, y, i] = 3

                if M[x, y, i] > 0:
                    z = S - x - y
                    m = max(x, y, z)
                    if m < global_min:
                        # print x, y, z, m, i, a
                        global_min = m
                        global_min_boxes = (x, y, z)
                        global_min_last_i = i
                    # P.append([x, y, z])
    seen = defaultdict(bool)
    distribution = construct_distribution(A, M, global_min_boxes[0], global_min_boxes[1], global_min_last_i, seen)
    distribution.append([A[i] for i in xrange(len(A)) if not seen[i]])
    distribution = [sorted(d) for d in distribution]
    # distribution[0] = set(distribution[0])
    # distribution[1] = set(distribution[1])
    # distribution.append(set(A) - distribution[0] - distribution[1])
    return global_min, global_min_boxes, distribution


def scheduler(A, d):
    """Schedule tasks taking times in A for d machines."""
    P = []
    S = sum(A)
    M = defaultdict(int)
    best = S
    M[tuple([0] * (d - 1)), -1] = 1
    for i, a in enumerate(A):
        for p in product(*[range(S + 1) for __ in xrange(d-1)]):
            # M[p, i] = M[p, i - 1]
            # if M[p, i] > 0:
            #     continue
            for j in xrange(d - 1):
                pp = list(p[:])
                pp[j] -= a
                if M[tuple(pp), i - 1] > 0:
                    M[p, i] = 1
                    break

            if M[p, i] > 0:
                m = max(p)
                m = max(m, S - sum(p))
                best = min(best,m)
                P.append(tuple(p) + tuple([S - sum(p)]))

        # for s1 in xrange(S):
        #     for s2 in xrange(S):
                # if i == 0:
                #     M[s1, s2] = (s1 == a) or (s2 == a)
                # else:
                #     M[s1, s2, i] = M[s1][s2]


    # for m in sorted(M):
    #     print m, " - ", M[m]

    return best, P



if __name__ == '__main__':
    # A = [5, 3, 3, 2, 2, 1]
    # A = [30,29,28,27,26,30,29,28,27,26,30,29,28,27,26,30,29,28,27,26,30,29,28,27,26,30,29,28,27,26,30,29,28,27,26,30,29,28,27,26]
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 11, 11, 13, 13, 16, 17, 17, 17, 17, 18, 18, 19, 19, 22, 23, 24, 25, 27, 30, 30, 30, 30]
    A = [1, 1, 2, 3, 5, 8, 13]
    # A = [1, 1, 2, 2, 4, 5, 5, 7, 10, 12, 13, 13, 14, 14, 16, 16, 16, 17, 17, 20, 20, 22, 23, 26, 28]
    # best, P = scheduler(A, 3)
    # print best
    # print P
    best, best_boxes, dist = scheduler3(A)
    print best
    print best_boxes
    print dist
    # print P

