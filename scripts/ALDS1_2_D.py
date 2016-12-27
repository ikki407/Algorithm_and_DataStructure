def insertionSort(A, n, g, cnt):
    for i in xrange(1,n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
    return A, cnt

def shellSort(A, n):
    cnt = 0
    G = [1]
    idx = 0
    for i in xrange(1,len(A)):
        if 3*G[idx]+1 < len(A):
            G.append(3*G[idx]+1)
            idx += 1
    G = list(reversed(G[:]))
    #print G
    m = len(G)
    print m
    print ' '.join(map(str,G))
    newA = A[:]
    for i in range(0,m):
        newA, cnt = insertionSort(newA[:],len(A),G[i],cnt)
    return newA, cnt

def main():
    n = int(input())
    A = [int(input()) for i in xrange(n)]
    newA, cnt = shellSort(A, n)
    print cnt
    for i in range(len(newA)):
        print newA[i]
    return 0

if __name__ == '__main__':
    main()

