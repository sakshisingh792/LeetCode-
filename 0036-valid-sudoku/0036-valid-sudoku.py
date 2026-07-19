class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] ==".":
                    continue

                num=board[r][c]
                box_idx=r//3*3+c//3
                if num in row[r] or num in col[c]   or num in box[box_idx]:
                    return False

                row[r].add(num)
                col[c].add(num)
                box[box_idx].add(num)
        return True        
