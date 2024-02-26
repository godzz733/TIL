while 1:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
    a,b = max(a,b), min(a,b)
    ans = 'A'
    while a%b:
        if a//b > 1:
            print(ans,'wins')
            break
        a,b = b, a%b
        ans = 'A' if ans == 'B' else 'B'
    else:
        print(ans,'wins')