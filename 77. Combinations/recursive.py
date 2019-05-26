class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not (0 <= k <= n):
            return []
        if k == 0:
            return [[]]
        res = self.combine(n - 1, k - 1)
        for x in res:
            x.append(n)
        for x in self.combine(n - 1, k):
            res.append(x)
        return res
