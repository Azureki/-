class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(left, right, tar):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] < tar:
                return bin_search(mid + 1, right, tar)
            elif nums[mid] > tar:
                return bin_search(left, mid - 1, tar)
            else:
                return mid
        return bin_search(0, len(nums) - 1, target)
