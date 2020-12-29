dp = [-1 for _ in range(90)]
dp2 = [[-1 for _ in range(90)],[-1 for _ in range(90)]]

def fibo(n):
    if n == 0:
        dp2[0][0] = 1
        dp2[1][0] = 0
        return 0
    if n == 1:
        dp2[0][1] = 0
        dp2[1][1] = 1 
        return 1
    if dp[n] != -1:
        return dp[n]
        
    dp[n] = fibo(n-1) + fibo(n-2)
    dp2[0][n] = dp2[0][n-1] + dp2[0][n-2] 
    dp2[1][n] = dp2[1][n-1] + dp2[1][n-2]
    return dp[n]

t = int(input())

for i in range(t):
    n = int(input())
    fibo(n)
    print(dp2[0][n],dp2[1][n])