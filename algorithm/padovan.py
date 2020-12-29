t = int(input())

n = []

dp = [0 for _ in range(101)]
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2

for _ in range(t):
    n.append(int(input()))

def padovan(n):
    if n <= 5: return dp[n]
    elif dp[n] == 0:
        dp[n] = padovan(n-1) + padovan(n-5)
    return dp[n]

for i in n:
    print(padovan(i))
