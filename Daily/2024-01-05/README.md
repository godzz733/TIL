# 회고

### 2024-01-05 (금)

- 오늘은 9시 ~ 6시 아르바이트로 인해 공부를 많이 못함

#### 순 공부시간

- 1시간

<br>

# 공부 목록

## 강의

### SQL

- 저장 프로시저 stored procedure 쓰면 간지남

  - 많이 쓰는 SQL문을 저장해서 사용 (함수형으로)
  - stored procedure은 같은 DB쓰는 모든 사람이 사용가능
  - 캐싱으로 성능 약간 상승

    ```SQL
    -- select * from card where 사용금액 > 25000; -- 기존

    DELIMITER $$ -- ;로 끝내는걸 $$로 바꿔줌
    CREATE PROCEDURE get_all()
    BEGIN
        SELECT * FROM card WHERE 사용금액 > 25000;
    end $$
    DELIMITER ; -- 다시 ;로 바꿔줌


    CALL get_all();
    ```

  - DELIMITER 는 왜 사용할까? -> 함수 안에서 쿼리문 짤 때 ; 에서 안끝나게 하도록 사용

  ```text
    저장 프로시저 내부에 사용하는 SQL문은 일반 SQL문이기때문에 세미콜론(;)으로 문장을 끝맺어야 한다.

    이 때, 저장 프로시저 작성이 완료되지 않았음에도 SQL문이 실행되는 위험을 막기 위해 구분자(;)를 다른 구분자로 바꿔주어야하는데 이 때 사용하는 명령어가 DELIMITER 이다.

    따라서 저장 프로시저 생성 전에 구분자(DELIMITER)를 $$ 으로 바꿔주고 프로시저 작성이 끝났을 때 END $$ 로 저장 프로시저의 끝을 알려준다.

    마지막으로 구분자를 원래대로 되돌리기 위해 구분자(DELIMITER)를 세미콜론(;)으로 바꿔준다.
  ```
