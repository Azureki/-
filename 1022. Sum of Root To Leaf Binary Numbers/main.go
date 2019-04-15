package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dFS(root *TreeNode, base int) int {
	if root == nil {
		return 0
	}
	res := 0
	base = (base << 1) + root.Val
	if root.Left != nil {
		res += dFS(root.Left, base)
	}
	if root.Right != nil {
		res += dFS(root.Right, base)
	}
	if res != 0 {

		return res
	}
	return base
}

func sumRootToLeaf(root *TreeNode) int {
	return dFS(root, 0)
}

func main() {
	root := TreeNode{1, nil, nil}
	res := sumRootToLeaf(&root)
	fmt.Println(res)
}
