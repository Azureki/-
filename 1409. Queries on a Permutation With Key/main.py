class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1, m+1)]
        res = []
        for i in queries:
            res.append(P.index(i))
            P.remove(i)
            P.insert(0, i)
        return res
