# 회고

### 2024-02-02 (금)

#### 순 공부시간

- 1시간

<br>

# 공부 목록

## 알고리즘

|         제목         |  티어  |      분류       |                               링크                                |
| :------------------: | :----: | :-------------: | :---------------------------------------------------------------: |
| 2개 이하로 다른 비트 | 레벨 2 | 비트 연산, 수학 | (https://school.programmers.co.kr/learn/courses/30/lessons/77885) |

## SQL 문제

|                   제목                    |  티어  |    분류    |                                링크                                |
| :---------------------------------------: | :----: | :--------: | :----------------------------------------------------------------: |
| 흉부외과 또는 일반외과 의사 목록 출력하기 | 레벨 1 |   SELECT   | (https://school.programmers.co.kr/learn/courses/30/lessons/132203) |
|    12세 이하인 여자 환자 목록 출력하기    | 레벨 1 | IF, ISNULL | (https://school.programmers.co.kr/learn/courses/30/lessons/132201) |
|           가장 비싼 상품 구하기           | 레벨 1 |    MAX     | (https://school.programmers.co.kr/learn/courses/30/lessons/131697) |

### SQL

- ISNULL = NULL 판단

### 문제 풀이

- XOR을 통해 n이 가진 제일 낮은 위치의 0을 구하고 2비트 까지는 차이가 나도 되니 >>2
- 그리고 n이 가능한 최소 조건인 +1을 해줘서 더하면 됨

```Python
def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer
```
