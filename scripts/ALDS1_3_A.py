from collections import deque

def main():
    S = raw_input().split()
    D = deque([])
    for s in S:
        if s == '+':
            b = D.pop()
            a = D.pop()
            D.append(a+b)   
        elif s == '-':
            b = D.pop()
            a = D.pop()
            D.append(a-b)
        elif s == '*':
            b = D.pop()
            a = D.pop()
            D.append(a*b)
        else:
            D.append(int(s))
    print D.pop()
    return 0

main()

