def solution(n, lost, reserve):
    check = []
    for i in range(1, n+1):
        if i in reserve:
            if i in lost:
                lost.remove(i)
            else:
                check.append(i)

    for r in check:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)

    return n - len(lost)
