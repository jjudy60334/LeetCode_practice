class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            l = [u for u in i if u != '.']
            if len(set(l)) != len(l):
                return False
        for k in range(9):
            v = [i[k] for i in board if i[k] != '.']
            if len(set(v)) != len(v):
                return False
        for j in range(3):
            g = board[j*3:j*3+3]
            for i in range(3):
                grid = [r[i*3:i*3+3] for r in g]
                o = []
                for p in grid:
                    o += [k for k in p if k != '.']
                if len(set(o)) != len(o):
                    return False
        return True
