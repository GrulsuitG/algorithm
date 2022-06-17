from collections import defaultdict


def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    A = defaultdict(int)
    B = defaultdict(int)
    union = defaultdict(int)
    inter = defaultdict(int)

    for i in range(1, len(str1)):
        string = str1[i - 1:i + 1]
        if string.isalpha():
            A[string] += 1

    for i in range(1, len(str2)):
        string = str2[i - 1:i + 1]
        if string.isalpha():
            B[string] += 1

    print(set(A.keys()).union(B.keys()))


    return A

solution("FRANCE", "french")