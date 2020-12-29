import sys

n = int(sys.stdin.readline())
w = [int(sys.stdin.readline()) for _ in range(n)]
w.insert(0,0)
w.append(0)
dp = [-1 for _ in range(n+2)]
dp[0] = 0
dp[1] = w[1]
dp[2] = w[1] + w[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-1], dp[i-2] + w[i], dp[i-3] + w[i-1] + w[i])

print(dp[n])

"""
n = int(sys.stdin.readline())
w = [int(sys.stdin.readline()) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(2)]

if n == 1: print(w[0])
elif n == 2: print(w[0]+w[1])
elif n == 3: print(max(w[0]+w[1],w[1]+w[2]))
else:
    dp[0][0] = w[0]
    dp[1][0] = 0
    dp[0][1] = w[1]
    dp[1][1] = w[0]
    dp[0][2] = w[0]+w[2]
    dp[1][2] = w[0]+w[1]
    for i in range(2,n-2):
        dp[0][i+2] = max(dp[1][i]+w[i+2],dp[0][i]+w[i+2])
        dp[1][i+2] = max(dp[1][i],dp[0][i],dp[0][i]+w[i+1],dp[1][i+2])
        if i <= (n-4):
            dp[1][i+3] = dp[1][i]+w[i+1]+w[i+2]
        else:
            dp[0][i+2] = max(dp[0][i+2],dp[1][i]+w[i+1]+w[i+2])

    print(max(dp[0][n-1],dp[1][n-1]))
"""