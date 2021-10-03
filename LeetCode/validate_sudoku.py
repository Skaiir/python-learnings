validSudoku = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".","8","8",".",".","7","9"]]

def isValidSudoku(board) -> bool:
    threes = [0,1,2]
    
    def isUniqueSudokuSet(arr):
        arr = [num for num in arr if not num is "."]
        return len(arr) == len(set(arr)) 
        
    for i in range(9): # 0, 1, .. 8
        row_nums = board[i]
        col_nums = [row[i] for row in board]
        square_coordinates = [((i//3) * 3 + i_1, (i % 3) * 3 + i_2) for i_1 in threes for i_2 in threes]            
        sq_nums = [board[row][col] for row, col in square_coordinates]
        if not(isUniqueSudokuSet(row_nums) and isUniqueSudokuSet(col_nums) and isUniqueSudokuSet(sq_nums)):
            return False
    return True

print(isValidSudoku(validSudoku))