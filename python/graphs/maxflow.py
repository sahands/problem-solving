from collections import defaultdict
from sys import stdin


def read_graph(f):
    A = defaultdict(list)
    C = defaultdict(int)
    n = int(f.readline())
    source = int(f.readline()) + 1
    target = int(f.readline()) + 1
    for l in f:
        u, v, c = tuple(int(x) for x in l.split(' '))
        u += 1
        v += 1
        A[u].append(v)
        A[v].append(u)
        C[u, v] = c
        C[v, u] = 0
    return (A, C, source, target)


def construct_path(C, F, P, s, t):
    path = [t]
    while P[t]:
        t = P[t]
        path.append(t)
    path = list(reversed(path))
    min_capacity = None
    if len(path) > 1:
        min_capacity = min(residual_capacity(C, F, path[i], path[i+1]) for i in
                xrange(len(path)-1))
    return path, min_capacity


def residual_capacity(C, F, u, v):
    return C[u, v] - F[u, v] if C[u, v] > 0 else F[v, u]


def bfs_residual(A, C, F, s, t):
    seen = dict()
    parent = {s: None}
    Q = [s]
    while Q:
        u = Q.pop()
        seen[u] = True
        # print u, parent[u], A[u], Q
        for v in A[u]:
            cf = residual_capacity(C, F, u, v)
            if v not in seen and cf > 0:
                if v not in parent:
                    parent[v] = u
                if v == t:
                    path, min_capacity = construct_path(C, F, parent, s, t)
                    S = set(parent.keys())
                    return path, min_capacity, None
                Q.insert(0, v)
    return None, None, set(parent.keys())



def max_flow(A, C, s, t):
    S = set()
    F = defaultdict(int)
    while True:
        path, min_capacity, S = bfs_residual(A, C, F, s, t)
        if not path:
            break
        for i in xrange(len(path)-1):
            u, v = path[i], path[i+1]
            if C[u, v] > 0:
                F[u, v] += min_capacity
            else:
                F[u, v] -= min_capacity

    return F, S, set(A.keys()) - S



if __name__ == '__main__':
    A, C, s, t = read_graph(stdin)
    F, S, T = max_flow(A, C, s, t)
    val = sum(F[s, v] for v in A[s])
    print "S = {" + ','.join(str(x) for x in S) + '}'
    print "S = {" + ','.join(str(x) for x in T) + '}'
    print "Max-flow value = " + str(val)
    print "Flow:"
    print '\n'.join('{0} {1} - {2}/{3}'.format(u, v, F[u, v], C[u, v]) for u, v in sorted(F.keys()) if F[u, v] > 0)


