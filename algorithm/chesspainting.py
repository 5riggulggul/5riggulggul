n, m = input().split()
n = int(n)
m = int(m)
a = [input() for _ in range(n)]

dap = 64

for i in range(n-7):
    for j in range(m-7):
        flag1 = 0
        flag2 = 0
        sum1 = 0
        sum2 = 0

        for k in range(8):
            for l in range(8):
                if ((a[i+k][j+l] == 'B') & ((k+l)%2 == 1)) | ((a[i+k][j+l] == 'W') & ((k+l)%2 == 0)):
                    sum1 += 1
                if ((a[i+k][j+l] == 'B') & ((k+l)%2 == 0)) | ((a[i+k][j+l] == 'W') & ((k+l)%2 == 1)):
                    sum2 += 1
        
        if sum1 < dap : dap = sum1
        if sum2 < dap : dap = sum2

     
print(dap)