#multiple assignment
x, y, z = 5, "hi", "paxis" # sae as x = 5 and y= "hi"

#swap values using multiple assignment
#x, y = y,  x
#having a temporary variable can help

temp = x
x = y
y= temp
#Cracking The Coding Interview(CTCI)

#communicate info to and from functions
# x and y are integers
# write code that swaps their values without
#multiple assignment, and without temp variable

#puzzle:
x = 5
y = 9
#outcome x = 9, y = 5
x = x + y #first line of solution x = 14
y = x - y # y = 9
x = x - y

print(x,y)



#commnications informations to and from funtions

def square(x):
    return x*x



#docsting: a descripiton of what the function does
#'''enclosed in '''

def has_roots(a,b,c):
    #disc is a local vaiable
    #think of it as scratch work
    #not accessible outside of function
    disc = b**2-2*a*c
    if disc > 0:
        return True
    elif disc == 0:
        return True
    else:
        return False
#or u can do it this way:
def has_roots(a,b,c):
    return b**2 - 4*a*c

print(has_roots(1,100,3))

def pirate(s):#its job is to compute
    return "Ahoy!" + s + " Yarr!"

def pp(s):
    print(pirate(str(s)))#its job is to print something, not compute

pp(44)

print(pirate("I love jokes"))

#global variables
#variables that are defined outside of any functon and are accessible from anywhere
x = 90
def print_x():
    print(x)
print_x()
def set_x_to_43():
    global x
    x = 43
set_x_to_43()
print_x()




if __name__=='__main__':
    print(square(5))


