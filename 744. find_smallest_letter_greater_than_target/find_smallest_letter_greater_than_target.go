package problem744

func nextGreatestLetter(letters []byte, target byte) byte {
	if letters[len(letters)-1] <= target {
		return letters[0]
	}
	left, right := 0, len(letters)-1
	var mid int
	for left < right {
		mid = (left + right) / 2
		if letters[mid] <= target {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return letters[left]
}
