import java.util.*;
class Pos{
    int x,y;
    Pos(int x, int y){
        this.x = x;
        this.y = y;
    }
}
class Solution {
    static ArrayList<Integer> ans = new ArrayList();
    static int [] dx = {-1,1,0,0};
    static int [] dy = {0,0,1,-1};
    static int [][] arr;
    static int n,m;
    public int[] solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        arr= new int[n][m];
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (maps[i].charAt(j) == 'X'){
                    arr[i][j] = 0;
                } else {
                    arr[i][j] = maps[i].charAt(j) - '0';
                }
            }
        }
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                int tem = bfs(i,j);
                if (tem != 0){
                    ans.add(tem);
                }
            }
        }
        Collections.sort(ans);
        int [] answer = ans.stream().mapToInt(Integer::intValue).toArray();
        answer = answer.length == 0 ? new int [] {-1} : answer;
        
        return answer;
    }
    static int bfs(int r, int c){
        if (arr[r][c] == 0) return 0;
        int cnt = arr[r][c];
        arr[r][c] = 0;
        Deque<Pos> q = new ArrayDeque();
        q.add(new Pos(r,c));
        while (!q.isEmpty()){
            Pos cur = q.poll();
            for (int i=0; i<4; i++){
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (nx < 0 || nx>=n || ny<0 || ny>=m || arr[nx][ny] == 0) continue;
                cnt += arr[nx][ny];
                arr[nx][ny] = 0;
                q.add(new Pos(nx,ny));
            }
        }
        return cnt;
    }
}