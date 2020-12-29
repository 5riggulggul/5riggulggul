import sys

n = int(sys.stdin.readline())

line = [[0] * 2] * n

dp = [0] * n

dp[0] = 1

for i in range(n):
    line[i] = list(map(int,sys.stdin.readline().split()))

line.sort(key = lambda x: x[0])

for i in range(n):
    max1 = 0
    for j in range(i):
        if (dp[j] > max1) & (line[i][1] > line[j][1]):
            max1 = dp[j]
    dp[i] = max1 + 1

print(n - max(dp))