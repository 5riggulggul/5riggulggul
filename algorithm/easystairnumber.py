import sys

n = int(sys.stdin.readline())

dp = [[0 for _ in range(101)] for _ in range(10)]

summ = 0

for i in range(1,10):
    dp[i][1] = 1

for j in range(1,n):
    for i in range(10):
        if (i-1) >= 0:
            dp[i-1][j+1] += dp[i][j]
        if (i+1) <= 9:
            dp[i+1][j+1] += dp[i][j]
 

for i in range(10):
    summ += dp[i][n]

print(summ%1000000000)

