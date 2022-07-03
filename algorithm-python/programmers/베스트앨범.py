from collections import defaultdict
from collections import Counter


def solution(genres, plays):
    answer = []
    n = len(genres)
    times = defaultdict(dict)
    total = defaultdict(int)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        times[genre][idx] = play
        total[genre] += play

    for genre in Counter(total).most_common():
        for idx, time in Counter(times[genre[0]]).most_common(2):
            answer.append(idx)

    return answer


