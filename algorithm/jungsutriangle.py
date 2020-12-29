import sys
n = int(sys.stdin.readline())

su = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in range(n-1):
    maxx = [0 for _ in range(501)]
    for j in range(i+1):
        if su[i][j]+su[i+1][j] > maxx[j]:
            maxx[j] = su[i][j]+su[i+1][j]
        if su[i][j]+su[i+1][j+1] > maxx[j+1]:
            maxx[j+1] = su[i][j]+su[i+1][j+1]
    for j in range(i+2):
        su[i+1][j] = maxx[j]

max2 = 0

for i in range(n):
    if max2 < su[n-1][i]: max2 = su[n-1][i]

print(max2)