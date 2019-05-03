package problem287

func findDuplicate(nums []int) int {
	N := len(nums) - 1
	var mid int
	lo, hi := 0, N
	for lo < hi {
		mid = (lo + hi) / 2
		leftNum := 0
		for _, x := range nums {
			if x <= mid {
				leftNum++
			}
		}
		if leftNum <= mid {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}
