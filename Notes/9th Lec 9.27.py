def is_prime(n):
    if n <= 1:
        return False

    for i in range(n - 2):
        if n % (i + 2) == 0:
            return False
        return True

#while loops
#while<condition>:
#    BLOCK
#keep repearing block while cond is true

i = 0
n = 5
while i < n:
    print(i)
    i = i + 1

#if you know how many times the loop wull reapat, use for _ in range

#log10(n) towhat degree do i need to raise to 10 so that i get n
#10^k = n, k = ?

#log10(100) = 2
#log10(1million) = 6

10000

#log10(1000000) is the number of times that i can divide 10000 by 10
#before i get to i

def log10(n):
    ans = 0
    while n > 1:
        n //= 10 # n = n // 10
        ans = ans + 1

if __name__ == '__main__':







def g():
    global x
    x = 2
    return x
print(g())




#trick qestion on quiz:
def g(x):
    global x
    x = 2
    return 3

if __name__ == '__main__':
    x = 4
    g(x)
    print(x)

#answer: syntax ERROR

#Ruels
#A variable is local unless
#you are accessing a variable's value and there is no local variable by that name
#the variable is specifically declared as global in the function
#local variables are only accessible from inside of the function

#in which they exist
#parameters are local
#if there is ambiguity abbout whether the variable is global or local


# it is a syntax error
# arises in two situation:
#
#










def log10(n):
    ans = 0
    while n > 1:
        n //= 10 # n = n // 10
        ans = ans + 1

if __name__ == '__main__':
    a = log10(10000)




#####################
start = 9
end = 1234
step = 20
for i in range(start,end,step):#i goes from start, up to but not includuing end, in steps step
    print(i)

start = 1234
end = 9
step =-20
for i in range(start,end,step):
    print(i)

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2,n,1):
        if n % i == 0:
            return False
        return True



