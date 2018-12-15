class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            pre = root
            while pre:
                if pre.left or pre.right:
                    pass
                else:
                    pre = pre.next
                    continue
                cur = pre
                while cur:
                    # find cur.left.next
                    if cur.left:
                        if cur.right:
                            cur.left.next = cur.right
                        else:
                            tem = cur.next
                            while tem:
                                if tem.left:
                                    cur.left.next = tem.left
                                    break
                                elif tem.right:
                                    cur.left.next = tem.right
                                    break
                                tem = tem.next
                    # find cur.right.next
                    if cur.right:
                        tem = cur.next
                        while tem:
                            if tem.left:
                                cur.right.next = tem.left
                                break
                            elif tem.right:
                                cur.right.next = tem.right
                                break
                            tem = tem.next

                    cur = cur.next
                pre = pre.left if pre.left else pre.right

