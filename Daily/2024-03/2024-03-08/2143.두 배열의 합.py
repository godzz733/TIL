import sys; input = sys.stdin.readline
t = int(input())
n = int(input())
ans = 0
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
t1 = [0]
t2 = [0]
for i in range(n):
    t1.append(t1[-1] + arr1[i])
for i in range(m):
    t2.append(t2[-1] + arr2[i])
dic= {}
for i in range(1,n+1):
    for j in range(i):
        num = t1[i]-t1[j]
        dic[num] = dic.get(num,0) + 1

for i in range(1,m+1):
    for j in range(i):
        ans += dic.get(t-(t2[i]-t2[j]),0)

print(ans)