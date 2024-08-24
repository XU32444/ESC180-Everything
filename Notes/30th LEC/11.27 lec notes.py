# Analyze: say what the run time will proportional to

comp1: Program A rumtime, program B runtime
comp2: Program A rumtime, program B runtime

# Runtime is proportional to f(n), n is the length/magnitude of input

on comp1: runtime will be c*f(n)
on comp2: runtime will be c1*f(n)

# worst-case asymptotic runtime complexity for input
# if size/mag n

#O(n^2)

# usually (for programs with loops)

for/while<>:        #assume run k1 times
    for/while<>:    #assume run k2 times
        #block of code

#assume the block runs in constnat time, the runtime is
# O(k1*k2)

# the block might not run in constant time if the runtime depends on n
# (e.g. if the block is for i in range(n) )
#

a = 10
while i <10:
    a = a * a #different case cuz integer multiplication will take longer time especially when it times itself
# integer operations are not necessarily constant

for <>:
    for<>: #runs for variable amounts of time #but in total the number of iteration is known # or there is a formula
        # block of code


##

while n>1:
    n = n / 2 # log 2 n basically

n             2^k
n/2           #
n/4           #

2^k = n => log2(2^k) = k = log2(n)


# catogorize different types of "tricks" just go over the examples thrugh the past lectures.



# Recursion
# functions using themsleves as helper functions

# n! = 1 * 2 * ... * n

#recusion way

#structure of recursion
# 1. need a base ase: return value of simple input
# 2. Need a recursive step: using function itself as a helper function, for a "simplter" inout




def fact(n):
    pass




# Leap of faith: if the function woks for hte base case and it works assuming it works for simpler cases, it will work in general



# call tree: a graphical represenation of the recusive computation

def fact(n):
    if n==0:
        return 1
    return fact(n-1) * n

# leap of faith : if the function works for the base case and it works assuming it works for simpler cases, it will work in general

# call tree: a graphical repersentiation of the recursive computation

fact(0)
    | \ 1
fact(1)\
        \ 1*1
fact(2)  \ 2*1*1
   ...
fact(n)    \ fact(n-3)*fact(n-2)*fact(n-1)*...*fact(1)




# using for loops
def fact(n):
    ans = 1
    for e in range(1,n+1):
        ans = ans * e
    return ans




# print the list L
# no print(L), no loops

# 1. base case (dont push on a rope)
# if len(L) = 1, can just print L[0]

# 2. recursive step (to get a answer u need first knowt the annswer)
# first print L[0], then print hte rst of list

# 3. F = ma

def print_list_rec(L):
    if len(L) = 1:
        print(L[0])
        return
    print(L[0])
    print_list_rec(L[1:])


# to print L in reverse:
#
def print_list_rev(L):
    if len(L) = 1:
        print(L[0])
        return
    print_list_rev(L[1:])
    print(L[0])




# a^n
def power(a,n):
    res = 1
    for i in range(n):
        res = res * a
    return res

# a^n = a^(n-1)*a
def power_rec(a,n):
    if n == 0:
        return 1
    else:
        reutrn a*power_rec(a,n-1) # a>n = a*a^(n-1)


def power_while(a,n):
    res = 1
    i = 0
    while i < n:
        res = res * a
        i = i + 1
    return res

def power_while_rec(a,n,i,res):
    if i == n:
        return res
    return power_while_rec(a,n,i-1,res*a)







































