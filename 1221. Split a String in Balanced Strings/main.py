class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        flag = 0
        for c in s:
            if c == 'L':
                flag += 1
            else:
                flag -= 1
            if flag == 0:
                res += 1
        return res
