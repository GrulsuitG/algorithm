def solution(lottos, win_nums):
    high, low = 7, 7
    for num in lottos:
        if num == 0:
            high -= 1
        if num in win_nums:
            high -= 1
            low -= 1
    if high == 0 :
        high = 1
    if low == 0:
        low = 1
    if high == 7 :
        high = 6
    if low == 7:
        low = 6
    return [high, low]

def best(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    zero = lottos.count(0)
    ans = 0
    for num in lottos:
        if num in win_nums:
            ans += 1

    return [rank[ans+zero], rank[ans]]
