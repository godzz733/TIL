# 회고

### 2024-02-04 (일)

#### 순 공부시간

- 1시간

<br>

# 공부 목록

## SQL 문제

|                  제목                  |  티어  |   분류   |                                링크                                |
| :------------------------------------: | :----: | :------: | :----------------------------------------------------------------: |
|  3월에 태어난 여성 회원 목록 출력하기  | 레벨 2 |   DATE   | (https://school.programmers.co.kr/learn/courses/30/lessons/131120) |
|             중복 제거하기              | 레벨 2 | DISTINCT | (https://school.programmers.co.kr/learn/courses/30/lessons/59408)  |
| 강원도에 위치한 생산공장 목록 출력하기 | 레벨 1 |   LIKE   | (https://school.programmers.co.kr/learn/courses/30/lessons/131112) |
| 경기도에 위치한 식품창고 목록 출력하기 | 레벨 1 | IF, LIKE | (https://school.programmers.co.kr/learn/courses/30/lessons/131114) |
|    나이 정보가 없는 회원 수 구하기     | 레벨 1 |  ISNULL  | (https://school.programmers.co.kr/learn/courses/30/lessons/131528) |

### SQL

- 날짜관련 함수
  - YEAR
  - MONTH
  - DAYOFMONTH
  - DATEDIFF -> A날짜에서 BSKFwK qORL
  - CURDATE -> 오늘날짜 추출
  ```SQL
  SELECT * FROM test.please2 WHERE YEAR(orderdate) = '2021'
  SELECT * FROM test.please2 WHERE month(orderdate) = '2'
  SELECT * FROM test.please2 WHERE DAYOFMONTH(orderdate) = '11'
  SELECT orderdate, id, DATEDIFF(CURDATE(), orderdate) FROM test.please2;
  ```
