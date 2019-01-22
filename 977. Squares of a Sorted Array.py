class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(map(lambda x: x * x, A))


lst = [-4,-1,0,3,10]
print(Solution().sortedSquares(lst))
