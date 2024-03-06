st = input()

arr = [['K','S','A'],['S','A','K'],['A','K','S']]

ans = 25* 10**10 + 1

for i in range(3):

    idx = 0

    t = 0

    for j in st:

        if arr[i][idx] == j:

            idx = (idx+1)% 3

        else:

            t += 1

    ans = min(ans,t + abs( i - t ) + i)

print(ans)        