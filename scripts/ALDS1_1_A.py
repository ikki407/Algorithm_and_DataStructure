#!/usr/bin/ python
# -*- coding: utf-8 -*-

def main():
    N = input()
    a = map(int, raw_input().split())
    print ' '.join(map(str,a))
    for i in xrange(1,len(a)):
        v = a[i]
        j = i - 1
        while (j >= 0) & (a[j] > v):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = v
        print ' '.join(map(str,a))
    return 0

main()


