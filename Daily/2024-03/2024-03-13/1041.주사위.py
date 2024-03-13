n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(sum(sorted(arr)[:5]))
else:
    t = (min(arr[0]+arr[1]+arr[2],arr[0]+arr[2]+arr[4],arr[0]+arr[4]+arr[3],arr[0]+arr[3]+arr[1]
            ,arr[5]+arr[1]+arr[2],arr[5]+arr[2]+arr[4],arr[5]+arr[4]+arr[3],arr[5]+arr[3]+arr[1]),
            min(arr[0]+arr[1],arr[0]+arr[2],arr[0]+arr[4],arr[0]+arr[3],arr[5]+arr[1]
                ,arr[5]+arr[2],arr[5]+arr[4],arr[5]+arr[3],
                arr[1]+arr[2],arr[2]+arr[4],arr[4]+arr[3],arr[3]+arr[1]
                ),
            min(arr))
    print(4*t[0] + ((n-2)*4 + (n-1)*4) * t[1] + ((n-2)**2 + (n-2)*(n-1)*4)*t[2])