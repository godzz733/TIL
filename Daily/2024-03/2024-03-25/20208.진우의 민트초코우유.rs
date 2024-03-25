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

fn check(now: (i32, i32), cnt: i32, idx: i32, health: i32, home: &(i32, i32), arr: &[(i32, i32)], v: &mut Vec<bool>, ans: &mut i32, k: i32) {
    let size = arr.len() as i32;
    if *ans > cnt + size - idx {
        return;
    }

    if idx == size {
        if (home.0 as i32 - now.0 as i32).abs() + (home.1 as i32 - now.1 as i32).abs() <= health {
            *ans = (*ans).max(cnt);
        }
        return;
    }

    for i in 0..size {
        if !v[i as usize] {
            let (x, y) = arr[i as usize];
            let distance = (now.0 as i32 - x as i32).abs() + (now.1 as i32 - y as i32).abs();

            if distance <= health {
                v[i as usize] = true;
                check((x, y), cnt + 1, idx + 1, health - distance + k, home, arr, v, ans, k);
                v[i as usize] = false;
            }
        }
    }

    check(now, cnt, idx + 1, health, home, arr, v, ans, k);
}

fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();
    
    let (n,m,k) = (next::<i32>(&mut it), next::<i32>(&mut it), next::<i32>(&mut it));
    let mut arr = Vec::new();
    let mut home = (0,0);
    (0..n).for_each(|i| {
        (0..n).for_each(|j| {
            let tem = next::<i32>(&mut it);
            if tem == 2 {
                arr.push((i,j));
            } else if tem == 1{
                home = (i,j);
            }
        })
    });
    let mut ans = 0;
    let mut v = vec![false; arr.len()];

    check(home, 0, 0, m, &home, &arr, &mut v, &mut ans, k);
    writeln!(so, "{}", ans).ok();
}