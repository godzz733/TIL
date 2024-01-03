# 회고

### 2024-01-03 (수)

#### 순 공부시간

- 2시간

<br>

# 공부 목록

## 강의

### SQL

- 컬럼 출력시 사칙연산 넣기 & 문자다루는 함수

  - 사칙연산
    ```SQL
    select 사용금액 * 10 from card;
    select 사용금액 - 10 from card;
    select 사용금액 - 10, 연체횟수 * 10 from card; --여러개도 가능
    ```
  - 컬럼끼리 사칙연산
    ```SQL
    select 사용금액 / 연체횟수 from card;
    ```
  - CONCAT(컬럼명1,컬럼명2, 임이의 문자 등) -> 문자 붙이기
  - TRIM(컬럼명 or 문자) -> 좌우 공백제거
  - REPLACE(컬럼명, 바뀔단어, 바꿀단어) -> 단어 바꾸기
  - SUBSTR(컬럼명, 몇째글자부터,몇자), RIGHT(컬럼,글자수), LEFT(컬렴,글자수) -> 문자 일부만 출력
  - INSERT(컬럼명, 몇째글자부터, 몇자, 바꿀단어) -> X번째 글자 교체

- 숫자 조작하는 SQL 함수들

  - GREATEST / LEAST -> 최대,최소
    ```SQL
        SELECT GREATEST(5, 3, 2, 1, 4);
        SELECT LEAST(5, 3, 2, 1, 4);
    ```
  - FLOOR(내림)/CEIL(올림) -> 소수 -> 정수

    ```SQL
    SELECT FLOOR(10.1); --10
    SELECT FLOOR(10.9); --10

    SELECT CEIL(10.1); --11
    SELECT CEIL(10.9); --11
    ```

  - ROUND(반올림)/TRUNCATE(내림)
    ```SQL
    SELECT ROUND(10.777, 2); --10.78
    SELECT TRUNCATE(10.777, 2); --10.77
    ```
  - POWER -> 제곱
  - ABS -> 절대값

- SELECT 안에 SELECT 또 쓸 수 있음 (서브쿼리)

  ```SQL
    select * from card
    where 사용금액 > (select AVG(사용금액) from card)
  ```

  - 서브쿼리 룰
    - 데이터 대신 서브쿼리
    - 1개의 데이터를 뱉는 쿼리문만 가능
    - 소괄호 넣기
    - 예외 -> in안에서는 여러개 데이터뱉어도 됨
    ```SQL
        select * from card where 고객명 in (select username from blacklist);
    ```

- 그룹지어 통계낼 땐 GROUP BY

  - group by를 해주는 컬럼은 보통 중복이 있는 카테고리 컬럼임
  - group by 필터링 -> having ( having은 group by 결과 필터링할때 사용) (where은 select뒤에 사용)

  ```SQL
  select 고객등급, avg(사용금액) from card group by 고객등급;
  select 고객등급, max(사용금액) from card group by 고객등급;
  select 고객등급, count(사용금액) from card group by 고객등급;

  select 고객등급, max(사용금액) from card group by 고객등급 having 고객등급 = 'vip' or 고객등급 = '패밀리';

  ```

- 중요한 IF / CASE 문법

  - if(조건식, 참일때 값, 거짓일때 값)

  ```SQL
  select 사용금액, if(사용금액 > 200000,'우수','거지') as 등급 from card order by 사용금액;
  ```

  - CASE
    - CASE WHEN 조건식 THEN ~~~ END

  ```SQL
  select 사용금액,
  case
    when 사용금액 >= 200000 then '우수'
    when 사용금액 >= 100000 and 사용금액 < 200000 then '준수'
    when 사용금액 < 100000 then '미약'
  end as 평가 from card order by 사용금액;

  -- 위의 코드 최적화
  select 사용금액,
  case
    when 사용금액 >= 200000 then '우수'
    when 사용금액 >= 100000 then '준수'
    else '미약'
  end as 평가 from card order by 사용금액;

  -- 문제
  select sum(
  case
    when 고객등급 = 'vip' then 3
    when 고객등급 = '로열' then 2
    else 1
  end
  ) from card;
  ```
