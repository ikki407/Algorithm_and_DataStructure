n = int(raw_input())



FORMAT = ('node {0.id}: parent = {0.parent}, sibling = {0.sibling}, degree = {0.degree}, depth = {0.depth}, height = {0.height}, {0.type}').format

class Node:
    def __init__(self):
        self.id = -1
        self.parent = -1
        self.left = -1
        self.right = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = 'leaf' if self.height == 0 else 'internal node'
        
    def setType(self):
        if self.height == 0 and self.parent != -1:
            self.type = 'leaf'
        elif self.parent == -1:
            self.type = 'root'
        else:
            self.type = 'internal node'

    def __str__(self):
        return FORMAT(self)

def preParse(u):
    if u == -1:
        return
    print u,
    preParse(T[u].left)
    preParse(T[u].right)

def inParse(u):
    if u == -1:
        return
    inParse(T[u].left)
    print u,
    inParse(T[u].right)

def postParse(u):
    if u == -1:
        return
    postParse(T[u].left)
    postParse(T[u].right)
    print u,


T = [Node() for _ in xrange(n)]

for i in xrange(n):
    a = map(int, raw_input().split())
    u = a[0]
    l = a[1]
    r = a[2]
    T[u].id = u
    T[u].left = l  #set child
    T[u].right = r  #set child
    if l != -1 and r != -1:
        T[l].parent = u  #set parent
        T[r].parent = u  #set parent
    elif l != -1 and r == -1:
        T[l].parent = u  #set parent
    elif l == -1 and r != -1:
        T[r].parent = u  #set parent

    if l != -1 and r != -1:
        T[u].degree = 2
        T[l].sibling = r
        T[r].sibling = l
    elif l != -1 and r == -1:
        T[u].degree = 1
    elif  l == -1 and r != -1:
        T[u].degree = 1

N = 0
for i in xrange(n):
    if T[i].parent == -1:
        N = T[i].id

print 'Preorder'
print '',
preParse(N)
print 
print 'Inorder'
print '',
inParse(N)
print 
print 'Postorder'
print '',
postParse(N)
print 






