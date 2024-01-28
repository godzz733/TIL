const fs = require("fs");
var [n, ...arr] = fs.readFileSync("./dev/stdin").toString().split(/\s/).map(Number);
var dp = new Array(n + 1).fill(0);
for (let i = 0; i < n; i++) {
  dp[arr[i]] = Math.max(dp[arr[i] - 1] + 1, dp[arr[i]]);
}
console.log(n - Math.max(...dp));
