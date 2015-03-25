l = int(raw_input())
n = int(raw_input())
while n > 0:
    a = raw_input()
    p = a.split()
    w = int(p[0])
    h = int(p[1])
    n -= 1
    if w < l or h < l:
        print "UPLOAD ANOTHER"
    elif w == h:
        print "ACCEPTED"
    else:
        print "CROP IT"
