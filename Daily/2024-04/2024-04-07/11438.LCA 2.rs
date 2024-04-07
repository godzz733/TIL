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

fn dfs(x: usize, mut cnt:usize, v: &mut [usize], arr:&[Vec<usize>], parent: &mut [Vec<usize>], d: &mut [usize]) {
    v[x] = 1;
    d[x] = cnt;
    for i in &arr[x] {
        if v[*i] == 0 {
            v[*i] = 1;
            parent[*i][0] = x;
            dfs(*i,cnt+1, v, arr, parent,d);
        }
    }
}

fn set_parent(v: &mut [usize], arr:&[Vec<usize>], parent: &mut [Vec<usize>], d: &mut [usize], n: usize) {
    dfs(1,0,v,arr,parent,d);
    for i in (1..21) {
        for j in (1..n+1) {
            parent[j][i] = parent[parent[j][i-1]][i-1];
        }
    }
}

fn lca(mut a: usize,mut b: usize,parent: &mut [Vec<usize>], d: &mut [usize]) -> usize{
    if d[a] > d[b] {
        let tem = b;
        b = a;
        a = tem;
    }

    for i in (0..21).rev() {
        if d[b] - d[a] >= (1<<i) {
            b = parent[b][i];
        }
    }

    if a == b {
        return a;
    }

    for i in (0..21).rev() {
        if parent[a][i] != parent[b][i] {
            a = parent[a][i];
            b = parent[b][i];
        }
    }
    parent[a][0]
}

fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();

    let n = next::<usize>(&mut it);
    let mut arr: Vec<Vec<usize>> = Vec::new();
    arr.extend((0..n+1).map(|_| Vec::<usize>::new()));
    for _ in 0..n-1 {
        let a = next::<usize>(&mut it);
        let b = next::<usize>(&mut it);
        arr[a as usize].push(b);
        arr[b as usize].push(a);
    }
    
    // let mut parent = Vec::new();
    let mut v: Vec<usize> = vec![0; n+1];
    let mut parent = Vec::new();
    parent.extend((0..n+1).map(|_| vec![0;21]));
    let mut d = vec![0; n+1];

    set_parent(&mut v, &mut arr, &mut parent, &mut d, n);

    let m = next::<usize>(&mut it);
    for _ in 0..m {
        let a = next::<usize>(&mut it);
        let b = next::<usize>(&mut it);
        writeln!(so,"{}", lca(a, b, &mut parent, &mut d)).ok();
    }
}