import sys

n = int(sys.stdin.readline())
dp = [1000001 for _ in range(1000001)]

def making(n):
    dp[1] = 0
    for i in range(1,n+1):
        if i*2 <= n:
            if dp[i*2] > (dp[i] + 1): dp[i*2] = dp[i] + 1
        if i*3 <= n:
            if dp[i*3] > (dp[i] + 1): dp[i*3] = dp[i] + 1
        if i+1 <= n:
            if dp[i+1] > (dp[i] + 1): dp[i+1] = dp[i] + 1
    return dp[n]
print(making(n))


"""
# 재귀함수버전 - depth가 너무 깊어서 안된다.
def making(n):
    if n == 1 :
        dp[1] = 0 
        return dp[1]
    if dp[n] != -1: return dp[n]
    if n % 2 == 0:
        dp[n] = min(making(int(n/2)), making(n-1)) + 1
    elif n % 3 == 0:
        dp[n] = min(making(int(n/3)), making(n-1)) + 1
    else : dp[n] = making(n-1) + 1
    return dp[n]

print(making(n))
"""