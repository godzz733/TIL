n = int(input())
arr = [i**2 for i in range(1,50001)]
dic = {}
for i in arr:
    dic[i] = 1
ans = []
for i in range(len(arr)-1,0,-1):
    if arr[i] - n in dic:
        ans.append(int(arr[i] ** 0.5))
for i in ans[::-1]:
    print(i)

if not ans:print(-1)