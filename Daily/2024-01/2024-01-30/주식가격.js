function solution(prices) {
  var answer = new Array(prices.length).fill(0);
  var arr = [];
  for (let i = 0; i < prices.length; i++) {
    if (arr.length == 0) {
      arr.push([prices[i], i]);
    } else {
      while (arr.length > 0 && prices[i] < arr[arr.length - 1][0]) {
        answer[arr[arr.length - 1][1]] = i - arr[arr.length - 1][1];
        arr.pop();
      }
      arr.push([prices[i], i]);
    }
  }
  for (let i = 0; i < arr.length; i++) {
    answer[arr[i][1]] = arr[arr.length - 1][1] - arr[i][1];
  }
  return answer;
}

console.log(solution([1, 2, 3, 2, 3]));
