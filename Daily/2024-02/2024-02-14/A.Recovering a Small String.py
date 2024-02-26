dic = {}
for i in range(1,27):
    for j in range(1,27):
        for k in range(1,27):
            if (i+j+k) not in dic:
                dic[i+j+k] = [chr(i+96)+chr(j+96)+chr(k+96)]
            else:
                dic[i+j+k].append(chr(i+96)+chr(j+96)+chr(k+96))
for i in range(3,79):
    dic[i] = sorted(dic[i])
for _ in range(int(input())):
    n = int(input())
    print(dic[n][0])