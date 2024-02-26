const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [n, m] = input[0].split(" ").map(Number);
let arr = input.slice(1).map(e => {
  return e.split(" ").map(Number);
});
// let n = 5,
//   m = 7;
// let arr = [
//   [0, 0, 0, 0, 0, 0, 0],
//   [0, 2, 4, 5, 3, 0, 0],
//   [0, 3, 0, 2, 5, 2, 0],
//   [0, 7, 6, 2, 4, 0, 0],
//   [0, 0, 0, 0, 0, 0, 0],
// ];

class Queue {
  constructor() {
    this.store = [];
    this.front = 0;
    this.rear = 0;
  }

  push(x) {
    this.store[this.rear++] = x;
  }

  pop() {
    return this.store[this.front++];
  }

  size() {
    return this.rear - this.front;
  }
}
const dx = [0, 0, 1, -1],
  dy = [1, -1, 0, 0];

const find_ans = (x, y, v) => {
  if (v[x][y] == 1 || arr[x][y] == 0) return false;
  let q = new Queue();
  q.push([x, y]);
  v[x][y] = 1;
  while (q.size() != 0) {
    let [x, y] = q.pop();
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i],
        ny = y + dy[i];
      if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
      if (v[nx][ny] == 1 || arr[nx][ny] == 0) continue;
      q.push([nx, ny]);
      v[nx][ny] = 1;
    }
  }
  return true;
};

let q = new Queue();

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (arr[i][j]) {
      q.push([i, j, arr[i][j]]);
    }
  }
}
let ans = 0;
while (true) {
  ans++;
  let t = 0;
  let v = new Array(n).fill(0).map(() => new Array(m).fill(0));
  let tarr = [];
  while (q.size()) {
    let [x, y, cnt] = q.pop();
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i],
        ny = y + dy[i];
      if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
      if (arr[nx][ny] == 0) {
        cnt--;
      }
    }
    if (cnt > 0) {
      tarr.push([x, y, cnt]);
    }
  }
  arr = new Array(n).fill(0).map(() => new Array(m).fill(0));
  for (let i = 0; i < tarr.length; i++) {
    let [x, y, cnt] = tarr[i];
    arr[x][y] = cnt;
    q.push([x, y, cnt]);
  }
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (find_ans(i, j, v)) {
        t++;
      }
    }
  }
  if (t >= 2) {
    console.log(ans);
    break;
  }
  if (t == 0) {
    console.log(0);
    break;
  }
}
