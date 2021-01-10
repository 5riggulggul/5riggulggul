def solution(citations):
    a = citations
    answer = 0
    a.sort()
    for i in range(len(a)):
        if (len(a) - a.index(a[i])) >= a[i]:
            if answer < a[i]:
                answer = a[i]
        else:
            if answer < len(a) - a.index(a[i]):
                answer = len(a) - a.index(a[i])
    return answer