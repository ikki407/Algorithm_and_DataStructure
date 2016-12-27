n = int(raw_input())
S = map(int, raw_input().split())
cnt = 0

def merge(A, left, mid, right):
    global cnt
    n1 = mid - left
    n2 = right - mid
    L = [0] * (n1+1) 
    R = [0] * (n2+1)
    L[:n1] = A[left:mid]
    R[:n2] = A[mid:right]
    #for i in xrange(n1):
    #    L[i] = A[left + i]
    #for i in xrange(n2):
    #    R[i] = A[mid + i]
    L[n1] = float('inf')
    R[n2] = float('inf')
    i = 0
    j = 0
    for k in xrange(left,right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            cnt += 1
        else:
            A[k] = R[j]
            j += 1
            cnt += 1
    return 0

def mergeSort(A, left, right):
    if right - left > 1:
        mid = int((left + right) / 2)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)
    return 0

def main():
    mergeSort(S, 0, len(S))
    print ' '.join(map(str, S))
    print cnt
    return 0

main()
