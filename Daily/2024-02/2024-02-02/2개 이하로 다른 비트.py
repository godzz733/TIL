def solution(numbers):
    answer = []
    for x in numbers:
        for i in range(49,-1,-1):
            if x&(1<<i):
                max_bi = 1<<i
                break
        if x & 1 == 0:
            answer.append(x|1)
        elif x & (x+1) == 0:
            answer.append(((x+1)|x)^max_bi)
        else:
            min_bi = 0
            max_bi = 0
            for i in range(50):
                if x & (1<<i) == 0:
                    min_bi = 1<<i
                    break
                if x&(1<<i):
                    max_bi = 1<<i
            answer.append((x|min_bi)^max_bi)
    return answer