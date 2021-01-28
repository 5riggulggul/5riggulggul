def solution(N, number):
    answer = 0
    dp = [set() for _ in range(11)]
    for i in range(1,9):
        dp[i-1].add(int(str(N)*i))
        for j in range(i):
            for k in dp[j]:
                for l in dp[i-j-2]:
                    dp[i-1].add(k + l)
                    dp[i-1].add(k - l)
                    dp[i-1].add(k * l)
                    if l != 0:
                        dp[i-1].add(k // l)
            if number in dp[i-1]:
                return i 
    return -1