class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:  x[0]-x[1])

        N = len(costs) // 2
        cost = 0
        for i in range(N):
            cost += costs[i][0]
        for i in range(N):
            cost += costs[N+i][1]
        return cost
