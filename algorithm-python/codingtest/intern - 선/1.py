def solution(logs):
    answer = []
    logs = set(logs)
    problems = {}
    for log in logs:
        name, problem = log.split()
        if problem in problems:
            problems[problem] += 1
        else:
            problems[problem] = 1

    n = len(logs) / 2
    for key, item in problems.items():
        if item >= n:
            answer.append(key)
    answer.sort()
    return answer


print(solution(["morgan string_compare", "felix string_compare", "morgan reverse", "rohan sort", "andy reverse", "morgan sqrt"]))