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

if __name__ == '__main__':
    print(sub(9))