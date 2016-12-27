import heapq
from collections import deque

WHITE = 0
GRAY = 1
BLACK = 2

n = int(raw_input())
M = []
for i in xrange(n):
    M.append(deque([]))
color = [WHITE] * n
d = [float('inf')] * n

for i in xrange(n):
    a = map(int, raw_input().split())
    for j in xrange(a[1]):
        M[a[0]].append((a[2*(j+1)],a[2*(j+1)+1]))

def dijkstra():
    d[0] = 0

    PQ = []
    heapq.heappush(PQ,(0,0))#value, node
    
    color[0] = GRAY

    while len(PQ) > 0:
        f = heapq.heappop(PQ)
        u = f[1]
        color[u] = BLACK

        if d[u] < f[0]:
            continue

        for j in xrange(len(M[u])):
            v = M[u][j][0]
            if color[v] == BLACK:
                continue
            if d[v] > d[u] + M[u][j][1]:
                d[v] = d[u] + M[u][j][1]
                heapq.heappush(PQ, (d[v],v))
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
