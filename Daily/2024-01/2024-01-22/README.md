# 회고

### 2024-01-22 (월)

#### 순 공부시간

- 4시간

<br>

# 공부 목록

## 알고리즘

|                              제목                              |  티어  |      분류      |                                          링크                                          |
| :------------------------------------------------------------: | :----: | :------------: | :------------------------------------------------------------------------------------: |
| 세상에는 많은 유튜버가 있고, 그중에서 버츄얼 유튜버도 존재한다 | 실버 1 |   해시, 구현   |                        (https://www.acmicpc.net/problem/29754)                         |
|                 Twitch Plays VIIIbit Explorer                  | 골드 5 |      구현      |                        (https://www.acmicpc.net/problem/25319)                         |
|                      가장 많이 받은 선물                       | 레벨 1 | 많은 조건 분기 | (https://school.programmers.co.kr/learn/courses/30/lessons/258712?language=javascript) |

## 강의

### Flutter

- ElevatedButton

```dart
Container(
  width: 200,
  height: 70,
  margin: EdgeInsets.all(32),
  child: ElevatedButton(
      onPressed: () {
        // 클릭 햇을 때 동작할 액션
        print('버튼이 클릭 되었습니다');
      },
      style: ElevatedButton.styleFrom(
          primary: Colors.amber, // 배경 색
          onPrimary: Colors.blue, // 글씨 색
          elevation: 5 // 그림자
          ),
      child: Text('눌러보세요')),
)
```

- ListView
  - 리스트 목록을 나타냄
  - ListView.builder 로 사용
  - itemCount가 나타낼 list 목록의 총 수

```dart
class _MainScreenState extends State<MainScreen> {
  List lstHello = ['Context1','Context2','Context3','Context4'];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('MainAppBar'),
        ),
        body: ListView.builder(
          itemBuilder: (context, index) {
            return ListTile(
              title: Text('${lstHello[index]}'),
              subtitle: Text('SubTitle $index'),
            );
          },
          itemCount: lstHello.length,
        ));
  }
}
```

- TextField (입력필드)

```dart
class _MainScreenState extends State<MainScreen> {
  List lstHello = ['Context1', 'Context2', 'Context3', 'Context4'];
  TextEditingController idController = TextEditingController();
  String msg = '업데이트 테스트';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('MainAppBar'),
        ),
        body: Column(
          children: [
            TextField(
              controller: idController,
              decoration: InputDecoration(labelText: '아이디를 입력해주세요'),
            ),
            ElevatedButton(
                onPressed: () {
                  setState(() {
                    msg = idController.text.toString();
                  });
                },
                child: Text('아이디 입력 가져옴')),
            Text(
              msg,
              style: TextStyle(fontSize: 30),
            )
          ],
        ));
  }
}
```

- Value Notifier

  - setState안쓰고 상태관리

  ```dart
  class _MainScreenState extends State<MainScreen> {
    List lstHello = ['Context1', 'Context2', 'Context3', 'Context4'];
    TextEditingController idController = TextEditingController();
    ValueNotifier<int> counter = ValueNotifier<int>(0);
    String msg = '업데이트 테스트';

    @override
    Widget build(BuildContext context) {
      return Scaffold(
          appBar: AppBar(
            title: const Text('MainAppBar'),
          ),
          body: Column(
            children: [
              TextField(
                controller: idController,
                decoration: InputDecoration(labelText: '아이디를 입력해주세요'),
              ),
              ElevatedButton(
                  onPressed: () {
                    counter.value += 1;
                  },
                  child: Text('아이디 입력 가져옴')),
              ValueListenableBuilder<int>(valueListenable: counter, builder: (context, value, child) {
                return Text('Count : $value');
              },),
              Text(
                msg,
                style: TextStyle(fontSize: 30),
              )
            ],
          ));
    }
  }
  ```

  - ValueNotifier를 쓰면 직접적으로 값을 가져올 수 있음
  - ValueListenableBuilder 안에서는 ValueNotifier의 값을 value로 가져올 수 있음
  - 잘 안씀

- Navigator를 활용한 화면 간 이동 및 오브젝트 전달

  - 버튼 클릭으로 이동하기

  ```dart
  TextButton(onPressed: () {
    Navigator.pushNamed(context, '/sub');
  }, child: Text('클릭해서 서브 화면으로 이동'))
  ```

  - 이동 시 오브젝트 전달 하는 법
  - main.dart

  ```dart
  class MyApp extends StatelessWidget {
    const MyApp({super.key});

    // This widget is the root of your application.
    @override
    Widget build(BuildContext context) {
      return MaterialApp(
        title: 'Flutter Demo',
        initialRoute: '/',
        routes: {
          '/' : (context) => SplashScreen(),
          '/main' : (context) => MainScreen(),
        },
  			// 오브젝트 받으려면 여기에 route 정의
        onGenerateRoute: (settings) {
          if (settings.name == '/sub') {
  					// 넘겨 받을 데이터가 settings안에 arguments 안에 있음
            String msg = settings.arguments as String;
            return MaterialPageRoute(builder: (context) {
              return SubScreen(msg:msg);
            },);
          }
        },
      );
    }
  }
  ```

  - main_screen.dart

  ```dart
  TextButton(onPressed: () {
    Navigator.pushNamed(context, '/sub',arguments: 'hello'); // arguments 가 넘길 오브젝
  }, child: Text('클릭해서 서브 화면으로 이동'))
  ```

  - sub_screen.dart

  ```dart
  class SubScreen extends StatelessWidget {
    String msg; // 미리 받을 곳을 선언
    SubScreen({super.key, required this.msg}); // required로 파라미터 설정

    @override
    Widget build(BuildContext context) {
      return Scaffold(
        appBar: AppBar(
          title: Text('서브 위젯'),
        ),
        body: Column(children: [
          Center(child: Text('서브화면 입니다. $msg'),),
          TextButton(onPressed: () {
            Navigator.pop(context); // pop은 뒤로가기
          }, child: Text('뒤로가기'))
        ],),
      );
    }
  }
  ```

- 네비게이션 바, 탭 바, 드로어 사용법 (appbar가 네이게이션 바임)

  - Appbar

  ```dart
  appBar: AppBar(
          automaticallyImplyLeading: false, // 기본 뒤로가기 끄기
          leading: TextButton(onPressed: () { // 왼쪽 영역
            Navigator.pop(context);
          },child: Text(
            '뒤로가기'
          ,style: TextStyle(color: Colors.blue),)),
          title: Text('서브 위젯'),
          actions: [ // 오른쪽 영역
            Icon(Icons.ac_unit_outlined)
          ],
        ),
  ```

  - TabBar

  ```dart
  class SubScreen extends StatelessWidget {
    String msg;

    SubScreen({super.key, required this.msg});

    @override
    Widget build(BuildContext context) {
      return DefaultTabController(
        length: 3,
        child: Scaffold(
            appBar: AppBar(
              automaticallyImplyLeading: false,
              leading: TextButton(
                  onPressed: () {
                    Navigator.pop(context);
                  },
                  child: Text(
                    '뒤로가기',
                    style: TextStyle(color: Colors.blue),
                  )),
              title: Text('서브 위젯'),
              actions: [Icon(Icons.ac_unit_outlined)],
              bottom: TabBar(tabs: [ // 누르면 탭바 이동
                Tab(text: 'Tab 1',),
                Tab(text: 'Tab 2',),
                Tab(text: 'Tab 3',)
              ],),
            ),
            body: TabBarView( // 탭바의 내용을 보여주는 곳
              children: [
                Center(child: Text('Tab 1 Content'),),
                Center(child: Text('Tab 2 Content'),),
                Center(child: Text('Tab 3 Content'),)
              ],

            )),
      );
    }
  }
  ```

  - TabBar 를 쓰려면 DefaultTabController를 최상위에 감싸 줘야함
  - 드로워 (body의 형제 위치에 넣으면 됨)

  ```dart
  drawer: Drawer(child: ListView(children: [
          DrawerHeader(child: Text('헤더 영역')),
          ListTile(title: Text('홈 화면'), onTap: () {

          },),
          ListTile(title: Text('메인 화면'), onTap: () {

          },),
          ListTile(title: Text('서브 화면'), onTap: () {

          },)
        ],),),
  ```
