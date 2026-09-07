class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        vertical = [set() for _ in range(len(board))]
        horizontal = [set() for _ in range(len(board))]

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):

                block3x3 = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        num = board[k][l]
                        if num in block3x3 or num in vertical[l] or num in horizontal[k]:
                            return False
                        elif num == '.':
                            continue

                        block3x3.add(num)
                        vertical[l].add(num)
                        horizontal[k].add(num)

        return True
