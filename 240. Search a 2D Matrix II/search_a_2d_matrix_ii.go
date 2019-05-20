package leetcode

func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 {
		return false
	}
	x, y := 0, len(matrix[0])-1
	for x < len(matrix) && y >= 0 {
		if matrix[x][y] > target {
			y--
		} else if matrix[x][y] < target {
			x++
		} else {
			return true
		}
	}
	return false
}
