def binarySearch(A, key):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) / 2
        if A[mid] == key:
            return True
        elif key < A[mid]:
            right = mid
        else:
            left = mid+1
    return False

def main():
    n = int(raw_input())
    S = [int(_) for _ in raw_input().split()]
    q = int(raw_input())
    T = [int(_) for _ in raw_input().split()]
    Sum = 0
    for t in T:
        if binarySearch(S[:], t): Sum += 1
    print Sum
    return 0

main()

