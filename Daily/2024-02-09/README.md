# 회고

### 2024-02-09 (금)

#### 순 공부시간

- 1시간

<br>

# 공부 목록

## SQL 문제

|                          제목                          |  티어  |          분류          |                                링크                                |
| :----------------------------------------------------: | :----: | :--------------------: | :----------------------------------------------------------------: |
| 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기 | 레벨 3 | JOIN, STRING, ORDER BY | (https://school.programmers.co.kr/learn/courses/30/lessons/164671) |
|       조건에 맞는 사용자와 총 거래금액 조회하기        | 레벨 3 |        GROUP BY        | (https://school.programmers.co.kr/learn/courses/30/lessons/164668) |
|       대여 기록이 존재하는 자동차 리스트 구하기        | 레벨 3 |    GROUP BY, STRING    | (https://school.programmers.co.kr/learn/courses/30/lessons/157341) |

## 알고리즘

| 제목 |    티어    |     분류     |                  링크                  |
| :--: | :--------: | :----------: | :------------------------------------: |
| 컨닝 | 플레티넘 4 | DP, 비트필드 | (https://www.acmicpc.net/problem/1014) |

### 컨닝 풀이

- n,m 이 최대 10 이므로 비트필드를 이용해서 전체를 탐색하면 됨
- 이때 탐색을 할 때 뒤의 사람은 자기 앞에 사람이 있어도 상관이 없으므로 바로 위의 행만 확인하면 됨
- 그러므로 (2 ^ 10) ^ 2 로 완전탐색 + 조건이 맞는다면 DP를 이용해서 최대값을 지정
- 이때 양옆이 안되므로 안되는 모든 숫자를 미리 기록해서 사용할 수 있음 ex) 101, 1, 1001 등 이런건 가능한 조건
- 그래서 가능한 비트 필드 중에서 바로 앞의 행을 보고 가능한지 안한지를 확인 -> 가능하면 DP로 최대값 기록

```python
import sys
input = sys.stdin.readline
def check_num(x):
    global key
    for i in range(1<<x):
        t = bin(i)[2:].zfill(x)
        for j in range(1,x-1):
            if t[j] == '1' and (t[j-1] == '1' or t[j+1] == '1'):
                break
        else:
            key.add(i)
def check_cnt(x,y):
    for i in range(m):
        if x & (1<<i):
            if i > 0 and ((1 << (i-1)) & y): return 0
            if i < m-1 and ((1 << (i+1)) & y): return 0
    return 1


for _ in range(int(input())):
    n,m = map(int,input().split())
    arr = [list(input()) for _ in range(n)]
    check = []
    for i in range(n):
        tem = 0
        for j in range(m):
            if arr[i][j] == 'x':
                tem |= 1<<j
        check.append(tem)
    dp = [[0 for i in range(1<<m)] for _ in range(n)]
    key = set()
    check_num(m)
    for i in key:
        if i & check[0]: continue
        dp[0][i] = bin(i).count('1')
    for i in range(1,n):
        for j in key:
            if j & check[i]: continue
            for k in key:
                if check_cnt(j,k):
                    dp[i][j] = max(dp[i][j],dp[i-1][k]+bin(j).count('1'))
    ans = 0
    for i in range(n):
        ans = max(ans,max(dp[i]))
    print(ans)
```
