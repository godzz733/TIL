n = int(input())
a = 1
for i in range(2,n+1):
    a *= i
    while not a%10:
        a//=10
    a %= int(1e12)

print(str(a%100000).zfill(5))