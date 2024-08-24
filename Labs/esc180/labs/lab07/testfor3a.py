
def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def is_sq_in_board(board,y,x):
    board_height = len(board)
    board_width = len(board[0])
    if y > board_height or x > board_width:
        return print(False)
    else:
        return print(True)


if __name__ == '__main__':
    board = make_empty_board(8)
    print_board(board)
    is_sq_in_board(board,1,1)