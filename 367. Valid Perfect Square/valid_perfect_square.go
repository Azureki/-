package problem367

func isPerfectSquare(num int) bool {
	if num == 1 {
		return true
	}
	left, right := 0, num
	var mid int
	for left <= right {
		mid = (left + right) / 2
		if mid*mid == num {
			return true
		} else if mid*mid < num {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return false
}
