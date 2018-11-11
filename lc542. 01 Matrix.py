from queue import Queue
from copy import deepcopy


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def bfs(i, j):
            marked = deepcopy(visited)
            q = Queue()
            num = 0
            q.put((i, j))
            while not q.empty():
                size = q.qsize()
                for _ in range(size):
                    mask = q.get()

                    marked[mask[0]][mask[1]] = 1
                    if matrix[mask[0]][mask[1]] == 0:
                        return num
                    for r, c in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        pos = mask[0] + r, mask[1] + c
                        if pos[0] > -1 and pos[0] < height:
                            if pos[1] > -1 and pos[1] < width:
                                if marked[pos[0]][pos[1]] == 0:
                                    q.put((pos[0], pos[1]))
                num += 1

        width = len(matrix[0])
        height = len(matrix)
        visited = [[0] * width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = bfs(i, j)
        return matrix


matrix = [
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1]
]

s = Solution()
print(s.updateMatrix(matrix))
