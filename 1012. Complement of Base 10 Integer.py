from math import log2
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        count = int(log2(N)) + 1
        return 2 ** count - N - 1

