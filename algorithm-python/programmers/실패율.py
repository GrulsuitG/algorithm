def solution(N, stages):
    answer = []
    counter = [0] * (N + 2)
    for stage in stages:
        counter[stage] += 1
    prefix_sum = [counter[1]] * (N + 2)
    for i in range(2, N + 2):
        prefix_sum[i] = prefix_sum[i - 1] + counter[i]

    failure = {1: counter[1] / prefix_sum[N + 1]}
    for i in range(2, N + 1):
        if prefix_sum[N + 1] - prefix_sum[i - 1] == 0:
            failure[i] = 0
        else:
            failure[i] = counter[i] / (prefix_sum[N + 1] - prefix_sum[i - 1])

    items = sorted(failure.items(), key=lambda x: x[1], reverse=True)
    for item in items:
        answer.append(item[0])
    return answer


def best(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)