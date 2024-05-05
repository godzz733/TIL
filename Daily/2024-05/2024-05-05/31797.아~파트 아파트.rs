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
    let mut ans = n % (m << 1);
    if ans == 0 {
        ans = m << 1;
    }
    let mut arr = vec![0; 10001];
    for i in 0..m {
        let a = next::<usize>(&mut it);
        let b = next::<usize>(&mut it);
        arr[a] = i + 1;
        arr[b] = i + 1;
    }
    let mut lst = Vec::new();
    lst.push(0);
    (0..=10000).for_each(|i| if arr[i] != 0 { lst.push(arr[i]); });
    writeln!(so, "{}", lst[ans]).ok();
}