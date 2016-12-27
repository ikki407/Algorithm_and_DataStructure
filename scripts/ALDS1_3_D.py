from collections import deque

def main():
    S1 = deque([])
    S2 = deque([])
    Sum = 0
    S = raw_input()
    for i,j in enumerate(S):
        if j == '\\': S1.append(i)
        elif j == '/' and len(S1) > 0 :
            k = S1.pop()
            Sum += i - k
            a = i - k
            while len(S2)>0 and S2[len(S2)-1][0] > k:
                a += S2.pop()[1]
            S2.append([k,a])

    ans = []
    while len(S2)>0:
        ans.append(S2.pop()[1])
    ans = ans[::-1]
    print sum(ans)
    print len(ans),
    for i in xrange(len(ans)):
        print ans[i],
    print
    return 0

main()
    

