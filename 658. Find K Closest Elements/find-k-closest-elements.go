package problem658

func findClosestElements(arr []int, k int, x int) []int {
	left, right := 0, len(arr)-k
	var mid int
	for left < right {
		mid = (left + right) / 2
		if x-arr[mid] > arr[right]-x {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return arr[left : left+k]
}
