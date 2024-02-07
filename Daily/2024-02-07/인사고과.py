def solution(scores):
    answer = 1
    arr = [0] * (200002)
    for i in scores:
        arr[i[0]] = max(arr[i[0]],i[1])
    for i in range(200000,-1,-1):
        arr[i] = max(arr[i],arr[i+1])
    cnt = [0] * (200001)
    if arr[scores[0][0]+1] > scores[0][1]:
        return -1
    for x,y in scores:
        if arr[x+1] <= y:
            cnt[x+y] += 1
    for i in range(200000,-1,-1):
        if i == sum(scores[0]):
            break
        answer += cnt[i]

    return answer

solution([[2,2],[1,4],[3,2],[3,2],[2,1]]) # 4