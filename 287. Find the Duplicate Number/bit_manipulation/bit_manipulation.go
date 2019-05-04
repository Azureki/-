package problem287

func findDuplicate(nums []int) int {
	res := 0
	for i := uint(0); i < 32; i++ {
		countNormal, countDup := 0, 0
		b := 1 << i
		for j := 0; j < len(nums); j++ {
			if j&b > 0 {
				countNormal++
			}
			if nums[j]&b > 0 {
				countDup++
			}
		}
		if countDup > countNormal {
			res += b
		}
	}
	return res
}
