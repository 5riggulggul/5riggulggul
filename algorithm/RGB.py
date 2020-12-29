import sys

n = int(input())

a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in range(n-1):
    minn = [100001,100001,100001]
    if a[i][0]+a[i+1][1] < minn[1]: minn[1] = a[i][0]+a[i+1][1]
    if a[i][0]+a[i+1][2] < minn[2]: minn[2] = a[i][0]+a[i+1][2]

    if a[i][1]+a[i+1][0] < minn[0]: minn[0] = a[i][1]+a[i+1][0]
    if a[i][1]+a[i+1][2] < minn[2]: minn[2] = a[i][1]+a[i+1][2]

    if a[i][2]+a[i+1][0] < minn[0]: minn[0] = a[i][2]+a[i+1][0]
    if a[i][2]+a[i+1][1] < minn[1]: minn[1] = a[i][2]+a[i+1][1]

    a[i+1][0], a[i+1][1],a[i+1][2] = minn[0], minn[1], minn[2]

min2 = a[n-1][0]

for i in range(1,3):
    if min2 > a[n-1][i]: min2 = a[n-1][i]

print(min2)