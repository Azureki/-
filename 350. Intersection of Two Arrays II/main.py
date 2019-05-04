from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        # 随手写了一个dict的与运算，没想到真的可以。
        # 看来是取小值了
        c = c1 & c2
        res = []
        for k, v in c.items():
            res += [k] * v
        return res
