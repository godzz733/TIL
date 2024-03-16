
// 정수 하나 받기
fn int(input: &mut std::str::SplitAsciiWhitespace) -> usize {
    input.next().unwrap().parse::<usize>().unwrap()
}

// 정수 여러개 받기
fn map_int(input: &mut std::str::SplitAsciiWhitespace) -> (usize, usize) {
    let n = input.next().unwrap().parse::<usize>().unwrap();
    let m = input.next().unwrap().parse::<usize>().unwrap();
    (n, m)
}

// 정수 여러개 받아서 list로 만들기
// Max_SIZE는 배열의 최대 크기
const MAX_SIZE: usize = 100;

fn list_int(input: &mut std::str::SplitAsciiWhitespace, n: usize) -> [usize; MAX_SIZE] {
    let mut arr: [usize; MAX_SIZE] = [0; MAX_SIZE]; // 모든 요소를 0으로 초기화
    for i in 0..n {
        arr[i] = input.next().unwrap().parse::<usize>().unwrap();
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

fn preorder(arr: &Vec<[Option<usize>; 2]>, x: usize) {
    print!("{}", (x + 65) as u8 as char);
    if arr[x][0].is_some() {
        preorder(arr, arr[x][0].unwrap());
    }
    if arr[x][1].is_some() {
        preorder(arr, arr[x][1].unwrap());
    }
}

fn inorder(arr: &Vec<[Option<usize>; 2]>, x:usize) {
    if arr[x][0].is_some() {
        inorder(arr, arr[x][0].unwrap());
    }
    print!("{}", (x+65) as u8 as char);
    if arr[x][1].is_some() {
        inorder(arr, arr[x][1].unwrap());
    }
}

fn postorder(arr: &Vec<[Option<usize>; 2]>, x:usize) {
    if arr[x][0].is_some() {
        postorder(arr, arr[x][0].unwrap());
    }
    if arr[x][1].is_some() {
        postorder(arr, arr[x][1].unwrap());
    }
    print!("{}", (x+65) as u8 as char);
}


fn main() {
    // 입력
    let mut input_str = String::new();
    stdin().read_to_string(&mut input_str).unwrap();
    let mut input = input_str.split_ascii_whitespace();
    
    let n = int(&mut input);

    let mut arr: Vec<[Option<_>; 2]> = vec![[None::<usize>; 2]; n];
    for i in 0..n {
        let (a,b,c) = (str(&mut input), str(&mut input), str(&mut input));
        if b != "." {
            arr[a.chars().next().unwrap() as usize - 65][0] = Some(b.chars().next().unwrap() as usize - 65);
        }
        if c != "." {
            arr[a.chars().next().unwrap() as usize - 65][1] = Some(c.chars().next().unwrap() as usize - 65);
        }
    }
    preorder(&arr, 0);
    println!();
    inorder(&arr, 0);
    println!();
    postorder(&arr, 0);
}
