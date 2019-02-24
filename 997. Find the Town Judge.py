class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        believe = {}
        believed = {}

        for a, b in trust:
            if believe.get(a):
                believe[a] += 1
            else:
                believe[a] = 1
            if believed.get(b):
                believed[b] += 1
            else:
                believed[b] = 1
        for k, v in believed.items():
            if v == N - 1 and believe.get(k, 0) == 0:
                return k
        return -1
