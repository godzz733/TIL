import sys; I = sys.stdin.readline
from collections import defaultdict 
n = int(I())
arr = [*map(int, I().split())]
lst = [arr[0]]
ans = [0,0]
dic = defaultdict(list)
dic[arr[0]].append(0)
for i in range(1,n):
    lst.append(lst[-1] + arr[i])
    dic[arr[i]].append(i)
lst.append(0)
for i in set(arr):
    if len(dic[i]) > 1:
        ans.append(lst[dic[i][-1]] - lst[dic[i][0]-1])
    else:
        ans.append(i)
print(max(ans),ans.count(max(ans)))