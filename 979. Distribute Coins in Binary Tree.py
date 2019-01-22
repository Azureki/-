# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def dfs(root):
            if not root:
                return 1
            left = dfs(root.left)
            right = dfs(root.right)
            self.res += abs(left-1)+abs(right-1)
            root.val += left -1 + right -1
            return root.val

        dfs(root)
        return self.res

