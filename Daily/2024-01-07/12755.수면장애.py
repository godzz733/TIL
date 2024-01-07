import sys; input = sys.stdin.readline
n = int(input())
arr = [0,0]
for i in range(9):
    arr.append(9*(i+1)*10**i+arr[-1])
if n<=9:print(n)
else:
    t = 0
    for i in range(2,10):
        if arr[i] > n:
            t = i-1
            break
    print(str(10**(t-1) + (n-arr[t]-1)//t)[(n-arr[t])%t-1])