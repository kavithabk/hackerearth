s = raw_input()
n = int(raw_input())
while n > 0:
    r = raw_input()
    p = r.split()
    l = len(s)
    a = int(p[0]) % l
    b = int(p[1]) % l
    if s[a-1] == s[b-1]:
        print "Yes"
    else:
        print "No"
    n = n - 1

    
    
