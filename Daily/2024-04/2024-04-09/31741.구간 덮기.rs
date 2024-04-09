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

fn bisect(arr: &Vec<(i64,i64)>, A_arr: &Vec<i64>, B_arr: &Vec<i64>, l: i64, r: i64) -> i64 {
    let mut st: i32 = 0;
    let mut fi:i32 = A_arr.len() as i32 - 1;
    let mut res = 0;
    let mut ans = 0;
    while st <= fi {
        let mid = (st+fi) >> 1;
        if A_arr[mid as usize] < l {
            st = mid + 1;
        } else {
            fi = mid - 1;
            res = A_arr[mid as usize] ;
        }
    }
    if res == 0  {
        return i64::MAX;
    }
    ans += i64::abs(res - l);
    res = 0;
    st = 0;
    fi = B_arr.len() as i32 - 1;
    while st <= fi {
        let mid = (st+fi) >> 1;
        if B_arr[mid as usize] > r {
            fi = mid - 1;
        } else {
            st = mid + 1;
            res = B_arr[mid as usize] ;
        }
    }
    if res == 0 {
        return i64::MAX;
    }
    ans += i64::abs(r - res);
    ans
}

fn bisect_mid(B_arr: &Vec<i64>, r: i64) -> i64 {
    let mut st: i32 = 0;
    let mut fi:i32 = B_arr.len() as i32 - 1;
    let mut res = 0;
    while st <= fi {
        let mid = (st+fi) >> 1;
        if B_arr[mid as usize] > r {
            fi = mid - 1;
        } else {
            st = mid + 1;
            res = B_arr[mid as usize] ;
        }
    }
    if res == 0 {
        return i64::MAX;
    }
    i64::abs(r - res)
}

fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();

    let n = next::<i64>(&mut it);
    let l = next::<i64>(&mut it);
    let r = next::<i64>(&mut it);

    let mut ans = i64::MAX;
    let mut arr: Vec<(i64,i64)> = Vec::new();
    let mut A_arr = Vec::new();
    let mut B_arr = Vec::new();
    for _ in 0..n {
        let a = next::<i64>(&mut it);
        let b = next::<i64>(&mut it);
        if a <= l && b >= r {
            ans = 0;
        }
        if b < l || a > r {
            continue;
        }
        if a <= l {
            A_arr.push(b);
        } else if b >= r {
            B_arr.push(a);
        } else {
            arr.push((a, b));
        }
    }
    if ans == 0 {
        writeln!(so, "0").ok();
    } else {
        A_arr.sort_unstable();
        B_arr.sort_unstable();
        for i in 0..arr.len() {
            let (x,y) = arr[i];
            ans = ans.min(bisect(&arr,&A_arr,&B_arr,x, y));
        }
        for i in 0..A_arr.len() {
            let x = A_arr[i];
            ans = ans.min(bisect_mid(&B_arr, x));
        }
        if ans == i64::MAX {
            writeln!(so, "-1").ok();
        } else {
            writeln!(so, "{}", ans).ok();
        }
    }
}