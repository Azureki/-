package leetcode

func getNext(board [][]byte, x, y int) (int, int, bool) {
	for {
		x, y = x+(y+1)/9, (y+1)%9
		if x == 9 {
			return x, y, true
		}
		if board[x][y] == '.' {
			break
		}
	}
	return x, y, false
}

func dfs(board [][]byte, x, y int) bool {
	x, y, out := getNext(board, x, y)
	if out {
		return true
	}
	for i := 1; i < 10; i++ {
		if isVaild(board, x, y, '0'+byte(i)) {
			board[x][y] = '0' + byte(i)
			if dfs(board, x, y) {
				return true
			}
		}
	}
	board[x][y] = '.'
	return false
}

func solveSudoku(board [][]byte) {
	// in dfs, firstly `getNext`, so first pos is (0, -1)
	dfs(board, 0, -1)
}

// judge if board[x][y] can be $tar
func isVaild(board [][]byte, x, y int, tar byte) bool {
	for _, val := range board[x] {
		if val == tar {
			return false
		}
	}
	for i := 0; i < 9; i++ {
		if board[i][y] == tar {
			return false
		}
	}
	startX, startY := x/3*3, y/3*3
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			newX, newY := startX+i, startY+j
			if board[newX][newY] == tar {
				return false
			}
		}
	}
	return true
}
