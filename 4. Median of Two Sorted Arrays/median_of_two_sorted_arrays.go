package problem4

func max(nums1, nums2 []int, m1, m2 int) int {
	if m1 < 0 {
		return nums2[m2]
	}
	if m2 < 0 {
		return nums1[m1]
	}
	if nums1[m1] < nums2[m2] {
		return nums2[m2]
	}
	return nums1[m1]
}

func min(nums1, nums2 []int, m1, m2 int) int {
	if m1 == len(nums1) {
		return nums2[m2]
	}
	if m2 == len(nums2) {
		return nums1[m1]
	}
	if nums1[m1] > nums2[m2] {
		return nums2[m2]
	}
	return nums1[m1]
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	if len(nums1) > len(nums2) {
		nums1, nums2 = nums2, nums1
	}
	n1, n2 := len(nums1), len(nums2)
	k := (n1 + n2 + 1) / 2
	left, right := 0, len(nums1)
	var m1, m2 int
	for left < right {
		m1 = (left + right) / 2
		m2 = k - m1 - 1
		if nums1[m1] < nums2[m2] {
			left = m1 + 1
		} else {
			right = m1
		}
	}
	m1, m2 = left, k-left-1
	numsKSub1 := max(nums1, nums2, m1-1, m2)
	if (n1+n2)&1 != 0 {
		return float64(numsKSub1)
	}
	numsK := min(nums1, nums2, m1, m2+1)
	return float64(numsK+numsKSub1) / float64(2)
}
