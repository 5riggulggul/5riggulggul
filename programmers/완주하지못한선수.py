def solution(participant, completion):
    p = participant
    c = completion
    a = {}
    b = {}
    l = []
    for i in range(len(p)):
        a[p[i]] = 0
    for i in range(len(p)):
        a[p[i]] += 1
    for i in range(len(c)):
        a[c[i]] -= 1

    for i in a:
        for _ in range(a[i]):
            l.append(i)
    return l[0]