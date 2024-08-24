#Lec 9.25
#primality testing, for loops, while loops

#Project 1

#for i in range(n):
    #...use i, which is 0,1,2,,n-1

#is n1 divisible by n2?
#n1 % n2 == 0

#is n prime?
# n % 2 == 0?
# n % 3 == 0?
#...

#range(n)i goes from 0 to n-1
#range(n) (i+2) goes form 2 to n + 1
#range(n-2) (i+2) goes from 2 to n _ 1

#range(3): i is 0,1,2
#range(3): i+2 is 2,3,4
#range(4-2): i+2 is 2,3
def is_prime(n):
    for i in range(n - 2):
        if n % (i+2) == 0:
            return False
    return True

if __name__ == '__main__':
    print(is_prime(291))













