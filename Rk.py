#!/bin/python

t = int(raw_input())
while t > 0:
    a = raw_input()
    l = len(a)
    i = 0
    count = 0
    flag = 0
    while i < l:
        if a[i] == 'R' and flag == 0:
            count = count + 1
            flag = 1
        else:
            if a[i] == 'K':
                count = count + 1
            elif a[i] == 'R':
                count = count + 1
                break
        i = i + 1
    print count

    t = t - 1
