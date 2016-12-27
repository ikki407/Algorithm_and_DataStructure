def parent(i):
    return int(i/2)

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def main():
    H = int(raw_input())
    A = map(int,raw_input().split())
    for i in xrange(1,H+1):
        print "node {}: key = {},".format(i, A[i-1]),
        if parent(i) >= 1: 
            print "parent key = {},".format(A[parent(i)-1]),
        if left(i) <= H: 
            print "left key = {},".format(A[left(i)-1]),
        if right(i) <= H:
            print "right key = {},".format(A[right(i)-1]),
        print '',
        print 
    return 0

main()

        
        
