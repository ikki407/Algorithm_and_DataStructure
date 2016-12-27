from collections import deque

n, m = map(int,raw_input().split())

color = [-1] * n
G = [ deque([]) for _ in xrange(n)]

def dfs(r, c):
    S = deque([])
    S.append(r)
    color[r] = c
    while len(S) > 0:
        u = S.pop()
        for i in xrange(len(G[u])):
            v = G[u][i]
            if color[v] == -1:
                color[v] = c
                S.append(v)

    return 

def assignColor():
    id_ = 1
    for u in xrange(n):
        if color[u] == -1:
            dfs(u,id_)
            id_ += 1
    return

def main():
    for i in xrange(m):
        a = map(int, raw_input().split())
        #print a,a[1],G[a[1]],color[9]
        G[a[0]].append(a[1])
        G[a[1]].append(a[0])

    assignColor()
    
    q = int(raw_input())
    for i in xrange(q):
        a = map(int, raw_input().split())
        if color[a[0]] == color[a[1]]:
            print 'yes'
        else:
            print 'no'

    return 0

main()

