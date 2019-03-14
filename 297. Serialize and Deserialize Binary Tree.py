# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        lst = []
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if not node:
                lst.append(None)
                continue
            lst.append(node.val)
            q.put(node.left)
            q.put(node.right)
        return ','.join(str(x) for x in lst)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def construct(lst, idx):
            if lst[idx] is None:
                return None
            node = TreeNode(lst[idx])
            left = idx * 2 + 1
            right = idx * 2 + 2
            if left < len(lst):
                node.left = construct(lst, left)
                node.right = construct(lst, right)
            return node

        lst = [int(x) if x.lstrip('-').isdigit() else None for x in data.split(',')]
        return construct(lst,0)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
