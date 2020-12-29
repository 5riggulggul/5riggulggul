import sys

n = int(sys.stdin.readline())
su = list(map(int,sys.stdin.readline().split()))
dp = [[0 for _ in range(n)] for _ in range(2)]
#dp = [0] * n 으로 대체 가능
max2 = 0
dp[0][0] = 1
dp[1][n-1] = 1
    
    
    
for i in range(1,n):
    max1 = 0
    for j in range(i):
        if (su[j] < su[i]) & (max1 < dp[0][j]):
            max1 = dp[0][j]    
    dp[0][i] = max1 + 1

for i in range(n-1,-1,-1):
    min1 = 0
    for j in range(n-1,i,-1):
        if (su[j] < su[i]) & (min1 < dp[1][j]):
            min1 = dp[1][j]
    dp[1][i] = min1 + 1

for i in range(n):
    if max2 < dp[0][i] + dp[1][i]:
        max2 = dp[0][i] + dp[1][i]
print(max2 - 1)