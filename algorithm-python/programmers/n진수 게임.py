digit = list("0123456789ABCDEF")


def solution(n, t, m, p):
    answer = ''
    turn = 0
    cur = 0
    while len(answer) < t:
        i = convert(cur, n)
        for j in i:
            if turn == p - 1:
                answer += j
                if len(answer) == t:
                    break
            turn = (turn + 1) % m
        cur += 1
    return answer


def convert(i, n):
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result += digit[i % n]
        i //= n

    return result[::-1]

solution(2, 4, 2, 1)
