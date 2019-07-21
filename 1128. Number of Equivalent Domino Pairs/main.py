from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = defaultdict(int)
        for domino in dominoes:
            d[tuple(sorted(domino))] += 1
        return sum([value*(value-1) for value in d.values()])
