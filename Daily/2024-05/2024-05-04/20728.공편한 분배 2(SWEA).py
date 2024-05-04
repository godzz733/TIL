for tc in range(1,int(input())+1):
    a,b = map(int,input().split())
    arr = sorted(list(map(int,input().split())))
    ans = int(1e12)
    for i in range(b-1, a):
        for j in range(0,i-b+2):
            ans = min(ans,arr[i] - arr[j])
    print(f"#{tc} {ans}")