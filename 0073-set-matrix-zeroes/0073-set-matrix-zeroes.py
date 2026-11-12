class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = set()
        column = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        
        for x in row:
            matrix[x] = [0] * n

        for y in column:
            for k in range(m):
                matrix[k][y] = 0
        