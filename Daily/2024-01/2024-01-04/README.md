# 회고

### 2024-01-04 (목)

#### 순 공부시간

- 2시간

<br>

# 공부 목록

## 강의

### SQL

- 테이블과 컬럼 생성할 때 SQL 써야 약간 멋있음 (DDL)

  ```SQL
  create database 테스트; -- 테이블 생성
  drop database 테스트; -- 테이블 삭제

  create table 테스트.new_table (
      id int,
      name varchar(100) default '홍길동', -- 값을 안넣을 때 기본값
      age int
  ); -- 테이블 생성

  drop table 테스트.new_table; -- 테이블 삭제

  alter table 테스트.new_table add 컬럼명 varchar(255); -- 컬럼추가
  alter table 테스트.new_table modify column 컬럼명 int; -- 컬럼수정, 이미 데이터가 들어가있을떄는 불가능
  alter table new_table drop column 컬럼명; -- 컬럼삭제

  ```

- 컬럼에 안전하게 제약 (Constraints) 주기

  ```SQL
  create table test.new_table (
  id int not null, -- null 금지
  name varchar(100) unique, -- 중복 허용안함
  age int check(age > 0), -- 들어올 데이터 값 검사
  id int primary key, -- PK, pk는 not null + unique 자동 적용
  id int auto_increment -- 자동으로 1씩 증가
  CONSTRAINT 제약조건작명 PRIMARY KEY (id),
  CONSTRAINT 제약조건작명2 CHECK(나이 > 10) -- 이렇게 작명도 가능, 오류시 작명때문에 오류 낫다고 명시해줌
  )
  ```

- Foreign Key

  ```SQL
  CREATE TABLE test.program (
  id INT PRIMARY KEY,
  프로그램 VARCHAR(100),
  가격 INT,
  강사id INT references test.teacher(id) -- FK 등록
  );

  CREATE TABLE test.teacher (
  id INT PRIMARY KEY,
  강사 VARCHAR(100),
  출신대학 VARCHAR(100)
  );

  -- 이미 테이블 생성을 햇다면
  ALTER TABLE test.program  ADD
  CONSTRAINT FK FOREIGN KEY (강사id) REFERENCES test.teacher(id)
  ```

- 테이블 2개 합쳐서 출력은 INNER JOIN

  - inner join 뒤에는 where 못씀 -> on 써야함

    ```SQL
    select * from program p, teacher t; -- cross join 과 같음
    select * from program inner join teacher t ; -- 두개는 같은 결과를 줌

    select * from program p , teacher t where p.강사id = t.id;

    select * from program p inner join teacher t
    on p.강사id = t.id
    ;
    ```

  - 테이블 3개 이상 붙이기
    ```SQL
    SELECT *
    FROM 테이블1
    INNER JOIN 테이블2 ON 조건1
    INNER JOIN 테이블3 ON 조건2
    ```

- LEFT, RIGHT JOIN

  - left join(left outer join) -> inner join + 왼쪽 테이블 전체 출력
  - right join -> inner join + 오른쪽 테이블 전체 출력
  - 테이블 간의 접점이 없는 행들을 출력하고 싶을 때 사용

  ```SQL
  select * from program p left join teacher t
  on p.강사id = t.id;
  select * from program p right join teacher t
  on p.강사id = t.id;

  select * from program p right join teacher t
  on p.강사id = t.id where p.강사id is null; -- 값이 없는거만 찾기
  ```

- 데이터 넣거나 복사하려면 INSERT

  ```SQL
  insert into ins_1 (id,name,price) values (2,'ㅈㅈ',500); -- 모든 필드에 값을 넣을경우 (id,name,price) 이건 생략가능
  insert into ins (name,price) values ('불고기',1000); -- 넣고싶은 필드에만 값 넣기, 나머지는 null로 들어감
  insert into ins (name,price) values ('치즈',(select price from ins_1 where id =1)); -- 값으로 서브쿼리 가능
  insert into ins select * from ins_1; -- 이렇게 복제 가능

  create table 새로운테이블명 select * from 기존테이블명; -- 새 테이블 생성 및 복사기능
  create temporary table 새로운테이블명 select * from 기존테이블명; -- 임시 테이블 생성 및 복사기능, 재접속시 삭제
  ```

- 수정 삭제는 UPDATE / DELETE

  - 수정 -> update 테이블명 set 컬럼명=바꿀값 where 조건식
  - where없으면 모든 행의 데이터가 다 바뀜
  - 삭제 -> delete from 테이블명 where 조건식
  - where없으면 모든 행 다 삭제
  - FK로 사용죽이면 삭제 불가능
  - join한 테이블에 update,delete 사용가능
  - UPDATE A INNER JOIN B
    ON 쪼인조건
    SET 수정할내용
    WHERE 조건식
    -> 이러면
  - DELETE A (이때 여기에 써주는 테이블의 데이터가 삭제됨)
    FROM A INNER JOIN B
    ON 쪼인조건

    WHERE 조건식
    -> 즉, 위에서는 A 테이블 데이터가 삭제되고 B또는 A,B 이렇게도 가능

  ```SQL
  update ins set price = 1200 where id = 1; -- price를 1200으로 변경
  update ins set price = 1200, name='부대' where id = 1; -- 한번에 여러개도 가능
  update ins set price = price + 100 where id = 1; -- 사칙연산 가능

  delete from ins where id =1; -- 삭제

  -- join한 테이블에 update 사용
  update ins inner join ins_1 on ins.id = ins_1.id set ins_1.price = 9999 where ins_1.price = 500;
  ```

- SELECT 결과들을 합치려면 UNION

  - select문 여러개를 하나의 결과로 합쳐보기
  - 중복 제거해줌 -> 중복제거 싫으면 union all 사용
  - 컬럼 갯수가 맞아야함, 컬럼 종류가 같을 필요는 없음
    ```SQL
    select name,price from ins
    union
    select 프로그램,가격 from program; -- 중복 없음
    select name,price from ins
    union ALL
    select 프로그램,가격 from program; -- 중복 있음
    ```

- table 대신 view 쓰는 이유
  - view는 가상의 테이블임, 임시 저장이라고 생각, 실제로 뭔가 만드는게 아님
  1. 복잡하게 JOIN 해놓은 테이블들을 하나의 테이블 또는 view로 만들어두면 두고두고 재사용할 수 있어서 편리합니다.
  2. 근데 view는 실제 테이블이 아니라서 테이블만큼 하드용량을 많이 차지하지 않습니다.
  3. table에 컬럼변경이 필요할 때 view를 만들어서 먼저 실험해볼 수 있습니다.
  4. view 안에서 또 SELECT 해서 view를 만들 수도 있습니다. 너무 많은 중첩은 금지
  ```SQL
  CREATE VIEW 뷰이름 AS
  SELECT 컬럼1, 컬럼2, ...
  FROM 테이블명
  ```
