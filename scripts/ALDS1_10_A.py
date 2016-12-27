n = int(raw_input())
F = [0] * (n+1)



def fibonacci(n):
    global F
    if n == 0 or n == 1:
        F[n] = 1
        return F[n]
    if F[n] != 0:
        return F[n]
    F[n] = fibonacci(n-2) + fibonacci(n-1)
    return F[n]

def makeFibonacci(n):
    global F
    F[0] = 1
    F[1] = 1
    for i in xrange(2,n+1):
        F[i] = makeFibonacci(i-2) + makeFibonacci(i-1)
    return F[n]

def main():
    ans = fibonacci(n)
    print ans
    return 0

main()
