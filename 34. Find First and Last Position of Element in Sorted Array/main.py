from bisect import bisect, bisect_left


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target)
        if left != len(nums) and nums[left] == target:
            right = bisect(nums, target, left)
            return left, right - 1
        else:
            return -1, -1
