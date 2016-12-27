from collections import deque
n = int(raw_input())

M = [[0]*n for _ in xrange(n)]
color = [0] * n
WHITE = 0
GRAY = 1
BLACK = 2
d = [-1] * n
Q = deque([])

def bfs():
    color[0] = GRAY
    d[0] = 0
    Q.append(0)
    while len(Q) > 0:
        u = Q.popleft()
        for v in xrange(n):
            if M[u][v] == 1 and color[v] == WHITE:
                color[v] = GRAY
                d[v] = d[u] + 1
                Q.append(v)
        color[u] = BLACK
    for u in xrange(n):
        print "{} {}".format(u+1, d[u])
    return

def main():
    for i in xrange(n):
        a = map(int, raw_input().split())
        u = a[0]-1
        k = a[1]
        for j in xrange(k):
            v = a[j+2] -  1
            M[u][v] = 1
    
    bfs()
    return 0

main()


