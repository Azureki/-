# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        q=Queue()
        if root:
            q.put(root)
        while not q.empty():
            length=q.qsize();
            tem=[]
            for i in range(length):
                node=q.get()
                tem.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            res.append(tem)
                
        return res

