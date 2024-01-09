# 회고

### 2024-01-09 (화)

#### 순 공부시간

- 1시간

<br>

# 공부 목록

## 강의

### SQL

- procedure에서 많이 쓰는 변수 문법

  - 변수 선언 법 -> set @작명 = 값;
  - 변수 사용법 @작명 (@까지 붙여서 써야함)
  - 서브쿼리를 할당 값으로 사용가능
  - procedure안에서는 declare 키워드로 변수선언 가능 -> DECLARE 변수명 데이터타입;
  - 이때 set = 전역변수(db종료시 제거), declare = 지역변수(함수 종료시 제거)

  ```SQL
  set @작명 = 값;

  set @name = 'john';
  set @age = 10;
  set @age = 20; -- 재 할당 가능
  set @age = @age + 1; -- 연산 가능

  select @name;
  select @age;


  drop procedure if exists mart.var_test;
  delimiter $$
  create procedure mart.var_test()
  begin
    declare 변수1 int;
    declare 변수2 int default 10; -- 기본값
    declare 변수3 varchar(100) default 'hello'; -- 문자
    set @변수4 = 123; -- 마찬가지로 set 사용가능
    select 변수3;
  end
  $$
  delimiter ;

  call mart.var_test()
  ```

- procedure 많이 만들기 싫으면 파라미터

  - 변수명 자료형 이렇게 쓰면 됨

  ```SQL
  drop procedure if exists mart.get_all;
  delimiter $$
  create procedure mart.get_all(price int, name varchar(100))
  begin
    select * from card where 사용금액 > price and 고객명 != name;
  end
  $$
  delimiter ;

  call mart.get_all(50000,'Amy')
  ```

  - out을 하려면 -> 이번엔 파라미터 자리에 out '변수명' '자료형' 을 적어주고 procedure안에서 변수명에 값을 넣어주면 그대로 전역으로 선언됨
  - 근데 out 하려면 function을 주로 씀

  ```SQL
  drop procedure if exists mart.get_age;

  delimiter $$
  create procedure mart.get_age(out price int)
  begin
    set price = 20;
  end
  $$
  delimiter ;

  call mart.get_age(@outage);
  select @outage;
  ```
