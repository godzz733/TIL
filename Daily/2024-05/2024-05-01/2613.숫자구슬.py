import sys; input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
st = max(arr)
fi = sum(arr)
ans = 0
lst = [0]
for i in range(n):
    lst.append(lst[-1]+arr[i])
# print(lst)
def check(mid):
    tem = []
    st = 0

    for i in range(n):
        if len(tem) == m:
            return False
        if lst[i+1] - lst[st] > mid:
            tem.append(i - st)
            st = i
    if len(tem) == m:
        return False
    if lst[i+1] - lst[st] > mid:
        return False
    tem.append(i - st + 1)
    return tem
t = 0
while st <= fi:
    mid = (st+fi) >> 1
    tem = check(mid)
    if not tem:
        st = mid + 1
    else:
        ans = tem
        t = mid
        fi = mid - 1
if len(ans) == m:
    print(t)
    print(*ans)
else:
    tem = []
    # print(ans)
    for i in range(len(ans)):
        tt = ans[i]
        while tt > 1 and len(tem) + (len(ans) - i - 1) < m - 1:
            tem.append(1)
            tt -= 1
        tem.append(tt)
    # print(tem, t)
    print(t)
    print(*tem)
    

    