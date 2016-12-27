n = int(raw_input())
A = map(int, raw_input().split())
B = [0] * n

def CountingSort(A, B, k):
    C = [0] * (k+1)
    for j in xrange(n):
        C[A[j]] += 1
    for i in xrange(1,k+1):
        C[i] = C[i] + C[i-1]
    for j in xrange(n-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return 0

def main():
    CountingSort(A, B, 10000)
    print ' '.join(map(str,B))
    return 0

main()


