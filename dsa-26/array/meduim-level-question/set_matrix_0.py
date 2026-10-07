class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = []
        col = []
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for k in row:
            for j in range(0, n):
                matrix[k][j] = 0
        for p in col:
            for i in range(0, m):
                matrix[i][p] = 0

        return matrix
# brute force approach
