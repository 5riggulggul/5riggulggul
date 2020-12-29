import sys

n = int(sys.stdin.readline())
su = list(map(int,sys.stdin.readline().split()))

dp = [0 for _ in range(n)]

dp[0] = 1

max1 = 1

for i in range(1,n):
    max2 = 0
    for j in range(i):
        if (dp[j] > max2) & (su[j] < su[i]):
            max2 = dp[j]
    dp[i] = max2 + 1

print(max(dp))

