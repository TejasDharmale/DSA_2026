class Solution:
    def rotateMatrix(self, matrix):
        n = len(matrix)

        for i in range(0, n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

        for i in range(0, n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
