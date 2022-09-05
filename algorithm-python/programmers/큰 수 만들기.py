def solution(number, k):
    cnt = 0
    number = list(number)
    idx = 1
    while cnt < k:
        if number[idx] > number[idx - 1]:
            number.pop(idx - 1)
            cnt += 1
        else:
            idx += 1

    return ''.join(number)

