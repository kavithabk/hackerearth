#!/bin/python

t = int(raw_input())
while t > 0:
    c = raw_input()
    a = c.split()
    print int(a[0]) + int(a[1])
    t= t - 1
