class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        comp = []
        for i in range(1, length):
            if A[i] > A[i - 1]:
                comp.append(1)
            elif A[i] < A[i - 1]:
                comp.append(-1)
            else:
                comp.append(0)
        res = 0
        length = len(comp)
        i = 0
        while i != length:
            num = 1 if comp[i] else 0
            j = i + 1
            while j != length:
                if comp[j] and comp[j] == -comp[j - 1]:
                    num += 1
                    j += 1
                else:
                    break

            res = max(res, num)
            i = j
        return res + 1


A = [9,9,9]
print(Solution().maxTurbulenceSize(A))
