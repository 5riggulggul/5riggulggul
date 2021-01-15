import math
def solution(numbers):
    result =[]
    index = [0]*1000001
    temp = []
    count = 0
    def recur():
        for j in range(len(numbers)):
            if index[j] == 0:
                index[j] = 1
                temp.append(numbers[j])
                result.append(''.join(temp))
                recur()
                index[j] = 0
                del temp[-1]


    recur()
    a1 = list(map(int,result))
    a2 = set(a1)
    a1 = list(a2)
    for i in range(len(a1)):
        flag = 0
        for j in range(2,int(math.sqrt(a1[i]))+1):
            if a1[i] % j == 0:
                flag = 1
        if a1[i] == 0 or a1[i] == 1:
            pass
        elif flag == 0:
            count += 1
    return count