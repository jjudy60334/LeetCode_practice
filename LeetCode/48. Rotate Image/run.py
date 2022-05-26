class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for k in range(n):
            matrix.append([])
        x = 0
        y = 0
        while (x < n and y < n):
            matrix[n + y].insert(0, matrix[x][y])
            x += 1
            if x >= n:
                x = 0
                y += 1
        del matrix[:n]
