"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Nov. 1, 2023
"""


def is_empty(board):
    for i in range(len(board)):
        for k in range(len(board[0])):
            if not board[i][k] == " ":
                return False
    return True


def is_bounded(board, y_tip, x_tip, length, d_y, d_x):
    block = 0
    block_end = False
    block_start = False
    if y_tip+d_y > len(board)-1 or y_tip+d_y < 0 or x_tip+d_x > len(board)-1 or x_tip+d_x < 0:
        block_end = True
        block += 1
    if y_tip-d_y*(length) > len(board)-1 or y_tip-d_y*(length) < 0 or x_tip-d_x*(length) > len(board)-1 or x_tip-d_x*(length) < 0:
        block_start = True
        block += 1
    if block_end == False:
        if not board[y_tip+d_y][x_tip+d_x] == " ":
            block += 1
    if block_start == False:
        if not board[y_tip-(d_y*(length))][x_tip-(d_x*(length))] == " ":
            block += 1
    if block == 2:
        return "CLOSED"
    if block == 1:
        return "SEMIOPEN"
    if block == 0:
        return "OPEN"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0
    y_tip = 0
    x_tip = 0
    while True:

        # check in bound or not
        # over max allowed
        if y_start + (length*d_y) > len(board) or x_start + (length*d_x) > len(board):
            break
        # under first row or column
        elif y_start + ((length - 1)*d_y) < 0 or x_start + ((length - 1)*d_x) < 0:
            break

        # Check the number of sequence
        if board[y_start][x_start] != col:
            y_start += d_y
            x_start += d_x
            # skip iteration without returning, check next position
            continue
        else:
            y_tip = y_start + ((length - 1)*d_y)
            x_tip = x_start + ((length - 1)*d_x)

            complete = 0
            for i in range(length):
                if board[y_start+(i*d_y)][x_start+(i*d_x)] != col:  # not complete sequence
                    # skip to new part
                    y_start += i*d_y
                    x_start += i*d_x
                    complete += 1
                    break
            if complete > 0:
                # skip iteration, check next position
                continue

            end_y = y_tip
            end_x = x_tip

            last = True
            if y_tip + d_y <= 7 and x_tip + d_x <= 7 and y_tip + d_y >= 0 and x_tip + d_x >= 0:  # in bounds
                if board[y_tip + d_y][x_tip + d_x] == col:  # if sequence is too long
                    y_start = y_tip
                    x_start = x_tip
                    last = False
                    while end_y + d_y <= 7 and end_y >= 0 and end_x >= 0 and end_x + d_x <= 7:  # in bounds
                        end_x += d_x
                        end_y += d_y
                        y_start += d_y
                        x_start += d_x
            if last == False:
                continue
            if is_bounded(board, y_tip, x_tip, length, d_y, d_x) == "OPEN":
                open_seq_count += 1
            elif is_bounded(board, y_tip, x_tip, length, d_y, d_x) == "SEMIOPEN":
                semi_open_seq_count += 1
            y_start = y_tip + d_y
            x_start = x_tip + d_x

    return open_seq_count, semi_open_seq_count


def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    if is_empty == True:  # empty board
        return 0, 0

    # vertical
    for i in range(len(board[0])):
        vert_seq = detect_row(board, col, 0, i, length, 1, 0)
        open_seq_count += vert_seq[0]
        semi_open_seq_count += vert_seq[1]

    # horizontal
    for i in range(len(board)):
        # row = i, d_y = 1
        hor_seq = detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count += hor_seq[0]
        semi_open_seq_count += hor_seq[1]

    # diagonal top right
    for i in range(1, len(board)-1):
        right_diagonal_row = detect_row(
            board, col, 0, i, length, 1, -1)  # first row
        open_seq_count += right_diagonal_row[0]
        semi_open_seq_count += right_diagonal_row[1]
        right_diagonal_column = detect_row(
            board, col, i, 7, length, 1, -1)  # first column
        open_seq_count += right_diagonal_column[0]
        semi_open_seq_count += right_diagonal_column[1]

    # diagonal top left
    for i in range(len(board)-2, -1, -1):
        left_diagon_column = detect_row(
            board, col, i, 0, length, 1, 1)  # first column
        open_seq_count += left_diagon_column[0]
        semi_open_seq_count += left_diagon_column[1]
    for i in range(1, 7):
        left_diagon_row = detect_row(
            board, col, 0, i, length, 1, 1)  # first row
        open_seq_count += left_diagon_row[0]
        semi_open_seq_count += left_diagon_row[1]
    return open_seq_count, semi_open_seq_count


def search_max(board):
    if is_empty == True:
        return None
    move_y = 0
    move_x = 0
    max_score = 0
    for i in range(len(board)):
        for k in range(len(board)):
            if board[i][k] == " ":
                board[i][k] = "b"
                if max_score < score(board):
                    max_score = score(board)
                    move_y = i
                    move_x = k
                board[i][k] = " "
    return move_y, move_x


def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)

    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4]) +
            500 * open_b[4] +
            50 * semi_open_b[4] +
            -100 * open_w[3] +
            -30 * semi_open_w[3] +
            50 * open_b[3] +
            10 * semi_open_b[3] +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    sum = 0
    for i in range(len(board)):
        for k in range(len(board[0])):
            if not board[i][k] == " ":
                sum += 1
    if sum == len(board)*len(board[0]):
        return "Draw"

    whitewin = detect_rows(board, "w", 5)
    if whitewin[0] > 0 or whitewin[1] > 0:
        return "White won"

    blackwin = detect_rows(board, "b", 5)
    if blackwin[0] > 0 or blackwin[1] > 0:
        return "Black won"
    return "Continue playing"


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


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i)
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")


def test_is_bounded():
    board = make_empty_board(8)
    x = 5
    y = 1
    d_x = 0
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_tip = 3
    x_tip = 5

    if is_bounded(board, y_tip, x_tip, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


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


def test_detect_rows():
    board = make_empty_board(8)
    x = 5
    y = 1
    d_x = 0
    d_y = 1
    length = 3
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col, length) == (1, 0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")


def test_search_max():
    board = make_empty_board(8)
    x = 5
    y = 0
    d_x = 0
    d_y = 1
    length = 4
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6
    y = 0
    d_x = 0
    d_y = 1
    length = 4
    col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4, 6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")


def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()


def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5
    x = 2
    d_x = 0
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3
    x = 5
    d_x = -1
    d_y = 1
    length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5
    x = 3
    d_x = -1
    d_y = 1
    length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


test_board = [[" ", " ", " ", " ", " ", " ", "w", " "],
              [" ", " ", " ", " ", " ", " ", "w", " "],
              [" ", " ", " ", " ", " ", "w", "w", " "],
              [" ", " ", " ", " ", "w", " ", "w", " "],
              [" ", " ", " ", "w", " ", " ", "w", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "]]
if __name__ == '__main__':
    # play_gomoku(8)
    # test_search_max()
    # test_detect_row()
    # test_search_max()
    # print(detect_row(test_board, "w", 0, 2, 2, 1, 0))
    # print(detect_rows(test_board, "w", 2))
    # print(detect_row(test_board,"w",0,7,4,1,-1))
    # easy_testset_for_main_functions()p
    # detect_row(test_board, "b", 4, 0, 3,0,1)
    # print(detect_row(test_board, "b", 3, 0, 3, 0, 1))
    # is_empty()
    # print(is_win(test_board))
    print(easy_testset_for_main_functions())
    print(some_tests())
