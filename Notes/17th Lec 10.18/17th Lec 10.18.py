#midterm, in more detail

#nested loops

#intro to storing objects into memory

#2022 midterm question 6:
import math

def next_integer():
    global cur_int
    cur_int = cur_int + 1
    return digits_pi[cur_int - 1]


if __name__ == '__main__':
    cur_int = 0
    print(next_integer())
    print(next_integer())
    print(next_integer())
    print(next_integer())
    print(next_integer())


