class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            check = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
            for j in range(n):
                if board[i][j] in check:
                    check.remove(board[i][j])
                elif board[i][j] == ".":
                    continue
                else:
                    return False

        for j in range(n):
            check = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
            for i in range(m):
                if board[i][j] in check:
                    check.remove(board[i][j])
                elif board[i][j] == ".":
                    continue
                else:
                    return False

        for r in range(0, m , 3):
            for c in range(0, n, 3):
                check = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] in check:
                            check.remove(board[i][j])
                        elif board[i][j] == ".":
                            continue
                        else:
                            return False
        return True