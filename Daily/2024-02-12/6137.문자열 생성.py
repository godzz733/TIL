n = int(input())
arr = [input() for _ in range(n)]
ans = ''
st = 0
fi = n-1
while st <= fi:
    if arr[st] < arr[fi]:
        ans += arr[st]
        st += 1
    elif arr[st] > arr[fi]:
        ans += arr[fi]
        fi -= 1
    else:
        l = st
        r = fi
        while l <= r:
            if arr[l] < arr[r]:
                ans += arr[st]
                st += 1
                break
            elif arr[l] > arr[r]:
                ans += arr[fi]
                fi -= 1
                break
            l += 1
            r -= 1
        else:
            ans += arr[st]
            st += 1
for i in range(len(ans)):
    if i % 80 == 0 and i != 0:
        print()
    print(ans[i], end='')