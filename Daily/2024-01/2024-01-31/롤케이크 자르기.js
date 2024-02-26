function solution(topping) {
  var answer = 0;
  var a = new Map();
  var b = new Map();
  topping.map(i => {
    if (a.get(i)) {
      a.set(i, a.get(i) + 1);
    } else {
      a.set(i, 1);
    }
  });
  topping.map(i => {
    if (!b.get(i)) {
      b.set(i, 1);
    }
    if (a.get(i) == 1) {
      a.delete(i);
    } else {
      a.set(i, a.get(i) - 1);
    }
    if (a.size == b.size) answer++;
  });
  return answer;
}

solution([1, 2, 1, 3, 1, 4, 1, 2]); // 2
