#using loops

#swap the values in a and b without using temporary variables
temp = a
a = b
b = temp
#or
a , b = b , a

# a and b are floats


#initially
#a: old a
#b: old b
a = a + b #a:old a + old b, b = old b
b = a - b #a:old a + old b, b = old a
a = a - b #a:old b, b = old a

#with floats: might get rounding errors
#in the last digits

#with integers: works, but a + b potentially needs more space thna a or b seperately

#want to know the number of trailing zerosi n!
#n! = 1 * 2 * 3 *... n
def fact(n):
    res = 1
    for i in range(1, n + 1):#does include n but not n + 1
        res = res * i
    return res

    # i = 1; res = 1
    # i = 2; res = 2
    # i = 3; res = 6
    # i = 4; res = 24
    # i = 5; res = 120

def trailing_zeros(n):
    times_divided_by_10 = 0#count the number of times divided by 10
    while n % 10 == 0:
        n = n / 10
        times_divided_by_10 = times_divided_by_10 + 1 #divded by 10 for once, update times_divided_by_10 right away
    return times_divided_by_10
    #when i am returning, the following are true
    #1. cant divided by 10 because n % 10 != 10(exited the loops
    #2. times_divided_by_10 is the number of times
    # i divided by 10 while possible

def trailing_zeros_fact(n):
    fact_n = fact(n)
    return trailing_zeros(fact_n)

if __name__ == '__main__':
    print(trailing_zeros_fact(120))


#another application of for loops
# i want to compute Pi

import random

random.random()#random number between 0 and 1

x, y = random.random(),random.random()
#repeatedly get coordinates x, y
#keep track how much are inside and quarter circle
def approx_pi(Npoints):
    N = 10000
    for i in range(Npoints):
        x, y = random.random(),random.random()
        if x**2 + y**2 < 1**2:
            inside = inside + 1
    return 4 * inside / N #approx pi


#break,continue
i = 0
while i < 10:
    i = i + 1
    if i % 3 == 0:
        continue#not gonna print 3 cuz when the if statemnet is met, it will go to the while loop and skip print(i)
    print(i)





































