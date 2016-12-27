n = int(raw_input())
A = map(int, raw_input().split())

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in xrange(p,r):
        if A[j] <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i+1]
    A[i+1] = A[r]
    A[r] = tmp
    return i+1

def main():
    i = partition(A, 0, n-1)
    print ' '.join(map(str, A[:i])), '[{}]'.format(A[i]), ' '.join(map(str,A[i+1:]))
    return 0

main()
