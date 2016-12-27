def lcs(X, Y):
    m = len(X) + 1
    n = len(Y) + 1
    c = [[0] * n for _ in xrange(m)]
    X = ' ' + X
    Y = ' ' + Y
    for i in xrange(1,m):
        for j in xrange(1,n):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    print c[m-1][n-1]
    return 0


def lcs(x,y):
    a, b = len(x), len(y)
    x1 = [0 for k in range(b+1)]
    for i in xrange(a):
        e = x[i]
        x2 = x1+[]
        for j in xrange(b):
            if e == y[j]:
                x1[j+1] = x2[j] + 1
            elif x1[j+1] < x1[j]:
                x1[j+1] = x1[j]
    print max(x1)
    return 0

def main():
    q = int(raw_input())
    for i in xrange(q):
        X = raw_input()
        Y = raw_input()
        lcs(X,Y)
    return 0

main()

