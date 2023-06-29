'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #ret = True 
        #print(board)
        # every row must contain digits 1-9 without repeating
        # every collumn must contain digits 1-9 without repeating
        # 3x3 collumn must contain digits 1-9 without repeating
        # assuming board has 1-9 atm and will cover if it changes 
        #cols= [["."]*9]*9
        ### row check ###
        for i in range(0,9):
            row_seen = set()
            for j in range(0,9):
                ## set up columns while doing row check 
                #cols[j][i] = board[i][j]
                if board[i][j] in row_seen and board[i][j] !=".":
                    return False
                else:
                    row_seen.add(board[i][j])
        print("passed-rows")
        ### column check ###
        for i in range(0,9):
            col_seen = set()
            for j in range(0,9):
                if board[j][i] in col_seen and board[j][i] !=".":
                #if cols[i][j] in col_seen and cols[i][j] !=".":
                    return False
                else:
                    col_seen.add(board[j][i])#col_seen.add(cols[i][j])
        print("passed-cols")
        ### 3x3 grid check ###
        #grid = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                grid_seen = set()
                curr = board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3]
                print("i,j: "+str(i)+" , "+str(j))
                print(curr)
                for k in range(0,9):
                    if curr[k] in grid_seen and curr[k] !=".":
                        return False
                    else:
                        grid_seen.add(curr[k])
        print("passed-3x3!")
        return True#ret 
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print(sol.isValidSudoku(board))