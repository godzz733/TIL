function solution(friends, gifts) {
  let dic = {};
  let l = friends.length;
  let arr = new Array(l).fill(0);
  friends.forEach(fr => {
    dic[fr] = [0, 0, {}];
    friends.forEach(f => {
      dic[fr][2][f] = 0;
    });
  });
  gifts.forEach(g => {
    let [a, b] = g.split(" ");
    dic[a][0]++;
    dic[b][1]++;
    dic[a][2][b]++;
  });

  for (let i = 0; i < l - 1; i++) {
    for (let j = i + 1; j < l; j++) {
      if (dic[friends[i]][2][friends[j]] || dic[friends[j]][2][friends[i]]) {
        let t = dic[friends[i]][2][friends[j]] - dic[friends[j]][2][friends[i]];
        if (t > 0) {
          arr[i]++;
        } else if (t < 0) {
          arr[j]++;
        } else {
          t = dic[friends[i]][0] - dic[friends[i]][1] - dic[friends[j]][0] + dic[friends[j]][1];
          if (t > 0) {
            arr[i]++;
          } else if (t < 0) {
            arr[j]++;
          }
        }
      } else {
        t = dic[friends[i]][0] - dic[friends[i]][1] - dic[friends[j]][0] + dic[friends[j]][1];
        if (t > 0) {
          arr[i]++;
        } else if (t < 0) {
          arr[j]++;
        }
      }
    }
  }
  return Math.max(...arr);
}
