import math
def solution(numbers):
    result =[]
    index = [0]*1000001
    temp = []
    count = 0
    def recur(): # 모든 경우의 수 만드는 부분
        for j in range(len(numbers)):
            if index[j] == 0:
                index[j] = 1
                temp.append(numbers[j])
                result.append(''.join(temp))
                recur()
                index[j] = 0
                del temp[-1]


    recur() #재귀함수 호출 -> 모든 수 result에 만들기
    
    a1 = list(map(int,result)) #int화 시켜서 0으로 시작하는 숫자에서 0 제거
    a2 = set(a1) # ----]
    a1 = list(a2) # ---] 집합에 넣었다가 빼서 중복되는 수 제거
    
  
    for i in range(len(a1)): #소수 찾는 부분
        flag = 0
        for j in range(2,int(math.sqrt(a1[i]))+1): # 2부터 자신의 제곱근까지만 탐색
            if a1[i] % j == 0:
                flag = 1
        if a1[i] == 0 or a1[i] == 1:
            pass
        elif flag == 0:
            count += 1
    return count