n,m = map(int,input().split())

arr1 = []

arr2= []

for i in range(n):

    t = int(input())

    if t >= 0:

        arr1.append(t)

    else: arr2.append(-t)

ans = 0

idx = len(arr1)-1

arr1.sort()

arr2.sort()

while idx >=0:

    ans += arr1[idx]<<1

    idx -= m

idx = len(arr2)-1

while idx >=0:

    ans += arr2[idx]<<1

    idx -= m

print(ans)