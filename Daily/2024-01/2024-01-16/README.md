# 회고

### 2024-01-16 (화)

#### 순 공부시간

- 2시간

<br>

# 공부 목록

## 알고리즘

|                  제목                   |  티어  |       분류       |                  링크                  |
| :-------------------------------------: | :----: | :--------------: | :------------------------------------: |
| 전국 대학생 프로그래밍 대회 동아리 연합 | 실버 5 |       구현       | (https://www.acmicpc.net/problem/5046) |
|                  암호                   | 골드 5 | 수학,해시,조합론 | (https://www.acmicpc.net/problem/1394) |

## 강의

### Dart

- 변수
  - String, int 등 원시 타입 → null 불가
  - var → 타입 추론 → 하지만 한번 추론된 타입은 바꿀 수 없음
  - dynamic → 타입 변경 가능 → 거의 사용 안함
  - ? → nullsafe = null 가능
  - late → 늦게 선언 가능 → 즉, 처음에는 null로 선언 가능 이때 nullsafe와의 차이점은 없지만 null이 가능하다는걸 명시적으로 나타낸다고 생각하면 됨
  - ?? → 자바스크립트의 nullish 생각하면 됨

```dart
late String name5; // null 가능

void main() {
  // null 불가능, 타입 변경 불가능
  String name = 'John';
  int age = 25;
  print('Hello $name');
  print('Hello ${age}');

  // null 불가능, 타입 추론 -> 추론이지 타입이 변경 가능한건 아님
  var name2 = 'John';

  dynamic name3 = 'John';
  name3 = 25;

  String? name4 = null;

  String nullish = name4 ?? 'John';
}
```
