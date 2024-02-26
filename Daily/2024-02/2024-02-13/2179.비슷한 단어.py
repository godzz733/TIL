import sys; input = sys.stdin.readline
n = int(input())
t = [input().strip() for _ in range(n)]
arr = t[::]
arr.sort()
ans = set()
cnt = 1
for i in range(n-1):
    for j in range(i+1,n):
        key = 0
        for k in range(len(arr[i])):
            if arr[i][k] != arr[j][k]:
                k -= 1
                break
        else:
            key = 1
        if cnt < k+1:
            cnt = k+1
            ans.clear()
            ans.add(arr[i][:k+1])
        elif cnt == k+1:
            ans.add(arr[i][:k+1])
        if not key:
            break
ans_word = ''
for i in t:
    if not ans_word:
        if i[:cnt] in ans:
            ans_word = i
            print(i)
    else:
        if i[:cnt] == ans_word[:cnt]:
            print(i)
            break