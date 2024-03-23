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

fn bisect(arr: &Vec<usize>, size: usize, target: usize) -> i32 {
    let mut st:i32 = 0;
    let mut end:i32 = size as i32;
    let mut res:i32 = -1;
    while st <= end {
        let mid = (st + end) >> 1;
        if arr[mid as usize] < target {
            st = mid + 1;
        } else {
            end = mid-1;
            res = mid as i32;
        }
    }
    if st == size as i32 {
        return -1;
    }
    res
}
fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();
    
    let n = next::<usize>(&mut it);
    let mut arr = (0..n).map(|_|
        next::<usize>(&mut it)).collect::<Vec<_>>();
    let mut lst = vec![(0,0); n];
    let mut dp = vec![0; n];
    let mut size = 0;
    for i in (0..n) {
        let idx = bisect(&dp, size, arr[i]);
        if idx == -1{
            dp[size] = arr[i];
            lst[i].0 = size+1;
            size += 1;
        } else {
            dp[idx as usize] = arr[i];
            lst[i].0 = idx as usize + 1;
        }
    }
    dp = vec![0; n];
    size = 0;
    for i in (0..n).rev() {
        let idx = bisect(&dp, size, arr[i]);
        if idx == -1{
            dp[size] = arr[i];
            lst[i].1 = size+1;
            size += 1;
        } else {
            dp[idx as usize] = arr[i];
            lst[i].1 = idx as usize + 1;
        }
    }
    let mut ans = 0;
    for i in (0..n) {
        ans = ans.max(lst[i].0 + lst[i].1 - 1);
    }
    writeln!(so, "{}", ans).ok();
}