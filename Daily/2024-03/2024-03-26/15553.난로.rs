use std::process::exit;
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
    let mut arr = Vec::new();
    (0..n).for_each(|_| {
        arr.push(next::<usize>(&mut it));
    });
    let mut lst = Vec::new();
    (1..n).for_each(|i| {
        lst.push(arr[i] - arr[i-1])
    });
    lst.sort_unstable();
    let mut ans = m;
    for i in 0..n-m {
        ans += lst[i];
    }
    writeln!(so, "{}", ans).ok();
}