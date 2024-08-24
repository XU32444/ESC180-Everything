
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    opp_col = None
    if col == "b":
        opp_col = "w"
    if col == "w":
        opp_col = "b"
    # opp_col  can be used to help determine if its at the edge of the board
    open_seq_count = 0
    semi_open_seq_count = 0
    if y_start + (length - 1) * d_y < 0 or y_start + (length - 1) * d_y > len(board) - 1:
        return open_seq_count, semi_open_seq_count
    if x_start + (length - 1) * d_x < 0 or x_start + (length - 1) * d_x > len(board[0]) - 1:
        return open_seq_count, semi_open_seq_count
    counter = 0
    for i in range(min(len(board), len(board[0]))):
        if board[y_start + i * d_y][x_start + i * d_x] == col:
            counter += 1
        else:
            pass
    if counter == length:  # if it find a sequence
        if d_y == 0 and d_x == 1:  # if its left to right
            # if the last step is at the edge
            if x_start + (length - 1) * d_x == len(board[0]) - 1:
                if board[y_start - d_y][x_start - d_x] == " ":
                    semi_open_seq_count += semi_open_seq_count
                else:
                    pass
            if x_start == 0:
                if board[y_start + length * d_y][x_start + length * d_x] == "":
                    semi_open_seq_count += semi_open_seq_count
                else:
                    pass
            else:
                if board[y_start - d_y][x_start - d_x] == " " and board[y_start + length * d_y][x_start + length * d_x] == " ":
                    open_seq_count += open_seq_count
                elif board[y_start - d_y][x_start - d_x] == " " or board[y_start + length * d_y][x_start + length * d_x] == " ":
                    semi_open_seq_count += semi_open_seq_count
        if d_y == 1 and d_x == 0:  # top to bottom
            if y_start == 0:
                if board[y_start + length * d_y][x_start + length * d_x] == " ":
                    semi_open_seq_count += semi_open_seq_count
            if y_start + length - 1 == len(board):
                if board[y_start - d_y][x_start - d_x] == " ":
                    semi_open_seq_count += semi_open_seq_count
            else:
                if board[y_start - d_y][x_start - d_x] == " " and board[y_start + length * d_y][x_start + length * d_x] == " ":
                    open_seq_count += open_seq_count
                elif board[y_start - d_y][x_start - d_x] == " " or board[y_start + length * d_y][x_start + length * d_x] == " ":
                    semi_open_seq_count += semi_open_seq_count

        if d_y == 1 and d_x == 1:  # direction upper left to lower right
            pass
        if d_y == 1 and d_x == -1:
            pass

    return open_seq_count, semi_open_seq_count


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board


def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i % 10) + "|"
    s += str((len(board[0])-1) % 10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i % 10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def test_detect_row():
    board = make_empty_board(8)
    x = 5
    y = 1
    d_x = 0
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0, x, length, d_y, d_x) == (1, 0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


if __name__ == '__main__':
    test_detect_row()
