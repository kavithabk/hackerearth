#!/bin/python

n = int(raw_input())
while n > 0:
    a = raw_input()
    b =a.split()
    a = raw_input()
    c =a.split()
    if int(b[1]) < len(c):
        print "Lame husband"
    elif int(b[1]) == len(c):
        print "Perfect husband"
    else:
        print "Bad husband"
    n = n - 1
