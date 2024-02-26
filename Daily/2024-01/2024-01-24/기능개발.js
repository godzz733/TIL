function solution(progresses, speeds) {
  var answer = [];
  let arr = [];
  let t;
  for (let i = progresses.length - 1; i >= 0; i--) {
    t = (100 - progresses[i]) % speeds[i] ? 1 : 0;
    t += Math.floor((100 - progresses[i]) / speeds[i]);
    arr.push(t);
  }
  let now = 0;
  let tem;
  while (arr.length) {
    tem = 1;
    now = arr.pop();
    while (arr.length && arr[arr.length - 1] <= now) {
      tem++;
      arr.pop();
    }
    answer.push(tem);
  }
  return answer;
}
