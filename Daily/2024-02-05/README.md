# 회고

### 2024-02-05 (월)

#### 순 공부시간

- 1시간

<br>

# 공부 목록

## SQL 문제

|              제목              |  티어  |   분류   |                                링크                                |
| :----------------------------: | :----: | :------: | :----------------------------------------------------------------: |
|  DATETIME에서 DATE로 형 변환   | 레벨 2 |   DATE   | (https://school.programmers.co.kr/learn/courses/30/lessons/59414)  |
|         NULL 처리하기          | 레벨 2 |   NULL   | (https://school.programmers.co.kr/learn/courses/30/lessons/59410)  |
|   가격대 별 상품 개수 구하기   | 레벨 2 | GROUP BY | (https://school.programmers.co.kr/learn/courses/30/lessons/131530) |
| 진료과별 총 예약 횟수 출력하기 | 레벨 2 | GROUP BY | (https://school.programmers.co.kr/learn/courses/30/lessons/132202) |
|  상품 별 오프라인 매출 구하기  | 레벨 2 |   JOIN   | (https://school.programmers.co.kr/learn/courses/30/lessons/131533) |

### SQL

- 반올림, 올림, 내림

  - ROUND(반올림 할 숫자, 반올림 자릿수, 반올림 여부)
  - CEIL(올림 할 숫자), 소수점 첫 번째 자리에서 올림
  - FLOOR(내릴 값), 소수점 첫 번째 자리에서 내림

  ```SQL
  SELECT ROUND(123.456)			--123
  SELECT ROUND(123.456, 1)		--123.500
  SELECT ROUND(123.456, 2)		--123.460
  SELECT ROUND(123.456, 2, 0)		--123.460
  SELECT ROUND(123.456, 2, 1)		--123.450
  SELECT ROUND(170,-2); 			-- 200

  SELECT CEILING(1.456)			--2
  SELECT CEILING(1.6) 			--2
  SELECT FLOOR(1.456)			--1
  SELECT FLOOR(1.6) 			--1
  ```

## 알고리즘

|      제목       |  티어  | 분류 |                  링크                   |
| :-------------: | :----: | :--: | :-------------------------------------: |
| BFS 스페셜 저지 | 골드 3 | BFS  | (https://www.acmicpc.net/problem/16940) |
