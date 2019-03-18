class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = {}
        for x in time:
            x %= 60
            d[x] = d.get(x, 0) + 1
        count = 0
        for k,v in d.items():
            if k in (0, 30):
                count += v * (v - 1) // 2
            elif k < 30:
                count += v * d.get(60 - k, 0)
        return count
