n = int(input())

t = [list(map(int,input().split())) for _ in range(n)]

check = [0 for _ in range(n)]

ans = 40000

def team(k,hap,cnt):
    global ans
    for i in range(k,n):
        if cnt == n/2:
            hap2 = 0
            for j in range(n):
                if check[j] == 0:
                    for l in range(j+1,n):
                        if check[l] == 0:
                            hap2 += t[j][l]
                            hap2 += t[l][j]
            #print(check,ans,hap,hap2) 
            if abs(hap2 - hap) < ans:
                ans = abs(hap2 - hap)
            return
            
        elif check[i] == 0: 
            check[i] = 1
            for j in range(n):
                if (check[j] == 1) & (i!=j):
                    hap += t[i][j]
                    hap += t[j][i]
            team(i,hap,cnt+1) # i가 아니라 k+1를 넣어서 dfs가 정상적으로 동작하지 않았음
            for j in range(n): # dfs 노드 빠져나오면 다시 더했던 hap을 빼주어야 함
                if (check[j] == 1) & (i!=j):
                    hap -= t[i][j]
                    hap -= t[j][i]
            check[i] = 0
            
    return

team(1,0,0)
print(ans)