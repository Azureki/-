# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        i = inorder.index(postorder[-1])
        root=postorder[-1]
        root.left=self.buildTree(inorder[:i], postorder[:i])
        root.right=self.buildTree(inorder[i+1:],postorder[i:-1])
        return root
