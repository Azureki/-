# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 0,n
        mid = 0
        while left<right:
            mid=(left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        # 事实上，在最后一般需要判断。但这题确定target存在。
        return left

