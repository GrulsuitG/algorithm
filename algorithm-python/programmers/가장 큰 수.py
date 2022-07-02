def solution(numbers):
    answer = ''
    items = [((str(number)*4)[:4], str(number)) for number in numbers]
    items.sort(reverse=True)
    for item in items:
        answer += item[1]
    return str(int(answer))


def best(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

