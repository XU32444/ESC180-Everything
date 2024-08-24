
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


if __name__ == '__main__':
    askuser()