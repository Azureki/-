func searchMatrix(matrix [][]int, target int) bool {
	for i := 0; i < len(matrix); i++ {
		if binsearch(matrix[i], target) {
			return true
		}
	}

	return false
}

func binsearch(arr []int, target int) bool {
	hi := len(arr) - 1
	lo := 0

	for lo <= hi {
		mid := (lo + hi) / 2
		if arr[mid] == target {
			return true
		} else if arr[mid] < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}

	return false
}