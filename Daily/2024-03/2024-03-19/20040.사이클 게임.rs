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

use std::{i32::MIN, i64::MAX, io::{stdin, Read}};

fn find_parent(parent: &mut Vec<i32>, x: i32) -> i32 {
    if parent[x as usize] != x {
        parent[x as usize] = find_parent(parent, parent[x as usize]);
    }
    parent[x as usize]
}

fn union_parent(parent: &mut Vec<i32>, a: i32, b: i32) {
    let a = find_parent(parent, a);
    let b = find_parent(parent, b);
    if a < b {
        parent[b as usize] = a;
    } else {
        parent[a as usize] = b;
    }
}

fn main() {
    // 입력
    let mut input_str = String::new();
    stdin().read_to_string(&mut input_str).unwrap();
    let mut input = input_str.split_ascii_whitespace();
    
    let (n,m) = map_int(&mut input);
    let mut arr:Vec<i32> = vec![0; 500001];
    for i in 0..n {
        arr[i as usize] = i;
    }
    let mut ans = 0;
    for i in 0..m {
        let (a,b) = map_int(&mut input);
        if find_parent(&mut arr, a) == find_parent(&mut arr, b) {
            ans = i + 1;
            break;
        } 
        union_parent(&mut arr, a, b);
    }
    println!("{}", ans);
}