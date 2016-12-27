a = raw_input().split()
n = int(a[0])
m = int(a[1])

C = map(int,raw_input().split())
T = [float('inf') for _ in xrange(n+1)]

def getTheNumberOfCoin():
    T[0] = 0
    for i in xrange(m):
        for j in xrange(C[i],n+1):
            T[j] = min(T[j], T[j-C[i]]+1)

    print T[n]
    return 0

getTheNumberOfCoin()
