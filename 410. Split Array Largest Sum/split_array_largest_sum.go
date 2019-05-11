package problem410

func max(nums ...int) int {
	max := nums[0]
	for _, x := range nums {
		if x > max {
			max = x
		}
	}
	return max
}

func sum(nums []int) int {
	res := 0
	for _, x := range nums {
		res += x
	}
	return res
}

func split(nums []int, capacity int) int {
	count := 1
	pack := 0
	for _, x := range nums {
		pack += x
		if pack > capacity {
			pack = x
			count++
		}
	}
	return count
}

func splitArray(nums []int, m int) int {
	left := max(nums...)
	right := sum(nums)
	var mid int
	for left < right {
		mid = (left + right) / 2
		if split(nums, mid) > m {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}
