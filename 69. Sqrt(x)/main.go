package main

import "fmt"

func mySqrt2(x int) int {
	x0 := 1
	var tem int
	for {
		tem = x0
		x0 = (x0 + x/x0) / 2
		fmt.Println(x0)
		if tem <= x0 {
			break
		}

	}
	return x0

}

func mySqrt(x int) int {
	if x == 0 {
		return 0
	}
	left, right := 1, x
	var mid int
	for left+1 < right {
		mid = (left + right) / 2
		if mid*mid > x {
			right = mid
			fmt.Println("right:", right)
		} else {
			left = mid
			fmt.Println("left:", left)
		}
	}
	return left
}

func main() {
	fmt.Println(mySqrt(4))
}
