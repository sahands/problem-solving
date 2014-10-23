import sys
# from collections import defaultdict


INF = 100000000


def read_ints():
    return [int(x) for x in next(sys.stdin).split()]


def floyd(dist):
    n = len(dist)
    M = [x[:] for x in dist]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                M[i][j] = min(M[i][j], M[i][k] + M[k][j])
    return M


def main():
    while True:
        n = read_ints()[0]
        if not n:
            break

        dist = [[INF] * n for i in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for i in range(n):
            contacts = read_ints()
            m = contacts[0]
            contacts = contacts[1:]
            for j in range(m):
                dist[i][contacts[2 * j] - 1] = contacts[2 * j + 1]

        # print('\n'.join(', '.join(str(x) for x in row) for row in dist))
        M = floyd(dist)
        # print('\n'.join(', '.join(str(x) for x in row) for row in M))
        best_start = 0
        best_worst = max(M[0])
        for i in range(1, n):
            worst = max(M[i])
            if best_worst > worst:
                best_worst = worst
                best_start = i

        print(best_start + 1, best_worst)


if __name__ == '__main__':
    main()
