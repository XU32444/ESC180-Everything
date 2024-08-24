def change_x():
    global x
    x = 42

def dont_change_x():
    x = 43

def dont_change_x2(x):
    x = 43

def change_x4():
    global x
    y = 43
    x = y

#this will produce an error because x must be local
#but later on x is defined as global
#python considers as an syntax error
def produce_error():
    global x
    x = 42

#if a varibale is not defined locally, oython will take the global variables
def print_x():
    print(x)


if __name__ == '__main__':
    x = 0
    change_x()#x is now 42
    dont_change_x()#x is still 42
    dont_change_x2()#x is still 42
    change_x4(x)#x is now  43
    x = 42
    change_x4(1234) # x is now 42

########################
def square(x):
    return x**2

def sqaure_bad():
    global ret_val_sb
    global x_for_sb
    ret_val_sb = x_for_sb**2

if __name__ == '__main__':
    x = sqaure(9)




#control flow
#controling which line of code are executed

def has_roots(a,b,c):
    disc = b**2 - 4*a*c
    if disc < 0:
        return print("chips")
    elif disc == 0:
        return True
    elif disc > 0:
        return True

if __name__ == '__main__':
    has_roots(1,2,3)











































