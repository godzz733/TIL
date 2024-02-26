function solution(a, b, n) {
  var answer = 0;
  while (n >= a) {
    answer += Math.floor(n / a) * b;
    n = (n % a) + Math.floor(n / a) * b;
  }
  return answer;
}
