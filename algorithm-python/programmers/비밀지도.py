def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        row = ''
        num1 = bin(num1)[2:]
        num2 = bin(num2)[2:]
        #num1 = '0' * (n - len(num1)) + num1
        num1 = num1.zfill(n)
        # num2 = '0' * (n - len(num2)) + num2
        num2 = num2.zfill(n)
        for n1, n2 in zip(num1, num2):
            if n1 == '1' or n2 == '1':
                row += '#'
            else:
                row += ' '
        answer.append(row)
    return answer
