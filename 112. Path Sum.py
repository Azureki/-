# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def dfs(root, tar):
            if not root:
                return False
            if root.val == tar and root.left is None and root.right is None:
                # print(23, res)
                return True
            return dfs(root.left, tar - root.val) or dfs(root.right, tar - root.val)

        if not root:
            return False
        return dfs(root, sum)


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.right = TreeNode(2)

print(Solution().hasPathSum(root, 22))
