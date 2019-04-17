package problem1026

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

func getMax(nums ...int) int {
	max := nums[0]
	for _, num := range nums {
		if max < num {
			max = num
		}
	}
	return max

}
func getMin(nums ...int) int {
	min := nums[0]
	for _, num := range nums {
		if min > num {
			min = num
		}
	}
	return min

}
func dFS(root *TreeNode) (min, max, diff int) {
	if root == nil {
		return 100001, -1, 0
	}
	lMin, lMax, lDiff := dFS(root.Left)
	rMin, rMax, rDiff := dFS(root.Right)
	min = getMin(lMin, rMin)
	max = getMax(lMax, rMax)
	diff = getMax(lDiff, rDiff)
	if min < 100001 {
		diff = getMax(diff, abs(root.Val-min))
	}
	if max > -1 {
		diff = getMax(diff, abs(root.Val-max))
	}

	min = getMin(min, root.Val)
	max = getMax(lMax, rMax, root.Val)
	return

}
func maxAncestorDiff(root *TreeNode) int {
	_, _, res := dFS(root)
	return res

}
