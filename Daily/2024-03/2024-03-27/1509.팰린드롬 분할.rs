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


fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();

    let arr = next::<String>(&mut it).chars().collect::<Vec<char>>();
    let mut dp = vec![vec![false; arr.len()]; arr.len()];
    let mut ans = vec![std::usize::MAX; arr.len()];
    let n = arr.len();
    for l in 0..n {
        for start in 0..n-l {
            let end = start + l;
            if start == end {
                dp[start][end] = true;
            }
            else if arr[start] == arr[end] {
                if start + 1 == end {
                    dp[start][end] = true;
                }
                else {
                    dp[start][end] = dp[start+1][end-1];
                }
            }
        }
    }
    ans[0] = 0;
    for i in 1..n {
        if dp[0][i] {
            ans[i] = std::cmp::min(ans[i], ans[0] + 1);
        }
    }
    ans[0] = 1;
    for i in 1..n {
        for j in i..n {
            if dp[i][j] {
                ans[j] = std::cmp::min(ans[j], ans[i-1] + 1);
            }
        }
    }
    writeln!(so, "{}", ans[n-1]).ok();
}