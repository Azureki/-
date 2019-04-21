import itertools


class Solution:
    def twoCitySchedCost(self, costs):
        def get_diff(cost):
            return abs(cost[0]-cost[1])

        res = 0
        N = len(costs)//2
        d = {0: 0, 1: 0}
        lst = sorted(costs, key=get_diff, reverse=True)
        for cost in lst:
            idx = 0 if cost[0]<cost[1] else 1
            if d[idx]!=N:
                d[idx]+=1
                res+=cost[idx]
            else:
                d[1-idx]+=1
                res+=cost[1-idx]

        return res


costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
res = Solution().twoCitySchedCost(costs)
print(res)

