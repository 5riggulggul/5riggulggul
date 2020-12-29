n = int(input())

dp = [-1 for _ in range(90)]

def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    if dp[n] != -1: return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

print(fibo(n))