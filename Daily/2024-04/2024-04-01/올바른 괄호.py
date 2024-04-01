def solution(s):
    q = []
    for i in s:
        if i == '(':
            q.append(i)
        else:
            if not q or q.pop() == ')':
                return False
    if q:
        return False

    return True