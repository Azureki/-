package leetcode

func sortArray(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	temp := nums[0]
	lo, hi := 0, len(nums)-1
	for lo < hi {
		for lo < hi && nums[hi] >= temp {
			hi--
		}
		for lo < hi && nums[lo] <= temp {
			lo++
		}
		nums[lo], nums[hi] = nums[hi], nums[lo]
	}
	nums[0], nums[hi] = nums[hi], nums[0]
	sortArray(nums[0:lo])
	sortArray(nums[lo+1 : len(nums)])
	return nums
}
