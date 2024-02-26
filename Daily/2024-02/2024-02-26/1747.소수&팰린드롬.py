import sys;input = sys.stdin.readline
n = int(input())
prime = [False,False] + [True] * 2000003
primes = [1]
for i in range(2, 2000003):
    if prime[i]:
        primes.append(i)
        for j in range(i*2, 2000003, i):
            prime[j] = False
def ispalindrome(s):
    if s < n:
        return False
    s = str(s)
    return s == s[::-1]
for i in primes:
    if ispalindrome(i):
        print(i)
        break