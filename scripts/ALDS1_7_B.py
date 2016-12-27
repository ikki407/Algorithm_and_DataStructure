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

def setHeight(T,u):#(T, root)高さは下からだから代入は最後
    h1 = h2 = 0
    if T[u].right != -1:
        h1 = setHeight(T, T[u].right) + 1
    if T[u].left != -1:
        h2 = setHeight(T, T[u].left) + 1
    T[u].height = max(h1, h2)
    return T[u].height

def setDepth(u, d):#(root,0)深さは上からだから代入は最初
    T[u].depth = d
    if T[u].left == -1 and T[u].right == -1:
        return
    if T[u].left != -1 and T[u].right == -1:
        setDepth(T[u].left, d+1)
    elif T[u].left == -1 and T[u].right != -1:
        setDepth(T[u].right, d+1)
    else:
        setDepth(T[u].left, d+1)
        setDepth(T[u].right, d+1)

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

setHeight(T, N)
setDepth(N, 0)


for i in xrange(n):
    T[i].setType()
    print T[i]






