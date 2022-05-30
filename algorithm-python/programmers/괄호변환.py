def solution(p):
    def split(w):
        l = r = 0
        for i in range(len(w)):
            if w[i] == '(':
                l += 1
            elif w[i] == ')':
                r += 1

            if l == r != 0:
                return w[:i + 1], w[i + 1:]

    def check(w):
        s = []
        for c in w:
            if c == '(':
                s.append(c)
            elif c == ')':
                if len(s):
                    if s[-1] == '(':
                        s.pop()
                    elif s[-1] == ')':
                        return False
                else:
                    return False
        return True

    if p == '':
        return ''
    u, v = split(p)
    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('

    return answer


def best(p):
    if p == '':
        return p
    r = True
    c = 0
    for i in range(len(p)):
        if p[i] == '(':
            c -= 1
        else:
            c += 1
        if c > 0:
            r = False
        if c == 0:
            if r:
                return p[:i + 1] + solution(p[i + 1:])
            else:
                return '(' + solution(p[i + 1:]) + ')' + ''.join(map(lambda x: '(' if x == ')' else ')', p[1:i]))
