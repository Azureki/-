# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        self.solve(root.left, root.right)

    def solve(self, left, right):
        if not left:
            return
        left.next = right
        self.solve(left.left, left.right)
        self.solve(right.left, right.right)
        self.solve(left.right, right.left)


class Solution2:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # Level order traversal does not satisfy this problem which calls for only constant extra space
#        if root:
#            queue = [ root ]
#            while queue:
#                for i in range(len(queue) - 1):
#                    queue[i].next = queue[i+1]
#                    
#                newLevel = []
#                for node in queue:
#                    if node.left:
#                        newLevel.append(node.left)
#                        
#                    if node.right:
#                        newLevel.append(node.right)
#                    
#                queue = newLevel

        # O(1) space 2 Pointer solution: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37472/A-simple-accepted-solution
        # Use the next at parent nodes to thread child nodes at the next level
        if root and root.left:
            pre = root # Parent node
            while pre.left: # child node at the next level
                cur = pre
                while cur:
                    cur.left.next = cur.right
                    if cur.next: # The problem assumes this is a perfect binary tree, no need to check cur.right
                        cur.right.next = cur.next.left
                    
                    cur = cur.next
                    
                # Finished connecting one level, go to the beginning of next level
                pre = pre.left
