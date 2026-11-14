class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(m):
            for j in range(n):
                count = 0
                for dr, dc in dirs:
                    r = i + dr
                    c = j + dc

                    if not ( 0 <= r < m and 0 <= c < n):
                        continue
                    elif board[r][c] == 1 or board[r][c] == -1:
                        count += 1
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = -1
                    else:
                        continue
                elif board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0
        