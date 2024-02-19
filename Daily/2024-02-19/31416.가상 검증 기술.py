import sys; input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    ans = 0
    if b*d >= a*c:
        ans = b*d
    else:
        st = 0
        fi = 10001
        while st<=fi:
            mid = (st+fi)//2
            if (mid-b*d)//a + mid//a >= c:
                fi = mid-1
                ans = mid
            else:
                st = mid+1
    print(ans)