''''1. Write a function that takes in two numbers and recursively multiplies them together.'''


def multiplier(a, b):
    if a < 1000 and b < 1000:
        print(a*b)
        return multiplier(a*b, a*b)
    else:
        return 1


print(multiplier(3, 2))

'''2. Write a function that takes in a base and an exp and recursively computes baseexp. You are not allowed to
use the ** operator!'''


def expo(base, exp):
    if exp > 1:
        print(base*base)
        return expo(base*base, exp - 1)
    else:
        return 1


expo(5, 2)

'''3. Write a function using recursion to print numbers from n to 0.'''


def printing(n):
    if n >= 0:
        print(n)
        return printing(n-1)
    else:
        return


printing(10)
'''4. Write a function using recursion to print numbers from 0 to n (you just need to change one line in the program
of problem 1).'''


def to_n(n):
    if n >= 0:
        to_n(n-1)
        print(n)
    else:
        return


to_n(10)

'''5. Write a function using recursion that takes in a string and returns a reversed copy of the string. The only
string operation you are allowed to use is string concatenation.'''


def reversed(thing):
    if len(thing) > 0:
        print(thing[-1])
        reversed(thing[:-1])
    else:
        return


reversed("stusdad")


'''6. Write a function using recursion to check if a number n is prime (you have to check whether n is divisible by
any number below n).'''


'''7. Write a recursive function that takes in one argument n and computes Fn, the nth value of the Fibonacci
sequence. Recall that the Fibonacci sequence is defined by the relation
Fn = Fn−1 + Fn−2
where
F0 = 0 and F1 = 1
Visit the Wikipedia page on the Fibonacci Number for more information if you’re still confused.'''
