class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] ==".":
                    continue


                box_idx=r//3*3+c//3
                num=board[r][c]
                if num in row[r] or num in col[c] or num in boxes[box_idx]:
                    return False

                row[r].add(num)
                col[c].add(num)
                boxes[box_idx].add(num)   
        return True     
        