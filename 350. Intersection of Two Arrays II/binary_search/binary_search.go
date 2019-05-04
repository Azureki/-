package problem350

/*
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
如果已经排序，而且len(nums1)<len(nums2)，应该用二分搜索
*/

import (
	"sort"
)

func intersect(nums1 []int, nums2 []int) []int {
	sort.Ints(nums1)
	sort.Ints(nums2)
	res := []int{}
	if len(nums1) > len(nums2) {
		nums1, nums2 = nums2, nums1
	}
	low := 0
	for _, x := range nums1 {
		index := sort.SearchInts(nums2, x)
		if index != len(nums2) && nums2[index] == x {
			res = append(res, x)
			low = index + 1
			nums2 = nums2[low:]
		}
	}
	return res
}
