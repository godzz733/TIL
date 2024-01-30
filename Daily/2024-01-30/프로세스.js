class Queue {
  constructor() {
    this.arr = new Array(100).fill(0);
    this.head = 0;
    this.tail = 0;
  }

  pop() {
    return this.arr[this.head++];
  }

  push(x) {
    this.arr[this.tail++] = x;
  }
}
function solution(priorities, location) {
  var answer = 0;
  var arr = [];
  var q = new Queue();
  for (let i = 0; i < priorities.length; i++) {
    q.push([priorities[i], i]);
  }
  for (let i = 0; i < priorities.length; i++) {
    arr.push(priorities[i]);
  }
  arr.sort((x, y) => {
    return y - x;
  });
  while (true) {
    let [t, tt] = q.pop();
    if (arr[0] == t) {
      arr.shift();
      answer++;
      if (tt == location) {
        return answer;
      }
    } else {
      q.push([t, tt]);
    }
  }
}

console.log(solution([2, 1, 3, 2], 2));
