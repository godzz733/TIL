# 회고

### 2024-01-20 (토)

#### 순 공부시간

- 3시간

<br>

# 공부 목록

## 알고리즘

|   제목    |  티어  |     분류     |                  링크                  |
| :-------: | :----: | :----------: | :------------------------------------: |
| 머리 톡톡 | 골드 5 | 정수론, 수학 | (https://www.acmicpc.net/problem/1241) |

## 강의

### Flutter

- 자동 정렬 → Ctrl + Alt + L
- 코드 추천 → Alt + Enter
- Widget

  - 앱의 모든 구성요소, 화면에 그려지는 모든 것을 위젯으로 표현
  - 다양한 종류와 계층구조로 구성되어 있음

  ```dart
  class MainScreen extends StatelessWidget {
    const MainScreen({super.key});

    @override
    Widget build(BuildContext context) {
      return Scaffold(appBar:AppBar(title: Text('나의 첫 앱')),body: Text('안녕하세요'));
    }
  }
  ```

- Stateless Widget vs Stateful Widget

  - Stateless Widget
    - 상태가 없는 위젯 → 내부 데이터나 UI가 변하지 않음
  - Stateful Widget
    - 상태나 state를 바꿀 수 있음
  - 둘 다 존재하는 이유 → stateless widget이 성능이 좋고 명시적으로도 화면이 변하지 않는 상황같을 때 두 개를 적절히 쓰는게 좋음

  ```dart
  class MainScreen2 extends StatefulWidget {
    const MainScreen2({super.key});

    @override
    State<MainScreen2> createState() => _MainScreen2State();
  }

  class _MainScreen2State extends State<MainScreen2> {
    String msg = 'State change';

    // 최초에 한번 실행
    @override
    void initState() {
      // TODO: implement initState
      super.initState();

      Future.delayed(Duration(seconds: 3),(){
        setState(() {
          msg = 'changed Message';
        });
      },);
    }
    @override
    Widget build(BuildContext context) {
      return Scaffold(appBar:AppBar(title: Text('나의 첫 앱')),body: Text(msg));
    }
  }
  ```

- Route

  ```dart
  class MyApp extends StatelessWidget {
    const MyApp({super.key});

    // This widget is the root of your application.
    @override
    Widget build(BuildContext context) {
      return MaterialApp(
        title: 'Flutter Demo',
        initialRoute: '/', // 시작 화면
        routes: {
          '/' : (context) => SplashScreen(),
          '/main' : (context) => MainScreen(),
        },
      );
    }
  }
  ```

  ```dart
  class SplashScreen extends StatelessWidget {
    const SplashScreen({super.key});
    @override
    Widget build(BuildContext context) {
      Future.delayed(Duration(seconds: 2),() {
        Navigator.pushNamed(context, '/main');
      });
      return Scaffold(
        body: Center(
          child: Text('시작 화면'),
        ),
      );
    }
  }
  ```

  - 먼저 StatelessWidget은 initstate가 ㅇ벗으므로 그냥 build안에 써주면 됨
  - Navigator.pushNamed(context, '/main'); 이게 route 이동시키는 함수임

- 위젯 여러개 설명
  - Column, Row, Expanded
    - children 안에 넣고싶은 요소를 넣으면 됨
    - mainAxisAlignment (자기 기준 정렬(column이면 column인거임)
    - CrossAxisAlignment (자기 나머지 기준 정렬)
    - Expanded 는 flex 역할 (일정 크기만큼 차지) → flex는 안주면 자동으로 1이 부여되고 명시적으로 주면 그만큼 크기를 차지하는 거임
    - Children = 여러개 자식, child = 한개의 자식만 가능
  ```dart
  class _MainScreenState extends State<MainScreen> {
    @override
    Widget build(BuildContext context) {
      return Scaffold(
        appBar: AppBar(
          title: const Text('MainAppBar'),
        ),
        body: const Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('First'),
            Text('Second'),
            Text('Thrid'),
            Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [Text('First'), Text('Second'), Text('Thrid')],
            ),
            Row(children: [
              Expanded(flex:2,child: Text('First')),
              Expanded(child: Text('Second')),
              Expanded(child: Text('Third')),
            ],)
          ],
        ),
      );
    }
  }
  ```
  - Container, SizedBox
    - SizedBox는 Container에서 색이나 다른 요소는 못 바꾸고 width,height만 바꿀 수 있는거임
    - Container는 margin,pading,radius등 다양한 것들을 할 수 있다
  ```dart
  Container(
              child: Text('컨테이너'),
              width: 300,
              height: 300,
              alignment: Alignment.center,
              color: Colors.blue,
              margin: EdgeInsets.all(32),
              padding: EdgeInsets.only(left: 16),
            ),
  SizedBox(child: Text('사이즈박스'),
  height: 100,
  width: 100,)
  ```
  - Text,Image,Icon
    - Text
    - Image
      - pubspect.yaml에
      ```dart
      flutter:
        assets:
          - assets/
      ```
      추가하기
