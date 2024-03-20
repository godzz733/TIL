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

use std::{io::{stdin, Read}};

const dx:[i8;5] = [0, 0, 1, -1,0];
const dy:[i8; 5] = [1, -1, 0, 0,0];

fn check(arr:&mut Vec<Vec<i8>>, cnt: i8) -> i8 {
    let mut tem = cnt;
    for i in 1..10 {
        for j in 0..10 {
            if arr[i-1][j] == 1 {
                tem += 1;
                for k in 0..5 {
                    let nx = i as i8 + dx[k];
                    let ny = j as i8 + dy[k];
                    if nx >= 0 && nx < 10 && ny >= 0 && ny < 10 {
                        arr[nx as usize][ny as usize] ^= 1;
                    }
                }
            }
        }
    }
    for i in 0..10 {
        for j in 0..10 {
            if arr[i][j] == 1 {
                return -1;
            }
        }
    }
    tem
}

fn main() {
    // 입력
    let mut input_str = String::new();
    stdin().read_to_string(&mut input_str).unwrap();
    let mut input = input_str.split_ascii_whitespace();
    
    let mut arr: Vec<Vec<i8>> = vec![vec![0;10]; 10];
    for i in 0..10 {
        let char_arr = list_str(&mut input);
        for j in 0..10 {
            if char_arr[j] == 'O' {
                arr[i][j] = 1;
            }
        }
    }
    let mut ans = 127;
    for x in 0..(1<<10) {
        let mut tem = arr.clone();
        let mut cnt = 0;
        for i in 0..10 {
            if x & (1<<i) != 0 {
                cnt += 1;
                for j in 0..5 {
                    let nx = 0 + dx[j];
                    let ny = i + dy[j];
                    if nx >= 0 && nx < 10 && ny >= 0 && ny < 10 {
                        tem[nx as usize][ny as usize] ^= 1;
                    }
                }
            }
        }
        let res = check(&mut tem, cnt);
        if res != -1 {
            ans = ans.min(res);
        }
    }
    println!("{}", if ans == 127 { -1 } else { ans });
}