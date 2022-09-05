def solution(sizes):
    w = max(i[0] for i in sizes)
    h = 0
    for size in sizes:
        if size[0] < size[1]:
            w = max(size[1], w)
            h = max(size[0], h)
        else:
            h = max(size[1], h)
    return w * h