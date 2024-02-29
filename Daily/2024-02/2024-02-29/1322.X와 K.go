package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


func main1() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

	defer writer.Flush()
	var n,m int
	fmt.Fscanln(reader, &n, &m)
	var arr []int
	for i := 0; i < 40; i++ {
		arr = append(arr, 0)
	}
	binaryStr := strconv.FormatInt(int64(n), 2)
	for _, digit := range binaryStr {
		arr = append(arr, int(digit-'0'))
	}

	// m을 2진수로 변환하여 이진수의 각 자리를 arr에 대응시켜 ans에 저장
	ans := make([]int, len(arr))
	binaryM := strconv.FormatInt(int64(m), 2)
	idx := len(binaryM) - 1
	for i := len(arr) - 1; i >= 0; i-- {
		if arr[i] == 0 {
			ans[i] = int(binaryM[idx] - '0')
			idx--
		}
		if idx == -1 {
			break
		}
	}

	// ans를 10진수로 변환하여 출력
	var result int64 = 0
	for _, digit := range ans {
		result = result*2 + int64(digit)
	}

	fmt.Fprint(writer, result)

}