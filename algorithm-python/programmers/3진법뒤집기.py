def solution(n):
    answer = 0
    three = ''
    while n:
        three += str(n % 3)
        n = n // 3

    three = int(three)
    digit = 0
    while three:
        num = three % 10
        answer += num * (3 ** digit)
        three //= 10
        digit += 1
    return answer


def best(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3) # int에 진법으로 변환해주는 기능이 있다.
    return answer

