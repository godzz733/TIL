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
    let mut arr = vec![vec![0; n]; n];
    let mut lst = vec![Vec::new(); n];
    for _ in 0..n-1 {
        let a = next::<usize>(&mut it);
        let b = next::<usize>(&mut it);
        let c = next::<usize>(&mut it);
        lst[a-1].push((b-1, c));
        lst[b-1].push((a-1, c));
    }
    for i in 0..n {
        let mut v = vec![0; n];
        v[i] = 1;
        let mut tem = Vec::new();
        tem.push((i,0));
        while !tem.is_empty() {
            let (a,b) = tem.pop().unwrap();
            for (x,y) in &lst[a] {
                if v[*x] == 0 {
                    v[*x] = 1;
                    arr[i][*x] = *y + b;
                    tem.push((*x, *y + b));
                }
            }
        }
    }
    (0..m).for_each(|_| {
        let a = next::<usize>(&mut it);
        let b = next::<usize>(&mut it);
        writeln!(so, "{}", arr[a-1][b-1]).unwrap();
    });
}