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
    let mut arr = Vec::new();

    (0..n).map(|_|
    next::<String>(&mut it)
    ).for_each(|x| arr.push(x));
    let mut lst: Vec<u32> = Vec::new();
    for i in 0..n {
        let mut tem = 0;
        for j in 0..arr[i].len() {
            tem |= 1 << (arr[i].as_bytes()[j] - 'a' as u8);
        }
        lst.push(tem);
    }
    let mut num = 0;
    for _ in 0..m {
        let a = next::<usize>(&mut it);
        let b = next::<char>(&mut it) as u8;
        let mut ans = 0;
        if a == 1{
            num |= 1 << (b - 'a' as u8);
        } else {
            num &= !(1 << (b - 'a' as u8));
        }
        for i in 0..n {
            if lst[i] & num == 0 {
                ans += 1;
            }
        }
        writeln!(so,"{}",ans).ok();
    }
}