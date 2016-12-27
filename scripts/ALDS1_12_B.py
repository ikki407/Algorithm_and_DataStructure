
WHITE = 0
GRAY = 1
BLACK = 2

n = int(raw_input())
M = [ [-1] * n for _ in xrange(n)]
color = [WHITE] * n
d = [float('inf')] * n

for i in xrange(n):
    a = map(int, raw_input().split())
    for j in xrange(a[1]):
        M[a[0]][a[2*(j+1)]] = a[2*(j+1)+1]

def dijkstra():
    d[0] = 0

    while True:
        mincost = float('inf')
        for i in xrange(n):
            if color[i] != BLACK and d[i] < mincost:
                mincost = d[i]
                u = i

        if mincost == float('inf'):
            break

        color[u] = BLACK

        for v in xrange(n):
            if color[v] != BLACK and M[u][v] >= 0:
                if d[u] + M[u][v] < d[v]:
                    d[v] = d[u] + M[u][v]
                    color[v] = GRAY

    for i in xrange(n):
        print "{} {}".format(i, d[i])

    return 0

def main():
    dijkstra()
    return 0

main()




5
0 3 2 3 3 1 1 2
1 2 0 2 3 4
2 3 0 3 3 1 4 1
3 4 2 1 0 1 1 4 4 3
4 2 2 1 3 3
