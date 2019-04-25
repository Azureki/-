package problem33

func search(nums []int, target int) int {
	if len(nums) == 0 {
		return -1
	}

	left, right := 0, len(nums)-1
	var mid int
	for left < right {
		mid = (left + right) / 2
		if nums[mid] < nums[left] {
			if target > nums[mid] && target <= nums[right] {
				// 为什么left要mid+1，而right可以=mid？
				// 因为mid=(left+right)/2,mid会=left，所以要+1
				left = mid + 1
			} else {
				right = mid
			}
		} else { // nums[mid] >= nums[left]
			if nums[left] <= target && target <= nums[mid] {
				right = mid
			} else {
				left = mid + 1
			}
		}
	}

	if nums[left] == target {
		return left
	}
	return -1
}
