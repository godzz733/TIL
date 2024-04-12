use std::{cmp, io, vec};
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

    let n = next::<usize>(&mut it);
    let m = next::<usize>(&mut it);
    let arr = (0..n).map(|_|
    next::<usize>(&mut it)).collect::<Vec<_>>();
    let a = next::<usize>(&mut it);
    let d = next::<usize>(&mut it);
    let mut ans = vec![vec![0; 1001]; 1001];
    ans[0][0] = arr[0];
    for i in 0..n {
        for j in 0..n {
            if ans[i][j] == 0 {
                continue;
            }
            if i + 1 >= n {
                ans[n][j] = cmp::max(ans[n][j], ans[i][j] + *arr.get(i+1).unwrap_or_else(|| &0));
            } else {
                ans[i+1][j] = cmp::max(ans[i+1][j], ans[i][j] + *arr.get(i+1).unwrap_or_else(|| &0));
            }
            if i+d >= n {
                ans[n][j+1] = cmp::max(ans[n][j+1], ans[i][j] - arr[i] + a + *arr.get(i+d).unwrap_or_else(|| &0));
            } else {
                ans[i+d][j+1] = cmp::max(ans[i+d][j+1], ans[i][j] - arr[i] + a + *arr.get(i+d).unwrap_or_else(|| &0));
            }
        }
    }
    let mut answer = -1;
    for i in 0..n+1 {
        if ans[n][i] >= m {
            answer = i as i32;
            break;
        }
    }
    writeln!(so, "{}", answer).ok();
}