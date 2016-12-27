n = int(raw_input())
W = map(int, raw_input().split())
s = min(W)
T = [0] * (max(W)+1)

def solve():
    ans = 0
    B = W[:]
    V = [False] * n

    B.sort()
    for i in xrange(n):
        T[B[i]] = i
    for i in xrange(n):
        if V[i]:
            continue
        cur = i
        S = 0
        m = max(W)+1
        an = 0
        while True:
            V[cur] = True
            an += 1
            v = W[cur]
            m = min(m, v)
            S += v
            cur = T[v]
            if V[cur]: break
        ans += min(S + (an - 2) * m, m + S + (an + 1) * s)

    return ans

def main():
    ans = solve()
    print ans
    return 0

main()


