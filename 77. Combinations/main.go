package leetcode

func combine(n int, k int) [][]int {
	combs := [][]int{}
	comb := make([]int, 0, k)
	myComb(&combs, &comb, 1, n, k)
	return combs

}

func myComb(combs *[][]int, comb *[]int, start, n, k int) {
	if k == 0 {
		tem := make([]int, len(*comb))
		copy(tem, *comb)
		*combs = append(*combs, tem)
		return
	}
	for i := start; i <= n; i++ {
		*comb = append(*comb, i)
		myComb(combs, comb, i+1, n, k-1)
		*comb = (*comb)[:len(*comb)-1]
	}
}
