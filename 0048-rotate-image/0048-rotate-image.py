class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start = 0
        n = len(matrix)
        end = n - 1
        i = 0
        while i <= n // 2:
            start = 0
            end = n - 1 - i
            while start + i < end:        
                matrix[i][i + start], matrix[i + start][end] = matrix[i + start][end], matrix[i][i + start]
                matrix[i][i + start], matrix[end][end - start] = matrix[end][end - start], matrix[i][i + start]
                matrix[i][i + start], matrix[end - start][i] = matrix[end - start][i], matrix[i][i + start]
                start += 1
            i += 1
        