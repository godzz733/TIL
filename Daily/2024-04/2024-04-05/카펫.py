def solution(brown, yellow):
    for i in range(1,100000):
        if yellow%i:continue
        if (i+2)*2+((yellow//i)+2)*2 - 4 == brown:return sorted([i+2,(yellow//i)+2],reverse=True)