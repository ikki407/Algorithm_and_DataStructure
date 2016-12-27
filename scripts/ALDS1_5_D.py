n = int(raw_input())
S = map(int, raw_input().split())

def merge(A, left, mid, right):
    cnt = 0
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
            
        else:
            A[k] = R[j]
            j += 1
            cnt += n1 - i
    return cnt

def mergeSort(A, left, right):
    if right - left > 1:
        mid = int((left + right) / 2)
        v1 = mergeSort(A, left, mid)
        v2 = mergeSort(A, mid, right)
        v3 = merge(A, left, mid, right)
        return v1+v2+v3
    else:
        return 0

def main():
    v = mergeSort(S, 0, len(S))
    print v
    return 0

main()

