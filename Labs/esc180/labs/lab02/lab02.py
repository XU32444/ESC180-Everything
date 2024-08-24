#Part A
def my_sqrt(x):
    sqr = x**.5
    return sqr

if __name__ == "__main__":
    res = my_sqrt(25)
    print(res)
#Part B
def my_sqrt(x):
    sqr = x**.5
    return sqr

if __name__ == "__main__":
    sqr = my_sqrt(25)
    print(sqr)
#Part C
x = 25
def my_print_square(x):
    print(x**0.5)

def main():
    res = my_print_square(25)
    print(res)

main()



#The difference are:my_sqrt only computes the value, but my_print_square does both computation and print at the same time

#Questions 2

#Question 3
#x = 0
#if __name__ == "__main__" :
#    print("Welcome to the calculator program")
#    print(f"Current value:")
#    display_current_value()

def display_current_value():
    global balance
    print("Welcome to the calculator Program")
    print(f"Current Value {balance}")

def add(to_add):
    global balance
    balance = to_add + balance

def mult(to_mult):
    global balance
    balance = balance * to_mult

def sub(to_sub):
    global balance
    balance = balance - to_sub

def div(to_div):
    global balance
    balance = balance / to_div

def main():
    while True:
        y = int(input("Whats the original value"))
        global balance
        balance = y
        x = int(input("What do you want to do? 1 = add, 2 = mult, 3 = sub, 4 = div, 5 = mem, 6 = recall"))
        if x == 1:
            t = int(input("add by?"))
            add(t)
            break
        elif x == 2:
            t = int(input("multiply by?"))
            mult(t)
            break
        elif x == 3:
            t = int(input("subtract by?"))
            sub(t)
            break
        elif x == 4:
            t = int(input("divide by?"))
            div(t)
            break
        elif x == 5:
            global balance
            global old_bal
            balance = old_bal
            break
    print(balance)


main()








