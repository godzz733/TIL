// 정수 하나 받기
fn int(input: &mut std::str::SplitAsciiWhitespace) -> usize {
    input.next().unwrap().parse::<usize>().unwrap()
}

// 정수 여러개 받기
fn map_int(input: &mut std::str::SplitAsciiWhitespace) -> (i64, i64,i64) {
    let n = input.next().unwrap().parse::<i64>().unwrap();
    let m = input.next().unwrap().parse::<i64>().unwrap();
    let k = input.next().unwrap().parse::<i64>().unwrap();
    (n, m, k)
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

use std::io::{stdin, Read};



fn main() {
    // 입력
    let mut input_str = String::new();
    stdin().read_to_string(&mut input_str).unwrap();
    let mut input = input_str.split_ascii_whitespace();

    let (n,m,k) = map_int(&mut input);
    let mut arr: [i64; 50] = list_int(&mut input, n as usize);
    let max = *arr.iter().max().unwrap();
    let mut ans = 0;
    for i in 1..=max{
        let mut cnt:i64 = 0;
        for j in 0..n {
            let mut t:i64 = 0;
            if i > arr[j as usize] {
                continue;
            }
            t += (arr[j as usize] / i) * i * k;
            if i == arr[j as usize] {
                
            } else if arr[j as usize] % i == 0 {
                t -= (arr[j as usize]/i - 1) * m;
            } else {
                t -= (arr[j as usize]/i) * m;
            }
            if t > 0 {
                cnt += t;
            }
        }
        ans = ans.max(cnt);
    }
    println!("{}", ans);
}
