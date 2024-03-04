a,b = map(int,input().split())

prime = [True]*(10**7)

ans = 0

for i in range(2,10**7):

    if not prime[i]:continue

    tem = i ** 2

    while tem <= b:

        if tem >= a:

            ans += 1

        tem *= i

    for j in range(i<<1,10**7,i):

        prime[j] = False

print(ans)