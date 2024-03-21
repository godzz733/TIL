// 정수 하나 받기
fn int(input: &mut std::str::SplitAsciiWhitespace) -> usize {
    input.next().unwrap().parse::<usize>().unwrap()
}

// 정수 여러개 받기
fn map_int(input: &mut std::str::SplitAsciiWhitespace) -> (i32, i32) {
    let n = input.next().unwrap().parse::<i32>().unwrap();
    let m = input.next().unwrap().parse::<i32>().unwrap();
    (n, m)
}

// 정수 여러개 받아서 list로 만들기
// Max_SIZE는 배열의 최대 크기
const MAX_SIZE: usize = 50;

fn list_int(input: &mut std::str::SplitAsciiWhitespace, n: usize) -> [i64; MAX_SIZE] {
    let mut arr: [i64; MAX_SIZE] = [0; MAX_SIZE]; // 모든 요소를 0으로 초기화
    for i in 0..n {
        arr[i] = input.next().unwrap().parse::<i64>().unwrap();
    }
    arr
}

// 문자열 받기
fn str(input: &mut std::str::SplitAsciiWhitespace) -> String {
    input.next().unwrap().to_string()
}

// 문자열 받아서 char 배열 만들기
fn list_str(input: &mut std::str::SplitAsciiWhitespace) -> Vec<char> {
    input.next().unwrap().chars().collect()
}
use std::io::{self, stdin};
use std::io::prelude::*;

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
    let mut input_str = String::new();
    io::stdin().read_to_string(&mut input_str).unwrap();
    let mut input = input_str.split_ascii_whitespace();
    
    let mut so = io::BufWriter::new(io::stdout().lock());
    let n = int(&mut input);
    let mut arr:Vec<usize> = vec![0; 500001];
    let mut ans:Vec<i32> = vec![-1; 500001];
    let mut size = 0;
    let mut tem:Vec<(usize, usize)> = vec![];
    for _ in 0..n {
        let (n,m) = map_int(&mut input);
        tem.push((n as usize, m as usize));
        ans[n as usize] = 0;
    }
    tem.sort_by(|a,b| a.0.cmp(&b.0));
    // last index of tem
    let mut n = tem[tem.len()-1].0;
    for (x,y) in tem {
        let mut t = bisect(&arr, size, y);
        if t == -1 {
            arr[size] = y;
            ans[x as usize] = size as i32 + 1;
            size += 1;
        } else {
            arr[t as usize] = y;
            ans[x as usize] = t+1;
        }
    }
    let mut res = vec![];
    for i in (1..=n).rev() {
        if ans[i] != size as i32 && ans[i] != -1 {
            res.push(i);
        } else if ans[i] == size as i32 {
            size -= 1;
        }
    }
    res.reverse();
    writeln!(so,"{}", res.len()).ok();
    for i in res {
        writeln!(so,"{} ", i).ok();
    }
}