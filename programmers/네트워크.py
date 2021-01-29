def solution(n, computers):
    su = [x for x in range(0,n)]
    answer = 0
    for i in range(n):
        for j in range(i):
            if computers[i][j] == 1:
                temp = j
                while True:
                    if su[temp] == temp:
                        for k in range(n):
                            if su[k] == su[i]:
                                su[k] = temp
                        break
                    else:
                        temp = su[temp]
    result = set(su)
    answer = len(result)
    return answer