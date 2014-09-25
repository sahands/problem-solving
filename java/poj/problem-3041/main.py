from sys import stdin
from collections import defaultdict
from queue import Queue
from copy import deepcopy
from itertools import product


INF = 10 ** 8


def max_flow(n, s, t, G, C):
    """
    Returns a max flow assignment given source s, sink t, on a graph
    with vertices labeled 1, ..., n, with capacity map C.
    """
    def residual_capacity(v, u):
        return C[v, u] - f[v, u] if C[v, u] > 0 else f[u, v]

    # Returns a path from s to t in the current
    # residual network, and the minimum capacity on
    # that path.
    def bfs():
        Q = Queue()
        Q.put(s)
        parent = {s: None}
        while not Q.empty():
            v = Q.get()
            if v == t:
                break
            for u in G[v]:
                cf = residual_capacity(v, u)
                if u not in parent and cf > 0:
                    parent[u] = v
                    Q.put(u)
        if t not in parent:
            return None, 0

        min_capacity = INF
        path = []
        v, u = t, parent[t]
        while v:
            path.insert(0, (u, v))
            min_capacity = min(min_capacity, residual_capacity(u, v))
            v, u = u, parent[u]
        return path, min_capacity

    f = defaultdict(int)
    while True:
        path, min_capacity = bfs()
        if not path:
            break
        for u, v in path:
            if C[u, v] > 0:
                f[u, v] += min_capacity
            else:
                f[v, u] -= min_capacity
    return f


def read_test_case():
    n, k = (int(x) for x in next(stdin).split())
    G = defaultdict(list)
    C = defaultdict(int)
    for line, i in zip(stdin, range(k)):
        x, y = (int(a) for a in line.split())
        y += n  # nodes 1...n represent the rows, n+1...2n the cols
        G[x].append(y)
        G[y].append(x)
        C[x, y] = 1

    B = deepcopy(G)
    s = 0
    t = 2 * n + 1
    for v in range(1, n + 1):
        G[s].append(v)
        G[v].append(s)
        G[t].append(n + v)
        G[n + v].append(t)
        C[s, v] = 1
        C[n + v, t] = 1

    return n, s, t, G, C, B


def min_vertex_cover(B, M):
    """
    Returns a min vertex cover given a bipartite graph B
    and a max matching M.
    """
    V = set(x for m in M for x in m)  # matched vertices

    # If perfect matching, return the left half of the bipartite graph.
    if len(V) == len(B):
        return set(u for u, v in M)

    min_cover = set()
    seen = set()
    S1 = set()
    MM = {u: v for u, v in M}
    MM.update({v: u for u, v in M})

    # Let S1 be the set of vertices connected to unmatched vertices and add S1
    # to the cover. Now all the unmatched vertices are covered. Mark all the
    # unmatched vertices and all the vertices in S1 as seen.
    for u in B:
        if u not in V:
            seen.add(u)
            for v in B[u]:
                S1.add(v)
                seen.add(v)

    # Then let S3 be the unseen vertices v such that a vertex u in S1 is
    # matched with t and t is connected to v. That is, u->t is in M and t->v is
    # an edge. Mark both t and v as seen now. Then let S1 = S3, add S1 to the
    # cover and continue until all vertices are seen. This way, all the matched
    # vertices are covered too.
    min_cover.update(S1)
    seen.update(S1)
    while(len(seen) < len(B)):
        S3 = set()
        for v in S1:
            seen.add(MM[v])
            S3.update(u for u in B[MM[v]] if u not in seen)
        S1 = S3
        seen.update(S1)
        min_cover.update(S1)

    return min_cover


if __name__ == '__main__':
    n, s, t, G, C, B = read_test_case()
    f = max_flow(n, s, t, G, C)
    max_matching = [(u, v) for u, v
                    in product(range(1, n + 1), range(n + 1, 2 * n + 1))
                    if f[u, v] == 1]
    # print(max_matching)
    min_cover = min_vertex_cover(B, max_matching)
    # print(min_cover)
    print(len(min_cover))
