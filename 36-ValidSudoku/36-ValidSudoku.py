# Last updated: 6/28/2026, 6:10:57 AM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)] 
        grd = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                box = (i//3)*3 +(j//3)
                if num == ".":
                    continue
                if num in list(row[i]):
                    return False
                if num in list(col[j]):
                    return False
                if num in list(grd[box]):
                    return False
                row[i].add(num)
                col[j].add(num)
                grd[box].add(num)
        return True
        