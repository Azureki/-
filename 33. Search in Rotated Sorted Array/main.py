"""
非常复杂，思考的方向错了。应该首先判断mid
"""


class Solution:
    def search(self, nums, target) -> int:
        left, right = 0, len(nums) - 1
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            # if nums[left]<target<nums[mid]:
            #     right = mid
            if target > nums[left]:
                if nums[mid] > target:
                    # nums[left] < target < nums[mid]
                    right = mid - 1
                elif nums[mid] < nums[left]:
                    # nums[mid] < nums[left] < target
                    right = mid - 1
                elif nums[mid] < target:
                    # nums[left] <= nums[mid]<=target
                    left = mid + 1
                else:
                    return mid

            elif target < nums[left]:
                if nums[mid] < target:
                    # nums[mid] < target < nums[left]
                    left = mid + 1
                elif nums[mid] > nums[left]:
                    # target<nums[left]<nums[mid]
                    left = mid + 1
                elif nums[mid] > target:
                    # target<nums[mid]<=nums[left]
                    right = mid - 1
                else:
                    return mid
            else:
                return left

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
nums = [1]
target = 0
print(Solution().search(nums, target))
