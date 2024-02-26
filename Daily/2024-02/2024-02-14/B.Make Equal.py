for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    t = sum(arr)//n
    for i in range(n-1):
        if arr[i] > t:
            arr[i+1] += arr[i] - t
            arr[i] = t
        elif arr[i] < t:
            print('NO')
            break
    else:
        for i in range(n):
            if arr[i] != t:
                print('NO')
                break
        else:
            print('YES')
            