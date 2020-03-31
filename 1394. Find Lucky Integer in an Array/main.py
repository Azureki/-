class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for x in arr:
            d[x] = d.get(x, 0) + 1

        max_res = -1
        for k,v in d.items():
            if k==v and max_res < k:
                max_res = k
        return max_res
