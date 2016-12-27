import sys
sys.setrecursionlimit(13000)
n = int(raw_input())


#class of node
class Node:
    def __init__(self):
        self.p = -1
        self.l = -1
        self.r = -1

T = [ Node() for _ in xrange(n)] #info of u
D = [0] * n #depth of u

def printInfo(u):
    #print 'node', u, ':',
    #print 'parent = ', T[u].p, ',',
    #print 'depth = ', D[u], ',',
    print "node {}: parent = {}, depth = {},".format(u, T[u].p, D[u]) ,
    if T[u].p == -1: 
        print 'root, ',
    elif T[u].l == -1:
        print 'leaf, ',
    else:
        print 'internal node, ',

    #print '[',
    sys.stdout.write("[")

    c = T[u].l
    i = 0
    while c != -1:
        if i > 0:
            print ', ',
        sys.stdout.write(str(c))
        #print "{}".format(c),
        c = T[c].r
        i += 1
    #print ']'
    sys.stdout.write("]\n")

    return 0

def rec(u, p):
    D[u] = p
    if T[u].r != -1:
        rec(T[u].r, p)
    if T[u].l != -1:
        rec(T[u].l, p+1)
    return

def main():
    for i in xrange(n):
        a = map(int, raw_input().split())
        v = a[0]
        d = a[1]
        for j in xrange(d):
            if j == 0:
                T[v].l = a[j+2]
            else:
                T[l].r = a[j+2]
            l = a[j+2]
            T[a[j+2]].p = v
    for i in xrange(n):
        if T[i].p == -1:
            r = i

    rec(r, 0)

    for i in xrange(n):
        printInfo(i)

    return 0

if __name__ == '__main__':
    main()

'''
#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin
 
FORMAT = ('node {0.id}: parent = {0.parent}, depth = {0.depth},'
          ' {0.kind}, {0.childs}').format
 
 
class Node(object):
    def __init__(self, node):
        self.depth = 0
        self.parent = -1
        self.id = node[0]
        self.degree = node[1]
        self.kind = 'internal node' if node[1] else 'leaf'
        self.childs = node[2:]
 
    def __str__(self):
        return FORMAT(self)
 
 
def calc_depth(tree, i):
    for j in tree[i].childs:
        tree[j].depth += 1
        calc_depth(tree, j)
 
 
n = int(stdin.readline())
tree = [-1] * n
#assert 1 <= n <= 100000
for _ in range(n):
    node = Node([int(s) for s in stdin.readline().split()])
    i = node.id
    node.parent = tree[i]
    for j in node.childs:
        if isinstance(tree[j], int):
            tree[j] = i
        else:
            tree[j].parent = i
    tree[i] = node
 
for i in range(n):
    calc_depth(tree, i)
 
for i, node in enumerate(tree):
    if node.parent == -1:
        node.kind = 'root'
    print(node)
'''
