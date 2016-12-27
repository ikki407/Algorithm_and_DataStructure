
class Node:
    def __init__(self, key=-1):
        self.key = key
        self.parent = -1
        self.left = -1
        self.right = -1
    
    def setKey(self, key):
        self.key = key


def insert(T_, z): #(T, Node)
    global T
    y = -1
    x = T_ #Node()
    while x != -1 :
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == -1:
        T = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def preParse(T):
    if T == -1 :
        return
    print T.key,
    preParse(T.left)
    preParse(T.right)

def inParse(T):
    if T == -1 :
        return
    inParse(T.left) #Node() or -1
    print T.key,
    inParse(T.right)


T = -1

def main():
    com = ''
    m = int(raw_input())
    #for i in xrange(m):
    #    com.append(raw_input())
    for i in xrange(m):
        com = raw_input()
        if com[0] == 'i':
            insert(T,Node(key=int(com[7:])))
        else:
            print '',
            inParse(T)
            print
            print '',
            preParse(T)
            print 
    return 0

main()
            


