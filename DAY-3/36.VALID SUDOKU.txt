class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #a_r_s = []
        #does the row has repeat
        for row in board:
            seen = set()
            for i in row:
                if i != '.' and i in seen:
                    return False
                else:
                    seen.add(i)    
            #a_r_s.add(seen)

        #does the col has repeat
        c = 0
        while(c < 9):
            seen = set()
            for i in board:
                if i[c] != '.' and i[c] in seen:
                    return False
                else:
                    seen.add(i[c])
            c += 1    

        #does the 3*3 grid has repeat
        for i in range(0,7,3):
            for j in range(0,7,3):
                if not self.chk(i,j,board):
                    return False
                
        return True
        

    def chk(self, i : int, j : int, board: List[List[str]]) -> bool:
        seen = set()
        for s in range(i,i+3):
            for e in range(j,j+3):
                if board[s][e] != '.' and board[s][e] in seen:
                    return False
                else:
                    seen.add(board[s][e])
        return True