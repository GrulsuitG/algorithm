def solution(n, k):
    answer = 0
    numbers = transform(n, k).split("0")

    for number in numbers:
        if number.isdigit():
            answer += isPrime(int(number))

    return answer


def transform(n, k):
    result = ''
    while n > 0:
        result += str(n % k)
        n = n // k

    return result[::-1]


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True