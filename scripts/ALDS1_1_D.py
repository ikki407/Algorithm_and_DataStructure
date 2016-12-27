#!/usr/bin/ python
# -*- coding: utf-8 -*-

def main():
    
    N = input() #1つだけ入力
    a = [input() for y in range(N)] #2つめから入力
    a_max = -10**9
    a_min = a[0]
    for j in xrange(1,len(a)):
        if a[j] - a_min > a_max:
            a_max = a[j] - a_min
        if a[j] < a_min:
            a_min = a[j]
    print a_max
        
main()

