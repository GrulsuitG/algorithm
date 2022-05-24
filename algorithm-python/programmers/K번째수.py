def solution(array, commands):
    answer = []
    for command in commands:
        target = array[command[0]-1 : command[1]]
        target.sort()
        answer.append(target[command[2] - 1])
    return answer

def best(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))