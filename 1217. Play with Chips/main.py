from sys import maxsize


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        length = len(chips)
        min_cost = maxsize
        for i in range(length):
            tem = 0
            for j in range(length):
                if (chips[j] - chips[i]) & 1 != 0:
                    tem += 1
            if tem < min_cost:
                min_cost = tem

        return min_cost
