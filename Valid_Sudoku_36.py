#Check List:
#make 3 dicts for the row one save it as 0:[list of first row] for the column it is the same
#for the grid one have to save it by adding elements based on their position so something in the 4th row and 8th column is saved as 
# (1,2):[list of things in this]
#iterate it so that each small block gets iterated and added to their specific lists
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        grid_dict = defaultdict(set)

        for row, lists in enumerate(board):
            for col, num in enumerate(lists):
                #checking if num is in row_dict
                if num == ".":
                        pass
                else: 
                        if num in row_dict.get(row, set()):
                                return False
                        row_dict[row].add(num)

                        #checks if num is in col_dict
                        if num in col_dict.get(col,set()):
                                return False
                        col_dict[col].add(num)

                        #checks if num is already in its grid_dict
                        grid_row = row //3
                        grid_col = col //3
                        if num in grid_dict.get(tuple([grid_row,grid_col]), set()):
                                return False
                        grid_dict[tuple([grid_row,grid_col])].add(num)

        print(row_dict)
        print(col_dict)
        print(grid_dict)

        return True
        #return null

            


if __name__ == "__main__":
    solution = Solution()
    test1 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    test2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    run1 = solution.isValidSudoku(test1)
    print(run1)

    run2 = solution.isValidSudoku(test2)
    print(run2)