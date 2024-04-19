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
    let mut arr = (0..n).map(|_| next::<usize>(&mut it)).collect::<Vec<_>>();
    let mut q = Vec::<(usize,usize)>::new();
    let mut ans = (0..n).map(|_| -1).collect::<Vec<_>>();

    let mut num = (0..*arr.iter().max().unwrap() as usize + 1).map(|_| 0).collect::<Vec<_>>();
    for i in 0..n {
        num[arr[i]] += 1;
    }
    for i in 0..n {
        if q.is_empty() {
            q.push((i, num[arr[i]]));
        } else {
            while !q.is_empty() {
                let (idx, cnt) = q[q.len()-1];
                if cnt < num[arr[i]] {
                    ans[idx] = arr[i] as isize;
                    q.pop();
                } else {
                    break;
                }
            }
            q.push((i, num[arr[i]]));
        }
    }
    for i in 0..n {
        write!(so, "{} ", ans[i]).ok();
    }
}