def initialize():
    global balance
    global old_balance
    global old_old_balance
    balance = 0
    old_balance = 0
    old_old_balance = 0


def display_current_value():
    global balance
    print("Welcome to the calculator Program")
    print(f"Current Value {balance}")

def add(to_add):
    global balance
    global old_balance
    global old_old_balance
    old_old_balance = old_balance
    old_balance = balance
    balance = to_add + balance

def mult(to_mult):
    global balance
    global old_balance
    global old_old_balance
    old_old_balance = old_balance
    old_balance = balance
    balance = balance * to_mult

def sub(to_sub):
    global balance
    global old_balance
    global old_old_balance
    old_old_balance = old_balance
    old_balance = balance
    balance = balance - to_sub

def div(to_div):
    global balance
    global old_balance
    global old_old_balance
    old_old_balance = old_balance
    old_balance = balance
    balance = balance / to_div

def recall():
    global saved_value
    print(saved_value)

def undo2():
    global old_old_balance
    print(old_old_balance)

if __name__ == "__main__":
    initialize()
    while True:
        y = int(input("Whats the original value"))
        balance = y
        old_balance = 0
        old_old_balance = 0
        while True:
            x = int(input("What do you want to do? 1 = add, 2 = mult, 3 = sub, 4 = div, 5 = mem, 6 = undo, 7 = change original value, 8 = recall saved Value, 9 = undo2"))
            if x == 1:
                t = int(input("add by?"))
                add(t)
                print(balance)
            elif x == 2:
                t = int(input("multiply by?"))
                mult(t)
                print(balance)
            elif x == 3:
                t = int(input("subtract by?"))
                sub(t)
                print(balance)
            elif x == 4:
                t = int(input("divide by?"))
                div(t)
                print(balance)
            elif x == 5:
                saved_value = balance
            elif x == 6:
                print(old_balance)
                old_balance, balance = balance, old_balance
            elif x == 7:
                break
            elif  x == 8:
                recall()
            elif x == 9:
                undo2()




