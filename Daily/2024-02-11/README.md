# 회고

### 2024-02-11 (일)

#### 순 공부시간

- 2시간

<br>

# 공부 목록

## SQL 문제

|                         제목                          |  티어  |        분류         |                                링크                                |
| :---------------------------------------------------: | :----: | :-----------------: | :----------------------------------------------------------------: |
|             우유와 요거트가 담긴 장바구니             | 레벨 4 | GROUP BY, DISTINCT  | (https://school.programmers.co.kr/learn/courses/30/lessons/62284)  |
|               보호소에서 중성화한 동물                | 레벨 4 |    JOIN, STRING     | (https://school.programmers.co.kr/learn/courses/30/lessons/59045)  |
|       식품분류별 가장 비싼 식품의 정보 조회하기       | 레벨 4 | GROUP BY, SUB QUERY | (https://school.programmers.co.kr/learn/courses/30/lessons/131116) |
| 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기 | 레벨 3 | GROUP BY, SUB QUERY | (https://school.programmers.co.kr/learn/courses/30/lessons/157340) |

## 우유와 요거트 풀이 3개

```SQL
-- 1번 GROUP BY
SELECT CART_ID FROM CART_PRODUCTS
WHERE NAME IN ('Milk','Yogurt')
GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME) >= 2
ORDER BY ID;

-- 2번 GROUP_CONCAT
SELECT CART_ID
FROM (
    SELECT CART_ID, GROUP_CONCAT(NAME) AS NAMES
    FROM CART_PRODUCTS
    GROUP BY CART_ID
) TMP

WHERE NAMES LIKE '%Milk%'
    AND NAMES LIKE '%Yogurt%'

-- 3번 JOIN

WITH M AS (
SELECT DISTINCT CART_ID, NAME FROM CART_PRODUCTS
WHERE NAME = 'Milk'),
Y AS (
SELECT DISTINCT CART_ID, NAME FROM CART_PRODUCTS
WHERE NAME = 'Yogurt')

SELECT Y.CART_ID
FROM Y
INNER JOIN M
ON Y.CART_ID = M.CART_ID;
```

## 알고리즘

|           제목           |  티어  |    분류    |                                링크                                |
| :----------------------: | :----: | :--------: | :----------------------------------------------------------------: |
| 연속 펄스 부분 수열의 합 | 레벨 3 | DP, 누적합 | (https://school.programmers.co.kr/learn/courses/30/lessons/161988) |

### 연속 펄스 부분 풀이

- 내 풀이에서 생각한건 구간합에서 만약 뒤의 구간에 최소값이 있고 앞의 구간에 최대값이 있다면 max, min으로 불가능하지 않을 까 생각함
- 하지만 어처피 1,-1,1 에서 저런 상태라면 -1,1,-1로 바꾸고 최대값 - 최소값을 하면 되므로 그냥 저거를 반환해도 됨

```Python
def solution(sequence):
    answer = 0
    a = [(-1) ** i for i in range(len(sequence))] + [0]
    for i in range(len(sequence)):
        a[i] *= sequence[i]

    for i in range(1,len(sequence)):
        a[i] += a[i-1]

    return abs(max(a)-min(a))
```
