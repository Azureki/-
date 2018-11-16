# from queue import Queue


class Solution:
    def updateMatrix(self, matrix):
        width = len(matrix[0])
        height = len(matrix)
        q=[]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = float('inf')

        # while not q.empty():
            # tem = q.get()
        for tem in q:
            for d in dirs:
                x, y = tem[0] + d[0], tem[1] + d[1]
                if x < 0 or x >= height or y < 0 or y >= width or matrix[x][y] <= matrix[tem[0]][tem[1]]:
                    continue
                else:
                    matrix[x][y] = matrix[tem[0]][tem[1]] + 1
                    q.append((x, y))
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
