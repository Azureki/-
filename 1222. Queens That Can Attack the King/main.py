class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (-1, -1), (1, -1), (-1, 1)]
        queens_set = set(tuple(queen) for queen in queens)
        for d in dirs:
            x, y = king
            while True:
                x, y = x + d[0], y + d[1]
                if 0 <= x < 8 and 0 <= y < 8:
                    if (x, y) in queens_set:
                        res.append([x, y])
                        break
                else:
                    break

        return res
