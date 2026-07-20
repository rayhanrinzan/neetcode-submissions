class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row_checker(row):
            count = 0
            for val in row:
                if val != ".":
                    count += 1
            if len(set(row))-1 == count:
                return(True)
            print("3")
            return(False)

        def transpose(board):
            transposed_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

            for i in range(len(board)):
                for j in range(len(board[i])):
                    transposed_board[j][i] = board[i][j]
            return(transposed_board)

        def mini_board_maker(board, r_idx, l_idx, t_idx, b_idx):
            mini_board = []
            for i in range(t_idx, b_idx):
                mini_row = []
                for j in range(r_idx, l_idx):
                    mini_row.append(board[i][j])
                mini_board.append(mini_row)
            return(mini_board)

        def contains_duplicate(lst, value):
            count = 0
            if value == ".":
                return(False)
            for num in lst:
                if num == value:
                    count += 1
            if count > 1:
                return(True)
            print("1")
            return(False)
            
        def mini_board_checker(mini_board):
            linear_board = []
            for row in mini_board:
                linear_board.extend(row)
            for value in linear_board:
                if contains_duplicate(linear_board, value):
                    print("2")
                    return(False)

        for row in board:
            if row_checker(row) == False:
                return(False)

        for row in transpose(board):
            if row_checker(row) == False:
                return(False)
 
        for i in range(0, len(board), 3):
            t_idx = i
            b_idx = i+3
            for j in range(0, len(board[i]), 3):
                r_idx = j
                l_idx = j+3
                mini_board = mini_board_maker(board, r_idx, l_idx, t_idx, b_idx)
                if mini_board_checker(mini_board) == False:
                    return(False)

        return(True)

        
            


        
