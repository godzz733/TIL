function solution(s) {
  var a = s.split(" ");
  return Math.min(...a) + " " + Math.max(...a);
}
