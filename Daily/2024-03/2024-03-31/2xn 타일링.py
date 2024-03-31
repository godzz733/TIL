def solution(n):
    answer = [1,2,3]
    for _ in range(n-3):
        answer.append((answer[-1]+answer[-2])%1000000007)
    return answer[n-1]