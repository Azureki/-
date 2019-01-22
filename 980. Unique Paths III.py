class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        self.res = 0
        dirs = [(-1, 0), (1, 0), (1, 0), (0, 1)]
        left = 0
        height = len(grid)
        length = len(grid[0])
        visited = [[0] * length for _ in range(height)]

        def dfs(x, y, left):
            if left == 0 and grid[x][y] == 2:
                self.res += 1
                return
            for d in dirs:
                i, j = x + d[0], y + d[1]
                if (0 <= i < height and 0 <= j < length and grid[i][j] != -1
                        and not visited[i][j]):
                    visited[i][j] = 1
                    dfs(i, j, left - 1)
                    visited[i][j] = 0

        for i in range(height):
            for j in range(length):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 0:
                    left += 1
        visited[x][y] = 1
        print(x, y, left)
        dfs(x, y, left + 1)
        return self.res


grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
print(Solution().uniquePathsIII(grid))
