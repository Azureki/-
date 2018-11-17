class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(pos):
            image[pos[0]][pos[1]] = newColor
            for d in dirs:
                x, y = pos[0] + d[0], pos[1] + d[1]
                if x in (-1, heigth) or y in (-1, width) or image[x][y] != color:
                    continue
                else:
                    dfs((x, y))
        if image[sr][sc] == newColor:
            return image
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        width = len(image[0])
        heigth = len(image)
        color = image[sr][sc]
        dfs((sr, sc))
        return image


image = [
    [0, 0, 0, ],
    [0, 1, 1],

]
sr = 1
sc = 1
newColor = 1
s = Solution()
print(s.floodFill(image, sr, sc, newColor))
