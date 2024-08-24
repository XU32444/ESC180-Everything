def get_free_squares(board):
    that_coord = []
    all_coord = []
    for i in range(len(board)):
        for s in range(len(board)):
            if board[i][s] == '': #if the board is empty
                that_coord.append(i)
                that_coord.append(s)
                all_coord.append(that_coord)
            else: # if the board is not empty
                pass
    return all_coord