a = list(input())
dic = {a[i]:i+1 for i in range(len(a))}
b = list(input())
size = len(b)
arr = [0,len(a)]
for i in range(size-1):
    arr.append((arr[-1]*len(a))%900528)
ans = sum(arr[:-1])%900528
for j in range(size-1):
    ans += arr[size-j-1]*(dic[b[j]]-1)
    ans = ans%900528
print((ans+dic[b[-1]])%900528)