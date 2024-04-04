use std::{io, vec};
use std::io::prelude::*;

fn read<T>(si: &mut T) -> String where T: Read {
    let mut s = String::new();
    si.read_to_string(&mut s).unwrap();
    s
}

fn next<T>(it: &mut std::str::SplitAsciiWhitespace) -> T where
    T: std::str::FromStr,
    <T as std::str::FromStr>::Err: std::fmt::Debug {
    it.next().unwrap().parse().unwrap()
}

const DX:[i32;4] = [0,0,1,-1];
const DY:[i32;4] = [1,-1,0,0];
fn solve(n: i32, m:i32, arr: &mut Vec<Vec<i16>>, dp: &mut [[i32; 500]; 500], x: usize, y: usize) -> i32 {
    if x as i32 == n-1 && y as i32 == m-1 {
        return 1;
    }
    if dp[x][y] != -1 {
        return dp[x][y];
    }

    dp[x][y] = 0;

    for i in 0..4 {
        let nx = x as i32 + DX[i];
        let ny = y as i32 + DY[i];
        if nx >= 0 && nx < n && ny >=0 && ny < m && arr[nx as usize][ny as usize] < arr[x][y]{
            dp[x][y] += solve(n,m,arr ,dp, nx as usize,ny as usize);
        }
    }

    dp[x][y]

}

fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();

    let n = next::<i32>(&mut it);
    let m = next::<i32>(&mut it);

    let mut arr = Vec::new();
    for _ in 0..n {
        let v = (0..m).map(|_| next::<i16>(&mut it)).collect::<Vec<_>>();
        arr.push(v);
    }
    let mut dp = [[-1;500]; 500];
    let ans = solve(n,m,&mut arr ,&mut dp, 0,0);
    writeln!(so,"{}",ans).ok();
}