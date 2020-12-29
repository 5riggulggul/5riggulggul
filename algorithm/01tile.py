dp = [-1 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2

def tile(n):
    cnt = 3
    while cnt <= n:    
        dp[cnt] = (dp[cnt-1] +dp[cnt-2])%15746
        cnt += 1
    return dp[n]

n = int(input())

if n == 1: print(1)
elif n == 2: print(2)
else: print(tile(n))