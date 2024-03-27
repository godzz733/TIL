from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    w = 0
    for i in truck_weights:
        if i+w <= weight:        
            q.append((i,answer + bridge_length))
            w += i
        else:
            while q and i+w > weight:
                x,y = q.popleft()
                w -= x
                answer = y
            w += i
            q.append((i,answer + bridge_length))
        answer += 1
        while q:
            x,y = q.popleft()
            if y >= answer:
                q.appendleft((x,y))
                break
            w -= x
    if q:
        answer = q.pop()[1]
    return answer + 1