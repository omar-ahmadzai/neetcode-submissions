class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        block = 3
        board_size = 9

        # checking rows
        for i in range(board_size):
            repeated = set()
            for j in range(board_size):
                cell_value = board[i][j]
                if cell_value in repeated:
                    return False
                elif cell_value != ".":
                    repeated.add(cell_value)

        # checking columns
        for i in range(board_size):
            repeated = set()
            for j in range(board_size):
                cell_value = board[j][i]
                if cell_value in repeated:
                    return False
                elif cell_value != ".":
                    repeated.add(cell_value)
        
        # checking blocks
        for i in range(0, board_size, 3):
            for j in range(0, board_size, 3):
                repeated = set()
                for row in range(block):
                    for column in range(block):
                        cell_value = board[i + row][j + column]
                        if cell_value in repeated:
                            return False
                        elif cell_value != ".":
                            repeated.add(cell_value)
        
        return True
