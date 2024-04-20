n = int(input())
arr = list(map(int, input().split()))
idx = 1
s = []
for i in arr:
    if i == idx:
        idx += 1
        while s and s[-1] == idx:
            s.pop()
            idx += 1
        continue
    s.append(i)
while s:
    if s[-1] == idx:
        s.pop()
        idx += 1
    else:
        print("Sad")
        break
else:
    print("Nice")