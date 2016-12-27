n, k = map(int, raw_input().split())
W = [input() for _ in xrange(n)]

def check(p):
    i = 0
    for j in xrange(k):
        s = 0
        while s + W[i] <= p:
            s += W[i]
            i += 1
            if (i == n):
                return n
    return i

def solve():
    left = 0
    right = 100000 * 10000
    while right - left > 1:
        mid = int((right + left) / 2)
        v = check(mid)
        if v >= n:
            right = mid
        else:
            left = mid

    return right

def main():
    ans = solve()
    print ans
    return 0

main()
