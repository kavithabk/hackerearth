import itertools
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

n = int(raw_input())
a = raw_input().split()
l = list(itertools.permutations(a))
c = len(l)
beauty = 0
total = 0
i = 0
j = 0
while i < c:
    while j < n-1:
        total += gcd(int(l[i][j]), int(l[i][j+1]))
        j += 1
    if total > beauty:
        beauty = total
    i += 1
    j = 0
    total = 0
print beauty
