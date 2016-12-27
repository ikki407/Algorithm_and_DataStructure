from collections import deque
import sys

def main():
    n, q = map(int,raw_input().split())
    Q = deque([])
    for i in xrange(n):
        a = raw_input().split()
        a[1] = int(a[1])
        Q.append(a)
    
    elaps = 0
    while len(Q) > 0:
        u = Q.popleft()
        a = min(u[1], q)
        u[1] -= a
        elaps += a
        if u[1] > 0:
            Q.append(u)
        else:
            print u[0], elaps
    return 0

main()

