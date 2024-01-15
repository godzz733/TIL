# 회고

### 2024-01-15 (월)

#### 순 공부시간

- 3시간

- SQL 강의 완료

<br>

# 공부 목록

## 강의

### SQL

- index 개념정리
  - primary key는 자동 index 생성, 나머지는 직접 생성해야함
  - B+ tree 사용
  - 미리 특정 컬럼을 index로 만들어서 정렬해 둔다음에 그걸 이진 탐색으로 찾고 그거에 맞는 index를 가진 행을 찾아서 출력하는거임
  - index를 만들고 저장하는 용량, 시간 등등이 손해, 단 검색이 매우 빠르므로 이득임
- index 만들기 / 성능평가

  - index 생성법

  ```SQL
  -- 단일 index 생성
  CREATE INDEX 인덱스이름작명 ON 테이블명 (컬럼명);

  -- 다중 컬럼 index 생성
  CREATE INDEX 인덱스이름작명 ON 테이블명 (컬럼명1, 컬럼명2);
  ```

  - 다중 컬럼 index -> where문에서 두개 이상의 조건을 같이 쓸 때 성능이 좋아짐
  - 다중 컬럼 index는 순서도 중요함
  - ex)
    ```SQL
    --(name, age) 를 다중 컬럼 index로 쓸 때
    -- name을 1순위, age를 2순위로 쓰면
    where name = ? and age = ? -> 인덱스 사용
    where name = ? -> 인덱스 사용
    where age = ? -> 인덱스 사용못함
    -- 이렇게 되므로 순서가 중요
    ```
  - 단, 특정 컬럼을 특별하게 많이 조회하는게 아니면, cardinallity가 높은거(중복이 많이 않은 컬럼)를 우선순위로 하면 됨

- 진짜 검색기능은 Full Text search

  - 생성법 -> CREATE FULLTEXT INDEX 작명 on 테이블명(컬럼명)
  - full text index 란 복잡한 문장 같은 걸 검색할 떄 사용하고 inverted index 이고 단어를 소자 별로 쪼개서 저장하는 거임 (elastic search랑 비슷 하다고 생각)
  - 영어는 stop word(is, are, the) 등등 의미 없는 단어는 안만듬
  - 검색시 정확도가 높은 걸 위에 보여 줌
  - select \* from library where match(컬럼명) against(찾을 단어);
    1. 두 글자 이하는 검색 안됨 (설정을 바꿔야 함)
    2. 기본적으로 natural language mode 임 (the 같은 단어는 빼고 검색)
    3. 그래서 한글에서는 boolean mode 를 사용하면 편함 (밑에는 boolean mode 기능)
       1. \*은 like의 % 기능 -> '부동산\*' in boolean mode -> 부동산뒤에 어떤게 있어도 됨
       2. 띄어쓰기는 OR
       3. - 는 필수 -> +를 쓰면 그 단어가 무조건 포함되어야 함
       4. - 는 not -> -붙은거는 없어야 함
  - MYSQL에서 ngram parser
  - CREATE FULLTEXT INDEX 작명 on 테이블명(컬럼명) with parser ngram
  - ngram parser는 기존의 fulltext index가 띄어쓰기를 기준으로 index를 생성하는 것과 다르게 띄어쓰기가 없는 언어를 사용할 때 사용
  - 예를들어 '주식 투자' 라는 단어는 -> 주식,식투,투자 이렇게 index를 만듬(글자수는 조절가능)

  ```SQL
  -- CREATE FULLTEXT INDEX library_서명_IDX ON index_test.library (서명); 생성법
  -- CREATE FULLTEXT INDEX 작명 on 테이블명(컬럼명)

  -- CREATE FULLTEXT INDEX 작명 on 테이블명(컬럼명) with parser ngram

  select * from library where match(컬럼명) against(찾을 단어);

  select * from library where match(서명) against('부동산');

  select * from library where match(서명) against('부동산' in natural mode);

  select * from library where match(서명) against('부동산*' in boolean mode); -- 부동산 뒤에 딴거 있어도 검색

  select * from library where match(서명) against('부동산 종이접기' in boolean mode); -- 부동산 or 종이접기

  select * from library where match(서명) against('+부동산 +빅데이터' in boolean mode); -- +를 쓰면 그 단어가 무조건 포함되어야 함

  select * from library where match(서명) against('-부동산 +빅데이터' in boolean mode); -- -를 쓰면 그 단어가 무조건 포함되지 않아야 함

  ```

