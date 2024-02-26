# 회고

### 2024-01-18 (목)

#### 순 공부시간

- 2시간

<br>

# 공부 목록

## 알고리즘

| 제목 |  티어  |     분류     |                  링크                  |
| :--: | :----: | :----------: | :------------------------------------: |
| 소트 | 골드 5 | 그리디, 정렬 | (https://www.acmicpc.net/problem/1083) |

### 소트 풀이

- 처음엔 무지성으로 버블정렬을 햇는데 그게 아니라 남은 S만큼 뒤에있는 최대 값을 앞으로 가져오는게 정답이다.

## 강의

### Dart

- 변수
  - String, int 등 원시 타입 → null 불가
  - var → 타입 추론 → 하지만 한번 추론된 타입은 바꿀 수 없음
  - dynamic → 타입 변경 가능 → 거의 사용 안함
  - ? → nullsafe = null 가능
  - late → 늦게 선언 가능 → 즉, 처음에는 null로 선언 가능 이때 nullsafe와의 차이점은 없지만 null이 가능하다는걸 명시적으로 나타낸다고 생각하면 됨
    - **_late키워드는 값의 초기화를 뒤로 미루지만, 개발자가 null을 실수로 사용하는것을 막아준다._**
    - nullable을 사용하면 개발자가 그 값이 null이어도 괜찮다고 느낄 수 있기 때문임
    - late는 초기화를 뒤로 미루지만 초기화가 안되면 에러를 내보내기 때문에 명시적으로 더 적절
  - ?? → 자바스크립트의 nullish 생각하면 됨
  - final - 값이 한번 할당되면 재 할당 불가, 선언 후 할당 가능
  - const - 재할당 불가능 같지만 선언과 동시에 값을 할당해야함, 즉 컴파일 시점에서 값이 결정되어야 함 → 그렇기 때문에 final보다 성능이 좋음
  - 산술 연산자
    - +,-,\*,/,%, ~/(몫)
  - 조건문, 반복문 = 자바와 동일
  - switch, case 문 있음

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

	final int age = 10;
  age = 20; // 재 할당 불가능
  final int age2;
  age2 = 10; // 선언 후 할당 가능

  const int age3 = 10;
  age3 = 20; // 재 할당 불가능
  const int age4; // 선언 후 할당 불가능, 반드시 선언과 동시에 할당

	int mok = 10 ~/ 3 // 몫이므로 3

	bool result = (true || false) // or
	bool result1 = (true && false) // and
	bool result1 = !true // not
	String ageStatus = age >= 18 ? '성인' : '미성년자';

	// switch case
	String grade = 'A';
	  switch (grade) {
	    case 'A':
	      print('Excellent grade of A');
	      break;
	    case 'B':
	      print('Very good!');
	      break;
	    case 'C':
	      print('Good enough. But work harder');
	      break;
	    case 'F':
	      print('You have failed');
	      break;
	    default:
	      print('Invalid grade');
	  }
}
```

- List, Map

  ```dart
  List<int> arr = [];
  List<int> arr2 = [1, 2, 3, 4, 5];

  Map<String, int> map = {"a": 1, "b": 2, "c": 3};
  void main() {
    arr.add(3);
    print(arr[0]);
    print(arr.length);
    arr2.removeAt(2);

    map["d"] = 4;
    print(map["d"]);

    map.forEach((key, value) { print("$key : $value");})
  }
  ```

- positional, named parameters

  - positional은 원래 아는 함수 파라미터
  - named는 기본값을 반드시 주고 이름으로 파라미터를 넣음
  - named에서 기본값을 안주고 required를 붙이면 반드시 이 파라미터를 넣어야 하므로 이제 기본값이 필요없음

  ```dart
  void main() {
    test('john', 25);
    test2(name: 'john', age: 25);
    test3(name: 'john');
  }

  // positional parameters
  void test(String name, int age) {
    print("name: $name, age: $age");
  }

  // named parameters
  void test2({String name = 'john', int age = 25}) {
    print("name: $name, age: $age");
  }

  // named parameters with required
  void test3({required String name}) {
    print("name: $name");
  }
  ```

- 클래스와 상속

  ```dart
  void main() {
    Person p1 = new Person("john", 20);
    p1.printInfo();
    Man m1 = new Man("eiden", 20);
    m1.printInfo();
    // var로 추론 가능
    var m2 = new Man('jon', 30);
  }

  class Person {
    String name;
    int age;
    Person(this.name, this.age);
    void printInfo() {
      print("${this.name}---${this.age}");
    }
  }

  class Man extends Person {
    // 상속받은 부모의 생성자를 사용할 수 있다.
    Man(String name, int age) : super(name, age);

    @override
    void printInfo() {
      super.printInfo(); // 상속받은 부모의 메소드를 사용할 수 있다.
      print("${this.name} 이름 ${this.age} 나이");
    }
  }
  ```

- 생성자와 선택적 매개변수

  ```dart
  void main() {
    var p1 = new Person();
    var p2 = new Person2('Bob', 20);
    var p3 = new Person3(name: 'Bob', age: 20);
    var p4 = new Person4(name: 'Bob', age: 20);
  }

  class Person {
    // 기본 생성자, 생략가능
    Person();
  }

  class Person2 {
    String name;
    int age;
    Person2(this.name, this.age);
  }

  class Person3 {
    String name;
    int age;
    Person3({this.name = 'john', this.age = 20});
  }

  class Person4 {
    String name;
    int age;
    Person4({required this.name, required this.age});
  }
  ```

- enum

  ```dart
  void main() {
    Color myColor = Color.red;

    if (myColor == Color.red) {
      print('Color is red');
    } else if (myColor == Color.green) {
      print('Color is green');
    } else if (myColor == Color.blue) {
      print('Color is blue');
    } else {
      print('Color is unknown');
    }

    print(Color.red.index); // 0
  }

  // enum 안의 값들은 소문자로, enum 안의 값들은 인덱스 0부터 부여됨
  enum Color { red, green, blue }
  ```

- Future와 await를 활용한 비동기 프로그래밍

  - Future - 비동기 작업의 결과 또는 완료 상태를 나타내는 객체

  ```dart
  void main() {
    playComputerGame();
  }

  Future<void> playComputerGame() async {
    startBoot();
    await startInternet();
    startGame();
  }

  void startBoot() {
    print('1. boot Comleted');
  }

  Future<void> startInternet() async {
    await Future.delayed(Duration(seconds: 3), () {
      print('2. Internet Comleted');
    });
    print('delay completed');
  }

  void startGame() {
    print('3. Game Comleted');
  }
  ```
