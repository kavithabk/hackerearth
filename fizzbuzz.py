#!/bin/python

t = int(raw_input())
a = raw_input()
b = a.split()
j = 0
while j < t:
    i = 1
    k = int(b[j])
    while i <= k:
        if i % 3 == 0 and i % 5 ==0:
            print "FizzBuzz"
        elif i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else:
            print i
        if i > k : break
        i = i + 1
    j = j + 1
