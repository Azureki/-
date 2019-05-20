package leetcode

func totalNQueens(n int) int {
	matrix := make([][]bool, n)
	for i := range matrix {
		matrix[i] = make([]bool, n)
	}
	return soln(matrix, 0)
}

func soln(matrix [][]bool, n int) int {
	if n == len(matrix) {
		return 1
	}
	count := 0
	for i := 0; i < len(matrix); i++ {
		if possible(matrix, n, i) {
			matrix[n][i] = true
			count += soln(matrix, n+1)
			matrix[n][i] = false
		}
	}
	return count
}

// 该点是否可能
func possible(matrix [][]bool, x, y int) bool {
	// 判断列
	for i := x - 1; i >= 0; i-- {
		if matrix[i][y] {
			return false
		}
	}
	// 判断左上
	for i, j := x-1, y-1; i >= 0 && j >= 0; i, j = i-1, j-1 {
		if matrix[i][j] {
			return false
		}
	}
	// 判断右上
	for i, j := x-1, y+1; i >= 0 && j < len(matrix); i, j = i-1, j+1 {
		if matrix[i][j] {
			return false
		}
	}
	return true
}
