n = int(raw_input())
#stable = 1

class Card():
    __slots__ = ('suit', 'value')

#mergeSort
A = [Card() for _ in xrange(n)]
#quickSort
B = [Card() for _ in xrange(n)]

s = set()
for i in xrange(n):
    a = raw_input().split()
    A[i].suit = a[0]
    B[i].suit = a[0]
    A[i].value = int(a[1])
    B[i].value = int(a[1])
    s.add(int(a[1]))
'''
def merge(A, left, mid, right):
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
    L[n1] = Card()
    R[n2] = Card()
    L[n1].value = float('inf')
    R[n2].value = float('inf')
    i = 0
    j = 0
    for k in xrange(left,right):
        if L[i].value <= R[j].value:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return 0

def mergeSort(A, left, right):
    if right - left > 1:
        mid = int((left + right) / 2)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)
    return 0
'''
def partition(A, p, r):
    x = A[r].value
    i = p-1
    for j in xrange(p,r):
        if A[j].value <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i+1]
    A[i+1] = A[r]
    A[r] = tmp
    return i+1

def quickSort(A,p,r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q, r)
    return 0

#mergeSort(A, 0, n)
quickSort(B, 0, n-1)

for i in s:
    if [d.suit for d in A if d.value == i] != [d.suit for d in B if d.value == i]:
        print('Not stable')
        break
else:
    print('Stable')

#for i in xrange(n):
#    if A[i].suit != B[i].suit:
#        stable = 0
for i in xrange(n):
    print B[i].suit, B[i].value

