# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from bisect import bisect_left


class Solution:
    def dfs(self, root, lst):
        if not root:
            return
        self.dfs(root.left, lst)
        lst.append(root.val)
        self.dfs(root.right, lst)

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        lst = []
        self.dfs(root, lst)
        lo = bisect_left(lst, L)
        hi = bisect_left(lst, R)
        return sum(lst[lo:hi + 1])


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
L = 7
R = 15
s = Solution()
print(s.rangeSumBST(root, L, R))
