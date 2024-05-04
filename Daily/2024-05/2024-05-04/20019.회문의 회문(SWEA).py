def pal(t):
    for i in range(len(t) >> 1):
        if t[i] != t[-1-i]:
            return True
    return False
for tc in range(1,int(input())+1):
    t = list(input())
    if pal(t):
        print(f"#{tc} NO")
        continue
    if pal(t[:len(t) >> 1]) or pal(t[(len(t)+1) >> 1:]):
        print(f"#{tc} NO")
        continue
    print(f"#{tc} YES")