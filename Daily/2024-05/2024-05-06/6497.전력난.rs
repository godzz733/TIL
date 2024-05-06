use std::collections::HashMap;
use std::iter::Map;
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

struct UnionFind {
    parent: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        UnionFind {
            parent,
        }
    }

    fn findparent(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            self.parent[x] = self.findparent(self.parent[x]);
        }
        self.parent[x]
    }

    fn unionparent(&mut self, x: usize, y: usize) {
        let x = self.findparent(x);
        let y = self.findparent(y);
        if x < y {
            self.parent[y] = x;
        } else {
            self.parent[x] = y;
        }
    }
}

fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();
    loop {
        let n = next::<usize>(&mut it);
        let m = next::<usize>(&mut it);
        if n == 0 && m == 0 {
            break;
        }
        let mut arr = Vec::new();
        for _ in 0..m {
            let a = next::<usize>(&mut it);
            let b = next::<usize>(&mut it);
            let c = next::<usize>(&mut it);
            arr.push((c,a,b));
        }

        arr.sort();
        let mut uf = UnionFind::new(n);
        let mut sum = 0;
        for (c,a,b) in arr {
            if uf.findparent(a) != uf.findparent(b) {
                uf.unionparent(a,b);
            } else {
                sum += c;
            }
        }

        writeln!(so, "{}", sum).ok();
    }

}