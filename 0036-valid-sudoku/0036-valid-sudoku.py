class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = []
        cols = []
        boxes = []
        for k in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())
        
        for r in range(9):
            for c in range(9):
                x = board[r][c]
                if x == ".":
                    continue
                box = (r // 3) * 3 + c // 3
                if x in rows[r] or x in cols[c] or x in boxes[box]:
                    return False
                rows[r].add(x)
                cols[c].add(x)
                boxes[box].add(x)
        return True