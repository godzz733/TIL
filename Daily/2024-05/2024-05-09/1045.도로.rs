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

fn find(x: usize, p: &mut Vec<usize>) -> usize {
    if x != p[x] {
        p[x] = find(p[x], p);
    }
    p[x]
}

fn merge(x: usize, y: usize, p: &mut Vec<usize>) {
    let a = find(x, p);
    let b = find(y, p);
    if a < b {
        p[b] = a;
    } else {
        p[a] = b;
    }
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
    for _ in 0..n {
        let t = next::<String>(&mut it).chars().collect::<Vec<char>>();
        let mut t2 = vec![0; n];
        for i in 0..n {
            if t[i] == 'Y' {
                t2[i] = 1;
            }
        }
        arr.push(t2);
    }
    let mut p = Vec::new();
    for i in 0..n {
        p.push(i);
    }
    let mut cnt = 0;
    let mut key = 0;
    let mut ans = vec![0; n];
    for i in 0..n {
        for j in 0..n {
            if arr[i][j] == 1 {
                if find(i, &mut p) != find(j, &mut p) {
                    merge(i, j, &mut p);
                    cnt += 1;
                    arr[i][j] = 0;
                    arr[j][i] = 0;
                    ans[i] += 1;
                    ans[j] += 1;
                }
            }
        }
    }
    let tem = find(0, &mut p);
    for i in 1..n {
        if find(i, &mut p) != tem {
            key = -1;
            break;
        }
    }
    if key == -1{
        writeln!(so, "-1").ok();
    } else if cnt == m {
        for i in 0..n {
            write!(so, "{} ", ans[i]).ok();
        }
    } else {
        for i in 0..n {
            if key != 0 {
                break;
            }
            for j in 0..n {
                if key != 0 {
                    break;
                }
                if arr[i][j] == 1{
                    ans[i] += 1;
                    ans[j] += 1;
                    arr[j][i] = 0;
                    cnt += 1
                }
                if cnt == m {
                    key = 1;
                }
            }
        }
        if key == 1 {
            for i in 0..n {
                write!(so, "{} ", ans[i]).ok();
            }
        } else {
            writeln!(so, "-1").ok();
        }
    }
}