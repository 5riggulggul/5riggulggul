n = int(input())

su = list(map(int,input().split()))

op = list(map(int,input().split()))

ma = -1000000000
mi = 1000000000

def cal(op2):
    hap = su[0]
    for i in range(n-1):
        if op2[i] == 0:
            hap = (hap + su[i+1])
        elif op2[i] == 1:
            hap = (hap - su[i+1])
        elif op2[i] == 2:
            hap = (hap * su[i+1])
        elif op2[i] == 3:
            hap = int(hap / su[i+1])
    return hap


def dfs(op,op2,cnt):
    global ma, mi
    flag = 0
    for i in range(4):
        if op[i] > 0:
            flag = 1
            op[i] -= 1

            op2[cnt] = i

            dfs(op,op2,cnt+1)
            
            op[i] += 1

    if flag == 0:
        hap = cal(op2)
        #print(op2,":",hap)
        if ma < hap: ma = hap
        if mi > hap: mi = hap
        return


dfs(op,[0 for _ in range(11)],0)
print(ma,mi,sep='\n')
