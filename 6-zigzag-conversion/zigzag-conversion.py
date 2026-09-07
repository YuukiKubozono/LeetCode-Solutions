class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s
        
        rows = []
        for _ in range(numRows):
            rows.append([])
        curr_row = 0
        direction = -1

        for char in s:
            rows[curr_row].append(char)

            if curr_row == 0 or curr_row == numRows - 1:
                direction *= -1
            curr_row += direction
        
        return "".join("".join(row) for row in rows)