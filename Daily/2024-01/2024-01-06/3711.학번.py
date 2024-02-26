import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    for i in range(1,int(1e6)):
        tem = set()
        for j in arr:
            if j%i in tem:
                break
            tem.add(j%i)
        else:
            print(i)
            break