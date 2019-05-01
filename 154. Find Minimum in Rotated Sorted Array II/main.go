package problem154

func findMin(nums []int) int {
	left, right := 0, len(nums)-1
	var mid int
	for left < right {
		if nums[left] < nums[right] {
			return nums[left]
		}
		mid = (left + right) / 2
		// if nums[mid] > nums[left] {
		// 	left = mid + 1
		// } else if nums[mid] < nums[right] {
		// 	right = mid
		// }
		// 上一种写法并不合理。*mid只需要比*right大。不需要比*left大，就可以说明mid落在左边
		// if nums[mid] < nums[left] {
		if nums[mid] > nums[right] {
			left = mid + 1
		} else if nums[mid] < nums[right] {
			right = mid
		} else {
			// nums[left]<=nums[mid]<=nums[right]
			// 三者相等
			left++
		}
	}
	return nums[left]
}
