func solveSudoku(board [][]byte) {
	var marks [9][27]bool
	for row := range board {
		for col := range board[row] {
			num := board[row][col]
			if num == '.' {
				continue
			}
			marks[num-49][row], marks[num-49][9+col], marks[num-49][18+row/3*3+col/3] = true, true, true
		}
	}
	sudoku(board, marks, 0, 0)
}

func sudoku(board [][]byte, marks [9][27]bool, row, col int) bool {
	if row == len(board) {
		return true
	}
	if board[row][col] != '.' {
		return sudoku(board, marks, row+(col+1)/9, (col+1)%9)
	}

	for num := 1; num <= 9; num++ {
		if marks[num-1][row] || marks[num-1][9+col] || marks[num-1][18+row/3*3+col/3] {
			continue
		}
		board[row][col] = byte(num + 48)
		marks[num-1][row], marks[num-1][9+col], marks[num-1][18+row/3*3+col/3] = true, true, true
		if sudoku(board, marks, row+(col+1)/9, (col+1)%9) {
			return true
		}
		board[row][col] = '.'
		marks[num-1][row], marks[num-1][9+col], marks[num-1][18+row/3*3+col/3] = false, false, false
	}
	return false
}