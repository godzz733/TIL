# 회고

### 2024-01-10 (수)

#### 순 공부시간

- 2시간

<br>

# 공부 목록

## 알고리즘

|    제목     |  티어  |      분류      |                  링크                   |
| :---------: | :----: | :------------: | :-------------------------------------: |
| SASA 마니또 | 실버 1 | 구현, 조건분기 | (https://www.acmicpc.net/problem/30505) |

## 강의

### SQL

- 날짜 & 시간데이터 다루기

  - 먼저 데이터 형식으로 datetime 사용하면 됨
  - 이때 datetime(6) 이런식으로 1~6까지의 숫자를 넣으면 초 단위 뒤에 몇초까지 쓸지 설정
  - ex) datetime(6) 는 나노초까지 저장
  - datetime은 그냥 문자열로 넣으면 됨 ex) '2023-10-22 10:20:33' (년-월-일 시:분:초)
  - 날짜 데이터 출력 형식 바꾸기 -> date_format이라 써주고 (바꿀 시간, 바꿀 형식)
  - %y,%m,%d,%h,%i,%s = 년,월,일,시,분,초

  ```SQL
  select * from blog where 발행일 > '2022-03-09 23:24:25';

  -- 2022-03-09 날짜 필터링
  select * from blog where 발행일 > '2022-03-10 00:00:00'
  and 발행일 < '2022-03-11 00:00:00';

  -- 2022-03-10부터 오늘까지 필터링
  select * from blog where 발행일 > '2022-03-10 00:00:00'
  and 발행일 < now();

  -- 날짜, 시간 포맷팅
  -- date_format이라 써주고 (바꿀 시간, 바꿀 형식)
  select date_format(now(),'%Y %m %d %h %i %s')
  ```

- procedure와 비슷한 function 문법

  - fuction은 긴 쿼리문을 저장하는 procedure과 다르게 계산기능을 위해 사용
  - MYSQL에서는 function 안에서 select문 불가능, select into는 가능
  - function 특징
    1. call 없이 사용가능
    2. 파라미터 가능
    3. 안에 return 필수
    4. return할 자료의 타입 기입필수 (returns는 맨위에 작성)
    5. DETERMINISTIC 기입필요 (상황따라 다름)
       1. 항상 같은 값을 return하면 DETERMINISTIC
       2. SQL문법을 안쓰면 NO SQL
       3. SELECT쓰면 READS SQL DATA
       4. INSERT DELETE 쓰면 MODIFIES SQL DATA
    - 실제로 엄격한 제한은 없으나 SQL실행시 추론할때 저걸 보고 하므로 성능에 영향이 있을수도 있음

  ```SQL
  CREATE FUCTION 함수이름()
  RETURNS INT
  DETERMINISTIC
  BEGIN
    RETURN 10
  END
  함수이름()
  ```

  - 달러로 변환 예제

  ```SQL
  delimiter $$
  create function dollar(price int)
  returns INT
  deterministic
  begin
    return price / 1300;
  end
  $$
  delimiter ;

  select dollar(사용금액) from card;
  ```

  - 결제횟수가 10 이상시 존댓말 예제

  ```SQL
  drop function if exists hello;

  delimiter $$
  create function hello(chance int)
  returns varchar(100)
  deterministic
  begin
    return if(chance >=10, '안녕하세요', '안녕');
  end
  $$
  delimiter ;

  select hello(결제횟수) from card;
  ```

- procedure, function 안에서 쓸 수 있는 IF

  - 조건에 따라 다른 select문 사용하고 싶을 때

  ```SQL
  drop procedure if exists test;
  delimiter $$
  create function test()
  begin
    if 조건식 1 then
      실행할 sql 쿼리문~~;
    elseif 조건식 2 then
      실행할 sql 쿼리문~~;
    else
      실행할 sql 쿼리문~~;
    end if;

  end
  $$
  delimiter ;

  ```

  - 예제 1

  ```SQL
  drop procedure if exists test;
  delimiter $$
  create procedure test()
  begin
    if (select sum(사용금액) from card) > 500000 then
      select '잘했어요';
    else
      select '분발하세요';
    end if;

  end
  $$
  delimiter ;

  call test()
  ```

  - 예제 2

  ```SQL
  drop function if exists test;
  delimiter $$
  create function test(age int)
  returns varchar(100)
  deterministic
  begin
    if age < 20 then
      return '미성년자입니다';
    else
      return '성인입니다';
    end if;
  end
  $$
  delimiter ;

  select test(19);
  ```
