def bubbleSort(A, N):
    flag = 1
    count = 0
    while flag:
        flag = 0
        for j in xrange(N-1,0,-1):
            if A[j] < A[j-1]:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flag += 1
                count += 1
    return A, count

def newbubbleSort(A, N):
    flag = 1
    count = 0
    i = 0
    while flag:
        flag = 0
        for j in xrange(N-1,i,-1):
            if A[j] < A[j-1]:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flag += 1
                count += 1
        i += 1
    return A, count


def main():
    N = int(raw_input())
    A = map(int, raw_input().split())
    new_A, count = newbubbleSort(A, N)
    print ' '.join(map(str,new_A))
    print count

if __name__ == "__main__":
    main()

