def solution(A,B):
    return sum([i*j for i,j in zip(sorted(A),sorted(B, reverse=True))])