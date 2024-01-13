import sys; I = sys.stdin.readline
import bisect
prime = [False, False] + [True] * 31374
ans = []
def find_ans(x):
    t = str(x)
    tt = t[1:]
    if '2' in tt or '4' in tt or '6' in tt or '8' in tt or '0' in tt or '5' in tt:
        return False
    for i in range(2,len(t)):
        for j in range(len(t) - i + 1):
            if not prime[int(t[j:j+i])]:
                return False
    return True
for i in range(2, 31376):
    if prime[i]:
        for j in range(i * 2, 31376, i):
            prime[j] = False
for i in range(100,31376):
    if not prime[i] and i%2 and find_ans(i):
        ans.append(i)
for _ in range(int(I())):
    n = int(I())
    a = bisect.bisect_right(ans, n)-1
    if a == -1:
        print(-1)
    else:
        print(ans[a])