- 돈 다루다가 큰일나기 싫으면 Transaction

  - start transaction; 뒤에 commit or rollback

  ```SQL
  start transaction;

  insert into books (bookName,bookPrice,bookType) value ('책1',10,'소설');
  insert into books (bookName,bookPrice,bookType) value ('책2',10,'소설');

  commit; -- -> transaction을 실행시킴
  rollback; -- -> transaction을 취소시킴

  select * from books b ;
  ```

  - 그러면 SQL문으로 쿼리가 실패하면 rollback 시키는 법 -> 실제로는 ORM으로 함

  ```SQL
  DROP PROCEDURE IF EXISTS test.transaction_test;
  DELIMITER $$
  CREATE PROCEDURE test.transaction_test()
  BEGIN


    DECLARE EXIT handler FOR SQLEXCEPTION -- -> 먼저 이렇게 써줌
    BEGIN
      ROLLBACK; -- -> 그럼 밑에있는 쿼리 문이 실행하다가 오류가 생기면 여기 있는 쿼리문을 실행시킴
    END;

    START TRANSACTION; -- -> 실제로는 여기부터 읽다가 오류 생기면 위의 쿼리 실행
      INSERT INTO ~~~~;
      INSERT INTO ~~~~:
    COMMIT;

  END$$
  DELIMITER ;
  ```

- Trigger 사용하기

  - INSERT UPDATE DELETE 하기 전에 자동으로 실행하는 코드
  - 쓰는이유
    - 데이터를 다른 테이블에 반영하고 싶을 때
    - 데이터 넣기 전에 데이터를 깔끔하게 정제하고 싶을 때
    - 테이블 변경기록 (로그)를 다른 테이블에 저장해두고 싶을 때
    - 테이블의 통계를 다른 테이블에 저장해두고 싶을 때
  - 사용법

  ```SQL

  DROP TRIGGER IF EXISTS counterup;
  DELIMITER $$
  CREATE TRIGGER counterup(trigger 이름)
  AFTER(after, before 가능, 실행시점임) INSERT(update, insert, delete 가능) ON product(어떤 테이블에서 쿼리가 날라오는지)
  FOR EACH ROW (모든 행에 대해 수행)
  BEGIN

    update counter set 상품개수 = 상품개수 + 1 where 자료 = '상품';

  END $$
  DELIMITER ;

  -- 실제 예시
  insert into product values('TV',3000);

  -- 이떄 product에 상품이 하나 추가되면 counter의 상품개수에 +1을 해주고 싶음

  DROP TRIGGER IF EXISTS counterup;
  DELIMITER $$
  CREATE TRIGGER counterup
  AFTER INSERT ON product
  FOR EACH ROW
  BEGIN

    update counter set 상품개수 = 상품개수 + 1 where 자료 = '상품';

  END $$
  DELIMITER ;

  insert into product values('TV',3000); -- 이제는 자동으로 상품개수 + 1 됨
  ```

  - NEW, OLD 문법 -> new = 새로 만들어질 값, old = 변경 전 값

  ```SQL
  DROP TRIGGER IF EXISTS counterup;
  DELIMITER $$
  CREATE TRIGGER counterup
  before insert ON product
  FOR EACH ROW
  BEGIN

    if new.가격 < 0 then
      set new.가격 = 1000;
    end if;

  END $$
  DELIMITER ;
  ```
