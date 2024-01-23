function solution(ingredient) {
  var answer = 0;
  var arr = [];
  var t = 0;
  ingredient.forEach(x => {
    arr.push(x);
    t = arr.length;
    if (x == 1 && t >= 4) {
      if (arr[t - 2] == 3 && arr[t - 3] == 2 && arr[t - 4] == 1) {
        for (let i = 0; i < 4; i++) {
          arr.pop();
        }
        answer++;
      }
    }
  });
  return answer;
}

solution([2, 1, 1, 2, 3, 1, 2, 3, 1]);
