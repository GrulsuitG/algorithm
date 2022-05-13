import re

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27


def solution(new_id):
    answer = []
    for i in new_id:
        if i.isalpha():
            answer.append(i.lower())
        elif i == '.' and len(answer) and answer[-1] != '.':
            answer.append('.')
        elif i.isdigit() or i == '-' or i == '_':
            answer.append(str(i))

    if len(answer) and answer[-1] == '.':
        answer.pop()
    if len(answer) == 0:
        answer.append('a')
    if len(answer) > 15:
        answer = answer[:15]
        while answer[-1] == '.':
            answer.pop()
    elif len(answer) < 3:
        while len(answer) < 3:
            answer.append(answer[-1])

    return ''.join(answer)


def best(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^a-z0-9-_\.]", '', new_id)
    new_id = re.sub("\.+", '.', new_id)
    new_id = re.sub("^[.]|[.]$", '', new_id)
    new_id = 'a' if new_id == '' else new_id[:15]
    new_id = re.sub("^[.]|[.]$", '', new_id)
    new_id = new_id if len(new_id) > 2 else new_id + ''.join([new_id[-1] for _ in range(3 - len(new_id))])

    return new_id

