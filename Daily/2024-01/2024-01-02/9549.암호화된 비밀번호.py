import sys; input = sys.stdin.readline
from collections import Counter,deque
for _ in range(1,int(input())+1):
    a,b = input().rstrip(), input().rstrip()
    tem = Counter(b)
    q = deque()
    ans = {}
    for i in a:
        if i not in tem:
            ans = {}
            q = deque()
        else:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
            q.append(i)
            
            if ans[i] > tem[i]:
                while ans[i] > tem[i]:
                    ans[q.popleft()] -= 1
        if ans == tem:
            print('YES')
            break
    else:
        print('NO')