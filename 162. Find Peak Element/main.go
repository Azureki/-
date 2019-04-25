package problem162

/* nums[i] ≠ nums[i+1] */
func findPeakElement(nums []int) int {
	left, right := 0, len(nums)-1
	var mid int
	for left < right {
		mid = (left + right) / 2
		// there must be a peak on the right
		// mid+1 won't be out of bound.
		if nums[mid+1] > nums[mid] {
			left = mid + 1
		} else { // there must be a peak on the right
			right = mid
		}
	}
	return left
}
