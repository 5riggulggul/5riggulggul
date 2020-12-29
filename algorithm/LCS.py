import sys

a = list(map(str,sys.stdin.readline()))
b = list(map(str,sys.stdin.readline()))
a.remove('\n')
b.remove('\n')

a2 = set(a)
b2 = set(b)

c = a2 & b2

a3 = list()
b3 = list()

dp = [0] * 1000

for i in a:
    if set(i) & c:
        a3.append(i)
for i in b:
    if set(i) & c:
        b3.append(i)

for i in range(len(a3)):
    max1 = 0

print(a,b,a2,b2,c,a3,b3,dp)