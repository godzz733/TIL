late String name5;
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
