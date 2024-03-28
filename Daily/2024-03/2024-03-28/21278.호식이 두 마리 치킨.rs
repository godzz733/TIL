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

    let n = next::<usize>(&mut it);
    let m = next::<usize>(&mut it);
    let mut arr = [[987654321;101];  101];

    for _ in 0..m {
        let a = next::<usize>(&mut it);
        let b = next::<usize>(&mut it);
        arr[a][b] = 1;
        arr[b][a] = 1;
    }
    for i in 1..=n {
        arr[i][i] = 0;
    }
    for k in 1..=n {
        for i in 1..=n {
            for j in 1..=n {
                if arr[i][j] > arr[i][k] + arr[k][j] {
                    arr[i][j] = arr[i][k] + arr[k][j];
                }
            }
        }
    }
    let mut ans = (0,0,987654321);
    for i in 1..n {
        for j in i+1..=n {
            let mut tem = 0;
            for k in 1..=n {
                tem += arr[k][i].min(arr[k][j]);
            }
            if tem*2 < ans.2 {
                ans = (i, j, tem*2);
            }
        }
    }
    writeln!(so, "{} {} {}", ans.0, ans.1, ans.2).ok();
}