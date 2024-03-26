n = input()
k = int(input())
arr = []
for i in range(len(n)):
    if n[i] in ('1','2','6','7'):
        if n[i] == '1' or n[i] == '6':
            arr.append(['1',i])
        else:
            arr.append(['2',i])
if k > 1<<len(arr):
    print(-1)
    exit()
idx = len(arr)-1
for i in bin(k-1)[2:][::-1]:
    if i == '1':
        if arr[idx][0] == '1':
            arr[idx][0] = '6'
        elif arr[idx][0] == '2':
            arr[idx][0] = '7'
    else:
        if arr[idx][0] == '6':
            arr[idx][0] = '1'
        elif arr[idx][0] == '7':
            arr[idx][0] = '2'
    idx -= 1
ans = list(n)
for x,y in arr:
    ans[y] = x
print(''.join(ans))