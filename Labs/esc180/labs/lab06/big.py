'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random

def sub(square_num):
    coord = []
    s =  0
    if square_num % 3 == 0:
        s = 2
    if square_num % 3 == 1:
        s = 0
    if square_num % 3 ==  2:
        s = 1
    coord.append((square_num-1)//3)
    coord.append(s)
    return coord


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")

def put_in_board(board,mark,square_num):
    s =  0
    if square_num % 3 == 0:
        s = 2
    if square_num % 3 == 1:
        s = 0
    if square_num % 3 ==  2:
        s = 1

    s = (square_num -1) % 3

    row_number = (square_num-1) // 3
    column_number = s
    board[row_number][column_number] = mark

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board


def askuser():
    L = []
    input_str = ''
    counter = 0
    while True:
        input_str = input("Please type in a coordinate")
        user_input_number = int(input_str)
        if counter <= 9:
            if user_input_number not in L:#if user input isnt in L
                counter = counter + 1
                L.append(user_input_number)
            else:#if the users input is already in L
                print("The coordinate has already been taken")
        else:
            print("All the coordinates have been taken already")

def get_free_squares(board):
    all_coord = []
    for i in range(len(board)):
        for s in range(len(board[i])):
            if board[i][s] == ' ': #if the board is empty
                L = [i, s]
                all_coord.append(L)
            else: # if the board is not empty
                pass
    return all_coord

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)
    L = []
    input_str = ''
    counter = 0
    while True:
        input_str = input("Please type in a coordinate")
        user_input_number = int(input_str)
        if user_input_number == 0:
            while True:
                s = int(10*random.random())
                if s not in L:
                    put_in_board(board,"X",s)
                    print_board_and_legend(board)
                    break
                else:
                    pass

        else:
            if counter <= 9:
                if user_input_number not in L:#if user input isnt in L
                    counter = counter + 1
                    L.append(user_input_number)
                    put_in_board(board,"X",user_input_number)
                    print_board_and_legend(board)
                else:#if the users input is already in L
                    print("The coordinate has already been taken")
            else:
                print("All the coordinates have been taken already")
        print(get_free_squares(board))








