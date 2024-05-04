use std::collections::HashMap;
use std::iter::Map;
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
    let mut m = next::<usize>(&mut it);
    let t = next::<String>(&mut it);
    let mut arr = t.chars().collect::<Vec<char>>();
    let mut st = 0;
    let mut fi = n - 1;
    while m > 0 && st < fi {
        while st < fi{
            if arr[st] == 'P' {
                st += 1;
            }
            if arr[fi] == 'C' {
                fi -= 1;
            }
            if arr[st] == 'C' && arr[fi] == 'P' {
                break;
            }
        }
        if st < fi {
            arr[st] = 'P';
            arr[fi] = 'C';
            st += 1;
            fi -= 1;
            m -= 1;
        }
    }
    let mut ans: i64 = 0;
    if arr[0] == 'C' {
        writeln!(so, "{}", ans).ok();
    } else {
        let mut tem = Vec::new();
        let mut t = 1;
        let mut now = arr[0];
        for i in 1..n {
            if arr[i] == now {
                t += 1;
            } else {
                tem.push(t);
                t = 1;
                now = arr[i];
            }
        }
        tem.push(t);
        let mut nump = 0;
        for i in (0..tem.len()).step_by(2) {
            if i + 1 ==  tem.len() {
                break;
            }
            nump += tem[i];
            ans += (nump * (nump-1) * tem[i+1])/2;
        }
        writeln!(so, "{}", ans).ok();
    }    


}