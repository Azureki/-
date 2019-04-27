package findboth

func bisecLeft(nums []int, target int) int {
	left, right := 0, len(nums)
	var mid int
	for left < right {
		mid = (left + right) / 2
		if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

func bisecRight(nums []int, target int) int {
	left, right := 0, len(nums)
	var mid int
	for left < right {
		mid = (left + right) / 2
		if nums[mid] <= target {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

func searchRange(nums []int, target int) []int {

	left := bisecLeft(nums, target)
	if left == len(nums) ||
		nums[left] != target {
		return []int{-1, -1}
	}
	right := bisecRight(nums[left+1:], target)
	return []int{left, left + right}
}
