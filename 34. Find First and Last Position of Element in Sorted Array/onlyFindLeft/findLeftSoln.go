package findleft

/* merely 1 function. merely find left
cannot judge in besecLeft() whether nums[left]==target
because we search target+1 to get the right position
*/

func bisecLeft(nums []int, target int) int {
	// 这个函数相当于 python中的bisect.bisect_left
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

func searchRange(nums []int, target int) []int {
	left := bisecLeft(nums, target)
	if left == len(nums) ||
		nums[left] != target {
		return []int{-1, -1}
	}
	right := bisecLeft(nums[left+1:], target+1)
	return []int{left, left + right}
}
