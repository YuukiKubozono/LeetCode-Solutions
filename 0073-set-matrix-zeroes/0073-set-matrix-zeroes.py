class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        column_first = False
        for r in range(m):
            if matrix[r][0] == 0:
                column_first = True
        
        row_first = False
        for c in range(n):
            if matrix[0][c] == 0:
                row_first = True
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for c in range(1, n):
            for r in range(1, m):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        
        if row_first:
            matrix[0] = [0] * n
        if column_first:
            for j in range(m):
                matrix[j][0] = 0