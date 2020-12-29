n = int(input())
a = [input() for _ in range(n)]
a = list(map(int,a))

for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j]:  a[i], a[j] = a[j], a[i]

print(*a,sep = '\n')