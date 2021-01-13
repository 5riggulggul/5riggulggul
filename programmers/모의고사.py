def solution(answers):
    first = [1,2,3,4,5]*2000
    second = [2,1,2,3,2,4,2,5] * 1250
    third = [3,3,1,1,2,2,4,4,5,5] * 1000
    result = [0,0,0]
    maxi = 0
    answer = []
    for i in range(len(answers)):
        if first[i] is answers[i]:
            result[0] += 1
        if second[i] is answers[i]:
            result[1] += 1
        if third[i] is answers[i]:
            result[2] += 1
    for i in range(3):
        if result[i] > maxi:
            answer =[]
            answer.append(i+1)
            maxi = result[i]
        elif result[i] == maxi:
            answer.append(i+1)
    return answer