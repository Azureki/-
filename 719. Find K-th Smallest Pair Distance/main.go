package problem719

import (
	"sort"
)

func smallestDistancePair(nums []int, k int) int {
	sort.Ints(nums)
	left, right := 0, nums[len(nums)-1]-nums[0]
	var mid int
	for left < right {
		mid = (left + right) / 2
		cnt, j := 0, 0
		for i, x := range nums {
			// 最关键的就是这里了，两个循环O(n^2)是过不了的
			// 为什么i++之后，j不需要清0？小于j的都成立吗？是的。
			// 因为nums[j-1]-nums[i]<=m，所以nums[j-1]-nums[i+1]<=m.(nums[i+1]>=nums[i])
			for j < len(nums) && nums[j]-x <= mid {
				j++
			}
			// 共有[i+1,j)个元素
			// nums[i]不满足条件，因为不能自己减自己
			// nums[j]不满足条件，因为是先加再判断的
			cnt += j - i - 1
		}
		if cnt < k {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}
