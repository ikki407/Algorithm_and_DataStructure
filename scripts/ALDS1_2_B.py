def selectionSort(A, N):
    count = 0
    for i in xrange(0,N):
        minj = i
        for j in xrange(i,N):
            if A[j] < A[minj]:
                minj = j
                
        if minj != i:
            tmp = A[i]
            A[i] = A[minj]
            A[minj] = tmp
            count += 1
    return A, count



def main():
    N = int(raw_input())
    A = map(int,raw_input().split())
    newA, count = selectionSort(A, N)
    print ' '.join(map(str,newA))
    print count
    return 0

if __name__ == "__main__":
    main()

