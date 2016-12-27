#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin
   
   
class Node(object):
    def __init__(self, key=None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
   
   
def tree_insert(top, z):
    y = None
    x = top
    while isinstance(x, Node):
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y is None:
        top = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    return top
   
def tree_find(top, k):
    x = top
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x

def deleteNode(top, z):#(top, Node())
    if z.left == None or z.right == None:
        y = z
    else:
        y = getSuccessor(z)

    if y.left != None:
        x = y.left
    else:
        x = y.right

    if x != None:
        x.parent = y.parent

    if y.parent == None:
        top = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x

    if y != z:
        z.key = y.key
    return top

def getSuccessor(x):
    if x.right != None:
        return getMinimum(x.right)

    y = x.parent
    while y != None and x == y.right:
        x = y
        y = y.parent
    return y

def getMinimum(x):
    while x.left != None:
        x = x.left
    return x


def inorder_walk(node):
    if node.left:
        inorder_walk(node.left)
    print('', node.key, end='')
    if node.right:
        inorder_walk(node.right)
   
   
def preorder_walk(node):
    print('', node.key, end='')
    if node.left:
        preorder_walk(node.left)
    if node.right:
        preorder_walk(node.right)
   
   
n = int(stdin.readline())
   
top = None
for _ in range(n):
    cmd = stdin.readline()
    if cmd.startswith('i'):
        key = int(cmd[7:])
        #assert -2000000000 <= key <= 2000000000
        top = tree_insert(top, Node(key))
    elif cmd.startswith('f'):
        key = int(cmd[5:])
        if tree_find(top, key) != None:
            print('yes')
        else:
            print('no')
    elif cmd.startswith('d'):
        key = int(cmd[7:])
        top = deleteNode(top, tree_find(top, key))
    else:
        inorder_walk(top)
        print()
        preorder_walk(top)
        print()
