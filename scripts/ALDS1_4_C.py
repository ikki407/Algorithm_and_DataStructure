M = 1046527
L = 14
H = [""] * M

def getChar(ch):
    if ch == 'A':
        return 1
    elif ch == 'C':
        return 2
    elif ch == 'G':
        return 3
    elif ch == 'T':
        return 4
    else:
        return 0

def getKey(strings):
    Sum = 0
    p = 1
    for i in xrange(len(strings)):
        Sum += p * getChar(strings[i])
        p *= 5

    return Sum

def h1(key):
    return key % M

def h2(key):
    return 1 + (key % (M-1))

def find(strings):
    key = getKey(strings)
    i = 0
    while True:
        h = (h1(key) + i * h2(key)) % M
        if H[h] == strings:
            return 1
        elif len(H[h]) == 0:
            return 0
        else:
            i += 1
    return 0

def insert(strings):
    key = getKey(strings)
    i = 0
    while True:
        h = (h1(key) + i * h2(key)) % M
        if H[h] == strings:
            return 1
        elif len(H[h]) == 0:
            H[h] = strings
            return 0
        else:
            i += 1
    return 0

def main():
    n = input()
    for i in xrange(n):
        com = raw_input().split()
        if com[0][0] == 'i':
            insert(com[1])
        else:
            if find(com[1]):
                print 'yes'
            else:
                print 'no'
    return 0

main()



