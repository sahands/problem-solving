from sys import stdin
from collections import Counter


def calculate_tree_hash(T, H, S):
    """
    Calculate hash values for subtrees of labeled binary tree T.

    Assumes T is a dictionary with T[v][0] holding the label of node v
    and T[v][1] holding the adjacency list of node v. Assumes the tree
    is rooted at node 0.

    Outputs are H, a dictionary, with H[v] containing the hash value for
    subtree starting at node v, and S, another dictionary, with S[h] containing
    the number of nodes in subtree with hash h.
    """
    stack = [0]
    j = 0
    while j < len(stack):
        stack += T[stack[j]][1]
        j += 1

    while stack:
        v = stack.pop()
        label = T[v][0]
        adj = T[v][1]
        h = label
        subtree_count = 1
        if adj:
            h = hash(tuple([h] + [H[k] for k in adj]))
            subtree_count += sum(T[k][2] for k in adj)
        H[v] = h
        T[v][2] = S[h] = subtree_count


def find_largest_commmon_subtree(L):
    """
    Finds the number of nodes in the largest common subtree among all binary
    trees in a list of labelled binary trees L.
    """
    n = len(L)
    C = Counter()
    S = dict()
    H = [dict() for __ in xrange(n)]
    for i in xrange(n):
        calculate_tree_hash(L[i], H[i], S)
        C.update(set(H[i].values()))
    best = -1
    for c in C:
        if C[c] == n and S[c] > best:
            best = S[c]
    return best


def read_tree(N):
    T = dict()
    for i in xrange(N):
        u, parent = tuple(stdin.readline().split(' '))
        parent = int(parent)
        T[i] = [u, [], 0]
        if parent in T:
            T[parent][1].append(i)
    return T


def read_test_case():
    N, M = tuple(int(x) for x in stdin.readline().split(' '))
    return [read_tree(N), read_tree(M)]


if __name__ == "__main__":
    T = int(stdin.readline())
    for t in xrange(T):
        L = read_test_case()
        print find_largest_commmon_subtree(L)
