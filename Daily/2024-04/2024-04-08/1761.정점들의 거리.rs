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

fn dfs(x: usize, mut cnt:usize, v: &mut [usize], arr:&[Vec<(usize,usize)>], parent: &mut Vec<Vec<[usize; 2]>>, d: &mut [usize]) {
    v[x] = 1;
    d[x] = cnt;
    cnt += 1;
    for (i,j) in &arr[x] {
        if v[*i] == 0 {
            parent[*i][0][0] = x;
            parent[*i][0][1] = *j + parent[x][0][1];
            dfs(*i, cnt, v, arr, parent, d);
        }
    }
}

fn set_parent(v: &mut [usize], arr:&[Vec<(usize,usize)>], parent: &mut Vec<Vec<[usize; 2]>>, d: &mut [usize], n: usize) {
    dfs(1, 0, v, arr, parent, d);
    for i in 1..21 {
        for j in 1..n+1 {
            parent[j][i][0] = parent[parent[j][i-1][0]][i-1][0];
        }
    }
}

fn lca(mut a: usize,mut b: usize,parent: &mut Vec<Vec<[usize; 2]>>, d: &mut [usize]) -> usize{
    if d[a] > d[b] {
        std::mem::swap(&mut a, &mut b);
    }
    let tem_a = a;
    let tem_b = b;
    for i in (0..21).rev() {
        if d[b] - d[a] >= (1 << i) {
            b = parent[b][i][0];
        }
    }
    if a == b {
        return parent[tem_b][0][1] - parent[tem_a][0][1];
    }
    for i in (0..21).rev() {
        if parent[a][i][0] != parent[b][i][0] {
            a = parent[a][i][0];
            b = parent[b][i][0];
        }
    }
    parent[tem_b][0][1] + parent[tem_a][0][1] - 2 * parent[parent[a][0][0]][0][1]
}

fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();

    let n = next::<usize>(&mut it);
    let mut arr: Vec<Vec<(usize,usize)>> = Vec::new();
    arr.extend((0..n+1).map(|_| Vec::<(usize,usize)>::new()));
    for _ in 0..n-1 {
        let a = next::<usize>(&mut it);
        let b = next::<usize>(&mut it);
        let c = next::<usize>(&mut it);
        arr[a as usize].push((b,c));
        arr[b as usize].push((a,c));
    }
    
    let mut v: Vec<usize> = vec![0; n+1];
    let mut parent: Vec<Vec<[usize; 2]>> = Vec::new();
    parent.extend((0..n+1).map(|_| vec![[0,0];21]));
    let mut d = vec![0; n+1];

    set_parent(&mut v, &mut arr, &mut parent, &mut d, n);

    let m = next::<usize>(&mut it);
    for _ in 0..m {
        let a = next::<usize>(&mut it);
        let b = next::<usize>(&mut it);
        writeln!(so,"{}", lca(a, b, &mut parent, &mut d)).ok();
    }
}