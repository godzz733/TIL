function solution(maps) {
  let n = maps.length,
    m = maps[0].length;
  let arr = [[0, 0, 0]];
  let x, y, t, nx, ny, cnt;
  let tarr = [0];
  let dx = [1, -1, 0, 0];
  let dy = [0, 0, 1, -1];
  while (tarr.length) {
    tarr = [];
    while (arr.length) {
      t = arr.pop();
      x = t[0];
      y = t[1];
      cnt = t[2];
      if (x == n - 1 && y == m - 1) return cnt + 1;
      for (let i = 0; i < 4; i++) {
        nx = x + dx[i];
        ny = y + dy[i];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m || maps[nx][ny] == 0) continue;
        if (maps[nx][ny] == 1) {
          maps[nx][ny] = maps[x][y] + 1;
          tarr.push([nx, ny, cnt + 1]);
        } else if (maps[nx][ny] > maps[x][y] + 1) {
          maps[nx][ny] = maps[x][y] + 1;
          tarr.push([nx, ny, cnt + 1]);
        }
      }
    }
    arr = [...tarr];
  }

  return -1;
}
