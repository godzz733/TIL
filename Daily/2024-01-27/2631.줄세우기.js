const fs = require("fs");
var arr = fs.readFileSync("./dev/stdin").toString().split("\n").map(Number);
var n = arr.shift();
var dp = new Array(n + 1).fill(1);
for (var i = 1; i < n; i++) {
  for (var j = 0; j < i; j++) {
    if (arr[i] > arr[j] && dp[i] < dp[j] + 1) {
      dp[i] = dp[j] + 1;
    }
  }
}
var ans = 0;
for (var i = 0; i < n; i++) {
  if (ans < dp[i]) {
    ans = dp[i];
  }
}
console.log(n - ans);
