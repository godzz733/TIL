# 회고

### 2024-01-06 (토)

#### 순 공부시간

- 1시간

<br>

# 공부 목록

## 알고리즘

|   제목   |  티어  |       분류       |                  링크                   |
| :------: | :----: | :--------------: | :-------------------------------------: |
|   학번   | 실버 5 |     완전탐색     | (https://www.acmicpc.net/problem/3711)  |
| 수강변경 | 실버 4 | 그리디, 완전탐색 | (https://www.acmicpc.net/problem/23305) |

### 수강변경 풀이

- 접근 방식으로는 완전탐색을 생각함
- 그 이유는 만약 현재 수강하고있는 수업과 원하는 수업을 전부 배열에 집어넣고 만약 수강을 하고 있는 수업과 원하는 수업이 같다면 그 둘을 없애주면 그 둘은 어떤 방식으로든 매칭을 시켜줄 수 있기 때문에 남은 갯수에서 제외
- 모든 학생에 대해서 이 과정들을 수행하고 남은 것들은 모두 매칭이 불가능한 수업들임
- 그러므로 이 수업들의 수가 정답이고 한 학생당 수강중 수업 + 원하는 수업이기 때문에 정답에서 //2 를 해줘서 출력

### 풀이 코드

- input 사용

```python
import sys; input = sys.stdin.readline
n = int(input())
arr = [*map(int,input().split())]
arr2 = [*map(int,input().split())]
a = [0] * (int(1e6)+1)
for i in range(n):
    a[arr[i]] += 1
    a[arr2[i]] -= 1
ans = 0
for i in a:
    ans += abs(i)
print(ans//2)
```

- open(0) 사용

```python
n,arr,arr2 = open(0)
a = [0] * (int(1e6)+1)
for i in map(int, arr.split()):
    a[i] += 1
for i in map(int, arr2.split()):
    a[i] -= 1
ans = 0
for i in a:
    ans += abs(i)
print(ans>>1)
```

### 배운점

- open(0) 이라는 새로운 입력방법을 배워서 해봣는데 상당히 빠름 자주 사용할 듯
- 문제가 어려워 보여도 쉽게 풀수있는 방식은 항상 존재한다.
