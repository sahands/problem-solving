from __future__ import division
import sys
from operator import itemgetter
from collections import defaultdict


class Vertex:
    def __init__(self):
        self.adj = []
        self.cost = 0.0
        self.count = 1
        self.key = None
        self.parent = None
        self.children = []
        self.removed = False

    def __repr__(self):
        return str(self.adj)


def read_test_case():
    weight_sum = 0
    G = defaultdict(Vertex)
    N, k = tuple(int(x) for x in sys.stdin.readline().split(' '))
    for i in xrange(N-1):
        u, v, weight = tuple(int(x) for x in sys.stdin.readline().split(' '))
        G[u].adj.append((v, weight))
        G[u].key = u
        G[v].adj.append((u, weight))
        G[v].key = v
        weight_sum += weight

    return G, N, k, weight_sum


def process_test_case(G, N, k, weight_sum):
    leaves = []
    for v in G:
        if len(G[v].adj) == 1:
            leaves.append(v)

    candidates = []

    while len(leaves) > 0:
        v = leaves[0]
        del leaves[0]
        if len(G[v].adj) == 0:
            break
        u = G[v].adj[0][0]
        G[v].cost += G[v].adj[0][1]
        G[v].parent = u
        if G[u].count == 1:
            G[u].count += G[v].count
        else:
            G[u].count = min(G[v].count + 1, G[u].count + 1)
        G[u].cost += G[v].cost
        G[u].children.append(v)
        G[u].adj = [edge for edge in G[u].adj if edge[0] != v]
        candidates.append([v, G[v].cost/G[v].count, G[v].count, G[v].cost])
        if len(G[u].adj) == 1 and G[u].count <= k:
            leaves.append(u)

    # for v in G:
        # print "Vertex", v, "has count=", G[v].count, "and cost=", G[v].cost

    weights_removed = 0
    while k > 0 and len(candidates) > 0:
        candidates.sort(key=itemgetter(1))
        c = candidates.pop()
        if c[2] > k or G[c[0]].removed:
            continue
        # print "Removing vertex:", c[0], "with cost", c[1] * c[2]
        k -= c[2]
        for cn in candidates:
            if cn[0] == G[c[0]].parent:
                cn[2] -= 1
                cn[3] -= G[c[0]].cost
                cn[1] = cn[3] / cn[2]
        weights_removed += c[1] * c[2]
        for v in G[c[0]].children:
            G[v].removed = True
        # print "Candidates are", candidates

    # print weights_removed
    # print "Final answer:", int(weight_sum - weights_removed) * 2
    print int(weight_sum - weights_removed) * 2


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in xrange(T):
        G, N, k, weight_sum = read_test_case()
        process_test_case(G, N, k, weight_sum)
