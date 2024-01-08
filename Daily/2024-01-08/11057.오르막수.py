# n = open(0)
arr = [[] for _ in range(1001)]
arr[1] = [1 for _ in range(10)]
for i in range(2, 1001):
    for j in range(10):
        arr[i].append(sum(arr[i-1][:j+1]))
print(sum(arr[int(input())]) % 10007)