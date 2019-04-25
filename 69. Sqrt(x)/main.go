package problem64

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
		} else {
			left = mid
		}
	}
	return left
}
