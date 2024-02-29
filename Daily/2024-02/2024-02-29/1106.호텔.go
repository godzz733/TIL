package main

import (
	"bufio"
	"fmt"
	"os"
)


func main2() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n,m int
	fmt.Fscanln(reader, &n, &m)
	arr := make([]int,n+1)
	for i:=0; i<n; i++ {
		arr[i] = 987654321
	}
	var a,b int
	for i:=0; i<m; i++ {
		fmt.Fscanln(reader, &a, &b)
		for j:=n; j>=0; j-- {
			if j-b < 0 {
				arr[0] = min(arr[0],arr[j]+a)
			} else {

				arr[j-b] = min(arr[j-b],arr[j]+a)
			}
		}
	}
	fmt.Fprint(writer,arr[0])

}