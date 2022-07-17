def solution(brown, yellow):
    total = brown + yellow

    for i in range(1, int(total ** 0.5) + 1):
        if total % i == 0:
            div = total // i
            if (i - 2) * (div - 2) == yellow:
                return [div, i]


